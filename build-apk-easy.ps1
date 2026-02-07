# بناء APK بسهولة - Petrofac Lubrication

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  بناء APK - Petrofac Lubrication" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 1. فتح PWABuilder
Write-Host "[1/3] فتح PWABuilder للحصول على APK..." -ForegroundColor Yellow
Start-Process "https://www.pwabuilder.com"
Start-Sleep -Seconds 2

# 2. تشغيل السيرفر
Write-Host "[2/3] تشغيل السيرفر المحلي..." -ForegroundColor Yellow
Write-Host ""
Write-Host "السيرفر سيعمل على: http://localhost:3000" -ForegroundColor Green
Write-Host ""

# بناء المشروع أولاً
Write-Host "بناء التطبيق..." -ForegroundColor Gray
npm run build | Out-Null

# نسخ ملفات PWA
Copy-Item public\manifest.json dist\ -ErrorAction SilentlyContinue
Copy-Item public\sw.js dist\ -ErrorAction SilentlyContinue
Copy-Item public\icon.svg dist\icon-192.png -ErrorAction SilentlyContinue
Copy-Item public\icon.svg dist\icon-512.png -ErrorAction SilentlyContinue

# تشغيل السيرفر في نافذة جديدة
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD\dist'; http-server -p 3000"

Start-Sleep -Seconds 3

# 3. التعليمات
Write-Host "[3/3] خطوات الحصول على APK:" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. في موقع PWABuilder الذي فُتح:" -ForegroundColor White
Write-Host "   - أدخل: http://localhost:3000" -ForegroundColor Green
Write-Host "   - اضغط: 'Start' أو 'Generate'" -ForegroundColor Green
Write-Host ""
Write-Host "2. اختر خيار 'Android':" -ForegroundColor White
Write-Host "   - اضغط على أيقونة Android" -ForegroundColor Green
Write-Host "   - اضغط 'Generate'" -ForegroundColor Green
Write-Host ""
Write-Host "3. حمّل APK:" -ForegroundColor White
Write-Host "   - اضغط 'Download'" -ForegroundColor Green
Write-Host "   - ستحصل على ملف .apk جاهز!" -ForegroundColor Green
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "⚡ APK سيكون جاهز في أقل من دقيقة!" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "📱 معلومات APK:" -ForegroundColor Cyan
Write-Host "   • الاسم: Petrofac Lubrication" -ForegroundColor Gray
Write-Host "   • المعدات: 827 عنصر" -ForegroundColor Gray
Write-Host "   • الحجم: ~3-5 MB" -ForegroundColor Gray
Write-Host "   • يعمل: بدون إنترنت" -ForegroundColor Gray
Write-Host ""
Write-Host "لإغلاق السيرفر: أغلق نافذة PowerShell الأخرى" -ForegroundColor DarkGray
Write-Host ""

Read-Host "Press Enter to finish"
