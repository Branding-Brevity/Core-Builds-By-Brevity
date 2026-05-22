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
*Cross-service failover. TorBox handles Usenet and uncached traffic. Real-Debrid serves cached streams only, with full RD Infringing File Scrub for account protection.*

| Template | Resolution | Best For | Docs |
|---|---|---|---|
| [Dual Core 1080p SDR](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Dual/core-nexus-dual-core-1080p.json) | 1080p SDR | Budget hardware, phones, tablets | [README](Templates/Torbox/Dual/core-nexus-dual-core-1080p.md) |
| [Dual Core 4K Unleashed](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Dual/core-nexus-4k-dual-core.json) | 4K HDR | Shield, Apple TV 4K, OLED/QLED | [README](Templates/Torbox/Dual/core-nexus-4k-dual-core.md) |
| [4K Essential Dual Core](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Dual/core-nexus-4k-essential-dual-core.json) | 4K HDR | Shield, Apple TV 4K -- TorBox Essential plan | [README](Templates/Torbox/Dual/core-nexus-4k-essential-dual-core.md) |

### 📦 Single Service — TorBox Exclusive
*Optimised for a pure TorBox and Usenet experience. No secondary debrid service required.*

| Template | Resolution | Best For | Docs |
|---|---|---|---|
| [TorBox Exclusive (RPDB)](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Single/core-nexus-torbox-exclusive_rpdb.json) | 1080p SDR | Budget hardware, RPDB poster art | [README](Templates/Torbox/Single/core-nexus-torbox-exclusive_rpdb.md) |
| [4K Home Theater](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Single/core-nexus-4k-ht-torbox.json) | 4K HDR | Shield, Apple TV 4K, full HT setup | [README](Templates/Torbox/Single/core-nexus-4k-ht-torbox.md) |

### 🔀 Hybrid — TorBox + Usenet Indexer
*For users pairing TorBox with a dedicated Usenet indexer for maximum source diversity.*

| Template | Resolution | Best For | Docs |
|---|---|---|---|
| [TB Hybrid 1080p](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Hybrid/core-nexus-tb-hybrid-1080p.json) | 1080p SDR | TorBox + NZBGeek, cached + uncached | [README](Templates/Hybrid/core-nexus-tb-hybrid-1080p.md) |

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

## 📂 Repository Structure

```
Core-Builds-By-Brevity/
├── 📁 Assets/              Banners and icons
├── 📁 Formatters/          UI layouts (Core Zenith Diamond, Core Clean Stream)
├── 📁 Guides/              Setup and editing documentation
│   ├── IMPORT_GUIDE.md
│   ├── FORMATTER_GUIDE.md
│   ├── ADVANCED_EDITING.md
│   └── DEVICE_PROFILES.md
├── 📁 Regex/               Hosted trusted regex patterns
├── 📁 Templates/
│   └── 📁 Single/          TorBox-only builds (RPDB, 4K HT)
│       ├── 📁 Dual/            TorBox + Real-Debrid (1080p, 4K)
│       └── 📁 Hybrid/          TorBox + Usenet Indexer
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
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/main/Templates/Torbox/Dual/core-nexus-4k-dual-core.json
```

### 3. Configure Services

Enable only the debrid services you actually subscribe to — all 12 are pre-loaded and set to opt-in.

### 4. Install

Click **Save** and copy the generated manifest URL into Stremio or WuPlay.

Detailed instructions in the [Import Guide](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Guides/IMPORT_GUIDE.md).

---

## 🔧 Under the Hood

### All Templates
- **Tamtaro SEL stack** — Live-synced excluded stream expressions, preferred stream expressions, and excluded regex via Tamtaro's GitHub URLs. Stays current without manual updates.
- **Vidhin05 ranked regex + expressions** — Release group scoring and ranking pulled from Vidhin05's maintained lists.
- **Hard CAM kill** — Wipes CAM, SCR, TS, TC, HC HD-Rip at both quality and stream expression layers.
- **Hard YouTube kill** — Catches AI-enhanced YouTube links other filters miss.
- **3D / H-OU / H-SBS block** — Glasses-required 3D content excluded across all templates.
- **Full 12-service roster** — All services pre-loaded and set to opt-in. Enable only what you use.
- **Tamtaro deduplicator** — Full smartDetect config with 13 attributes: size, resolution, quality, visualTags, audioTags, audioChannels, languages, encode, edition, network, remastered, bitrate, releaseGroup.
- **Aggressive deduplication + exact title matching** — No duplicate streams, no false matches.
- **EZTV** — TV show torrent search available as an opt-in built-in addon on all templates.
- **MediaFusion** — Pre-configured to ElfHosted's public instance (`mediafusion.elfhosted.com`). Works out of the box on any AIOStreams host.
- **Audio sort corrected** — All templates sort 7.1 > 5.1 > 2.0. Ascending sort (stereo first) was a bug in earlier versions.
- **Series sort rebuilt** — TV show results were previously sorted with 3 keys. Now fully specified per resolution tier.

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

> **Stability Notice:** Versions prior to `1.1.2` should be considered **unstable**. Earlier releases contained broken JSON, invalid enum values, and non-functional stream expressions. The first stable, publish-ready release across all templates is `v1.1.2`. Current version is **`v2.1.0`**.

See the [full CHANGELOG](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/CHANGELOG.md) for complete version history.

---

## ☕ Support the Project

If these templates have levelled up your home theater or Stremio setup and saved you from buffering headaches, consider buying me a coffee. Your support fuels the late-night testing and continuous updates.

[![Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/branding_brevity/?hidefeed=true&widget=true&embed=true)

---

*Built and maintained by Brevity.*
