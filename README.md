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

# 🛡️ Core Builds by Brevity

Welcome to **Core Builds**. This repository hosts highly optimised, frictionless configuration templates and custom formatters for **AIOStreams**, specifically tuned for seamless playback on WuPlay, Stremio, and Android-based home theater setups.

## 🎯 The Philosophy

Streaming shouldn't involve trial and error. These builds are engineered to strip out unplayable clutter, prevent network choking, and serve only the highest quality compatible files. Every build features aggressive deduplication, smart caching, YouTube/CAM filtering, and prioritises English/Dual-Audio tracks natively.

---

## 🚀 The Flagship Builds

### ⛓️ Dual Service — TorBox + Real-Debrid
*Cross-service failover. TorBox handles Usenet and uncached traffic. Real-Debrid serves cached streams only, with full RD Infringing File Scrub for account protection.*

| Template | Resolution | Best For | Docs |
|---|---|---|---|
| [Dual Core 1080p SDR](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Dual/core-nexus-dual-core-1080p.json) | 1080p SDR | Budget hardware, phones, tablets | [README](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Dual/README_dual-core-1080p.md) |
| [Dual Core 4K Unleashed](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Dual/core-nexus-4k-dual-core.json) | 4K HDR | Shield, Apple TV 4K, OLED/QLED | [README](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Dual/README_4k-dual-core.md) |
| [4K Essential Dual Core](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Dual/core-nexus-4k-essential-dual-core.json) | 4K HDR | Shield, Apple TV 4K -- TorBox Essential plan | [README](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Dual/README_4k-essential-dual-core.md) |

### 📦 Single Service — TorBox Exclusive
*Optimised for a pure TorBox and Usenet experience. No secondary debrid service required.*

| Template | Resolution | Best For | Docs |
|---|---|---|---|
| [TorBox Exclusive (RPDB)](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Single/core-nexus-torbox-exclusive_rpdb.json) | 1080p SDR | Budget hardware, RPDB poster art | [README](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Single/README_torbox-exclusive-rpdb.md) |
| [4K Home Theater](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Single/core-nexus-4k-ht-torbox.json) | 4K HDR | Shield, Apple TV 4K, full HT setup | [README](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Single/README_4k-ht-torbox.md) |

### 🔀 Hybrid — TorBox + Usenet Indexer
*For users pairing TorBox with a dedicated Usenet indexer for maximum source diversity.*

| Template | Resolution | Best For | Docs |
|---|---|---|---|
| [TB Hybrid 1080p](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Hybrid/core-nexus-tb-hybrid-1080p.json) | 1080p SDR | TorBox + NZBGeek, cached + uncached | [README](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Hybrid/README_tb-hybrid-1080p.md) |


### ⚡ Speed Tier — Instant Autoplay (2-3 Second Load)
*Stripped to 4 addons only: Library, TorBox Search, Comet, Zilean. For users who prioritise instant results over maximum source coverage.*

#### With EasyNews (TorBox Essential + EasyNews)

| Template | Resolution | Docs |
|---|---|---|
| [Speed 1080p (EasyNews)](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/refs/heads/main/Templates/Torbox/Speed/EasyNews/core-nexus-speed-1080p.json) | 1080p SDR | [README](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/refs/heads/main/Templates/Torbox/Speed/EasyNews/README_speed-1080p-easynews.md) |
| [Speed 4K (EasyNews)](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/refs/heads/main/Templates/Torbox/Speed/EasyNews/core-nexus-speed-4k.json) | 4K HDR | [README](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/refs/heads/main/Templates/Torbox/Speed/EasyNews/README_speed-4k-easynews.md) |

#### TorBox Essential Only (No EasyNews)

| Template | Resolution | Docs |
|---|---|---|
| [Speed 1080p](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/refs/heads/main/Templates/Torbox/Speed/TorBox/core-nexus-speed-1080p-torbox.json) | 1080p SDR | [README](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/refs/heads/main/Templates/Torbox/Speed/TorBox/README_speed-1080p-torbox.md) |
| [Speed 4K](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/refs/heads/main/Templates/Torbox/Speed/TorBox/core-nexus-speed-4k-torbox.json) | 4K HDR | [README](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/refs/heads/main/Templates/Torbox/Speed/TorBox/README_speed-4k-torbox.md) |

