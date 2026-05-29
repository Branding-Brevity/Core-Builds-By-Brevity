# Core Builds — Template Directory

All active templates for AIOStreams v2.30+. Every template requires a **TorBox subscription**. All templates ship with the Core Nexus Uniform Formatter, Core Builds ESE/PSE/ISE filtering, tier-specific audio PSEs, and in-app update notifications.

---

## 🗺️ Which Template Should I Use?

```
Do you have TorBox Pro or Essential?
│
├── Pro ──────────────────────────────────────────────────────────────────────┐
│   Do you use a Usenet indexer (NZBGeek, NinjaCentral etc.)?                 │
│   ├── Yes → Core Nexus Hybrid                                               │
│   └── No                                                                    │
│       What resolution do you want?                                          │
│       ├── 4K HDR → Core Nexus 4K Pro                                        │
│       └── 1080p WEB-DL only → Core Nexus Stream                            │
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
        └── 1080p → Core Nexus Essential                                      │
                                                                              │
Watching anime? → Core Nexus Anime (any plan)
```

---

## 📋 Full Template Comparison

| Template | Plan | Resolution | Usenet | Speed | Best For |
|---|---|---|---|---|---|
| [Core Nexus 4K Pro](#-core-nexus-4k-pro) | TorBox Pro | 4K + 1080p | ✅ | Standard | Home theater, Shield, Apple TV 4K |
| [Core Nexus Stream](#-core-nexus-stream) | TorBox Pro | 1080p WEB only | ✅ | Standard | Budget hardware, WEB-DL purists |
| [Core Nexus Hybrid](#-core-nexus-hybrid) | TorBox Pro + NZBGeek | 1080p | ✅ NZBGeek | Standard | Dual Usenet indexer setup |
| [Core Nexus 4K Essential](#-core-nexus-4k-essential) | Essential | 4K + 1080p | ❌ | Standard | Shield, Apple TV 4K, no Usenet |
| [Core Nexus Essential](#-core-nexus-essential) | Essential | 1080p | ❌ | Standard | 1080p, no Usenet |
| [Core Nexus Speed 4K+](#-core-nexus-speed-4k) | Essential + EasyNews | 4K | ✅ EasyNews | ⚡ Fast | Instant 4K + Usenet depth |
| [Core Nexus Speed 4K](#-core-nexus-speed-4k-1) | Essential | 4K | ❌ | ⚡ Fast | Instant 4K |
| [Core Nexus Speed+](#-core-nexus-speed) | Essential + EasyNews | 1080p | ✅ EasyNews | ⚡ Fast | Instant 1080p + Usenet depth |
| [Core Nexus Speed](#-core-nexus-speed-1) | Essential | 1080p | ❌ | ⚡ Fast | Instant 1080p |
| [Core Nexus Anime](#-core-nexus-anime) | Essential | 1080p + 4K | ❌ | Standard | Anime — seasonal, movies, series |

---

## 📥 How to Import

1. Copy the raw URL for your chosen template below
2. Open your AIOStreams host → **About → Get Started → Use a Template**
3. Paste the URL and click **Load**
4. Enable **TorBox** in Services and enter your API key
5. Click **Save** → copy the manifest URL → install in Stremio or WuPlay

Full walkthrough: [Import Guide](../../Guides/IMPORT_GUIDE.md)

---

## 🔵 TorBox Pro Templates

### 🏆 Core Nexus 4K Pro

The flagship build. Full addon stack — Library, Zilean, STorz, Meteor, Comet, MediaFusion, Knaben, Torrent Galaxy, Newznab, OpenSubtitles. Usenet failover via cacheAndPlay. Targets DV/HDR, TrueHD/Atmos, BluRay REMUX.

| | |
|---|---|
| **File** | `core-nexus-4k-pro.json` |
| **Folder** | `Templates/Torbox/Single/` |
| **Version** | v2.4.0 |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Single/core-nexus-4k-pro.json` |
| **Resolution** | 2160p primary, 1080p fallback |
| **Usenet** | ✅ cacheAndPlay + nzbFailover |
| **Docs** | [README](Single/README_4k-ht-torbox.md) |

---

### 📺 Core Nexus Stream

1080p WEB-DL only. BluRay and Remux excluded. For budget hardware or WEB-DL purists.

| | |
|---|---|
| **File** | `core-nexus-stream.json` |
| **Folder** | `Templates/Torbox/Single/` |
| **Version** | v2.4.0 |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Single/core-nexus-stream.json` |
| **Resolution** | 1080p · 720p fallback |
| **Usenet** | ✅ via Newznab (opt-in) |
| **Docs** | [README](Single/README_torbox-exclusive-rpdb.md) |

---

### 🔀 Core Nexus Hybrid

TorBox Pro + NZBGeek. Maximum source diversity — debrid and Usenet combined, cached and uncached.

| | |
|---|---|
| **File** | `core-nexus-hybrid.json` |
| **Folder** | `Templates/Torbox/Hybrid/` |
| **Version** | v2.4.0 |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Hybrid/core-nexus-hybrid.json` |
| **Resolution** | 1080p · 720p fallback |
| **Usenet** | ✅ NZBGeek API key required |
| **Docs** | [README](Hybrid/README_tb-hybrid-1080p.md) |

> ⚠️ After import go to **Add-ons → Newznab** and enter your NZBGeek API key.

---

## 🟡 TorBox Essential Templates

### 💎 Core Nexus 4K Essential

Full 4K build for TorBox Essential. DV, HDR, REMUX targets — no Usenet layer.

| | |
|---|---|
| **File** | `core-nexus-4k-essential.json` |
| **Folder** | `Templates/Torbox/Essential/` |
| **Version** | v2.4.0 |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Essential/core-nexus-4k-essential.json` |
| **Resolution** | 2160p primary, 1080p fallback |
| **Usenet** | ❌ |
| **Docs** | [README](Essential/README_4k-essential-torbox.md) |

---

### 📱 Core Nexus Essential

1080p for Essential subscribers. SDR-focused, clean WEB-DL streams.

| | |
|---|---|
| **File** | `core-nexus-essential.json` |
| **Folder** | `Templates/Torbox/Essential/` |
| **Version** | v2.4.0 |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Essential/core-nexus-essential.json` |
| **Resolution** | 1080p · 720p fallback |
| **Usenet** | ❌ |
| **Docs** | [README](Essential/README_1080p-essential-torbox.md) |

---

## ⚡ Speed Tier Templates

Zilean first (2000ms) for instant cached lookups. **Cached streams only** — zero results means the content isn't in TorBox's cache yet. Try a popular title first. Result limit 10 global / 4 per resolution.

### ⚡ Core Nexus Speed 4K+ *(EasyNews)*

| | |
|---|---|
| **File** | `core-nexus-speed-4k-plus.json` |
| **Folder** | `Templates/Torbox/Speed/EasyNews/` |
| **Version** | v2.4.0 |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/EasyNews/core-nexus-speed-4k-plus.json` |
| **Requires** | TorBox Essential + EasyNews |

### ⚡ Core Nexus Speed 4K

| | |
|---|---|
| **File** | `core-nexus-speed-4k.json` |
| **Folder** | `Templates/Torbox/Speed/TorBox/` |
| **Version** | v2.4.0 |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/TorBox/core-nexus-speed-4k.json` |
| **Requires** | TorBox Essential |

### ⚡ Core Nexus Speed+ *(EasyNews)*

| | |
|---|---|
| **File** | `core-nexus-speed-plus.json` |
| **Folder** | `Templates/Torbox/Speed/EasyNews/` |
| **Version** | v2.4.0 |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/EasyNews/core-nexus-speed-plus.json` |
| **Requires** | TorBox Essential + EasyNews |

### ⚡ Core Nexus Speed

| | |
|---|---|
| **File** | `core-nexus-speed.json` |
| **Folder** | `Templates/Torbox/Speed/TorBox/` |
| **Version** | v2.4.0 |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/TorBox/core-nexus-speed.json` |
| **Requires** | TorBox Essential |

---

## 🎌 Anime Template

### 🎌 Core Nexus Anime

SeaDex best-release enforcement, AnimeTosho for Nyaa coverage, FLAC/AAC audio priority, SDR-first, WEB-DL from Crunchyroll and HiDive prioritised. Japanese + English + Dual Audio.

| | |
|---|---|
| **File** | `core-nexus-anime.json` |
| **Folder** | `Templates/Torbox/Anime/` |
| **Version** | v2.4.0 |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Anime/core-nexus-anime.json` |
| **Resolution** | 1080p primary · 2160p supported · 720p fallback |
| **Languages** | Japanese · English · Dual Audio · Multi · Dubbed |
| **Docs** | [README](Anime/README_anime.md) |

---

## 🗂️ All Raw Import URLs

```
# TorBox Pro
Core Nexus 4K Pro
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Single/core-nexus-4k-pro.json

Core Nexus Stream
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Single/core-nexus-stream.json

Core Nexus Hybrid
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Hybrid/core-nexus-hybrid.json

# TorBox Essential
Core Nexus 4K Essential
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Essential/core-nexus-4k-essential.json

Core Nexus Essential
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Essential/core-nexus-essential.json

# Speed — EasyNews
Core Nexus Speed 4K+
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/EasyNews/core-nexus-speed-4k-plus.json

Core Nexus Speed+
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/EasyNews/core-nexus-speed-plus.json

# Speed — TorBox Only
Core Nexus Speed 4K
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/TorBox/core-nexus-speed-4k.json

Core Nexus Speed
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/TorBox/core-nexus-speed.json

# Anime
Core Nexus Anime
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Anime/core-nexus-anime.json
```

---

## 🛠️ Common to All Templates (v2.4.0)

- **Quality hard-blocking** — `CAM`, `SCR`, `TS`, `TC`, `HDTV`, `DVDRip`, `BluRay REMUX` (on 1080p templates) blocked via `excludedQualities`. ESEs provide a second layer.
- **Core Builds Filtering System** — Custom ESEs, PSEs, ISEs baked in. CAM Kill, YouTube Kill, 3D Kill, Season Pack Guard. No external whitelist dependency.
- **Core Nexus Uniform Formatter** — Resolution + service badge in title. 🚀/⚠️ cache status, SE score, release group, full video/audio/language rows.
- **Tier-specific audio PSEs** — Preferred audio formats scored per tier. 4K: Atmos first. 1080p: DD+ first. Speed: DD+/DD/AAC. Anime: FLAC first.
- **Vidhin05 ranked regex** — Release group scoring from `Vidhin05/Releases-Regex`.
- **RPDB free posters** — `t0-free-rpdb` baked in on all templates.
- **Matching filters** — Title (`contains`, 0.85 threshold), Year (±2yr, initial air date), Season/Episode (strict).
- **Deduplicator** — `filename + infoHash + smartDetect`. Cached: `single_result`.
- **`dynamicAddonFetching`** — Stops querying when enough quality cached results found.
- **`precacheNextEpisode` + `preloadStreams`** — Next episode queued while watching current.
- **`autoPlay`** — Pre-selects matching stream. Works with WuPlay autoplay.
- **`digitalReleaseFilter`** — 14-day tolerance. Prevents fake WEB-DL on in-theater content.
- **`metadata.changelog`** — In-app update notifications when new versions release.
- **TMDB API key** — Optional input field rendered on import.

---

*Part of [Core Builds by Brevity](https://github.com/Branding-Brevity/Core-Builds-By-Brevity) · [Main README](../../README.md) · [Import Guide](../../Guides/IMPORT_GUIDE.md)*


---

## 🌍 Community Templates

| Template | Author | Docs |
|---|---|---|
| [Prism TorBox Essential 1080p](Community/prism-torbox-essential-1080p.json) | MightyIcyy | [README](Community/README_prism-torbox-essential-1080p.md) |
| [Core Nexus Kids (Swedish)](Community/core-nexus-kids-swedish.json) | snusgeneralen | — |
