<p align="center">
  <img src="https://github.com/Branding-Brevity/Core-Builds-By-Brevity/raw/main/Assets/core_builds_banner.svg" alt="Core Builds Banner">
</p>

# 🛡️ Core Builds by Brevity

Welcome to **Core Builds**. This repository hosts highly optimised, frictionless configuration templates and custom formatters for **AIOStreams**, specifically tuned for seamless playback on WuPlay, Stremio, and Android-based home theater setups.

## 🎯 The Philosophy

Streaming shouldn't involve trial and error. These builds are engineered to strip out unplayable clutter, prevent network choking, and serve only the highest quality compatible files. Every build features aggressive deduplication, smart caching, YouTube/CAM filtering, and prioritises English/Dual-Audio tracks natively.

---

## 🚀 The Flagship Builds

### 📦 Single Service — TorBox Exclusive
*Optimised for a pure, high-speed TorBox and Usenet experience.*

- **[Core Nexus 1080p SDR](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/TorBox/Single/core-nexus-torbox-exclusive_rpdb.json)** — Low-end hardware build. Blocks 4K, AV1, DV, BluRay/Remux, and lossless audio for Android projectors and Google TV.
- **[Core Nexus 4K Home Theater](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/TorBox/Single/core-nexus-4k-ht-torbox.json)** — The unleashed edition. Hunts for 4K Remuxes, Dolby Vision, HDR10+, TrueHD, and Atmos.

### ⛓️ Dual Service — TorBox + Real-Debrid
*Cross-service failover with the RD Infringing File Scrub for account protection.*

- **[Dual Core 1080p SDR](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/TorBox/Dual/core-nexus-dual-core-1080p.json)** — Frictionless 1080p locking with dual-cache merging.
- **[Dual Core 4K Unleashed](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/TorBox/Dual/core-nexus-4k-dual-core.json)** — The ultimate master build. TorBox Usenet priority + massive RD cache.

### 🌐 Any Host — Universal Debrid Support *(NEW in v1.2.0)*
*Works with any debrid service. All 8 supported services pre-configured — TorBox, Real-Debrid, AllDebrid, Premiumize, DebridLink, Offcloud, Put.io, EasyDebrid.*

- **[Any Host 1080p](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Any-Host/Single/core-nexus-anyhost-1080p.json)** — Low-end single debrid.
- **[Any Host 4K](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Any-Host/Single/core-nexus-anyhost-4k.json)** — High-end single debrid.
- **[Any Host 1080p Dual](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Any-Host/Dual/core-nexus-anyhost-1080p-dual.json)** — Low-end with dual services.
- **[Any Host 4K Dual](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Any-Host/Dual/core-nexus-anyhost-4k-dual.json)** — High-end with dual services.

### 🔀 Hybrid — Cached + Uncached *(NEW in v1.1.3)*
*For users who want both instant cached streams AND uncached fallback access.*

- **[TB Hybrid 1080p](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/TorBox/Hybrid/core-nexus-tb-hybrid-1080p.json)** — TorBox cached + uncached with NZBGeek integration.

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
- **📺 Core Clean Stream** *(NEW)* — Minimal plain-text formatter matching native Stremio card layout. No emojis, no smallcaps, just clean readable text.

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
│   ├── 📁 TorBox/
│   │   ├── 📁 Single/      TorBox-only builds
│   │   ├── 📁 Dual/        TorBox + Real-Debrid
│   │   └── 📁 Hybrid/      Cached + Uncached
│   ├── 📁 Any-Host/
│   │   ├── 📁 Single/      Single debrid, any host
│   │   └── 📁 Dual/        Dual debrid, any host
│   └── 📁 Community-Templates/
│       └── 📁 RB3/         Community builds
├── CHANGELOG.md
└── README.md
```

---

## ⚙️ Quick Start

1. Open your preferred AIOStreams host:
   - **ForTheWeak** — `https://aiostreams.fortheweak.cloud`
   - **MidnightIgnite** — `https://aiostreams.midnightignite.com`
   - **ElfHosted** — `https://aiostreams.elfhosted.com`

2. Navigate to the **Template Import** menu and paste the raw GitHub URL for your chosen build:

   ```
   https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/main/Templates/TorBox/Single/core-nexus-torbox-exclusive_rpdb.json
   ```

3. Enter your API keys (only the services you actually use — others stay blank).

4. Click **Save** and copy the generated manifest URL into Stremio or WuPlay.

Detailed instructions in the [Import Guide](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Guides/IMPORT_GUIDE.md).

---

## 🔧 Under the Hood

Every template includes:

- **Triple-layer YouTube block** — `excludedStreamTypes`, `excludedStreamSources`, and a hard ESE kill, catching AI-enhanced YouTube links other filters miss
- **Hard CAM kill** — wipes CAM, SCR, TS, TC, HC HD-Rip at both quality and stream expression layers
- **RD Infringing File Scrub** *(dual templates)* — blocks WEB-DL/WEBRip pulls on Real-Debrid that trigger May 2026's "infringing file" errors
- **5-tier addon hierarchy** — fast scrapers (Library, Comet) load instantly, mid-tier (Meteor, Zilean, SeaDex, AnimeTosho) fills within 5s, fallbacks (TorrentGalaxy, Knaben, Peerflix) catch anything missed
- **Tamtaro trusted regex sync** — junk file extensions (iso, exe, dll, etc.) blocked without triggering ElfHosted forbidden-URL errors
- **Aggressive deduplication + exact title matching** — no duplicate streams, no false matches

---

## 📜 Version & Stability

> **Stability Notice:** Versions prior to `1.1.2` should be considered **unstable**. Earlier releases contained broken JSON, invalid enum values, and non-functional stream expressions. The first stable, publish-ready release across all templates is `v1.1.2`. Current version is **`v1.2.0`**.

See the [full CHANGELOG](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/CHANGELOG.md) for complete version history.

---

## ☕ Support the Project

If these templates have levelled up your home theater or Stremio setup and saved you from buffering headaches, consider buying me a coffee. Your support fuels the late-night testing and continuous updates.

[![Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/branding_brevity/?hidefeed=true&widget=true&embed=true)

---

*Built and maintained by Brevity.*
