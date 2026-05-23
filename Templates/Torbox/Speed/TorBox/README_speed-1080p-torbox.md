# Core Nexus Speed 1080p
**Version:** 2.2.0 · **Services:** TorBox Essential only · **Resolution:** 1080p SDR

> Speed-first, single service. Library, TorBox Search, Comet, and Zilean only. Cached results in 2-3 seconds. No secondary service required -- a single TorBox Essential subscription is all you need.

---

## Designed For

TorBox Essential users who prioritise instant stream loading. Budget hardware, phones, tablets, Fire TV Sticks. No EasyNews subscription needed.

---

## What It Targets / What It Blocks

| Category | Targets | Blocks |
|---|---|---|
| **Resolution** | 1080p, 720p | 2160p, 1440p, Unknown |
| **Quality** | WEB-DL, WEBRip, HDRip | BluRay, BluRay REMUX, CAM, SCR, TS, TC |
| **Visual** | SDR | DV, HDR+DV, HDR10+, HDR10, HDR, HLG, 3D |
| **Streams** | Cached only | P2P, uncached, YouTube |

---

## File Size Limits

| Resolution | Movies | Series |
|---|---|---|
| **Global** | 1 GB -- 25 GB | 512 MB -- 15 GB |
| **1080p** | 1 GB -- 25 GB | 512 MB -- 15 GB |
| **720p** | 256 MB -- 10 GB | 128 MB -- 6 GB |

---

## Addons

| Addon | Purpose | State |
|---|---|---|
| Library | Personal debrid library -- first priority, instant | On |
| TorBox Search | TorBox native search -- torrent index | On |
| Comet | Fastest external debrid scraper | On |
| Zilean | DMM hashlist -- fast hash-based debrid lookup | On |
| OpenSubtitles V3+ | Hash-matched subtitle search | On |

---

## Key Configuration

| Setting | Value |
|---|---|
| Services | TorBox Essential only (all 12 opt-in) |
| Stream types | Debrid only -- Usenet excluded |
| Timeouts | 3500ms across all addons |
| Result limit | 10 global · 4 per resolution |
| Sort keys | 5 -- cached > expression > quality > regexScore > seeders |
| SeaDex best-only | Off |
| Scored regex ranking | 131 patterns (1080p-optimised set) |
| Tamtaro ESEs | Full inline set -- no synced URL needed |
| Episode matching | Strict |
| cacheAndPlay | Off (no Usenet) |

---

## Quick Import

```
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/TorBox/core-nexus-speed-1080p-torbox.json
```

---

*Part of [Core Builds by Brevity](https://github.com/Branding-Brevity/Core-Builds-By-Brevity) -- [Import Guide](../../../Guides/IMPORT_GUIDE.md) -- [Changelog](../../../CHANGELOG.md)*
