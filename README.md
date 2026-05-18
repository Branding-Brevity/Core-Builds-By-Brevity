<p align="center">
  <img src="./Assets/core_builds_banner.svg" alt="Core Builds Banner">
</p>

# 🛡️ Core Builds by Branding_Brevity

Welcome to **Core Builds**. This repository hosts highly optimized configuration templates and custom formatters for **AIOStreams**, specifically tuned for seamless playback on WuPlay, Stremio, and Android-based home theater environments.

## 🎯 The Philosophy
Streaming should be frictionless. These builds are engineered to strip out unplayable clutter, prevent network bottlenecks, and serve only the highest quality compatible files. Every build features aggressive deduplication, smart caching, and prioritizes English/Dual-Audio tracks natively.

---

## 🚀 The Flagship Builds

### 📦 Single Service (TorBox Exclusive)
*Optimized for a pure, high-speed TorBox and Usenet experience.*

* **[Core Nexus 1080p SDR](./Templates/Single-Service/core-nexus-torbox-exclusive_rpdb.json):** Built for Android projectors and Google TV. Blocks 4K, AV1, DV, and heavy lossless audio.
* **[Core Nexus 4K Home Theater](./Templates/Single-Service/core-nexus-4k-ht-torbox.json):** The unleashed edition. Hunts for 4K Remuxes, Dolby Vision, and HDR10+.

### ⛓️ Dual Service (Dual Core Hybrid)
*For power users running TorBox + Real-Debrid. Features cross-service failover and massive library depth.*

* **[Dual Core 1080p SDR](./Templates/Dual-Service/core-nexus-dual-core-1080p.json):** Frictionless 1080p locking with dual-cache merging.
* **[Dual Core 4K Unleashed](./Templates/Dual-Service/core-nexus-dual-core-4k.json):** The ultimate master build. Combines TorBox Usenet priority with the massive Real-Debrid cache.

---

## 📂 Repository Structure

### [/Templates](Templates/)
Raw JSON configuration files organized into **Single-Service** and **Dual-Service** subfolders.

### [/Formatters](Formatters/)
Custom visual layouts for the AIOStreams UI featuring the **Core Zenith Diamond** system.

### [/Community-Templates](Community-Templates/)
A collection of experimental layouts and community-driven templates offering alternative aesthetics.

### [/Guides](Guides/)
Step-by-step setup guides explaining how to import these templates and link your manifest to WuPlay.

---

## 🤝 Community Templates & Non-Core Builds

While the **Core Nexus** builds represent our official configurations, we also host a collection of experimental layouts and community-driven templates. 

| Template Name | Vibe / Style | View Build |
| :--- | :--- | :--- |
| **RB3 TorBox Pro + RD Hybrid** | Premium Dual-Service | [View JSON](Community-Templates/Templates/RB3/rb3-2026-05-18.04-04-30-4r5bofv-template.json) |
| **Auburn Tiger Edition (by RB3)** | Warm / Aggressive | [View JSON](Community-Templates/Templates/RB3/auburn-tiger-rb3.json) |

> **⚠️ Note on Community Templates:**
> These files are not subject to the same strict character-limit and UI-breaking tests as the Core Nexus Masterfiles. Use them freely, but expect occasional formatting quirks depending on your scraper results.

### Want to contribute?
If you've built a killer AIOStreams formatter, open a Pull Request and submit your `.json` file to the `Community-Templates/Templates/` folder!

---

## ⚙️ Quick Start: How to Import

1. Navigate to your preferred AIOStreams host.
2. Go to the **Template Import** menu.
3. Copy the **Raw Link** for your chosen build and paste it into the importer:
    * [1080p Single - Raw Link](https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/main/Templates/Single-Service/core-nexus-torbox-exclusive_rpdb.json)
    * [4K Single - Raw Link](https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/main/Templates/Single-Service/core-nexus-4k-ht-torbox.json)
    * [1080p Dual Core - Raw Link](https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/main/Templates/Dual-Service/core-nexus-dual-core-1080p.json)
    * [4K Dual Core - Raw Link](https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/main/Templates/Dual-Service/core-nexus-dual-core-4k.json)
4. Follow the setup instructions in the [`/Guides`](./Guides) folder.

---

## 📜 Code of Conduct
We are committed to fostering a welcoming, respectful, and harassment-free environment for everyone. This project has adopted the Contributor Covenant Code of Conduct. 

By participating in this project or our Discord community, you agree to abide by its terms. Please read our full [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

---

## 💬 Connect on Discord
Have questions, feedback, or need help tweaking your setup? You can reach out to me directly on Discord:
* **Discord Username:** `tazzakaz` (Display Name: *Branding_Brevity*)

## ☕ Support the Project
If these templates have leveled up your home theater setup and saved you from buffering headaches, consider supporting the continuous updates! 

**✨ Supporter Perks:**
* **Custom Hardware Build:** Donations allow you to request a completely custom AIOStreams template, tailored specifically to your exact hardware capabilities, network limits, and viewing preferences!
* **Early Access:** Get temporary early access to all new beta builds and upcoming template updates before they go public!

[![Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/branding_brevity/?hidefeed=true&widget=true&embed=true)

---
*Built and maintained by Branding_Brevity.*
