<p align="center">
  <img src="./Assets/core_builds_banner.svg" alt="Core Builds Banner">
</p>

# 🛡️ Core Builds by Brevity

Welcome to **Core Builds**. This repository hosts highly optimized, frictionless configuration templates and custom formatters for **AIOStreams**, specifically tuned for seamless playback on WuPlay, Stremio, and Android-based home theater setups.

## 🎯 The Philosophy
Streaming shouldn't involve trial and error. These builds are engineered to strip out unplayable clutter, prevent network choking, and serve only the highest quality compatible files. Both builds feature aggressive deduplication, smart caching, and prioritize English/Dual-Audio tracks natively.

---

## 🚀 The Flagship Builds

### 1️⃣ Core Nexus: TorBox Exclusive (1080p SDR)
*Built for standard hardware, Google TV, and Android projectors.*
* **Frictionless Playback:** Aggressively filters out unsupported video formats (AV1, Dolby Vision) and heavy lossless audio (TrueHD, DTS-HD MA) to prevent black screens and audio drops on standard hardware.
* **Network Stability:** Hard bitrate capping at 60 Mbps to guarantee stutter-free playback over standard Wi-Fi.
* **SDR & Spatial Audio:** Prioritizes clean 1080p SDR streams paired with Dolby Digital Plus (DD+) and Atmos for flawless soundbar decoding.

### 2️⃣ Core Nexus: 4K Home Theater Edition
*The leash is off. Built for high-end displays, Nvidia Shields, and dedicated audio setups.*
* **Maximum Quality:** Prioritizes 4K Blu-ray Remuxes and actively hunts for dynamic metadata (Dolby Vision, HDR10+, and HDR). 
* **Lossless Audio Passthrough:** Prioritizes TrueHD Atmos, DTS-HD MA, and DTS:X to feed raw spatial metadata directly to your receiver or high-end soundbar.
* **Uncapped Bandwidth:** Removes the 60 Mbps network limit (features a 150 Mbps safety net to catch broken files), allowing massive 100GB+ files to stream flawlessly. Fully supports highly-efficient AV1 encodes.

---

## 📂 Repository Structure

### [`/Templates`](./Templates)
Contains the raw JSON configuration files for AIOStreams. *(Note: All personal API keys have been scrubbed. Free RPDB keys are baked in by default.)*

### [`/Formatters`](./Formatters)
Custom visual layouts for the AIOStreams UI.
* **Core Zenith Diamond:** Hardware-specific badging (e.g., JBL Spatial, SDR Master) for quick visual confirmation of file specs.
* **Auburn Tiger Edition:** Clean, tiger-striped alternating color scheme (Orange & Blue) using geometric diamond spacers for maximum readability.

### [`/Guides`](./Guides)
Step-by-step setup guides explaining how to import these templates, bypass requirements, and link the final manifest to WuPlay.

---

## ⚙️ Quick Start: How to Import

1. Navigate to your preferred AIOStreams web host (e.g., [ForTheWeak](https://aiostreams.fortheweak.cloud/)).
2. Go to the **Template Import** menu.
3. Copy the link for the build that fits your hardware, and paste it into the AIOStreams Template Importer:
   * **[1080p SDR Build - Raw Link](https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/main/Templates/core-nexus-torbox-exclusive_rpdb.json)**
   * **[4K Home Theater Build - Raw Link](https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/main/Templates/core-nexus-4k-ht-torbox.json)**
4. Follow the setup instructions in the [`/Guides`](./Guides) folder to finalize your API keys and install the manifest to your streaming app.

---
*Built and maintained by Brevity.*
