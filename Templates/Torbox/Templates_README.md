# Core Builds — Template Directory

All active templates for AIOStreams. Every template requires a **TorBox subscription** — choose the tier that matches your plan.

---

## 🗺️ Which Template Should I Use?

```
Do you have TorBox Pro or Essential?
│
├── Pro ──────────────────────────────────────────────────────────────────────┐
│   Do you use a Usenet indexer (NZBGeek etc.)?                               │
│   ├── Yes → Core Nexus Hybrid                                               │
│   └── No                                                                    │
│       What resolution do you want?                                          │
│       ├── 4K HDR → Core Nexus 4K Pro                                        │
│       └── 1080p WEB-DL only (no BluRay/Remux) → Core Nexus Stream          │
│                                                                             │
└── Essential ────────────────────────────────────────────────────────────────┐
    Do you want instant autoplay (2-3s) or maximum coverage?                  │
    ├── Instant → Speed tier                                                  │
    │   Do you also subscribe to EasyNews?                                    │
    │   ├── Yes, 4K → Core Nexus Speed 4K+                                   │
    │   ├── Yes, 1080p → Core Nexus Speed+                                    │
    │   ├── No, 4K → Core Nexus Speed 4K                                      │
    │   └── No, 1080p → Core Nexus Speed                                      │
    └── Maximum coverage                                                      │
        ├── 4K HDR → Core Nexus 4K Essential                                  │
        └── 1080p SDR → Core Nexus Essential                                  │
                                                                              │
Watching anime only? → Core Nexus Anime (any plan)
```

---

## 📋 Full Template Comparison

