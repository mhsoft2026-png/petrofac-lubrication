# Petrofac Lubrication - Android Studio Setup
# Prepare project for Android Studio

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Petrofac Lubrication - Build Setup" -ForegroundColor Green
Write-Host "  For Android Studio" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Cyan

# Step 1: Build web app
Write-Host "[1/4] Building web application..." -ForegroundColor Yellow
npm run build
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Build failed!" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Web build complete`n" -ForegroundColor Green

# Step 2: Sync Capacitor
Write-Host "[2/4] Syncing Capacitor with Android..." -ForegroundColor Yellow
npx cap sync android
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Capacitor sync failed!" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Android synced`n" -ForegroundColor Green

# Step 3: Check local.properties
Write-Host "[3/4] Checking Android SDK configuration..." -ForegroundColor Yellow
$localProps = "android\local.properties"
if (Test-Path $localProps) {
    Write-Host "✓ local.properties exists" -ForegroundColor Green
} else {
    Write-Host "Creating local.properties..." -ForegroundColor Yellow
    $sdkPath = "$env:LOCALAPPDATA\Android\Sdk"
    $content = "sdk.dir=" + $sdkPath.Replace('\', '\\')
    $content | Out-File -FilePath $localProps -Encoding ASCII
    Write-Host "✓ local.properties created" -ForegroundColor Green
}
Write-Host ""

# Step 4: Verify files
Write-Host "[4/4] Verifying project structure..." -ForegroundColor Yellow
$requiredFiles = @(
    "android\build.gradle",
    "android\app\build.gradle",
    "android\gradlew.bat",
    "android\app\src\main\AndroidManifest.xml"
)

$allGood = $true
foreach ($file in $requiredFiles) {
    if (Test-Path $file) {
        Write-Host "  ✓ $file" -ForegroundColor Green
    } else {
        Write-Host "  ✗ $file (missing)" -ForegroundColor Red
        $allGood = $false
    }
}
Write-Host ""

if ($allGood) {
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "  Project Ready for Android Studio! ✓" -ForegroundColor Green
    Write-Host "========================================`n" -ForegroundColor Green
    
    Write-Host "Next Steps:" -ForegroundColor Yellow
    Write-Host "  1. Open Android Studio" -ForegroundColor White
    Write-Host "  2. Choose: Open an Existing Project" -ForegroundColor White
    Write-Host "  3. Navigate to:" -ForegroundColor White
    Write-Host "     $PWD\android" -ForegroundColor Cyan
    Write-Host "  4. Wait for Gradle sync (5-10 min first time)" -ForegroundColor White
    Write-Host "  5. Build → Build Bundle(s) / APK(s) → Build APK(s)" -ForegroundColor White
    Write-Host ""
    Write-Host "APK will be in:" -ForegroundColor Yellow
    Write-Host "  android\app\build\outputs\apk\debug\app-debug.apk`n" -ForegroundColor Cyan
    
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "Read ANDROID_STUDIO_GUIDE.md for details!" -ForegroundColor Yellow
    Write-Host "========================================`n" -ForegroundColor Cyan
} else {
    Write-Host "========================================" -ForegroundColor Red
    Write-Host "  Some files are missing!" -ForegroundColor Red
    Write-Host "========================================`n" -ForegroundColor Red
    Write-Host "Try running: npx cap add android`n" -ForegroundColor Yellow
}
