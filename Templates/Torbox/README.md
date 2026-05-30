# Core Builds — Template Directory

All active templates for AIOStreams v2.30+. Every template requires a **TorBox subscription**. All templates ship with the **Core Syntax Formatter**, Tamtaro standard ESEs + Core Builds kill ESEs, Tamtaro ISEs, and in-app update notifications.

> **Current version: v2.4.4** · [CHANGELOG](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/CHANGELOG.md)

---

## 🗺️ Which Template?

```
TorBox Pro?
├── Got NZBGeek/Usenet indexer? → Hybrid
├── Want 4K? → 4K Pro
└── 1080p only? → Stream

TorBox Essential?
├── Instant play (2-3s)? → Speed tier
│   ├── + EasyNews, 4K → Speed 4K+
│   ├── + EasyNews, 1080p → Speed+
│   ├── No EasyNews, 4K → Speed 4K
│   └── No EasyNews, 1080p → Speed
├── Want 4K? → 4K Essential
└── 1080p standard? → Essential

Anime? → Anime (any plan)
```

---

## 📋 All Templates

| Template | Plan | Res | Import URL |
|---|---|---|---|
| **Core Nexus 4K Pro** | TorBox Pro | 4K+1080p | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Single/core-nexus-4k-pro.json` |
| **Core Nexus Stream** | TorBox Pro | 1080p | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Single/core-nexus-stream.json` |
| **Core Nexus Hybrid** | Pro + NZBGeek | 1080p | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Hybrid/core-nexus-hybrid.json` |
| **Core Nexus 4K Essential** | Essential | 4K+1080p | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Essential/core-nexus-4k-essential.json` |
| **Core Nexus Essential** | Essential | 1080p | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Essential/core-nexus-essential.json` |
| **Core Nexus Speed 4K+** | Essential + EasyNews | 4K | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/EasyNews/core-nexus-speed-4k-plus.json` |
| **Core Nexus Speed+** | Essential + EasyNews | 1080p | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/EasyNews/core-nexus-speed-plus.json` |
| **Core Nexus Speed 4K** | Essential | 4K | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/TorBox/core-nexus-speed-4k.json` |
| **Core Nexus Speed** | Essential | 1080p | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/TorBox/core-nexus-speed.json` |
| **Core Nexus Anime** 🎌 | Essential | 1080p+4K | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Anime/core-nexus-anime.json` |

---

## 📥 How to Import

1. Copy the import URL from the table above
2. Open your AIOStreams host → **About → Get Started → Load Template** → paste URL
3. Enter your **TorBox API key** in Services
4. Enter your **TMDB Access Token** (recommended — improves title matching)
5. Save → copy manifest URL → install in Stremio or WuPlay

---

## 🔵 TorBox Pro Templates

### 🏆 Core Nexus 4K Pro

Flagship 4K build. Full addon stack. Targets DV/HDR, TrueHD/Atmos, BluRay REMUX. cacheAndPlay for both Usenet and debrid torrents.

| | |
|---|---|
| **File** | `Templates/Torbox/Single/core-nexus-4k-pro.json` |
| **Version** | v2.4.4 |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Single/core-nexus-4k-pro.json` |
| **Resolution** | 2160p primary, 1080p fallback |
| **Usenet** | ✅ cacheAndPlay + nzbFailover |

---

### 📺 Core Nexus Stream

1080p WEB-DL only. BluRay and Remux excluded. Best for budget hardware or WEB-DL purists.

| | |
|---|---|
| **File** | `Templates/Torbox/Single/core-nexus-stream.json` |
| **Version** | v2.4.4 |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Single/core-nexus-stream.json` |
| **Resolution** | 1080p · 720p fallback |
| **Usenet** | ✅ via Newznab (opt-in) |

---

### 🔀 Core Nexus Hybrid

TorBox Pro + NZBGeek. Maximum source diversity.

