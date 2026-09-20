# ملفات الإعلان — KHW Studio

| الملف | المقاس | الاستخدام |
|-------|--------|-----------|
| `khw-ad-print.png` | 2800 × 4460 | النسخة الكاملة بأعلى دقة — طباعة، أو رفع على لينكدإن/بيهانس |
| `khw-ad-web.png` | 1400 × 2230 | نسخة أخف — واتساب، فيسبوك، تيليغرام، إرسال مباشر لعميل |
| `khw-poster-minimal.png` | 2400 × 3000 | نسخة مختصرة هادئة (4:5) — مناسبة لستوري إنستغرام أو بوست واحد |

النصوص كلها مأخوذة من `../freelance-ad.md`، وما فيها أي رقم أو ادعاء ما إله أساس
في الأعمال المنشورة فعلياً.

## إعادة البناء

```bash
# الخطوط (IBM Plex Sans Arabic — رخصة OFL) من npm مباشرة
mkdir -p fonts && cd fonts
npm pack @fontsource/ibm-plex-sans-arabic && tar -xzf *.tgz
cp package/files/ibm-plex-sans-arabic-{arabic-{300,400,500,600,700},latin-{300,400,500,700}}-normal.woff2 .
# و IBMPlexMono-Regular.ttf + IBMPlexMono-Bold.ttf بنفس المجلد

# التوليد ثم التصدير عبر Chromium (الأرقام والحروف العربية بتنرسم صح بالمتصفح فقط)
python3 src-build.py          # بيدمج الخطوط ويولّد ad.out.html
node shoot_ad.js              # لقطة بدقة 2x
```

الفلسفة البصرية اللي انبنى عليها التصميم في `DESIGN-PHILOSOPHY.md`.
