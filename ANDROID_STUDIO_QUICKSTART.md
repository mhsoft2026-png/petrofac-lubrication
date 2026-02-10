# 📱 Android Studio - Quick Start

## ✅ Project is Ready!

### Step 1: Download Android Studio
- https://developer.android.com/studio
- Install with default settings
- Wait for SDK downloads to complete

### Step 2: Open Project
1. Open Android Studio
2. Click **"Open"**
3. Navigate to:
   ```
   C:\Users\houar\OneDrive\Desktop\said\android
   ```
4. Click **"OK"**

### Step 3: Build APK
1. Wait for **Gradle Sync** (5-10 min first time)
2. **Build** → **Build Bundle(s) / APK(s)** → **Build APK(s)**
3. Wait 2-5 minutes
4. Click **"locate"** to open APK folder

### APK Location:
```
android\app\build\outputs\apk\debug\app-debug.apk
```

---

## 🔧 Quick Commands

In Android Studio Terminal:

```bash
# Build Debug APK
gradlew assembleDebug

# Build Release APK
gradlew assembleRelease

# Install on connected device
gradlew installDebug

# Clean project
gradlew clean
```

---

## 📝 Files Overview

✓ **android/** - Complete Android project
✓ **dist/** - Built web assets (synchronized)
✓ **build.gradle** - Build configuration
✓ **AndroidManifest.xml** - App manifest
✓ **MainActivity.java** - Entry point
✓ **827 equipment items** - Full database

---

## ⚙️ If SDK Not Found

1. **File** → **Project Structure** → **SDK Location**
2. Set SDK path to:
   ```
   C:\Users\houar\AppData\Local\Android\Sdk
   ```
3. Click **Apply** → **OK**

---

## 🚀 Run on Emulator/Device

### Emulator:
1. **Tools** → **Device Manager**
2. **Create Virtual Device**
3. Choose **Pixel 5** → **API 33**
4. Click **▶️ Run**

### Real Device:
1. Enable **Developer Options** + **USB Debugging**
2. Connect USB cable
3. Accept debugging prompt on device
4. Click **▶️ Run**

---

## 🎯 Important Notes

- First build takes **10-15 minutes**
- Subsequent builds: **1-2 minutes**
- Android Studio includes embedded Java
- No need to install Java separately

---

**Read ANDROID_STUDIO_GUIDE.md for full documentation!**
