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

## 📖 Quick Links & Guides

| Guide | Description |
| :--- | :--- |
| **[Import Guide](Guides/IMPORT_GUIDE.md)** | How to import templates, enter credentials, and install. |
| **[Formatter Guide](Guides/FORMATTER_GUIDE.md)** | Installing and switching between visual formatters. |
| **[Device Profiles](Guides/DEVICE_PROFILES.md)** | Setting up multi-device households (Low-end vs High-end). |
| **[Advanced Editing](Guides/ADVANCED_EDITING.md)** | Raw JSON
