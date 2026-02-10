# Petrofac Lubrication - Android Project

This is the Android project folder for Petrofac Lubrication application.

## ⚙️ Configuration Changes (تم تعديل الإعدادات)

### تقليل تحذيرات Google Play Protect:
- **targetSdkVersion**: خُفّض من 36 إلى 30
- **compileSdkVersion**: خُفّض من 36 إلى 34
- **usesCleartextTraffic**: مُفعّل للسماح بـ HTTP
- **requestLegacyExternalStorage**: مُفعّل للتوافق مع الإصدارات القديمة

هذه التعديلات تقلل من تحذيرات Google Play Protect عند تثبيت التطبيق.

## Quick Start

1. Open this folder in Android Studio
2. Wait for Gradle sync
3. Build → Build APK

## Files Overview

- `app/` - Main application module
- `build.gradle` - Build configuration
- `gradlew.bat` - Gradle wrapper (Windows)
- `local.properties` - SDK location (auto-generated)

## Build Commands

```bash
# Debug APK
gradlew assembleDebug

# Release APK  
gradlew assembleRelease

# Install on device
gradlew installDebug

# Clean
gradlew clean
```

## Output

APK will be in:
```
app/build/outputs/apk/debug/app-debug.apk
```

## Requirements

- Android Studio (includes Java JDK)
- Android SDK (installed with Android Studio)
- Min SDK: 22 (Android 5.1)
- Target SDK: 35 (Android 15)

## Project Details

- **App ID:** com.petrofac.lubrication
- **App Name:** Petrofac Lubrication
- **Version:** 1.0
- **Equipment Count:** 827 items
- **Framework:** Capacitor 7 + React + Vite

## Documentation

See parent folder for detailed guides:
- `../ANDROID_STUDIO_GUIDE.md` - Full guide (Arabic)
- `../ANDROID_STUDIO_QUICKSTART.md` - Quick reference
- `../ANDROID_STUDIO_SETUP.txt` - Setup instructions

---

**Ready to build!** 🚀
