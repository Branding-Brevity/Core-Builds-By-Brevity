# 📁 Proposed Repository Structure — v1.2.0

```
Core-Builds-By-Brevity/
│
├── 📁 Assets/                          # Banners, icons, preview images
│   ├── core_builds_banner.svg
│   ├── core_icon.svg
│   ├── auburn_tiger_banner.svg
│   ├── formatters_banner.svg
│   └── community_banner.svg
│
├── 📁 Formatters/                      # AIOStreams UI formatters
│   ├── Core_Zenith_Diamond.json        # Emoji-rich, smallcaps style
│   └── Core_Clean_Stream.json          # NEW — minimal screenshot-style
│
├── 📁 Guides/                          # Setup and import guides
│   ├── IMPORT_GUIDE.md
│   └── DEVICE_PROFILES.md             # NEW — dual-account guide
│
├── 📁 Regex/                           # Hosted trusted regex patterns
│   └── excluded-regex-patterns.json
│
├── 📁 Templates/
│   │
│   ├── 📁 TorBox/                      # TorBox + optional RD
│   │   ├── 📁 Single/                  # TorBox only
│   │   │   ├── core-nexus-torbox-exclusive_rpdb.json   # 1080p SDR low-end
│   │   │   └── core-nexus-4k-ht-torbox.json            # 4K HT unleashed
│   │   │
│   │   ├── 📁 Dual/                    # TorBox + Real-Debrid
│   │   │   ├── core-nexus-dual-core-1080p.json         # 1080p SDR + RD scrub
│   │   │   └── core-nexus-4k-dual-core.json            # 4K + RD scrub
│   │   │
│   │   └── 📁 Hybrid/                  # Cached + Uncached
│   │       └── core-nexus-tb-hybrid-1080p.json         # NZBGeek + uncached
│   │
│   ├── 📁 Any-Host/                    # Works with any debrid service
│   │   ├── 📁 Single/                  # One debrid service
│   │   │   ├── core-nexus-anyhost-1080p.json           # 1080p SDR low-end
│   │   │   └── core-nexus-anyhost-4k.json              # 4K HT unleashed
│   │   │
│   │   └── 📁 Dual/                    # Two debrid services
│   │       ├── core-nexus-anyhost-1080p-dual.json      # 1080p SDR dual
│   │       └── core-nexus-anyhost-4k-dual.json         # 4K dual
│   │
│   └── 📁 Community-Templates/         # Third-party / user builds
│       └── 📁 RB3/
│           ├── auburn-tiger-rb3.json
│           └── Readme.md
│
├── CHANGELOG.md
└── README.md
```

---

## 📋 Template Quick Reference

| Template | Resolution | Quality | Services | Use Case |
|---|---|---|---|---|
| `torbox-exclusive_rpdb` | 1080p | SDR · WEB-DL | TorBox | Low-end device, TorBox only |
| `4k-ht-torbox` | 4K | DV/HDR · Remux | TorBox | Shield/4K TV, TorBox only |
| `dual-core-1080p` | 1080p | SDR · WEB-DL | TB + RD | Low-end, dual debrid |
| `4k-dual-core` | 4K | DV/HDR · Remux | TB + RD | Shield/4K TV, dual debrid |
| `tb-hybrid-1080p` | 1080p | SDR · WEB-DL | TorBox | Low-end, cached + uncached |
| `anyhost-1080p` | 1080p | SDR · WEB-DL | Any | Low-end, any debrid |
| `anyhost-4k` | 4K | DV/HDR · Remux | Any | High-end, any debrid |
| `anyhost-1080p-dual` | 1080p | SDR · WEB-DL | Any × 2 | Low-end, any dual debrid |
| `anyhost-4k-dual` | 4K | DV/HDR · Remux | Any × 2 | High-end, any dual debrid |

---

## 📱 Device Profile Setup (Dual-Account)

Since AIOStreams cannot detect devices at runtime, the recommended approach
for multi-device households is two separate Stremio accounts:

### 🔵 Low-End Account
*Phones · Tablets · Budget Android TV · Projectors*

Install one of:
- `core-nexus-torbox-exclusive_rpdb.json` — TorBox only
- `core-nexus-dual-core-1080p.json` — TorBox + RD
- `core-nexus-anyhost-1080p.json` — Any debrid
- `core-nexus-anyhost-1080p-dual.json` — Any dual debrid

### 🟣 High-End Account
*Nvidia Shield · 4K OLED/QLED TVs · Apple TV 4K*

Install one of:
- `core-nexus-4k-ht-torbox.json` — TorBox only
- `core-nexus-4k-dual-core.json` — TorBox + RD
- `core-nexus-anyhost-4k.json` — Any debrid
- `core-nexus-anyhost-4k-dual.json` — Any dual debrid