> Speed templates use 3500ms timeouts, 10 results max, and a 5-key sort. All other Core Builds features (scored regex ranking, Tamtaro ESEs, episode matching, cacheAndPlay) remain intact.

> ⚠️ The Hybrid template requires a **NZBGeek API key** configured in the Addons section after loading. See the [Import Guide](Guides/IMPORT_GUIDE.md) for the full setup step.

---

## 🌍 Universal Debrid Support

All five templates ship with the **full 12-service roster** pre-loaded and set to opt-in. Enable only the services you actually subscribe to — the rest are ignored:

`TorBox` · `Real-Debrid` · `AllDebrid` · `Premiumize` · `DebridLink` · `Offcloud` · `Put.io` · `EasyNews` · `EasyDebrid` · `PikPak` · `Seedr` · `Debrider`

---

## 📱 Device Profiles — Multi-Device Setup

AIOStreams can't detect what device is requesting a stream — every request looks identical to the server. The cleanest workaround for households with mixed devices is **two separate Stremio accounts**:

- **🔵 Low-End Account** → install a 1080p SDR template on phones, tablets, budget TVs
- **🟣 High-End Account** → install a 4K template on Shield, Apple TV 4K, OLED/QLED sets

See the [Device Profiles Guide](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Guides/DEVICE_PROFILES.md) for full setup instructions.

---

## 🎨 Custom Formatters

Two formatters included to control how streams display in your list:

- **💎 Core Zenith Diamond** — Information-dense, emoji-coded badges, smallcaps text. Shows service pool, resolution, quality, audio, special flags (OWNED, LIBRARY, SEADEX BEST) and a 4-line metadata description.
- **📺 Core Clean Stream** — Minimal plain-text formatter matching native Stremio card layout. No emojis, no smallcaps, just clean readable text.

See the [Formatter Guide](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Guides/FORMATTER_GUIDE.md) for installation.

---

## 📖 Guides

| Guide | Description |
|---|---|
| [Import Guide](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Guides/IMPORT_GUIDE.md) | How to import templates, enter credentials, and install in Stremio or WuPlay |
| [Formatter Guide](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Guides/FORMATTER_GUIDE.md) | Installing and switching between Core Zenith Diamond and Core Clean Stream |
| [Device Profiles](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Guides/DEVICE_PROFILES.md) | Multi-device household setup using two Stremio accounts |
| [Advanced Editing](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Guides/ADVANCED_EDITING.md) | Raw JSON editing, valid enum values, SEL syntax rules |
| [Reset Guide](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Guides/RESET_GUIDE.md) | Soft reset, hard reset, and password recovery |
| [Troubleshooting](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Guides/TROUBLESHOOTING.md) | Common errors and quick fixes |

---

## 📂 Repository Structure

```
Core-Builds-By-Brevity/
├── 📁 Assets/              Banners and icons
├── 📁 Formatters/          UI layouts (Core Zenith Diamond, Core Clean Stream)
├── 📁 Guides/
│   ├── IMPORT_GUIDE.md         How to import templates and configure services
│   ├── FORMATTER_GUIDE.md      Installing and switching visual formatters
│   ├── DEVICE_PROFILES.md      Multi-device household setup
│   ├── ADVANCED_EDITING.md     Raw JSON editing and SEL syntax rules
│   ├── RESET_GUIDE.md          Soft and hard reset procedures
│   └── TROUBLESHOOTING.md      Common errors and fixes
├── 📁 Regex/               Hosted trusted regex patterns
├── 📁 Templates/
│   └── 📁 Torbox/
│       ├── 📁 Single/          TorBox-only builds -- universal (any host)
│       ├── 📁 Dual/            TorBox + Real-Debrid -- universal (any host)
│       ├── 📁 Hybrid/          TorBox + Usenet Indexer -- universal (any host)
│       ├── 📁 Speed/            Speed-optimised builds (4 addons only)
│       │   ├── 📁 EasyNews/      TorBox Essential + EasyNews
│       │   └── 📁 TorBox/        TorBox Essential only
│       └── 📁 Nightly/         Live-synced builds -- nightly hosts only
│           ├── 📁 Single/
│           ├── 📁 Dual/
│           └── 📁 Hybrid/
├── CHANGELOG.md
└── README.md
```

