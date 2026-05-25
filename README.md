<p align="center">
  <a href="https://github.com/Branding-Brevity/Core-Builds-By-Brevity/releases/latest">
    <img src="https://github.com/Branding-Brevity/Core-Builds-By-Brevity/raw/refs/heads/main/Assets/core_builds_banner.svg" alt="Core Builds Banner" width="100%"/>
  </a>
</p>

# 🛡️ Core Builds by Brevity

Welcome to Core Builds. This repository hosts highly optimised, frictionless configuration templates and custom formatters for AIOStreams, specifically tuned for seamless playback on WuPlay, Stremio, and Android-based home theater setups.

## 🎯 The Philosophy
Streaming shouldn't involve trial and error. These builds are engineered to strip out unplayable clutter, prevent network choking, and serve only the highest quality compatible files. Every build features aggressive deduplication, smart caching, and prioritises English/Dual-Audio tracks natively.

---

## 🚀 The Flagship Builds (v2.2.9)

### 📦 Single Service — TorBox Exclusive
Optimised for a pure TorBox and Usenet experience. No secondary debrid service required.

| Template | Resolution | Best For | Docs |
| :--- | :--- | :--- | :--- |
| **TorBox Exclusive (RPDB)** | 1080p SDR | Budget hardware, RPDB poster art | [README] |
| **4K Home Theater** | 4K HDR | Shield, Apple TV 4K, full HT setup | [README] |
| **Essential 4K** | 4K HDR | TorBox Essential cache only | [README] |

### 🔀 Hybrid — TorBox + Usenet Indexer
For users pairing TorBox with a dedicated Usenet indexer for maximum source diversity.

| Template | Resolution | Best For | Docs |
| :--- | :--- | :--- | :--- |
| **TB Hybrid 1080p** | 1080p SDR | TorBox + NZBGeek, cached + uncached | [README] |

*(Note: Dual Core templates are deprecated as of v2.2.9 due to upstream proxy instability).*

---

## ⚙️ Quick Start

1. **Choose a Host:** Start with ElfHosted or Yeb's. (Live status: `status.dinsden.top`)
2. **Import a Template:** Navigate to the AIOStreams Template Import menu and paste the raw GitHub URL for your chosen build.
3. **Configure Services:** Enable only the debrid services you actually subscribe to.
4. **Install:** Click Save and copy the generated manifest URL into Stremio or WuPlay.

---

<details>
<summary><strong>🔧 Click to expand: Under the Hood (Technical Specifications)</strong></summary>

### All Templates
* **Tamtaro SEL stack:** Live-synced excluded stream expressions, preferred stream expressions, and excluded regex via Tamtaro's GitHub URLs. Stays current without manual updates.
* **Vidhin05 ranked regex + expressions:** Release group scoring and ranking pulled from Vidhin05's maintained lists.
* **Hard CAM & YouTube kill:** Wipes CAM, SCR, TS, TC, HC HD-Rip, and AI-enhanced YouTube links.
* **Tamtaro deduplicator:** Full smartDetect config with 13 attributes: size, resolution, quality, visualTags, audioTags, audioChannels, languages, encode, edition, network, remastered, bitrate, releaseGroup.
* **Audio sort corrected:** All templates correctly sort lossless audio (7.1 > 5.1 > 2.0).
* **Series sort rebuilt:** Fully specified sort stacks per resolution tier.

### 4K Templates Only
* **SeaDex best-release enforced:** `seadexBestOnly: true` ensures only the definitive best encode is served for anime. Quality over compatibility on high-end hardware.
* **Size range 5 GB–150 GB:** Floor prevents mislabelled junk, ceiling accommodates full BluRay REMUX.
* **Visual tag priority:** DV → HDR+DV → HDR10+ → HDR10 → HDR → HLG → SDR.
* **Audio priority:** TrueHD → Atmos → DTS:X → DTS-HD MA → FLAC.

### 1080p Templates Only
* **4K and HDR fully excluded:** 2160p, 1440p, DV, HDR10+, HDR10, HDR, HLG all blocked.
* **BluRay and Remux blocked:** Too large and often unplayable on budget hardware.
* **Size range 1 GB–25 GB:** Tight ceiling prevents oversized files on hardware with limited buffering headroom.

</details>

<details>
<summary><strong>📱 Click to expand: Device Profiles & Custom Formatters</strong></summary>

### Device Profiles (Multi-Device Setup)
AIOStreams can't detect what device is requesting a stream. The cleanest workaround for mixed households is two separate Stremio accounts:
* 🔵 **Low-End Account** → install a 1080p SDR template on phones, tablets, budget TVs.
* 🟣 **High-End Account** → install a 4K template on Shield, Apple TV 4K, OLED/QLED sets.

### Custom Formatters
* 💎 **Core Zenith Diamond** — Information-dense, emoji-coded badges, smallcaps text. Shows service pool, resolution, quality, audio, special flags, and a 4-line metadata description.
* 📺 **Core Clean Stream** — Minimal plain-text formatter matching native Stremio card layout. No emojis, no smallcaps.

</details>

<details>
<summary><strong>📖 Click to expand: Directory & Guides</strong></summary>

* **[Import Guide](Guides/IMPORT_GUIDE.md):** How to import templates, enter credentials, and install in Stremio or WuPlay.
* **[Formatter Guide](Guides/FORMATTER_GUIDE.md):** Installing and switching visual formatters.
* **[Device Profiles](Guides/DEVICE_PROFILES.md):** Multi-device household setup.
* **[Advanced Editing](Guides/ADVANCED_EDITING.md):** Raw JSON editing, valid enum values, SEL syntax rules.
* **[Troubleshooting](Guides/TROUBLESHOOTING.md):** Common errors and quick fixes.

</details>

---

## ☕ Support the Project

If these templates have levelled up your home theater or Stremio setup and saved you from buffering headaches, consider buying me a coffee. Your support fuels the late-night testing and continuous updates.

[![Ko-fi](https://img.shields.io/badge/DONATE-Ko--fi-ff5f5f?style=for-the-badge&logo=ko-fi&logoColor=white&labelColor=1a1f27)](https://ko-fi.com/branding_brevity)

*Built and maintained by Brevity.*