| | |
|---|---|
| **File** | `Templates/Torbox/Hybrid/core-nexus-hybrid.json` |
| **Version** | v2.4.4 |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Hybrid/core-nexus-hybrid.json` |
| **Resolution** | 1080p · 720p fallback |
| **Usenet** | ✅ NZBGeek API key required |

> ⚠️ After import go to **Add-ons → Newznab** and enter your NZBGeek API key.

---

## 🟡 TorBox Essential Templates

### 💎 Core Nexus 4K Essential

Full 4K for Essential plan. No Usenet.

| | |
|---|---|
| **File** | `Templates/Torbox/Essential/core-nexus-4k-essential.json` |
| **Version** | v2.4.4 |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Essential/core-nexus-4k-essential.json` |
| **Resolution** | 2160p primary, 1080p fallback |
| **Usenet** | ❌ |

---

### 📱 Core Nexus Essential

1080p for Essential subscribers.

| | |
|---|---|
| **File** | `Templates/Torbox/Essential/core-nexus-essential.json` |
| **Version** | v2.4.4 |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Essential/core-nexus-essential.json` |
| **Resolution** | 1080p · 720p fallback |
| **Usenet** | ❌ |

---

## ⚡ Speed Tier

> **Zero results?** Check two things: (1) Did you enter your TorBox API key? (2) Speed templates only show cached streams — try a popular title first (e.g. Breaking Bad S01E01). Use Core Nexus Essential for full coverage.

### EasyNews Speed Templates

| | Speed 4K+ | Speed+ |
|---|---|---|
| **Resolution** | 4K | 1080p |
| **Requires** | Essential + EasyNews | Essential + EasyNews |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/EasyNews/core-nexus-speed-4k-plus.json` | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/EasyNews/core-nexus-speed-plus.json` |

### TorBox-Only Speed Templates

| | Speed 4K | Speed |
|---|---|---|
| **Resolution** | 4K | 1080p |
| **Requires** | Essential | Essential |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/TorBox/core-nexus-speed-4k.json` | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/TorBox/core-nexus-speed.json` |

---

## 🎌 Anime

SeaDex best-release enforcement · AnimeTosho (Nyaa.si mirror) · FLAC/AAC first · SDR-first · 1080p WEB-DL · Japanese + English + Dual Audio.

| | |
|---|---|
| **File** | `Templates/Torbox/Anime/core-nexus-anime.json` |
| **Version** | v2.4.4 |
| **Import URL** | `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Anime/core-nexus-anime.json` |
| **Resolution** | 1080p primary · 2160p supported · 720p fallback |

---

## 🛠️ Common to All Templates (v2.4.4)

| Feature | Detail |
|---|---|
| **Formatter** | Core Syntax · `id: tamtaro` · `overrides['tamtaro']` |
| **ESEs** | 24 total — 20 Tamtaro standard + Hard CAM Kill, YouTube Kill, 3D Kill, Season Pack Guard |
| **ISEs** | 6 Tamtaro ISEs — Library, 0Cached, digitalRelease Bypass, SeaDex (anime only) |
| **Sort** | cached → matched → score → resolution → quality → audio → language |
| **Deduplication** | filename + infoHash + smartDetect · 14 attributes · `libraryBehaviour: prefer` |
| **Matching** | title `contains/0.75` · year `±2yr` · season/episode `non-strict` |
| **Auto features** | autoPlay · precacheNextEpisode · preloadStreams · dynamicAddonFetching · checkOwned |
| **Scoring** | Vidhin05 ranked regex · Tamtaro synced PSEs |
| **RPDB** | `t0-free-rpdb` baked in |
| **In-app updates** | `metadata.changelog` embedded |

---

## 🌍 Community Templates

| Template | Author | Import |
|---|---|---|
| [Prism TorBox Essential 1080p](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Community-Templates/prism-torbox-essential-1080p.json) | MightyIcyy | [↓ JSON](https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Community-Templates/prism-torbox-essential-1080p.json) |
| [RB3 TorBox Pro + RD Hybrid](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Community-Templates/Templates/RB3/RB3%20Hybrid/RB3%20TorBox%20Pro%20%2B%20RD%20Hybrid.json) | RB3 | [↓ JSON](https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Community-Templates/Templates/RB3/RB3%20Hybrid/RB3%20TorBox%20Pro%20%2B%20RD%20Hybrid.json) |

> Want your template listed? Open a PR to `Community-Templates/` with your JSON and a README.

---

*Part of [Core Builds by Brevity](https://github.com/Branding-Brevity/Core-Builds-By-Brevity) · [Main README](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/README.md) · [CHANGELOG](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/CHANGELOG.md)*
