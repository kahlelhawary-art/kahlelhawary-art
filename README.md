<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,30:1a1b27,60:2d2a55,100:414868&height=220&section=header&text=KHW%20Studio&fontSize=60&fontColor=c0caf5&fontAlignY=45&animation=fadeIn" alt="KHW Studio Banner" width="100%"/>

</div>

## About

Full-stack developer building software that ships — a pharmacy management suite running on Windows
and Android, an autonomous job-application agent, and a management system a German home-care
business runs every day.

Most of my work sits where AI meets the web: agent pipelines, LLM tooling, and interfaces that make
both feel effortless. Everything I build is bilingual by default (AR/EN, often DE) — which is
where [rtl-lint](https://www.npmjs.com/package/rtl-lint) came from.

- **Focus** — full-stack products, AI agents, developer tooling
- **Currently exploring** — multi-agent orchestration and LLM reliability
- **Portfolio** — [khw-studio.vercel.app](https://khw-studio.vercel.app)
- **Contact** — [khaleelhw@gmail.com](mailto:khaleelhw@gmail.com)

## Selected Work

| Project | What it does | Built with | Links |
|---------|--------------|------------|-------|
| **electron-capacitor-starter** | Template: one React codebase shipping as a Windows app, an Android app and a web app, joined by a single storage interface — SQLite via `node:sqlite` on the desktop, IndexedDB on the device, one contract suite run against both. CI boots the real Electron app and builds the installer | Electron · Capacitor · React · TypeScript · SQLite | [Code](https://github.com/kahlelhawary-art/electron-capacitor-starter) |
| **Offline Developer Playbook** | Staying productive as a developer with no internet at all — local code models, offline docs, pre-cached npm/PyPI/Docker, cloud-free backups. 1,400 lines across seven chapters, written twice in English and Arabic, with setup, verify, backup and drill scripts for Windows, macOS and Linux | PowerShell · Bash · Docs | [Code](https://github.com/kahlelhawary-art/offline-developer-playbook) |
| **rtl-mcp** | Published on npm — an MCP server that gives a coding agent right-to-left awareness: lint code for RTL breakage, normalise Arabic for search keys, detect script direction. Protocol layer written without the reference SDK's 17 dependencies, then verified against its client in CI | Node.js · MCP | [npm](https://www.npmjs.com/package/rtl-mcp) · [Code](https://github.com/kahlelhawary-art/rtl-mcp) |
| **rtl-lint** | Published on npm — finds layout that breaks in Arabic and Hebrew: physical CSS properties, directional Tailwind utilities, missing `dir`, each with the logical fix. Zero dependencies, 44 tests | Node.js · CLI | [npm](https://www.npmjs.com/package/rtl-lint) · [Code](https://github.com/kahlelhawary-art/rtl-lint) |
| **KHW Pharmacy — Desktop** | Pharmacy management suite for Windows, shipping at v0.1.7 — point of sale, FIFO inventory by expiry batch, reports, bilingual AR/EN, auto-update, and a licensing server | Electron · React · TypeScript · SQLite · Tailwind | [Download](https://github.com/kahlelhawary-art/KHW/releases/latest) |
| **KHW Pharmacy — Mobile** | Offline-first Android companion — the full point of sale runs on-device with no server, plus barcode scanning, thermal printing, and JSON backup | Capacitor · React · TypeScript · Dexie · Tailwind | — |
| **Sore Care** | Management system a German home-care business runs every day — client records, scheduling, service documentation and invoicing in one place. Private deployment, no public link | React · Vite · Supabase | — |
| **CareerAgent** | Autonomous job-application system — scrapes StepStone and Indeed Germany, tailors CV and cover letter with AI, then applies by email | FastAPI · SQLModel · OpenAI · React · TypeScript | — |
| **PhD Match DE** | Matches candidates to open PhD positions in German life-sciences programs — AI matching, PDF parsing, trilingual DE/EN/AR | React · Supabase · Tailwind · PDF.js | [Live](https://phd-match-de.vercel.app) · [Code](https://github.com/kahlelhawary-art/phd-match-de) |
| **FlowAgent** | Published on PyPI — AI agent orchestration framework with automatic parallelisation of independent steps, a built-in RAG engine, and a runtime plugin system | Python · TypeScript · Go | [PyPI](https://pypi.org/project/flowagent-framework/) · [Code](https://github.com/kahlelhawary-art/FlowAgent) |
| **Veg Lab** | Android app for round-pattern analysis — Markov sequence models, prediction accuracy measured honestly, and an expected-value check on whether a winning bet exists at all | Capacitor · Android · JavaScript | — |
| **Nuqoosh** | Cinematic personalized poem pages as a keepsake gift — trilingual AR/EN/DE with scroll-reveal typography | JavaScript · Canvas · HTML5 | [Live](https://nuqoosh.vercel.app) · [Code](https://github.com/kahlelhawary-art/nuqoosh) |
| **TaskFlow** | Full-stack task management app with auth, boards, and real-time updates | React · FastAPI · PostgreSQL | [Live](https://taskflow-frontend-ezbw.onrender.com) · [Code](https://github.com/kahlelhawary-art/TaskFlow) |
| **Portfolio** | Cinematic developer portfolio with scroll-driven animations | React · TypeScript · Framer Motion | [Live](https://khw-studio.vercel.app) · [Code](https://github.com/kahlelhawary-art/Portfolio) |
| **King Barber** | Barbershop website with booking flow and gallery | React · Tailwind | [Live](https://king-barbier.vercel.app) |

## Tech Stack

**Frontend**

![React](https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB)
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=flat-square&logo=typescript&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-0F172A?style=flat-square&logo=tailwind-css&logoColor=38BDF8)
![Three.js](https://img.shields.io/badge/Three.js-000000?style=flat-square&logo=three.js&logoColor=white)
![Framer Motion](https://img.shields.io/badge/Framer_Motion-0055FF?style=flat-square&logo=framer&logoColor=white)
![GSAP](https://img.shields.io/badge/GSAP-88CE02?style=flat-square&logo=greensock&logoColor=black)

**Backend & AI**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=node.js&logoColor=white)
![Express](https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)

**Desktop & Mobile**

![Electron](https://img.shields.io/badge/Electron-47848F?style=flat-square&logo=electron&logoColor=white)
![Capacitor](https://img.shields.io/badge/Capacitor-119EFF?style=flat-square&logo=capacitor&logoColor=white)
![Android](https://img.shields.io/badge/Android-3DDC84?style=flat-square&logo=android&logoColor=white)

**Data & Infrastructure**

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3FCF8E?style=flat-square&logo=supabase&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=flat-square&logo=sqlite&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white)

## GitHub

<div align="center">

<img src="https://github-readme-stats-theta-rouge-30.vercel.app/api?username=kahlelhawary-art&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=7aa2f7&icon_color=7aa2f7&text_color=a9b1d6&rank_icon=github" height="165" alt="GitHub Stats"/>
&nbsp;&nbsp;
<img src="https://github-readme-stats-theta-rouge-30.vercel.app/api/top-langs/?username=kahlelhawary-art&layout=compact&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=7aa2f7&text_color=a9b1d6&langs_count=8" height="165" alt="Top Languages"/>

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/kahlelhawary-art/kahlelhawary-art/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/kahlelhawary-art/kahlelhawary-art/output/github-contribution-grid-snake.svg">
  <img alt="Contribution snake" src="https://raw.githubusercontent.com/kahlelhawary-art/kahlelhawary-art/output/github-contribution-grid-snake-dark.svg" width="100%">
</picture>

</div>

## Contact

[![Email](https://img.shields.io/badge/Email-khaleelhw%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:khaleelhw@gmail.com)
&nbsp;
[![Portfolio](https://img.shields.io/badge/Portfolio-khw--studio.vercel.app-7AA2F7?style=flat-square&logo=vercel&logoColor=white)](https://khw-studio.vercel.app)
&nbsp;
[![GitHub](https://img.shields.io/badge/GitHub-kahlelhawary--art-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/kahlelhawary-art)

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:414868,50:2d2a55,100:0d1117&height=100&section=footer" width="100%"/>

</div>
