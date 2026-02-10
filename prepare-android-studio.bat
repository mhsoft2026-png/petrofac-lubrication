@echo off
chcp 65001 >nul
echo ========================================
echo   Petrofac Lubrication - Build Setup
echo   For Android Studio
echo ========================================
echo.

echo [1/2] Building web app...
call npm run build
if errorlevel 1 (
    echo ERROR: Build failed!
    pause
    exit /b 1
)
echo ✓ Build complete
echo.

echo [2/2] Syncing with Android...
call npx cap sync android
if errorlevel 1 (
    echo ERROR: Sync failed!
    pause
    exit /b 1
)
echo ✓ Sync complete
echo.

echo ========================================
echo   Project Ready for Android Studio!
echo ========================================
echo.
echo Next Steps:
echo   1. Download Android Studio from:
echo      https://developer.android.com/studio
echo.
echo   2. Open Android Studio
echo   3. Choose: Open an Existing Project
echo   4. Navigate to: %CD%\android
echo   5. Wait for Gradle sync
echo   6. Build -^> Build APK
echo.
echo APK Location after build:
echo   android\app\build\outputs\apk\debug\app-debug.apk
echo.
echo Read ANDROID_STUDIO_GUIDE.md for details!
echo ========================================
echo.
pause
