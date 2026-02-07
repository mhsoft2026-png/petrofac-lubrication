@echo off
echo ========================================
echo   بناء APK - Petrofac Lubrication
echo ========================================
echo.

echo [1/3] فتح PWABuilder...
echo.
start https://www.pwabuilder.com

echo [2/3] تشغيل السيرفر المحلي...
echo.
echo سيتم فتح التطبيق على: http://localhost:3000
echo.
start cmd /k "cd /d %~dp0 && npm run dev"

timeout /t 5 /nobreak >nul

echo.
echo [3/3] التعليمات:
echo ========================================
echo.
echo 1. في PWABuilder، أدخل: http://localhost:3000
echo 2. اضغط: "Start" أو "Generate"
echo 3. اضغط على "Android"
echo 4. اضغط "Download" لتحميل APK
echo.
echo ========================================
echo سيكون APK جاهز في أقل من دقيقة!
echo ========================================
echo.
pause
