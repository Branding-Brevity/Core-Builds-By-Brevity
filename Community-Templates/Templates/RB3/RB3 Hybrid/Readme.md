# 🚀 RB3 TorBox Pro + RD Hybrid

A premium, dual-service AIOStreams template designed to maximize stream availability by combining the power of **TorBox Pro** and **Real-Debrid**. Built on top of the robust Tamtaro SEL framework, this configuration is heavily biased toward high-quality, cached Usenet releases. 

## ✨ Key Features

### 🔗 Dual-Service Engine
* **Primary:** TorBox (with specific rules to respect TB Pro limits, e.g., 1TB uncached download limits).
* **Fallback:** Real-Debrid seamlessly fills in any gaps.
* **Usenet Priority:** Employs a custom Stream Expression (`/*Boost Cached Usenet*/`) to force all cached Usenet streams to the absolute top of your results.

### 📺 High-End Hardware Profile
* **Unrestricted Quality:** Prefers all premium formats ranging from 4K down to 144p. Prioritizes `BluRay REMUX` and `BluRay` releases.
* **Massive File Allowances:** Global size limits are set to a massive **100GB** for both Movies and Series.
* **Uncapped Bitrate:** Hardware bitrate ceiling is pushed to **250 Mbps**, ensuring zero compression bottlenecks for heavy 4K REMUXes.
* **Premium A/V Tags:** Fully prioritizes advanced visual tags (Dolby Vision, HDR10+, IMAX) and heavy lossless audio formats (Dolby Atmos, DTS:X, TrueHD, DTS-HD MA).

### ⚙️ Advanced Filtering & Sorting
* **Tamtaro SEL Framework (v2.6.1):** Integrates Tamtaro's live-synced Preferred, Excluded, and Included Stream Expressions (PSE/ESE/ISE) for dynamic, cloud-updated filtering.
* **Vidhin's English Regex:** Live-syncs Vidhin's Ranked Regexes to intelligently score and sort releases based on trusted release groups and formatting standards.
* **Aggressive Deduplication:** Uses AIOStreams' "Aggressive" Smart Detect deduplicator to clean up bloated result lists by merging identical files based on infoHashes, file sizes, and audio/video tracks.

### 🧩 Included Addons (Presets)
This template comes pre-wired with a highly optimized stack of scrapers and utilities:
* **Debrid / Torrents:** Meteor, Comet, Torrentio, Knaben, Sootio
* **Usenet Search:** Searchⁿᶻᵇ (via TorBox), STorz (Torznab)
* **Anime:** SeaDex
* **Subtitles:** OpenSubtitles V3+ (Defaulted to English)
* **UI:** Library integration (TorBox & Real-Debrid catalogs pushed to Discover)

### 🎨 Custom Visual Formatter
Includes a highly customized, compact data formatter that injects visual badges directly into Stremio. It translates complex stream data into easy-to-read icons:
* **Source Tags:** `[nzb]`, `[p2p]`, `[web]`
* **Health Indicators:** Identifies verified/unverified Usenet health directly in the title.
* **Dynamic Badging:** Replaces standard tags with clean typography (e.g., `4K`, `Remux`, `HDR`, `Atmos`).
* **SeaDex Integration:** Clearly marks "Best Release" and "Alt Best Release" for anime watchers.

## 🛠️ Prerequisites
To use this template to its full potential, ensure you have the following API keys ready during the AIOStreams setup:
1. **TorBox API Key** (Pro tier recommended for Usenet)
2. **Real-Debrid API Key**
3. **TMDB API Key & Read Access Token** (Free)
4. **TVDB API Key** (Free)
5. **RPDB API Key** (Free tier supported for custom posters)
6. 
