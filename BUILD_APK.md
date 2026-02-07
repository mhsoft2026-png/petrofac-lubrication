# دليل بناء تطبيق APK - Petrofac Lubrication

## ✅ تم إعداد المشروع بنجاح!

تم تحويل التطبيق إلى مشروع أندرويد باستخدام Capacitor.

---

## 📋 متطلبات بناء APK:

### 1. تثبيت Android Studio
- حمّل Android Studio من: https://developer.android.com/studio
- ثبّت Android SDK و Gradle

### 2. تثبيت Java Development Kit (JDK)
- حمّل JDK 17 من: https://www.oracle.com/java/technologies/downloads/
- أضف JAVA_HOME إلى متغيرات البيئة

---

## 🔨 طريقة بناء APK:

### الطريقة 1: باستخدام Android Studio (الأسهل)

```powershell
# 1. افتح المشروع في Android Studio
npx cap open android

# 2. في Android Studio:
#    - Build > Build Bundle(s) / APK(s) > Build APK(s)
#    - انتظر حتى ينتهي البناء
#    - ستجد الملف في: android/app/build/outputs/apk/debug/app-debug.apk
```

### الطريقة 2: باستخدام سطر الأوامر

```powershell
# 1. انتقل إلى مجلد android
cd android

# 2. بناء APK
./gradlew assembleDebug

# 3. ستجد APK في:
# android/app/build/outputs/apk/debug/app-debug.apk
```

### الطريقة 3: بناء APK موقّع للإنتاج

```powershell
# في مجلد android
./gradlew assembleRelease

# APK في: android/app/build/outputs/apk/release/app-release-unsigned.apk
```

---

## 📱 تثبيت APK على الهاتف:

### الطريقة 1: USB
1. فعّل وضع المطور في هاتفك (Developer Mode)
2. فعّل USB Debugging
3. وصّل الهاتف بالكمبيوتر
4. شغّل: `npx cap run android`

### الطريقة 2: نقل الملف
1. انقل ملف `app-debug.apk` إلى الهاتف
2. افتح الملف من File Manager
3. اسمح بتثبيت التطبيقات من مصادر غير معروفة
4. ثبّت التطبيق

---

## 🔄 تحديث التطبيق:

إذا قمت بتعديل الكود:

```powershell
# 1. بناء التطبيق
npm run build

# 2. مزامنة مع أندرويد
npx cap sync

# 3. بناء APK جديد
npx cap open android
# ثم Build > Build APK
```

---

## 📊 معلومات التطبيق:

- **اسم التطبيق:** Petrofac Lubrication
- **معرّف الحزمة:** com.petrofac.lubrication
- **الإصدار:** 1.0.0
- **عدد المعدات:** 827
- **النظام:** Dark Theme Professional

---

## ⚠️ ملاحظات مهمة:

1. **APK Debug:** للتجربة والتطوير فقط
2. **APK Release:** للنشر والإنتاج (يحتاج توقيع)
3. **الحجم:** حوالي 5-10 MB
4. **الأذونات:** الإنترنت (لـ Gemini AI)

---

## 🐛 حل المشاكل:

### إذا فشل البناء:
```powershell
# تنظيف المشروع
cd android
./gradlew clean

# إعادة البناء
./gradlew assembleDebug
```

### إذا لم يعمل Gradle:
```powershell
# تحديث Gradle Wrapper
cd android
./gradlew wrapper --gradle-version=8.0
```

---

## 🎉 بعد التثبيت:

التطبيق سيعمل بشكل كامل على الهاتف مع:
- ✅ جميع المعدات (827)
- ✅ البحث الدقيق
- ✅ الواجهة الاحترافية
- ✅ النظام الداكن
- ✅ التنقل السلس

---

## 📞 دعم إضافي:

للمزيد من المعلومات:
- Capacitor Docs: https://capacitorjs.com/docs
- Android Studio: https://developer.android.com/studio/build
