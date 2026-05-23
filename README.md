<p align="center">
  <a href="https://github.com/Branding-Brevity/Core-Builds-By-Brevity/releases/latest">
    <img src="https://github.com/Branding-Brevity/Core-Builds-By-Brevity/raw/refs/heads/main/Assets/core_builds_banner.svg" alt="Core Builds Banner" width="100%"/>
  </a>
</p>

<p align="center">
  <a href="https://github.com/Branding-Brevity/Core-Builds-By-Brevity/actions/workflows/validate.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/Branding-Brevity/Core-Builds-By-Brevity/validate.yml?style=for-the-badge&label=BUILD&logo=github&logoColor=white&labelColor=1a1f27&color=2ea44f" alt="Build Status"/>
  </a>
  <a href="https://github.com/Branding-Brevity/Core-Builds-By-Brevity/releases/latest">
    <img src="https://img.shields.io/github/v/release/Branding-Brevity/Core-Builds-By-Brevity?style=for-the-badge&label=RELEASE&logo=github&logoColor=white&labelColor=1a1f27&color=00d4ff" alt="Latest Release"/>
  </a>
  <a href="https://github.com/Branding-Brevity/Core-Builds-By-Brevity/stargazers">
    <img src="https://img.shields.io/github/stars/Branding-Brevity/Core-Builds-By-Brevity?style=for-the-badge&label=STARS&logo=github&logoColor=white&labelColor=1a1f27&color=00d4ff" alt="Stars"/>
  </a>
  <a href="https://ko-fi.com/branding_brevity">
    <img src="https://img.shields.io/badge/DONATE-Ko--fi-ff5f5f?style=for-the-badge&logo=ko-fi&logoColor=white&labelColor=1a1f27" alt="Donate"/>
  </a>
</p>

**Core Builds** is a collection of highly optimised, frictionless AIOStreams templates — engineered to serve only the highest quality compatible streams, strip out unplayable clutter, and work reliably across every host and device.

---

## 📦 Templates

Templates are grouped by service combination and use case. Every template includes full release group scoring, strict title and episode matching, Tamtaro ESEs, and the complete 12-service opt-in roster.

### ⛓️ Dual Service — TorBox Pro + Real-Debrid

TorBox handles Usenet and uncached traffic. Real-Debrid serves cached streams only, with full RD Infringing File Scrub for account protection.

| Template | Resolution | Best For | Docs |
|---|---|---|---|
| [Dual Core 1080p](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Dual/core-nexus-dual-core-1080p.json) | 1080p SDR | Budget hardware, phones, tablets | [README](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Dual/README_dual-core-1080p.md) |
| [Dual Core 4K](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Dual/core-nexus-4k-dual-core.json) | 4K HDR | Shield, Apple TV 4K, OLED/QLED | [README](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Dual/README_4k-dual-core.md) |
| [4K Essential + RD](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Dual/core-nexus-4k-essential-dual-core.json) | 4K HDR | TorBox Essential plan + Real-Debrid | [README](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Dual/README_4k-essential-dual-core.md) |

### 📦 Single Service — TorBox Only

No secondary debrid service required. TorBox Pro builds include Usenet. TorBox Essential builds use torrent cache only.

| Template | Plan | Resolution | Best For | Docs |
|---|---|---|---|---|
| [TorBox Exclusive (RPDB)](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Single/core-nexus-torbox-exclusive_rpdb.json) | Pro | 1080p SDR | Budget hardware, RPDB poster art | [README](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Single/README_torbox-exclusive-rpdb.md) |
| [4K Home Theater](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Single/core-nexus-4k-ht-torbox.json) | Pro | 4K HDR | Shield, Apple TV 4K, full HT setup | [README](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Single/README_4k-ht-torbox.md) |
| [1080p Essential](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/refs/heads/main/Templates/Torbox/Single/core-nexus-1080p-essential-torbox.json) | Essential | 1080p SDR | Budget hardware, no Usenet needed | — |
| [4K Essential](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/refs/heads/main/Templates/Torbox/Single/core-nexus-4k-essential-torbox.json) | Essential | 4K HDR | Shield, Apple TV 4K, no Usenet needed | — |

### 🔀 Hybrid — TorBox Pro + Usenet Indexer

Combines TorBox with NZBGeek for maximum source diversity. Shows both cached and uncached streams.

| Template | Resolution | Best For | Docs |
|---|---|---|---|
| [TB Hybrid 1080p](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Hybrid/core-nexus-tb-hybrid-1080p.json) | 1080p SDR | TorBox Pro + NZBGeek subscribers | [README](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Hybrid/README_tb-hybrid-1080p.md) |

> ⚠️ Requires a **NZBGeek API key** — enter it in the Addons section after loading. See the [Import Guide](Guides/IMPORT_GUIDE.md) for the setup step.

### ⚡ Speed Tier — Instant Autoplay

Stripped to 4 addons only (Library, TorBox Search, Comet, Zilean) for 2-3 second cached stream delivery. For users who prioritise instant results over maximum coverage.

