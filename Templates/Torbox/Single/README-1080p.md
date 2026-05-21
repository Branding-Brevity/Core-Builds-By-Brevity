# 📦 Core Nexus 1080p SDR — TorBox Exclusive

**File:** `core-nexus-torbox-exclusive_rpdb.json`
**Version:** `1.2.0`
**Profile:** Low-End Hardware · 1080p · SDR · TorBox Only

---

## 🎯 Purpose

Engineered for low-end hardware running on a single TorBox subscription. Strips out everything that causes buffering, network choking, or codec incompatibility on Android projectors, Google TV sticks, and budget Android TVs.

## ⚙️ What It Does

- **Resolution locked to 1080p / 720p** — blocks 4K, 1440p, and Unknown
- **BluRay & Remux killed** at both quality filter and stream expression layers
- **SDR only** — strips Dolby Vision, HDR10, HDR10+, HLG, HDR
- **Encode-safe** — HEVC and AVC only, blocks AV1
- **Audio capped at 5.1** — blocks TrueHD, DTS-HD MA, DTS:X, FLAC. Allows DD+/EAC3/DTS/AAC
- **Bitrate cap: 60Mbps** — prevents network choking
- **File size limits:** 15GB movies / 8GB series
- **Cached streams only** — instant playback, no waiting
- **YouTube triple-block** — AI-enhanced YouTube links blocked at 3 layers
- **CAM/SCR/TS/TC hard-killed**

## 🧩 Addon Stack (14 presets)

| Tier | Speed | Addons |
|---|---|---|
| 1 | ≤4000ms | Library · TorBox Search · StremThru Torz · Comet |
| 2 | 5000ms | Meteor · Zilean · SeaDex · AnimeTosho · Searchⁿᶻᵇ · MediaFusion |
| 3 | 6000ms | TorrentGalaxy · Knaben · Peerflix |
| 4 | 4000ms | OpenSubtitles V3+ |

## 🔑 Required Keys

- **TorBox API Key** (required)
- **TMDB API Key** (required — link below the input field)
- **RPDB API Key** (pre-filled with free tier, leave as-is)

## 📥 Quick Import

```
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/main/Templates/TorBox/Single/core-nexus-torbox-exclusive_rpdb.json
```

## ⚠️ Best For

✅ Android projectors · Google TV · low-end Android TV · phones · tablets
❌ Nvidia Shield · 4K OLED/QLED — use the [4K HT TorBox](../4K-HT/README.md) instead

---

*Part of [Core Builds by Brevity](https://github.com/Branding-Brevity/Core-Builds-By-Brevity)*
