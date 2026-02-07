# Script لتحميل Java وبناء APK

Write-Host "====================================" -ForegroundColor Cyan
Write-Host "  تثبيت Java وبناء APK" -ForegroundColor Cyan
Write-Host "====================================" -ForegroundColor Cyan
Write-Host ""

# 1. تحميل Java 17
Write-Host "[1/4] تحميل Java 17..." -ForegroundColor Yellow
$javaUrl = "https://download.oracle.com/java/17/latest/jdk-17_windows-x64_bin.exe"
$javaInstaller = "$env:TEMP\jdk-17-installer.exe"

# إذا كان Java موجود، تخطي التحميل
$javaPath = "C:\Program Files\Java\jdk-17"
if (Test-Path $javaPath) {
    Write-Host "✓ Java 17 موجود بالفعل" -ForegroundColor Green
    $env:JAVA_HOME = $javaPath
    $env:PATH = "$javaPath\bin;$env:PATH"
} else {
    Write-Host "يرجى تحميل Java 17 يدوياً من:" -ForegroundColor Red
    Write-Host "https://www.oracle.com/java/technologies/downloads/#jdk17-windows" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "بعد التثبيت، أغلق وأعد فتح PowerShell ثم شغّل:" -ForegroundColor Yellow
    Write-Host "cd android" -ForegroundColor Cyan
    Write-Host ".\gradlew.bat assembleDebug" -ForegroundColor Cyan
    exit 1
}

# 2. التحقق من Java
Write-Host "[2/4] التحقق من Java..." -ForegroundColor Yellow
try {
    $javaVersion = & java -version 2>&1 | Select-Object -First 1
    Write-Host "✓ $javaVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ فشل في التحقق من Java" -ForegroundColor Red
    exit 1
}

# 3. بناء APK
Write-Host "[3/4] بناء APK..." -ForegroundColor Yellow
Write-Host "هذا قد يستغرق بضع دقائق..." -ForegroundColor Gray
cd android
.\gradlew.bat assembleDebug

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ تم بناء APK بنجاح!" -ForegroundColor Green
    
    # 4. نسخ APK
    Write-Host "[4/4] نسخ APK..." -ForegroundColor Yellow
    $apkSource = "app\build\outputs\apk\debug\app-debug.apk"
    $apkDest = "..\petrofac-lubrication.apk"
    
    if (Test-Path $apkSource) {
        Copy-Item $apkSource $apkDest -Force
        Write-Host "✓ APK محفوظ في: petrofac-lubrication.apk" -ForegroundColor Green
        Write-Host ""
        Write-Host "====================================" -ForegroundColor Cyan
        Write-Host "  ✓ تم بناء التطبيق بنجاح!" -ForegroundColor Green
        Write-Host "====================================" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "📱 الآن انقل الملف إلى هاتفك:" -ForegroundColor Yellow
        Write-Host "   petrofac-lubrication.apk" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "الحجم: $((Get-Item $apkDest).Length / 1MB) MB" -ForegroundColor Gray
    } else {
        Write-Host "✗ لم يتم العثور على APK" -ForegroundColor Red
    }
} else {
    Write-Host "✗ فشل بناء APK" -ForegroundColor Red
    Write-Host "حاول استخدام Android Studio بدلاً من ذلك" -ForegroundColor Yellow
}

cd ..
