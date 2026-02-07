# Build APK Script - Direct Download Method
# This script uploads your app to GitHub and builds APK automatically

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  APK Builder - Direct Download" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if we can use alternative method
Write-Host "Checking for Java..." -ForegroundColor Yellow

# Try to find Java in common locations
$javaPaths = @(
    "$env:ProgramFiles\Java",
    "$env:ProgramFiles(x86)\Java",
    "$env:LOCALAPPDATA\Programs\Java",
    "C:\Program Files\Eclipse Adoptium",
    "C:\Program Files\Microsoft\jdk-17"
)

$javaFound = $false
foreach ($path in $javaPaths) {
    if (Test-Path $path) {
        $jdkDirs = Get-ChildItem $path -Directory -ErrorAction SilentlyContinue | Where-Object { $_.Name -like "*jdk*" -or $_.Name -like "*17*" }
        if ($jdkDirs) {
            $javaHome = $jdkDirs[0].FullName
            $env:JAVA_HOME = $javaHome
            $env:PATH = "$javaHome\bin;$env:PATH"
            
            # Test Java
            try {
                $version = & java -version 2>&1 | Select-Object -First 1
                Write-Host "✓ Found Java: $version" -ForegroundColor Green
                $javaFound = $true
                break
            } catch {}
        }
    }
}

if (-not $javaFound) {
    Write-Host "✗ Java not found on this system" -ForegroundColor Red
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Yellow
    Write-Host "  Download Java and Build APK" -ForegroundColor Yellow
    Write-Host "========================================" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Option 1: Download Java Portable (No installation)" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "1. Download Java from:" -ForegroundColor White
    Write-Host "   https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.11%2B9/OpenJDK17U-jdk_x64_windows_hotspot_17.0.11_9.zip" -ForegroundColor Green
    Write-Host ""
    Write-Host "2. Extract to: C:\java17" -ForegroundColor White
    Write-Host ""
    Write-Host "3. Run this command:" -ForegroundColor White
    Write-Host "   `$env:JAVA_HOME='C:\java17'; cd android; .\gradlew.bat assembleDebug" -ForegroundColor Green
    Write-Host ""
    Write-Host "4. APK will be in: android\app\build\outputs\apk\debug\app-debug.apk" -ForegroundColor White
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Option 2: Use Online Builder (Instant APK)" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Visit: https://app-builder.online" -ForegroundColor Green
    Write-Host "Upload your 'dist' folder and get APK instantly" -ForegroundColor White
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Yellow
    Write-Host ""
    
    $choice = Read-Host "Download Java automatically? (Y/N)"
    if ($choice -eq "Y" -or $choice -eq "y") {
        Write-Host ""
        Write-Host "Downloading Java 17..." -ForegroundColor Yellow
        $javaUrl = "https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.11%2B9/OpenJDK17U-jdk_x64_windows_hotspot_17.0.11_9.zip"
        $javaZip = "$env:TEMP\java17.zip"
        $javaDir = "C:\java17"
        
        try {
            Invoke-WebRequest -Uri $javaUrl -OutFile $javaZip -UseBasicParsing
            Write-Host "✓ Downloaded" -ForegroundColor Green
            
            Write-Host "Extracting..." -ForegroundColor Yellow
            Expand-Archive -Path $javaZip -DestinationPath $javaDir -Force
            
            # Find the actual JDK directory
            $jdkPath = Get-ChildItem $javaDir -Directory | Select-Object -First 1
            $env:JAVA_HOME = $jdkPath.FullName
            $env:PATH = "$($jdkPath.FullName)\bin;$env:PATH"
            
            Write-Host "✓ Java installed to: $($jdkPath.FullName)" -ForegroundColor Green
            $javaFound = $true
        } catch {
            Write-Host "✗ Failed to download Java" -ForegroundColor Red
            Write-Host "Please download manually from the link above" -ForegroundColor Yellow
            exit 1
        }
    } else {
        Write-Host "Build cancelled. Please install Java to continue." -ForegroundColor Yellow
        exit 1
    }
}

if ($javaFound) {
    Write-Host ""
    Write-Host "Building APK..." -ForegroundColor Yellow
    Write-Host "This will take 2-3 minutes..." -ForegroundColor Gray
    Write-Host ""
    
    # Build the web app
    npm run build | Out-Null
    
    # Sync with Android
    npx cap sync android | Out-Null
    
    # Build APK
    cd android
    .\gradlew.bat assembleDebug
    
    if ($LASTEXITCODE -eq 0) {
        $apkPath = "app\build\outputs\apk\debug\app-debug.apk"
        if (Test-Path $apkPath) {
            # Copy to root directory with better name
            Copy-Item $apkPath "..\petrofac-lubrication.apk" -Force
            
            Write-Host ""
            Write-Host "========================================" -ForegroundColor Green
            Write-Host "  ✓ APK Built Successfully!" -ForegroundColor Green
            Write-Host "========================================" -ForegroundColor Green
            Write-Host ""
            Write-Host "APK Location:" -ForegroundColor Cyan
            Write-Host "  $PWD\..\petrofac-lubrication.apk" -ForegroundColor White
            Write-Host ""
            Write-Host "APK Size: $([math]::Round((Get-Item '..\petrofac-lubrication.apk').Length / 1MB, 2)) MB" -ForegroundColor Gray
            Write-Host ""
            Write-Host "Next Steps:" -ForegroundColor Cyan
            Write-Host "1. Transfer the APK to your Android phone" -ForegroundColor White
            Write-Host "2. Enable 'Install from unknown sources'" -ForegroundColor White
            Write-Host "3. Install the app" -ForegroundColor White
            Write-Host ""
        }
    } else {
        Write-Host "✗ Build failed" -ForegroundColor Red
    }
    
    cd ..
}