#### TorBox Essential + EasyNews

| Template | Resolution | Docs |
|---|---|---|
| [Speed 1080p (EasyNews)](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/refs/heads/main/Templates/Torbox/Speed/EasyNews/core-nexus-speed-1080p.json) | 1080p SDR | [README](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/refs/heads/main/Templates/Torbox/Speed/EasyNews/README_speed-1080p-easynews.md) |
| [Speed 4K (EasyNews)](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/refs/heads/main/Templates/Torbox/Speed/EasyNews/core-nexus-speed-4k.json) | 4K HDR | [README](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/refs/heads/main/Templates/Torbox/Speed/EasyNews/README_speed-4k-easynews.md) |

#### TorBox Essential Only

| Template | Resolution | Docs |
|---|---|---|
| [Speed 1080p](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/refs/heads/main/Templates/Torbox/Speed/TorBox/core-nexus-speed-1080p-torbox.json) | 1080p SDR | [README](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/refs/heads/main/Templates/Torbox/Speed/TorBox/README_speed-1080p-torbox.md) |
| [Speed 4K](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/refs/heads/main/Templates/Torbox/Speed/TorBox/core-nexus-speed-4k-torbox.json) | 4K HDR | [README](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/refs/heads/main/Templates/Torbox/Speed/TorBox/README_speed-4k-torbox.md) |

> Speed templates use 3500ms timeouts, 10 results max, and a 5-key sort. All Core Builds features (scored regex ranking, Tamtaro ESEs, episode matching) remain intact.

### 🌙 Nightly Versions

Nightly versions of all standard templates are available with live-synced Tamtaro SEL stack and Vidhin05 ranked expressions. **Nightly and whitelisted AIOStreams hosts only** — will fail to import on stable instances.

Find them in `Templates/Torbox/Nightly/` — same filenames as the standard builds.

---

## 🌍 Universal Debrid Support

All templates ship with the **full 12-service roster** pre-loaded and set to opt-in. Enable only the services you actually subscribe to — the rest are ignored:

`TorBox` · `Real-Debrid` · `AllDebrid` · `Premiumize` · `DebridLink` · `Offcloud` · `Put.io` · `EasyNews` · `EasyDebrid` · `PikPak` · `Seedr` · `Debrider`

---

## 📱 Device Profiles

AIOStreams can't detect what device is requesting a stream — every request looks identical. Use **two separate Stremio accounts** for mixed households:

- **Low-End Account** → 1080p SDR template on phones, tablets, budget TVs
- **High-End Account** → 4K template on Shield, Apple TV 4K, OLED/QLED sets

See the [Device Profiles Guide](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Guides/DEVICE_PROFILES.md) for full setup instructions.

---

## 🎨 Custom Formatters

| Formatter | Style |
|---|---|
| **💎 Core Zenith Diamond** | Emoji-coded badges, smallcaps text. Service pool, resolution, quality, audio, SEADEX / OWNED / LIBRARY flags. |
| **📺 Core Clean Stream** | Minimal plain text. Matches native Stremio card layout. No emojis, no smallcaps. |

See the [Formatter Guide](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Guides/FORMATTER_GUIDE.md) for installation.

---

## ⚙️ Quick Start

### 1. Choose a Host

