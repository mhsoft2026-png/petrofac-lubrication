@echo off
chcp 65001 >nul
echo.
echo ╔════════════════════════════════════════════════╗
echo ║   Petrofac Lubrication - APK Generator        ║
echo ╚════════════════════════════════════════════════╝
echo.
echo [i] Starting server...
echo.

REM Start the dev server in a new window
start "Petrofac Server" cmd /k "npm run dev"

REM Wait for server to start
timeout /t 5 /nobreak >nul

echo ✓ Server running at: http://localhost:3000
echo.
echo ════════════════════════════════════════════════
echo  STEP 1: Open one of these websites
echo ════════════════════════════════════════════════
echo.
echo  Option 1 (Easiest):
echo  → https://appsgeyser.com
echo.
echo  Option 2:
echo  → https://gonative.io
echo.
echo  Option 3:
echo  → https://www.pwabuilder.com
echo.
echo ════════════════════════════════════════════════
echo  STEP 2: Enter this URL in the website
echo ════════════════════════════════════════════════
echo.
echo  → http://localhost:3000
echo.
echo ════════════════════════════════════════════════
echo  STEP 3: Download APK
echo ════════════════════════════════════════════════
echo.
echo  Click "Create App" or "Generate"
echo  Then download the APK file
echo.
echo ✓ APK will be ready in 1-2 minutes!
echo.
echo ════════════════════════════════════════════════
echo.

REM Open the easiest website
start https://appsgeyser.com

echo Press any key to stop the server...
pause >nul

REM Close the server window
taskkill /FI "WindowTitle eq Petrofac Server*" /T /F >nul 2>&1

echo.
echo Server stopped. Goodbye!
timeout /t 2 /nobreak >nul
