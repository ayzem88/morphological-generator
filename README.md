# المولد الصرفي / Morphological Generator

<div dir="rtl">

## نظرة عامة

نظام متقدم لتوليد الصيغ الصرفية العربية من الجذور. يدعم توليد التصريفات والمشتقات للجذور الثلاثية والرباعية (الصحيحة والمعتلة والمهموزة) باستخدام خوارزميات متقدمة.

## المميزات

- ✅ توليد التصريفات والمشتقات للجذور الثلاثية الصحيحة
- ✅ توليد التصريفات والمشتقات للجذور الثلاثية المعتلة
- ✅ توليد التصريفات والمشتقات للجذور الثلاثية المهموزة
- ✅ توليد التصريفات والمشتقات للجذور الرباعية
- ✅ معالجة تاء الافتعال
- ✅ توحيد الهمزات
- ✅ دمج المتماثل والمتجانس من الحروف
- ✅ معالجة الجذور المفصولة

## التثبيت

### المتطلبات

- Python 3.7 أو أحدث
- مكتبات Python المطلوبة (سيتم تثبيتها تلقائياً)

### خطوات التثبيت

1. استنسخ المستودع:
```bash
git clone https://github.com/ayzem88/morphological-generator.git
cd morphological-generator
```

2. قم بتشغيل البرامج النصية مباشرة:
```bash
python "01 نظام_التصريف_والاشتقاق_للثلاثي.py"
```

## الاستخدام

### توليد التصريفات للجذور الثلاثية

```bash
python "01 نظام_التصريف_والاشتقاق_للثلاثي.py"
```

### توليد التصريفات للجذور الرباعية

```bash
python "01 نظام_التصريف_والاشتقاق_للرباعي.py"
```

## هيكل المشروع

```
المولد الصرفي/
├── الثلاثي الصحيح المهموز/
│   ├── 01 نظام_التصريف_والاشتقاق_للثلاثي.py
│   ├── التصريفات والمشتقات/
│   └── [ملفات الأوزان والجذور]
├── الثلاثي_المعتل_المهموز/
│   ├── التوليد_الآلي/
│   └── [ملفات المعالجة]
├── الرباعي الصحيح المعتل المهموز/
│   ├── 01 نظام_التصريف_والاشتقاق_للرباعي.py
│   └── [ملفات التصريفات]
└── كشكول/
    └── [ملفات إضافية]
```

## الملفات الرئيسية

- **نظام_التصريف_والاشتقاق_للثلاثي.py**: توليد التصريفات للجذور الثلاثية
- **نظام_التصريف_والاشتقاق_للرباعي.py**: توليد التصريفات للجذور الرباعية
- **معدل_الهمزات.py**: توحيد الهمزات
- **قلب_تاء_الافتعال.py**: معالجة تاء الافتعال
- **دمج_المتماثل_من_الحروف.py**: دمج المتماثل

## ملاحظات مهمة

⚠️ **ملاحظة**: بعض ملفات البيانات الكبيرة غير مرفوعة في المستودع. يمكنك إضافة ملفاتك الخاصة في المجلدات المناسبة.

## التطوير المستقبلي

- [ ] واجهة رسومية (GUI)
- [ ] دعم المزيد من أنواع الجذور
- [ ] تحسين الأداء
- [ ] تصدير النتائج بصيغ متعددة

## المساهمة

نرحب بمساهماتكم! يرجى قراءة [CONTRIBUTING.md](CONTRIBUTING.md) للمزيد من التفاصيل.

## الترخيص

هذا المشروع مخصص للاستخدام الأكاديمي والبحثي.

## عن المطور

