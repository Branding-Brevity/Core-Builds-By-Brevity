# Core Nexus Speed 4K (EasyNews)
**Version:** 2.2.0 · **Services:** TorBox Essential + EasyNews · **Resolution:** 4K HDR

> Speed-first at 4K. Strips all slow scrapers to 4 addons -- Library, TorBox Search, Comet, and Zilean. Delivers cached 4K results in 2-3 seconds. Dolby Vision, TrueHD, full REMUX up to 150 GB. SeaDex enforced for anime.

---

## Designed For

Users with TorBox Essential and EasyNews who want 4K quality without sacrificing load speed. Shield, Apple TV 4K, high-end OLED/QLED displays.

---

## What It Targets / What It Blocks

| Category | Targets | Blocks |
|---|---|---|
| **Resolution** | 2160p, 1080p | 1440p, Unknown |
| **Quality** | BluRay REMUX, BluRay, WEB-DL, WEBRip | CAM, SCR, TS, TC, HC HD-Rip |
| **Visual** | DV, HDR+DV, HDR10+, HDR10, HDR, HLG, SDR | 3D, H-OU, H-SBS |
| **Audio** | Atmos, DTS:X, TrueHD, DTS-HD MA | -- |
| **Channels** | 7.1 preferred, 5.1 fallback | -- |
| **Streams** | Cached only | P2P, uncached, YouTube |

---

## File Size Limits

| Resolution | Movies | Series |
|---|---|---|
| **Global** | 5 GB -- 150 GB | 1 GB -- 80 GB |
| **2160p** | 5 GB -- 150 GB | 1 GB -- 80 GB |
| **1080p** | 1 GB -- 30 GB | 512 MB -- 20 GB |

---

## Addons

| Addon | Purpose | State |
|---|---|---|
| Library | Personal debrid library -- first priority, instant | On |
| TorBox Search | TorBox native search -- torrent + usenet index | On |
| Comet | Fastest external debrid scraper | On |
| Zilean | DMM hashlist -- fast hash-based debrid lookup | On |
| OpenSubtitles V3+ | Hash-matched subtitle search | On |

---

## Key Configuration

| Setting | Value |
|---|---|
| Services | TorBox Essential + EasyNews (all 12 opt-in) |
| Timeouts | 3500ms across all addons |
| Result limit | 10 global · 4 per resolution |
| Sort keys | 5 -- cached > expression > quality > regexScore > seeders |
| SeaDex best-only | On (anime) |
| Scored regex ranking | 149 patterns (full 4K set) |
| Tamtaro ESEs | Full inline set -- no synced URL needed |
| Episode matching | Strict |
| cacheAndPlay | Enabled for Usenet streams |

---

## Quick Import

```
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/EasyNews/core-nexus-speed-4k.json
```

---

*Part of [Core Builds by Brevity](https://github.com/Branding-Brevity/Core-Builds-By-Brevity) -- [Import Guide](../../../Guides/IMPORT_GUIDE.md) -- [Changelog](../../../CHANGELOG.md)*
