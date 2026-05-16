<p align="center">
  <img src="./Assets/core_builds_banner.svg" alt="Core Builds Banner">
</p>

# 🛡️ Core Builds by Brevity

Welcome to **Core Builds**. This repository hosts highly optimized, frictionless configuration templates and custom formatters for **AIOStreams**, specifically tuned for seamless playback on WuPlay, Stremio, and Android-based home theater setups.

## 🎯 The Philosophy
Streaming shouldn't involve trial and error. These builds are engineered to strip out unplayable clutter, prevent network choking, and serve only the highest quality compatible files. 

### Key Features of the Core Nexus (TorBox Exclusive) Build:
* **Frictionless Playback:** Aggressive filtering of unsupported video formats (AV1, Dolby Vision) and heavy lossless audio (TrueHD, DTS-HD MA) to prevent black screens and audio drops on standard hardware.
* **Smart Deduplication:** Conservative deduplication across 13 data points ensures you only see the absolute best version of a release.
* **Network Stability:** Hard bitrate capping at 60 Mbps to guarantee stutter-free playback over Wi-Fi.
* **Premium Scraping:** Prioritizes cached Usenet and Torrents through TorBox, pushing dual-audio and English tracks to the top.

---

## 📂 Repository Structure

### [`/Templates`](./Templates)
Contains the raw JSON configuration files for AIOStreams. 
* **Current Flagship:** `core-nexus-torbox-exclusive` 
* *Note: All personal API keys have been scrubbed. Free RPDB keys are baked in by default.*

### [`/Formatters`](./Formatters)
Custom visual layouts for the AIOStreams UI.
* **Core Zenith Diamond:** Hardware-specific badging (e.g., JBL Spatial, SDR Master) for quick visual confirmation of file specs.
* **Auburn Tiger Edition:** Clean, tiger-striped alternating color scheme (Orange & Blue) using geometric diamond spacers for maximum readability.

### [`/Guides`](./Guides)
Step-by-step PDF manuals on how to import these templates, generate your poster API keys, and link the final manifest to WuPlay.

---

## 🚀 Quick Start: How to Import

1. Navigate to your preferred AIOStreams web host (e.g., [ForTheWeak](https://aiostreams.fortheweak.cloud/)).
2. Go to the **Template Import** menu.
3. Copy this link: [Core Nexus TorBox Exclusive - Raw Link](https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/main/Templates/core-nexus-torbox-exclusive_rpdb.json) and paste it into the AIOStreams Template Importer.
4. Follow the setup guide in the `/Guides` folder to finalize your API keys and install the manifest to your streaming app.

---
*Built and maintained by Brevity.*