**أيمن الطيّب بن نجي** ([ayzem88](https://github.com/ayzem88))

خبير لغوي في معجم الدوحة التاريخي للغة العربية، مهتم بالأدوات والبرامج اللغوية، ومبرمج Vibe Coding.

🌐 **الموقع الشخصي**: [aymannji.com](https://www.aymannji.com/)

## منهج التطوير

أُعتمد في مشاريعي البرمجية على منهج Vibe Coding؛ أسلوب يتجاوز كتابة كلّ سطر يدوياً، إذ أوجّه نماذج الذكاء الاصطناعي بوصف منطقي وواضح للوظيفة المطلوبة، ثم أُقيّم النتائج وأُدخِل التحسينات.

هذا النهج يعزّز السرعة في إنشاء النماذج الأولية والوِحدات البرمجية، ويمنحني تركيزاً أكبر على التصوّر العام والتصميم بدلاً من التفاصيل الدقيقة.

في هذا المستودع، تجد أدوات ومشاريع بُنيت بهذه المقاربة — يُرحّب بتجربتها والمساهمة فيها.

## المطور

تم تطوير هذا المشروع بواسطة **أيمن الطيّب بن نجي** ([ayzem88](https://github.com/ayzem88))

---

# [English]

<div dir="ltr">

## Overview

An advanced system for generating Arabic morphological forms from roots. Supports generating conjugations and derivatives for trilateral and quadrilateral roots (sound, weak, and hamzated) using advanced algorithms.

## Features

- ✅ Generate conjugations and derivatives for sound trilateral roots
- ✅ Generate conjugations and derivatives for weak trilateral roots
- ✅ Generate conjugations and derivatives for hamzated trilateral roots
- ✅ Generate conjugations and derivatives for quadrilateral roots
- ✅ Handle tā' al-ifti'āl
- ✅ Unify hamzas
- ✅ Merge identical and similar letters
- ✅ Process separated roots

## Installation

### Requirements

- Python 3.7 or later
- Required Python libraries (will be installed automatically)

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/ayzem88/morphological-generator.git
cd morphological-generator
```

2. Run the scripts directly:
```bash
python "01 نظام_التصريف_والاشتقاق_للثلاثي.py"
```

## Usage

### Generate Conjugations for Trilateral Roots

```bash
python "01 نظام_التصريف_والاشتقاق_للثلاثي.py"
```

### Generate Conjugations for Quadrilateral Roots

```bash
python "01 نظام_التصريف_والاشتقاق_للرباعي.py"
```

## Project Structure

```
morphological-generator/
├── الثلاثي الصحيح المهموز/
│   ├── 01 نظام_التصريف_والاشتقاق_للثلاثي.py
│   ├── التصريفات والمشتقات/
│   └── [Pattern and root files]
├── الثلاثي_المعتل_المهموز/
│   ├── التوليد_الآلي/
│   └── [Processing files]
├── الرباعي الصحيح المعتل المهموز/
│   ├── 01 نظام_التصريف_والاشتقاق_للرباعي.py
│   └── [Conjugation files]
└── كشكول/
    └── [Additional files]
```

## Main Files

- **نظام_التصريف_والاشتقاق_للثلاثي.py**: Generate conjugations for trilateral roots
- **نظام_التصريف_والاشتقاق_للرباعي.py**: Generate conjugations for quadrilateral roots
- **معدل_الهمزات.py**: Unify hamzas
- **قلب_تاء_الافتعال.py**: Handle tā' al-ifti'āl
- **دمج_المتماثل_من_الحروف.py**: Merge identical letters

## Important Notes

⚠️ **Note**: Some large data files are not uploaded to the repository. You can add your own files in the appropriate folders.

## Future Development

- [ ] Graphical user interface (GUI)
- [ ] Support for more root types
- [ ] Performance improvements
- [ ] Export results in multiple formats

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

This project is intended for academic and research use.

## About the Developer

**Ayman Atieb ben NJi** ([ayzem88](https://github.com/ayzem88))

Linguistic expert at the Historical Dictionary of the Arabic Language of Qatar (Doha Dictionary), interested in linguistic tools and software, and a Vibe Coding programmer.

🌐 **Personal Website**: [aymannji.com](https://www.aymannji.com/)

## Development Approach

I adopt the Vibe Coding paradigm in my software projects: rather than writing every line manually, I direct AI models with clear natural-language descriptions of the desired functionality, then evaluate and refine the generated code.

This approach accelerates prototype and module creation, allowing me to focus more on concept and design than on low-level implementation details.

In this repository you'll find tools and projects developed with this mindset — feel free to explore and contribute.

## Developer

Developed by **Ayman Atieb ben NJi** ([ayzem88](https://github.com/ayzem88))

</div>

