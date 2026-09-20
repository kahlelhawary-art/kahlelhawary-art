# -*- coding: utf-8 -*-
import base64, pathlib
SD = pathlib.Path(__file__).parent; F = SD/"fonts"
def b64(p): return base64.b64encode((F/p).read_bytes()).decode()

AR_RANGE = "U+0600-06FF,U+0750-077F,U+0870-088E,U+08A0-08FF,U+FB50-FDFF,U+FE70-FEFF,U+200C-200F,U+2010-2011,U+204F,U+2E41,U+FBB2-FBC1"
faces = []
for w in (300,400,500,600,700):
    faces.append(f"@font-face{{font-family:'Plex Arabic';font-weight:{w};font-display:block;"
                 f"src:url(data:font/woff2;base64,{b64(f'ibm-plex-sans-arabic-arabic-{w}-normal.woff2')}) format('woff2');"
                 f"unicode-range:{AR_RANGE};}}")
for w,src in ((300,300),(400,400),(500,500),(600,700),(700,700)):
    faces.append(f"@font-face{{font-family:'Plex Arabic';font-weight:{w};font-display:block;"
                 f"src:url(data:font/woff2;base64,{b64(f'ibm-plex-sans-arabic-latin-{src}-normal.woff2')}) format('woff2');}}")
for w,f in ((400,'IBMPlexMono-Regular.ttf'),(700,'IBMPlexMono-Bold.ttf')):
    faces.append(f"@font-face{{font-family:'Plex Mono';font-weight:{w};font-display:block;"
                 f"src:url(data:font/ttf;base64,{b64(f)}) format('truetype');}}")

# ── editor lines: keyword / type / string / ident / comment, shaped like real source ──
K,T,S,I,C,N = "#7AA2F7","#7DCFFF","#9ECE6A","#7E8CA6","#39445C","#E0AF68"
LINES = [
 (0,[(28,C,.85),(74,C,.85)]),
 (0,[(34,K,.95),(58,T,.9),(20,I,.7),(96,S,.85)]),
 (0,[(34,K,.95),(46,I,.75),(64,T,.9)]),
 (0,[]),
 (0,[(40,K,.95),(88,T,.95),(16,I,.6)]),
 (14,[(52,I,.8),(30,T,.8),(24,N,.85)]),
 (14,[(44,I,.8),(70,S,.85)]),
 (14,[(38,K,.9),(56,I,.75),(28,T,.8),(18,N,.8)]),
 (28,[(66,I,.7),(34,T,.75),(48,S,.75)]),
 (14,[(22,I,.6)]),
 (0,[]),
 (0,[(30,C,.8),(96,C,.8)]),
 (0,[(34,K,.95),(62,T,.9),(26,I,.7)]),
 (14,[(48,K,.85),(40,I,.7),(58,T,.8),(22,N,.8)]),
 (14,[(36,I,.7),(78,S,.8),(20,I,.55)]),
 (0,[(18,I,.5)]),
]
code = []
for i,(ind,bars) in enumerate(LINES, start=1):
    inner = "".join(f'<b style="width:{w}px;background:{c};opacity:{o}"></b>' for w,c,o in bars)
    code.append(f'<div class="cl"><span class="g">{i}</span>'
                f'<span style="display:flex;gap:7px;margin-left:{ind}px">{inner}</span></div>')

# ── services ──
def svc(icon, name, sub):
    return (f'<div class="svc"><span class="ic">{icon}</span><span><span class="n">{name}</span>'
            f'<span class="s">{sub}</span></span></div>')
ST='stroke="#7AA2F7" stroke-width="1.3" fill="none" stroke-linecap="round" stroke-linejoin="round"'
SV = [
 svc(f'<svg width="20" height="20" viewBox="0 0 20 20"><rect x="2" y="3.5" width="16" height="13" rx="2" {ST}/>'
     f'<path d="M2 7.5h16" {ST}/><circle cx="4.8" cy="5.5" r=".8" fill="#7AA2F7"/><circle cx="7.2" cy="5.5" r=".8" fill="#7AA2F7"/></svg>',
     "تطبيقات ويب كاملة", "React + TypeScript — لوحات تحكم وتقارير"),
 svc(f'<svg width="20" height="20" viewBox="0 0 20 20"><rect x="1.6" y="3.5" width="11.5" height="9" rx="1.6" {ST}/>'
     f'<path d="M5.5 16h5.5" {ST}/><path d="M7.4 12.5V16" {ST}/><rect x="14" y="7.5" width="4.6" height="8.5" rx="1.3" {ST}/></svg>',
     "ويندوز وأندرويد من كود واحد", "Electron + Capacitor — ملف تثبيت و APK جاهز"),
 svc(f'<svg width="20" height="20" viewBox="0 0 20 20"><ellipse cx="10" cy="5" rx="6.6" ry="2.6" {ST}/>'
     f'<path d="M3.4 5v5c0 1.4 3 2.6 6.6 2.6s6.6-1.2 6.6-2.6V5" {ST}/>'
     f'<path d="M3.4 10v4.6c0 1.4 3 2.6 6.6 2.6s6.6-1.2 6.6-2.6V10" {ST}/></svg>',
     "أنظمة إدارة داخلية", "مخزون، فواتير، حجوزات، ومتابعة عملاء"),
 svc(f'<svg width="20" height="20" viewBox="0 0 20 20"><rect x="5.2" y="5.2" width="9.6" height="9.6" rx="1.8" {ST}/>'
     f'<rect x="8.4" y="8.4" width="3.2" height="3.2" rx=".8" fill="#7AA2F7"/>'
     f'<path d="M8 5.2V2.6M12 5.2V2.6M8 17.4v-2.6M12 17.4v-2.6M14.8 8h2.6M14.8 12h2.6M2.6 8h2.6M2.6 12h2.6" {ST}/></svg>',
     "دمج الذكاء الاصطناعي", "وكلاء، أتمتة، RAG، وربط الـ APIs"),
 svc(f'<svg width="20" height="20" viewBox="0 0 20 20"><path d="M17 6.5H8.5a3 3 0 100 6H10" {ST}/>'
     f'<path d="M13.2 4.2 16.6 6.5 13.2 8.8" {ST}/><path d="M3 15.5h14" {ST}/><path d="M6.8 13.2 3.4 15.5l3.4 2.3" {ST}/></svg>',
     "إصلاح الواجهات بالعربي", "الاتجاه، الخطوط، التواريخ، الأرقام، والتنسيق المعكوس"),
 svc(f'<svg width="20" height="20" viewBox="0 0 20 20"><path d="M14.6 15.5H5.4a3.4 3.4 0 01-.5-6.8 4.8 4.8 0 019.1-1.5" {ST}/>'
     f'<path d="M3 3l14 14" {ST}/><path d="M14.4 9a3.3 3.3 0 012.8 3.2c0 1-.4 1.9-1.1 2.5" {ST}/></svg>',
     "تطبيقات تشتغل بدون إنترنت", "قاعدة بيانات محلية، ومزامنة لما يرجع النت"),
]

html = (SD/"ad.html").read_text(encoding="utf-8")
html = html.replace("__FONTS__", "\n".join(faces))
html = html.replace("__CODE__", "".join(code))
html = html.replace("__SERVICES__", "".join(SV))
html = html.replace("مع تنفيذ متوازٍ للخطوات المستقلة ومحرك RAG",
                    "مع تشغيل الخطوات المستقلة بالتوازي، ومحرك RAG جاهز")
(SD/"ad.out.html").write_text(html, encoding="utf-8")
print("ad.out.html", len(html))
