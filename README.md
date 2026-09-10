<div align="center">

# KHW Studio

**AI-assisted application development · Web · Desktop · Mobile**

Practical business applications, tools for Arabic interfaces, and experiments with AI agents.

[Explore the portfolio](https://khw-studio.vercel.app) · [Browse repositories](https://github.com/kahlelhawary-art?tab=repositories)

</div>

## About this portfolio

This portfolio brings together business applications, developer tools, and creative web projects built with AI-assisted workflows. The work spans pharmacy management, service-business administration, multilingual interfaces, and AI agent tooling.

The projects below link to source code, published packages, or live demonstrations where available. Private deployments are identified explicitly. Technologies describe the tools used in each project.

## Business applications

### Sore Care

Management system a German home-care business runs every day — client records, scheduling, service documentation and invoicing in one place. Private deployment, no public link

**Built with:** React · Vite · Supabase

No public demo or source link listed.

### KHW Pharmacy — Desktop

Pharmacy management suite for Windows, shipping at v0.1.7 — point of sale, FIFO inventory by expiry batch, reports, bilingual AR/EN, auto-update, and a licensing server

**Built with:** Electron · React · TypeScript · SQLite · Tailwind

[Download](https://github.com/kahlelhawary-art/KHW/releases/latest)

### KHW Pharmacy — Mobile

Offline-first Android companion — the full point of sale runs on-device with no server, plus barcode scanning, thermal printing, and JSON backup

**Built with:** Capacitor · React · TypeScript · Dexie · Tailwind

No public demo or source link listed.

## Developer tools and AI frameworks

### rtl-lint

Published on npm — finds layout that breaks in Arabic and Hebrew: physical CSS properties, directional Tailwind utilities, missing `dir`, each with the logical fix. Zero dependencies, 44 tests

**Built with:** Node.js · CLI

[npm](https://www.npmjs.com/package/rtl-lint) · [Code](https://github.com/kahlelhawary-art/rtl-lint)

### rtl-mcp

Published on npm — an MCP server that gives a coding agent right-to-left awareness: lint code for RTL breakage, normalise Arabic for search keys, detect script direction. Protocol layer written without the reference SDK's 17 dependencies, then verified against its client in CI

**Built with:** Node.js · MCP

[npm](https://www.npmjs.com/package/rtl-mcp) · [Code](https://github.com/kahlelhawary-art/rtl-mcp)

### electron-capacitor-starter

Template: one React codebase shipping as a Windows app, an Android app and a web app, joined by a single storage interface — SQLite via `node:sqlite` on the desktop, IndexedDB on the device, one contract suite run against both. CI boots the real Electron app and builds the installer

**Built with:** Electron · Capacitor · React · TypeScript · SQLite

[Code](https://github.com/kahlelhawary-art/electron-capacitor-starter)

### FlowAgent

Published on PyPI — AI agent orchestration framework with automatic parallelisation of independent steps, a built-in RAG engine, and a runtime plugin system

**Built with:** Python · TypeScript · Go

[PyPI](https://pypi.org/project/flowagent-framework/) · [Code](https://github.com/kahlelhawary-art/FlowAgent)

## More applications and web experiences

### PhD Match DE

Matches candidates to open PhD positions in German life-sciences programs — AI matching, PDF parsing, trilingual DE/EN/AR

**Built with:** React · Supabase · Tailwind · PDF.js

[Live](https://phd-match-de.vercel.app) · [Code](https://github.com/kahlelhawary-art/phd-match-de)

### TaskFlow

Full-stack task management app with auth, boards, and real-time updates

**Built with:** React · FastAPI · PostgreSQL

[Live](https://taskflow-frontend-ezbw.onrender.com) · [Code](https://github.com/kahlelhawary-art/TaskFlow)

### CareerAgent

Autonomous job-application system — scrapes StepStone and Indeed Germany, tailors CV and cover letter with AI, then applies by email

**Built with:** FastAPI · SQLModel · OpenAI · React · TypeScript

No public demo or source link listed.

### Nuqoosh

Cinematic personalized poem pages as a keepsake gift — trilingual AR/EN/DE with scroll-reveal typography

**Built with:** JavaScript · Canvas · HTML5

[Live](https://nuqoosh.vercel.app) · [Code](https://github.com/kahlelhawary-art/nuqoosh)

### King Barber

Barbershop website with booking flow and gallery

**Built with:** React · Tailwind

[Live](https://king-barbier.vercel.app)

## Guides and resources

### Offline Developer Playbook

Staying productive as a developer with no internet at all — local code models, offline docs, pre-cached npm/PyPI/Docker, cloud-free backups. 1,400 lines across seven chapters, written twice in English and Arabic, with setup, verify, backup and drill scripts for Windows, macOS and Linux

**Built with:** PowerShell · Bash · Docs

[Code](https://github.com/kahlelhawary-art/offline-developer-playbook)

## Technologies used across the projects

| Area | Technologies |
| --- | --- |
| Web interfaces | React, TypeScript, JavaScript, Tailwind CSS, Vite |
| Visual experiences | Three.js, Framer Motion, GSAP, Canvas |
| Backend and AI | Python, Node.js, FastAPI, Express, LLM integrations, MCP |
| Desktop and mobile | Electron, Capacitor, Android |
| Data and deployment | PostgreSQL, SQLite, Supabase, IndexedDB, Firebase, Docker, Vercel |

## Explore the work

Start with the business applications for practical use cases, or browse the developer tools for installation instructions and tests. Project documentation contains the implementation details and setup requirements.

[Portfolio](https://khw-studio.vercel.app) · [All public repositories](https://github.com/kahlelhawary-art?tab=repositories)