| Template | Plan | Resolution | Usenet | Speed | Best For |
|---|---|---|---|---|---|
| [Core Nexus 4K Pro](#-core-nexus-4k-pro) | Pro | 4K + 1080p | ✅ | Standard | Full home theater, Shield, Apple TV 4K |
| [Core Nexus Stream](#-core-nexus-stream) | Pro | 1080p WEB only | ✅ | Standard | Budget hardware, WEB-DL purists |
| [Core Nexus Hybrid](#-core-nexus-hybrid) | Pro | 1080p | ✅ NZBGeek | Standard | TorBox Pro + Usenet indexer subscribers |
| [Core Nexus 4K Essential](#-core-nexus-4k-essential) | Essential | 4K + 1080p | ❌ | Standard | Shield, Apple TV 4K, no Usenet |
| [Core Nexus Essential](#-core-nexus-essential) | Essential | 1080p | ❌ | Standard | Budget hardware, no Usenet |
| [Core Nexus Speed 4K+](#-core-nexus-speed-4k) | Essential | 4K | ✅ EasyNews | ⚡ Fast | Instant 4K + Usenet depth |
| [Core Nexus Speed 4K](#-core-nexus-speed-4k-1) | Essential | 4K | ❌ | ⚡ Fast | Instant 4K |
| [Core Nexus Speed+](#-core-nexus-speed) | Essential | 1080p | ✅ EasyNews | ⚡ Fast | Instant 1080p + Usenet depth |
| [Core Nexus Speed](#-core-nexus-speed-1) | Essential | 1080p | ❌ | ⚡ Fast | Instant 1080p |
| [Core Nexus Anime](#-core-nexus-anime) | Essential | 1080p + 4K | ❌ | Standard | Anime — seasonal, movies, series |

---

## 📥 How to Import

1. Copy the raw URL for your chosen template from the table below
2. Open your AIOStreams host → **About → Get Started → Use a Template**
3. Paste the URL and click **Load**
4. Enable your TorBox service and enter your API key
5. Click **Save**, copy the manifest URL, install in Stremio or WuPlay

Full walkthrough: [Import Guide](../../Guides/IMPORT_GUIDE.md)

---

## 🔵 TorBox Pro Templates

### 🏆 Core Nexus 4K Pro

The flagship build. Full addon stack with Usenet failover. Targets DV/HDR, TrueHD/Atmos, BluRay REMUX up to 150 GB.

| | |
|---|---|
| **File** | `core-nexus-4k-ht-torbox.json` |
| **Folder** | `Templates/Torbox/Single/` |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Single/core-nexus-4k-ht-torbox.json` |
| **Resolution** | 2160p primary, 1080p fallback |
| **Addons** | Library · Zilean · Meteor · Comet · Knaben · Torrent Galaxy · Newznab · OpenSubtitles |
| **Usenet** | ✅ cacheAndPlay + nzbFailover |
| **Docs** | [README](Single/README_4k-ht-torbox.md) |

---

### 📺 Core Nexus Stream

1080p WEB-DL only. BluRay and Remux blocked. For hardware that struggles with 4K or users who want pure streaming sources only.

| | |
|---|---|
| **File** | `core-nexus-torbox-exclusive_rpdb.json` |
| **Folder** | `Templates/Torbox/Single/` |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Single/core-nexus-torbox-exclusive_rpdb.json` |
| **Resolution** | 1080p · 720p fallback |
| **Addons** | Library · Zilean · Meteor · Comet · Knaben · Torrent Galaxy · OpenSubtitles |
| **Usenet** | ✅ via Newznab (opt-in) |
| **Docs** | [README](Single/README_torbox-exclusive-rpdb.md) |

---

### 🔀 Core Nexus Hybrid

TorBox Pro combined with NZBGeek. Maximum source diversity — debrid and Usenet combined, cached and uncached.

| | |
|---|---|
| **File** | `core-nexus-tb-hybrid-1080p.json` |
| **Folder** | `Templates/Torbox/Hybrid/` |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Hybrid/core-nexus-tb-hybrid-1080p.json` |
| **Resolution** | 1080p · 720p fallback |
| **Addons** | Library · Zilean · Meteor · Comet · Knaben · Torrent Galaxy · Newznab · OpenSubtitles |
| **Usenet** | ✅ NZBGeek API key required |
| **Docs** | [README](Hybrid/README_tb-hybrid-1080p.md) |

> ⚠️ After import go to **Add-ons → Newznab** and enter your NZBGeek API key.

---

## 🟡 TorBox Essential Templates

### 💎 Core Nexus 4K Essential

Full 4K build for TorBox Essential subscribers. Same quality targets as 4K Pro — DV, HDR, REMUX — without the Usenet layer.

| | |
|---|---|
| **File** | `core-nexus-4k-essential-torbox.json` |
| **Folder** | `Templates/Torbox/Essential/` |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Essential/core-nexus-4k-essential-torbox.json` |
| **Resolution** | 2160p primary, 1080p fallback |
| **Addons** | Library · Zilean · Meteor · Comet · Knaben · Torrent Galaxy · OpenSubtitles |
| **Usenet** | ❌ |
| **Docs** | [README](Essential/README_4k-essential-torbox.md) |

---

### 📱 Core Nexus Essential

1080p for Essential subscribers. SDR-focused, clean WEB-DL streams, no REMUX.

| | |
|---|---|
| **File** | `core-nexus-1080p-essential-torbox.json` |
| **Folder** | `Templates/Torbox/Essential/` |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Essential/core-nexus-1080p-essential-torbox.json` |
| **Resolution** | 1080p · 720p fallback |
| **Addons** | Library · Zilean · Meteor · Comet · Knaben · Torrent Galaxy · OpenSubtitles |
| **Usenet** | ❌ |
| **Docs** | [README](Essential/README_1080p-essential-torbox.md) |

---

## ⚡ Speed Tier Templates

Speed templates put Zilean first for instant cached lookups. Optimised for 2-3 second stream delivery.

### ⚡ Core Nexus Speed 4K+ *(EasyNews)*

4K with EasyNews Usenet boost. Best instant 4K option.

| | |
|---|---|
| **File** | `core-nexus-speed-4k.json` |
| **Folder** | `Templates/Torbox/Speed/EasyNews/` |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/EasyNews/core-nexus-speed-4k.json` |
| **Resolution** | 2160p · 1080p fallback |
| **Requires** | TorBox Essential + EasyNews subscription |
| **Docs** | [README](Speed/EasyNews/README_speed-4k-easynews.md) |

### ⚡ Core Nexus Speed 4K

4K instant autoplay. TorBox Essential only.

| | |
|---|---|
| **File** | `core-nexus-speed-4k-torbox.json` |
| **Folder** | `Templates/Torbox/Speed/TorBox/` |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/TorBox/core-nexus-speed-4k-torbox.json` |
| **Resolution** | 2160p · 1080p fallback |
| **Requires** | TorBox Essential |
| **Docs** | [README](Speed/TorBox/README_speed-4k-torbox.md) |

### ⚡ Core Nexus Speed+ *(EasyNews)*

1080p with EasyNews Usenet boost. Best instant 1080p option.

| | |
|---|---|
| **File** | `core-nexus-speed-1080p.json` |
| **Folder** | `Templates/Torbox/Speed/EasyNews/` |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/EasyNews/core-nexus-speed-1080p.json` |
| **Resolution** | 1080p · 720p fallback |
| **Requires** | TorBox Essential + EasyNews subscription |
| **Docs** | [README](Speed/EasyNews/README_speed-1080p-easynews.md) |

### ⚡ Core Nexus Speed

1080p instant autoplay. TorBox Essential only.

| | |
|---|---|
| **File** | `core-nexus-speed-1080p-torbox.json` |
| **Folder** | `Templates/Torbox/Speed/TorBox/` |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/TorBox/core-nexus-speed-1080p-torbox.json` |
| **Resolution** | 1080p · 720p fallback |
| **Requires** | TorBox Essential |
| **Docs** | [README](Speed/TorBox/README_speed-1080p-torbox.md) |

---

## 🎌 Anime Template

### 🎌 Core Nexus Anime

Dedicated anime build. SeaDex best-release enforcement, AnimeTosho for full Nyaa coverage, FLAC/AAC audio priority, SDR-first, WEB-DL from Crunchyroll and HiDive prioritised.

| | |
|---|---|
| **File** | `core-nexus-anime.json` |
| **Folder** | `Templates/Torbox/Anime/` |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Anime/core-nexus-anime.json` |
| **Resolution** | 1080p primary · 2160p supported · 720p fallback |
| **Addons** | Library · SeaDex · AnimeTosho · Zilean · Comet · Meteor · Knaben · OpenSubtitles |
| **Usenet** | ❌ |
| **Languages** | Japanese · English · Dual Audio · Multi · Dubbed |
| **Docs** | [README](Anime/README_anime.md) |

---

## 🗂️ All Raw Import URLs

```
# TorBox Pro
Core Nexus 4K Pro
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Single/core-nexus-4k-ht-torbox.json

Core Nexus Stream
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Single/core-nexus-torbox-exclusive_rpdb.json

Core Nexus Hybrid
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Hybrid/core-nexus-tb-hybrid-1080p.json

# TorBox Essential
Core Nexus 4K Essential
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Essential/core-nexus-4k-essential-torbox.json

Core Nexus Essential
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Essential/core-nexus-1080p-essential-torbox.json

# Speed — EasyNews
Core Nexus Speed 4K+
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/EasyNews/core-nexus-speed-4k.json

Core Nexus Speed+
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/EasyNews/core-nexus-speed-1080p.json

# Speed — TorBox Only
Core Nexus Speed 4K
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/TorBox/core-nexus-speed-4k-torbox.json

Core Nexus Speed
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/TorBox/core-nexus-speed-1080p-torbox.json

# Anime
Core Nexus Anime
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Anime/core-nexus-anime.json
```

---

## 🛠️ Common to All Templates

- **Core Builds Filtering System** — Custom ESEs, PSEs, ISEs baked in. No external whitelist dependency.
- **Core Nexus Uniform Formatter** — Pre-loaded. Resolution badge · service name · cache status · SE score · release group · video/audio/language rows.
- **Vidhin05 ranked regex** — Release group scoring synced from `Vidhin05/Releases-Regex`.
- **RPDB free posters** — `t0-free-rpdb` baked in on all templates.
- **TMDB API key** — Optional input field rendered on import.
- **12-service roster** — All opt-in. Enable only what you subscribe to.
- **TorBox pre-enabled** — Toggle on and enter your API key after import.

---

*Part of [Core Builds by Brevity](https://github.com/Branding-Brevity/Core-Builds-By-Brevity) · [Main README](../../README.md) · [Import Guide](../../Guides/IMPORT_GUIDE.md)*