---

## ⚙️ Quick Start

### 1. Choose a Host

A live status page for all instances is at [docs.aiostreams.viren070.me](https://docs.aiostreams.viren070.me/getting-started/public-instances/).

| Rank | Host | URL | Channel | Notes |
|------|------|-----|---------|-------|
| 🥇 | **ElfHosted** | [aiostreams.elfhosted.com](https://aiostreams.elfhosted.com/stremio/configure) | Stable | Professional hosting service. Most stable and reliable. Public instance excludes P2P/HTTP/Live — debrid-only, which suits these templates perfectly. Private paid plans available with no restrictions. |
| 🥈 | **Yeb's** | [aiostreams.fortheweak.cloud](https://aiostreams.fortheweak.cloud/stremio/configure) | Stable | Hosted by an AIOStreams Discord admin. Long-standing, community-trusted. Also offers a [Nightly build](https://aiostreams-nightly.fortheweak.cloud/stremio/configure) for early access. |
| 🥉 | **Midnight's** | [aiostreamsfortheweebsstable.midnightignite.me](https://aiostreamsfortheweebsstable.midnightignite.me/stremio/configure) | Stable | Hosted by the TorBox community manager. Well-regarded, TorBox-optimised. Also offers a [Nightly build](https://aiostreamsfortheweebs.midnightignite.me/stremio/configure). |
| 4 | **Viren's** | [aiostreams.viren070.me](https://aiostreams.viren070.me/stremio/configure) | Nightly | Hosted by the developer himself. Always on the latest features. Nightly-only — good for power users comfortable with occasional minor bugs. |
| 5 | **Kuu's** | [aiostreams.stremio.ru](https://aiostreams.stremio.ru/stremio/configure) | Stable | Officially listed community instance. Also offers a [Nightly build](https://aiostreams-nightly.stremio.ru/stremio/configure). |
| 6 | **ATBP Hosting** | [aio.atbphosting.com](https://aio.atbphosting.com/stremio/configure) | Stable | Officially listed community instance. |
| 7 | **Omni's** | [aiostreams.12312023.xyz](https://aiostreams.12312023.xyz/stremio/configure) | Stable | Hosted by @a.ves. Officially listed community instance. |

> **Recommendation:** Start with **ElfHosted** or **Yeb's**. For TorBox users, **Midnight's** is purpose-built for that workflow.

### 2. Import a Template

Navigate to the **Template Import** menu and paste the raw GitHub URL for your chosen build:

```
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Dual/core-nexus-4k-dual-core.json
```

### 3. Configure Services

Enable only the debrid services you actually subscribe to — all 12 are pre-loaded and set to opt-in.

### 4. Install

Click **Save** and copy the generated manifest URL into Stremio or WuPlay.

Detailed instructions in the [Import Guide](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Guides/IMPORT_GUIDE.md).

---

## 🔧 Under the Hood

### All Templates
- **Hard CAM kill** — Wipes CAM, SCR, TS, TC, HC HD-Rip at both quality and stream expression layers.
- **Hard YouTube kill** — Catches AI-enhanced YouTube links other filters miss.
- **3D / H-OU / H-SBS block** — Glasses-required 3D content excluded.
- **Full 12-service roster** — All services pre-loaded and set to opt-in. Enable only what you use.
- **Tamtaro deduplicator** — Full smartDetect config with 13 attributes.
- **Exact title + year + episode matching** — `titleMatching: exact`, `yearMatching: strict tolerance 1`, `seasonEpisodeMatching: strict`. No false matches on sequels, remasters, or wrong episodes.
- **149-pattern release group scoring** — Fully scored regex patterns baked directly into every template. No synced URL or whitelist required. Remux T1 (+100) through LQ groups (-75) to Extras (-200).
- **`rankedRegexPatterns` + `preferredRegexPatterns`** — Both active and feeding into `regexScore` sort. Top-tier groups surface above mid-tier groups within the same quality level.
- **`streamExpressionScore` in sort** — Numeric expression scoring feeds into stream ordering alongside `streamExpressionMatched`.
- **`regexScore` in sort** — Release group ranking actively influences final stream order.
- **`cacheAndPlay` for Usenet** — Background download while playback begins. No waiting for a full Usenet download before the stream starts.
- **`nzbFailover`** — Automatic Usenet NZB failover when a download fails.
- **`hideErrors: true`** — Error and informational streams hidden from the list. No more GitHub redirect card appearing in Stremio.
- **`bitrate.useMetadataRuntime: true`** — Accurate runtime-based bitrate calculation using actual video metadata.
- **6 Tamtaro ESEs** — Low Seeders, Extra Cached (HQ), Extra Cached (LQ), Extra Uncached (All), Unknown Resolution, Unknown Quality — all inline, no whitelist needed.
- **EZTV** — TV show torrent search available as an opt-in built-in addon.
- **MediaFusion** — Pre-configured to ElfHosted's public instance. Works out of the box on any AIOStreams host.
- **Audio sort corrected** — All templates sort 7.1 > 5.1 > 2.0.
- **Series sort fully specified** — Per resolution tier, not the 3-key stub from earlier versions.

### 4K Templates Only
- **SeaDex best-release enforced** — `seadexBestOnly: true` ensures only the definitive best encode is served for anime. Quality over compatibility on high-end hardware.
- **Size range 5 GB–150 GB** — Floor prevents mislabelled junk, ceiling accommodates full BluRay REMUX.
- **Visual tag priority: DV → HDR+DV → HDR10+ → HDR10 → HDR → HLG → SDR** — Dolby Vision first, always.
- **Audio priority: TrueHD → Atmos → DTS:X → DTS-HD MA → FLAC** — Lossless first, always.
- **Cached movie sort includes size tiebreaker** — When quality and audio are equal, the larger file wins. Larger typically means a better REMUX on high-end hardware.

### 1080p Templates Only
- **4K and HDR fully excluded** — 2160p, 1440p, DV, HDR10+, HDR10, HDR, HLG all blocked. SDR only.
- **BluRay and Remux blocked** — Too large and often unplayable on budget hardware.
- **Size range 1 GB–25 GB** — Tight ceiling prevents oversized files on hardware with limited buffering headroom.

### Dual Templates Only (TorBox + Real-Debrid)
- **RD Infringing File Scrub** *(all dual templates)* — Covers the full May 2026 RD keyword blocklist: WEB-DL, WEBRip, AMZN, DSNP, HULU, NF, CR, PCOK, PMTP, ATVP, MAX, SHO, CRAV, STAN, BCORE, YTS, RARBG. BluRay REMUX intentionally exempt.
- **RD serves cached only** — Uncached streams are excluded from Real-Debrid. TorBox handles all uncached traffic via Usenet. RD's unreliable uncached is never surfaced.
- **MediaFlow proxy active for RD** — All Real-Debrid traffic routed through MediaFlow to protect against IP-based account flags.

---

## 📜 Version & Stability

> **Stability Notice:** Versions prior to `1.1.2` should be considered **unstable**. Earlier releases contained broken JSON, invalid enum values, and non-functional stream expressions. The first stable, publish-ready release across all templates is `v1.1.2`. Current version is **`v2.1.8`** (Universal) / **`v2.1.8-nightly`** (Nightly).

See the [full CHANGELOG](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/CHANGELOG.md) for complete version history.

---

---

## 💬 Don't See What You Need?

None of the five templates quite fit your setup? Open a request and we'll look into it.

**What to include:**
- Your debrid service(s) — e.g. TorBox Essential + AllDebrid
- Your target resolution — 4K or 1080p
- Your hardware — Shield, Fire Stick, phone, etc.
- Any specific requirements — IMAX, anime-only, no Remux, etc.

**Where to request:**
- **GitHub Issues** → [Open a Template Request](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/issues/new?labels=template+request&title=Template+Request:+) — use the `template request` label
- **Discord** → Drop a message in the AIOStreams community server

We can't guarantee every combination will get its own template, but common requests that fill a genuine gap will be considered for the next release.

---

## ☕ Support the Project

If these templates have leveled up your home theater or Stremio setup and saved you from buffering headaches, consider buying me a coffee. Your support fuels the late-night testing and continuous updates.

[![Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/branding_brevity/?hidefeed=true&widget=true&embed=true)

---

*Built and maintained by Brevity.*
