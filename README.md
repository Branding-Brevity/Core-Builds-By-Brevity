<p align="center">
  <img src="https://github.com/Branding-Brevity/Core-Builds-By-Brevity/raw/main/Assets/core_builds_banner.svg" alt="Core Builds Banner">
</p>

# 🛡️ Core Builds by Brevity

Welcome to **Core Builds**. This repository hosts highly optimised, frictionless configuration templates and custom formatters for **AIOStreams**, specifically tuned for seamless playback on WuPlay, Stremio, and Android-based home theater setups.

## 🎯 The Philosophy

Streaming shouldn't involve trial and error. These builds are engineered to strip out unplayable clutter, prevent network choking, and serve only the highest quality compatible files. Every build features aggressive deduplication, smart caching, YouTube/CAM filtering, and prioritises English/Dual-Audio tracks natively.

---

## 🚀 The Flagship Builds

### ⛓️ Dual Service — TorBox + Real-Debrid
*Cross-service failover with the RD Infringing File Scrub for account protection.*

- **[Dual Core 1080p SDR](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/TorBox/Dual/core-nexus-dual-core-1080p.json)** — Frictionless 1080p dual-cache merging. Filters 4K, HDR, and lossless audio for reliable playback on standard hardware.
- **[Dual Core 4K Unleashed](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/TorBox/Dual/core-nexus-4k-dual-core.json)** — The ultimate master build. TorBox Usenet priority merged with RD's massive cache. Targets Dolby Vision, HDR10+, TrueHD, and Atmos.

### 📦 Single Service — TorBox Exclusive
*Optimised for a pure, high-speed TorBox and Usenet experience.*

- **[Core Nexus TorBox Exclusive (RPDB)](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/TorBox/Single/core-nexus-torbox-exclusive_rpdb.json)** — 1080p SDR build with RPDB poster integration. Blocks 4K, Remux, and lossless audio for low-end and Android hardware.
- **[Core Nexus 4K Home Theater](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/TorBox/Single/core-nexus-4k-ht-torbox.json)** — The unleashed TorBox edition. Hunts for 4K Remuxes, Dolby Vision, HDR10+, TrueHD, and Atmos. 150GB file ceiling.

### 🔀 Hybrid — TorBox + Usenet Indexer
*For users pairing TorBox with a dedicated Usenet indexer for maximum source diversity.*

- **[TB Hybrid 1080p](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/TorBox/Hybrid/core-nexus-tb-hybrid-1080p.json)** — TorBox combined with NZBGeek Usenet integration. 1080p SDR, WEB-DL priority. Requires a NZBGeek API key to activate the Usenet tier.

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

## 📂 Repository Structure

```
Core-Builds-By-Brevity/
├── 📁 Assets/              Banners and icons
├── 📁 Formatters/          UI layouts (Core Zenith Diamond, Core Clean Stream)
├── 📁 Guides/              Setup and editing documentation
├── 📁 Regex/               Hosted trusted regex patterns
├── 📁 Templates/
│   └── 📁 TorBox/
│       ├── 📁 Single/      TorBox-only builds (RPDB, 4K HT)
│       ├── 📁 Dual/        TorBox + Real-Debrid (1080p, 4K)
│       └── 📁 Hybrid/      TorBox + Usenet Indexer
├── CHANGELOG.md
└── README.md
```

---

## ⚙️ Quick Start

### 1. Choose a Host

A live status page for all instances is at [status.dinsden.top](https://status.dinsden.top/status/aiostreams).

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
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/main/Templates/TorBox/Dual/core-nexus-4k-dual-core.json
```

### 3. Configure Services

Enable only the debrid services you actually subscribe to — all 12 are pre-loaded and set to opt-in.

### 4. Install

Click **Save** and copy the generated manifest URL into Stremio or WuPlay.

Detailed instructions in the [Import Guide](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Guides/IMPORT_GUIDE.md).

---

## 🔧 Under the Hood

Every template includes:

- **Tamtaro SEL stack** — Live-synced excluded stream expressions, preferred stream expressions, and excluded regex via Tamtaro's GitHub URLs. Stays current without manual updates.
- **Vidhin05 ranked regex + expressions** — Release group scoring and ranking pulled from Vidhin05's maintained lists.
- **Hard CAM kill** — Wipes CAM, SCR, TS, TC, HC HD-Rip at both quality and stream expression layers.
- **Hard YouTube kill** — Catches AI-enhanced YouTube links other filters miss.
- **RD Infringing File Scrub** *(dual templates)* — Expanded to cover the full May 2026 RD keyword blocklist: WEB-DL, WEBRip, AMZN, DSNP, HULU, NF, CR, PCOK, PMTP, ATVP, MAX, SHO, CRAV, STAN, BCORE, YTS, RARBG. BluRay REMUX intentionally exempt.
- **Per-resolution size enforcement** — Floors and ceilings set per resolution tier. 4K movies: 5 GB–150 GB. 1080p movies: 1 GB–25 GB. Prevents sub-gigabyte junk and over-sized bloat from slipping through.
- **Full 12-service roster** — All services pre-loaded and set to opt-in. Enable only what you use.
- **Tamtaro deduplicator** — Full smartDetect config with 13 attributes: size, resolution, quality, visualTags, audioTags, audioChannels, languages, encode, edition, network, remastered, bitrate, releaseGroup.
- **3D / H-OU / H-SBS block** — Glasses-required 3D content excluded across all templates.
- **EZTV** — TV show torrent search added as an opt-in built-in addon.
- **MediaFusion** — Pre-configured to ElfHosted's public instance (`mediafusion.elfhosted.com`). Works out of the box on any AIOStreams host.
- **Aggressive deduplication + exact title matching** — No duplicate streams, no false matches.

---

## 📜 Version & Stability

> **Stability Notice:** Versions prior to `1.1.2` should be considered **unstable**. Earlier releases contained broken JSON, invalid enum values, and non-functional stream expressions. The first stable, publish-ready release across all templates is `v1.1.2`. Current version is **`v2.0.0`**.

See the [full CHANGELOG](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/CHANGELOG.md) for complete version history.

---

## ☕ Support the Project

If these templates have levelled up your home theater or Stremio setup and saved you from buffering headaches, consider buying me a coffee. Your support fuels the late-night testing and continuous updates.

[![Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/branding_brevity/?hidefeed=true&widget=true&embed=true)

---

*Built and maintained by Brevity.*
