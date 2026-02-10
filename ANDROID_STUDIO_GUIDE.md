# 🚀 فتح المشروع في Android Studio

## ✅ المشروع جاهز تماماً لـ Android Studio!

### الخطوة 1: تحميل Android Studio

إذا لم يكن مثبتاً:
1. حمّل من: https://developer.android.com/studio
2. ثبّت مع SDK Tools
3. انتظر حتى ينتهي التثبيت الكامل (حوالي 10 دقائق)

---

### الخطوة 2: فتح المشروع

1. **افتح Android Studio**

2. **اختر "Open"** (وليس New Project)

3. **انتقل إلى:**
   ```
   C:\Users\houar\OneDrive\Desktop\said\android
   ```

4. **اضغط "OK"**

5. **انتظر Gradle Sync** (أول مرة تأخذ 5-10 دقائق)

---

### الخطوة 3: تكوين SDK (إذا لزم الأمر)

إذا ظهرت رسالة "SDK not found":

1. اذهب: **File** → **Project Structure** → **SDK Location**

2. أدخل موقع Android SDK:
   ```
   C:\Users\houar\AppData\Local\Android\Sdk
   ```

3. اضغط **Apply** → **OK**

---

### الخطوة 4: بناء APK

#### الطريقة 1: من القائمة
1. **Build** → **Build Bundle(s) / APK(s)** → **Build APK(s)**
2. انتظر البناء (2-5 دقائق أول مرة)
3. اضغط **locate** لفتح مجلد APK

#### الطريقة 2: من Terminal في Android Studio
```bash
# Debug APK
gradlew assembleDebug

# Release APK (غير موقّع)
gradlew assembleRelease
```

---

### الخطوة 5: تشغيل على المحاكي/الجهاز

1. **وصّل جهاز Android** أو **شغّل Emulator**

2. **اضغط زر "Run"** (▶️ الأخضر) في الأعلى

3. **اختر الجهاز**

4. **انتظر التثبيت والتشغيل**

---

## 📦 مواقع الملفات المهمة

### APK بعد البناء:
```
android/app/build/outputs/apk/debug/app-debug.apk
```

### الكود المصدري:
```
android/app/src/main/java/com/petrofac/lubrication/MainActivity.java
```

### الموارد:
```
android/app/src/main/res/
```

### ملفات Web:
```
android/app/src/main/assets/public/
```

---

## 🔧 الأوامر المفيدة

### في Terminal الخاص بـ Android Studio:

```bash
# تنظيف المشروع
gradlew clean

# بناء Debug
gradlew assembleDebug

# بناء Release
gradlew assembleRelease

# تثبيت على جهاز متصل
gradlew installDebug

# عرض المهام المتاحة
gradlew tasks
```

---

## ⚙️ إعدادات مهمة

### تفعيل Developer Options على Android:
1. **Settings** → **About Phone**
2. اضغط **Build Number** 7 مرات
3. ارجع → **Developer Options**
4. فعّل **USB Debugging**

### تسريع Build:
في `android/gradle.properties` (موجود مسبقاً):
```properties
org.gradle.jvmargs=-Xmx2048m
org.gradle.daemon=true
org.gradle.configureondemand=true
android.enableJetifier=true
android.useAndroidX=true
```

---

## 🐛 حل المشاكل الشائعة

### "SDK not found"
- حدد مسار SDK في Project Structure

### "Gradle sync failed"
- **File** → **Invalidate Caches** → **Restart**

### "Unable to find Java"
- Android Studio يأتي مع Java مدمج، استخدمه:
  - **File** → **Project Structure** → **SDK Location** → **JDK Location**
  - اختر: Embedded JDK

### "APK not building"
```bash
# في Terminal:
gradlew clean
gradlew assembleDebug --stacktrace
```

---

## 📱 اختبار التطبيق

### على المحاكي:
1. **Tools** → **Device Manager**
2. **Create Virtual Device**
3. اختر **Pixel 5** أو أي جهاز
4. اختر **API 33** (Android 13)
5. **Finish** → **Run**

### على جهاز حقيقي:
1. فعّل **USB Debugging**
2. وصّل كابل USB
3. اقبل **Allow USB Debugging** على الجهاز
4. اضغط **Run** في Android Studio

---

## 🎯 ملاحظات مهمة

✅ **المشروع جاهز** - كل الملفات موجودة
✅ **827 معدة** - البيانات كاملة
✅ **Capacitor مزامن** - أحدث إصدار
✅ **Gradle مكوّن** - جاهز للبناء
✅ **Dark Theme** - مطبّق بالكامل

---

## 🚀 خطوات سريعة (TL;DR)

1. حمّل Android Studio
2. افتح مجلد `android`
3. انتظر Gradle Sync
4. **Build** → **Build APK**
5. ستجد APK في `app/build/outputs/apk/debug/`

---

## 💡 نصيحة

**أول مرة يأخذ وقت طويل** (10-15 دقيقة)
- تحميل Gradle dependencies
- بناء المشروع أول مرة
- تكوين Android SDK

**من المرة الثانية** سيكون سريع جداً (1-2 دقيقة)!

---

**بالتوفيق! 🎉**