| Rank | Host | URL | Notes |
|------|------|-----|-------|
| 🥇 | **ElfHosted** | [aiostreams.elfhosted.com](https://aiostreams.elfhosted.com/stremio/configure) | Most stable. Debrid-only on public instance — suits these templates perfectly. |
| 🥈 | **Yeb's** | [aiostreams.fortheweak.cloud](https://aiostreams.fortheweak.cloud/stremio/configure) | AIOStreams Discord admin. Also offers [Nightly](https://aiostreams-nightly.fortheweak.cloud/stremio/configure). |
| 🥉 | **Midnight's** | [aiostreamsfortheweebsstable.midnightignite.me](https://aiostreamsfortheweebsstable.midnightignite.me/stremio/configure) | TorBox community manager. Also offers [Nightly](https://aiostreamsfortheweebs.midnightignite.me/stremio/configure). |
| 4 | **Viren's** | [aiostreams.viren070.me](https://aiostreams.viren070.me/stremio/configure) | Developer's own instance. Nightly only. |
| 5 | **Kuu's** | [aiostreams.stremio.ru](https://aiostreams.stremio.ru/stremio/configure) | Also offers [Nightly](https://aiostreams-nightly.stremio.ru/stremio/configure). |
| 6 | **ATBP Hosting** | [aio.atbphosting.com](https://aio.atbphosting.com/stremio/configure) | Community instance. |
| 7 | **Omni's** | [aiostreams.12312023.xyz](https://aiostreams.12312023.xyz/stremio/configure) | Community instance. |

Full instance list: [docs.aiostreams.viren070.me](https://docs.aiostreams.viren070.me/getting-started/public-instances/)

### 2. Import a Template

Paste a raw GitHub URL into the **Template Import** menu:

```
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Dual/core-nexus-4k-dual-core.json
```

### 3. Enable Your Services

Toggle on only the services you subscribe to — all 12 are pre-loaded and off by default.

### 4. Install

Click **Save**, copy the manifest URL, and paste it into Stremio or WuPlay.

Full walkthrough in the [Import Guide](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Guides/IMPORT_GUIDE.md).

---

## 🔧 Under the Hood

### All Templates
- **Hard CAM + YouTube kill** — CAM, SCR, TS, TC and AI-enhanced YouTube links blocked at multiple layers.
- **3D block** — H-OU, H-SBS and all 3D visual tags excluded.
- **149-pattern release group scoring** — Fully scored regex baked in. No synced URL or whitelist required. Remux T1 (+100) through Extras (-200).
- **`regexScore` + `streamExpressionScore` in sort** — Release group ranking and expression scoring both feed into final stream ordering.
- **Exact title, year, and episode matching** — Strict mode on all three. No wrong-year or wrong-episode results.
- **Full 12-service roster** — All opt-in. Enable only what you subscribe to.
- **Tamtaro deduplicator** — SmartDetect aggressive, 13 attributes.
- **Tamtaro ESEs inline** — Low Seeders, Extra Cached (HQ/LQ), Extra Uncached, Unknown Resolution, Unknown Quality — no whitelist needed.
- **`hideErrors: true`** — Info and error streams hidden. No GitHub redirect card in Stremio.
- **`bitrate.useMetadataRuntime: true`** — Accurate runtime-based bitrate.
- **EZTV** — TV-specific torrent search, opt-in.
- **MediaFusion** — Pre-configured to ElfHosted's public instance.

### 4K Templates
- **SeaDex best-release enforced** for anime.
- **Size range 5 GB–150 GB** — accommodates full BluRay REMUX.
- **DV → HDR10+ → HDR10 → HDR visual priority.**
- **TrueHD → Atmos → DTS:X → DTS-HD MA audio priority.**

### 1080p Templates
- **4K, HDR, BluRay and Remux blocked** — SDR WEB-DL only.
- **Size range 1 GB–25 GB.**

### Dual Templates (TorBox + Real-Debrid)
- **RD Infringing File Scrub** — Full May 2026 keyword blocklist. BluRay REMUX exempt.
- **RD cached only** — Uncached routed through TorBox exclusively.
- **MediaFlow proxy** — RD traffic protected against IP flags.

### Pro Templates (with Usenet)
- **`cacheAndPlay`** — Background Usenet download while playback begins.
- **`nzbFailover`** — Automatic NZB failover when a download fails.

---

## 📖 Guides

| Guide | Description |
|---|---|
| [Import Guide](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Guides/IMPORT_GUIDE.md) | Import templates, enter credentials, install in Stremio or WuPlay |
| [Formatter Guide](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Guides/FORMATTER_GUIDE.md) | Install and switch formatters |
| [Device Profiles](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Guides/DEVICE_PROFILES.md) | Multi-device household setup |
| [Advanced Editing](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Guides/ADVANCED_EDITING.md) | Raw JSON editing and SEL syntax |
| [Reset Guide](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Guides/RESET_GUIDE.md) | Soft reset, hard reset, password recovery |
| [Troubleshooting](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Guides/TROUBLESHOOTING.md) | Common errors and quick fixes |

---

## 📂 Repository Structure

```
Core-Builds-By-Brevity/
├── 📁 Assets/
├── 📁 Formatters/          Core Zenith Diamond, Core Clean Stream
├── 📁 Guides/              Import, Formatter, Device Profiles, Advanced, Reset, Troubleshooting
├── 📁 Regex/               Hosted scored regex patterns
├── 📁 Templates/
│   └── 📁 Torbox/
│       ├── 📁 Single/      TorBox-only (Pro + Essential variants)
│       ├── 📁 Dual/        TorBox + Real-Debrid
│       ├── 📁 Hybrid/      TorBox + Usenet Indexer
│       ├── 📁 Speed/       Speed-optimised (4 addons only)
│       │   ├── 📁 EasyNews/
│       │   └── 📁 TorBox/
│       └── 📁 Nightly/     Live-synced — nightly hosts only
│           ├── 📁 Single/
│           ├── 📁 Dual/
│           └── 📁 Hybrid/
├── CHANGELOG.md
└── README.md
```

---

## 💬 Don't See What You Need?

Open a request and we'll look into it.

**Include:** your debrid service(s), target resolution, hardware, and any specific requirements.

- **GitHub Issues** → [Open a Template Request](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/issues/new?labels=template+request&title=Template+Request:+)
- **Discord** → AIOStreams community server

---

## 📜 Version & Stability

> Versions prior to `1.1.2` are **unstable**. Current version: **`v2.2.1`** (Universal) / **`v2.1.8-nightly`** (Nightly).

[Full CHANGELOG](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/CHANGELOG.md)

---

## ☕ Support the Project

If these templates have leveled up your setup, consider buying me a coffee.

[![Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/branding_brevity/?hidefeed=true&widget=true&embed=true)

---

*Built and maintained by Brevity.*
