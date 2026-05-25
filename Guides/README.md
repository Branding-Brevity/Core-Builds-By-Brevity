<p align="center">
  <img src="https://github.com/Branding-Brevity/Core-Builds-By-Brevity/raw/refs/heads/main/Assets/master_guide_banner.svg" alt="Core Builds Guide Banner" width="100%"/>
</p>

# 📖 Core Builds by Brevity — Complete Guide

Everything you need to set up, customise, and maintain your build.

---

## Contents

1. [Which Template Should I Use?](#1--which-template-should-i-use)
2. [Importing a Template](#2--importing-a-template)
3. [Formatters](#3--formatters)
4. [Device Profiles](#4--device-profiles)
5. [Stremio vs WuPlay](#5--stremio-vs-wuplay)
6. [Advanced Editing](#6--advanced-editing)
7. [Resetting Your Instance](#7--resetting-your-instance)
8. [Troubleshooting](#8--troubleshooting)
9. [FAQ](#9--faq)

---


## 1 — Which Template Should I Use?

Not sure where to start? Answer the questions below to find your build.

---

#### Step 1 — What TorBox plan do you have?

```
┌─────────────────────────────────────────────────────┐
│                  What plan do you have?             │
│                                                     │
│        TorBox Pro          TorBox Essential         │
│            │                       │               │
│     ┌──────┴──────┐         ┌──────┴──────┐        │
│     ↓             ↓         ↓             ↓        │
│  Standard      Hybrid    Standard       Speed      │
│  Single        (+ NZB)   Essential      (fast)     │
└─────────────────────────────────────────────────────┘
```

---

#### Step 2 — Pick your resolution

#### I have TorBox Pro

| I want... | Use this |
|---|---|
| 4K with Dolby Vision, Atmos, full BluRay REMUX | **[Core Nexus 4K HT TorBox](../Templates/Torbox/Single/core-nexus-4k-ht-torbox.json)** |
| 1080p that works on any device, RPDB poster art | **[Core Nexus TorBox Exclusive RPDB](../Templates/Torbox/Single/core-nexus-torbox-exclusive_rpdb.json)** |
| 1080p + NZBGeek for maximum Usenet coverage | **[Core Nexus TB Hybrid 1080p](../Templates/Torbox/Hybrid/core-nexus-tb-hybrid-1080p.json)** |

#### I have TorBox Essential (no Usenet)

| I want... | Use this |
|---|---|
| 4K with full addon stack | **[Core Nexus 4K Essential](../Templates/Torbox/Essential/core-nexus-4k-essential-torbox.json)** |
| 1080p that works on any device | **[Core Nexus 1080p Essential](../Templates/Torbox/Essential/core-nexus-1080p-essential-torbox.json)** |
| Instant 4K (2-3s load, I also have EasyNews) | **[Core Nexus Speed 4K EasyNews](../Templates/Torbox/Speed/EasyNews/core-nexus-speed-4k.json)** |
| Instant 1080p (2-3s load, I also have EasyNews) | **[Core Nexus Speed 1080p EasyNews](../Templates/Torbox/Speed/EasyNews/core-nexus-speed-1080p.json)** |
| Instant 4K (TorBox only, no EasyNews) | **[Core Nexus Speed 4K](../Templates/Torbox/Speed/TorBox/core-nexus-speed-4k-torbox.json)** |
| Instant 1080p (TorBox only, no EasyNews) | **[Core Nexus Speed 1080p](../Templates/Torbox/Speed/TorBox/core-nexus-speed-1080p-torbox.json)** |

#### I have TorBox + Real-Debrid

The dual-core builds are **advanced** — they work best on WuPlay and require optional MediaFlow Proxy configuration for full RD protection. See [Advanced — Dual Core](../Templates/Torbox/Deprecated/Dual/).

---

#### Standard vs Speed — what's the difference?

| | Standard | Speed |
|---|---|---|
| **Active addons** | 8 | 4 |
| **Stream load time** | 3-6 seconds | 2-3 seconds |
| **Source coverage** | Maximum | Core only (Library, Search NZB, Comet, Zilean) |
| **Best for** | Most users | Fast hardware, low latency priority |
| **Trade-off** | Slightly slower | May miss some niche sources |

> Speed templates use the same filtering, ESEs, and regex ranking as Standard — just fewer scrapers. Quality of results is identical when streams are found.

---

#### Pro vs Essential — what's the difference?

| | TorBox Pro | TorBox Essential |
|---|---|---|
| **Usenet access** | ✅ Yes | ❌ No |
| **Torrent caching** | ✅ Yes | ✅ Yes |
| **NZBGeek support** | ✅ Hybrid template | ❌ |
| **cacheAndPlay** | ✅ Active | ❌ Disabled |
| **nzbFailover** | ✅ Active | ❌ Disabled |
| **Template options** | Single + Hybrid | Essential + Speed |

> All other features — ESE filtering, regex scoring, episode matching, formatter support — are identical between Pro and Essential builds.

---

#### Multi-Device Households

AIOStreams cannot detect which device is requesting a stream. If you have a mix of phones and a 4K TV:

- **Phone/tablet account** → install a 1080p template
- **TV/Shield account** → install a 4K template

Both accounts use the same TorBox credentials. See [Device Profiles](README.md#3--device-profiles) for full setup.

---

#### Still not sure?

Start with **4K Essential** (if you have TorBox Essential) or **4K HT TorBox** (if you have TorBox Pro). Both are the most complete builds for their respective plans and work well out of the box on any 4K-capable device.

---

---

## 2 — Importing a Template
Everything you need to import and configure your build. Follow the steps in order.

---

#### 1️⃣ Pick Your Template

#### 🎯 Which Plan Do You Have?

| I have... | Use this tier |
|---|---|
| TorBox Pro | Single or Hybrid |
| TorBox Essential | Essential or Speed |
| TorBox Essential + EasyNews | Speed (EasyNews) |
| TorBox Pro + NZBGeek | Hybrid |

---

#### 📦 Single — TorBox Pro

Full addon stack. Usenet included. Best overall coverage.

| Template | Resolution | Best For |
|---|---|---|
| [4K Home Theater](https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Single/core-nexus-4k-ht-torbox.json) | 4K HDR | Shield, Apple TV 4K, OLED/QLED |
| [TorBox Exclusive RPDB](https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Single/core-nexus-torbox-exclusive_rpdb.json) | 1080p SDR | Budget hardware, phones, RPDB art |

---

#### 📦 Essential — TorBox Essential

No Usenet required. Torrent cache only.

| Template | Resolution | Best For |
|---|---|---|
| [4K Essential](https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Essential/core-nexus-4k-essential-torbox.json) | 4K HDR | Shield, Apple TV 4K |
| [1080p Essential](https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Essential/core-nexus-1080p-essential-torbox.json) | 1080p SDR | Budget hardware, phones |

---

#### 🔀 Hybrid — TorBox Pro + NZBGeek

Adds NZBGeek Usenet indexer for maximum source diversity. Requires a NZBGeek API key — see Step 4.

| Template | Resolution | Best For |
|---|---|---|
| [TB Hybrid 1080p](https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Hybrid/core-nexus-tb-hybrid-1080p.json) | 1080p SDR | TorBox Pro + NZBGeek users |

---

#### ⚡ Speed — Instant Autoplay (2-3 seconds)

Stripped to 4 addons only. Maximum load speed, no compromise on filtering quality.

#### TorBox Essential + EasyNews

| Template | Resolution |
|---|---|
| [Speed 4K (EasyNews)](https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/EasyNews/core-nexus-speed-4k.json) | 4K HDR |
| [Speed 1080p (EasyNews)](https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/EasyNews/core-nexus-speed-1080p.json) | 1080p SDR |

#### TorBox Essential Only

| Template | Resolution |
|---|---|
| [Speed 4K](https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/TorBox/core-nexus-speed-4k-torbox.json) | 4K HDR |
| [Speed 1080p](https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Speed/TorBox/core-nexus-speed-1080p-torbox.json) | 1080p SDR |

---

#### ⚗️ Advanced — TorBox + Real-Debrid

Community-reported as working on WuPlay. Stremio users may see reduced RD results due to RD's May 2026 server-side filter. MediaFlow Proxy recommended — configure in Proxy section after import.

| Template | Resolution |
|---|---|
| [4K Dual Core](https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Deprecated/Dual/core-nexus-4k-dual-core.json) | 4K HDR |
| [Dual Core 1080p](https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Deprecated/Dual/core-nexus-dual-core-1080p.json) | 1080p SDR |
| [4K Essential + RD](https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Deprecated/Dual/core-nexus-4k-essential-dual-core.json) | 4K HDR |

---

#### 2️⃣ Choose a Host

| Rank | Host | URL |
|------|------|-----|
| 🥇 | **ElfHosted** | [aiostreams.elfhosted.com](https://aiostreams.elfhosted.com/stremio/configure) |
| 🥈 | **Yeb's** | [aiostreams.fortheweak.cloud](https://aiostreams.fortheweak.cloud/stremio/configure) |
| 🥉 | **Midnight's** | [aiostreamsfortheweebsstable.midnightignite.me](https://aiostreamsfortheweebsstable.midnightignite.me/stremio/configure) |
| 4 | **Viren's** | [aiostreams.viren070.me](https://aiostreams.viren070.me/stremio/configure) |
| 5 | **Kuu's** | [aiostreams.stremio.ru](https://aiostreams.stremio.ru/stremio/configure) |
| 6 | **ATBP** | [aio.atbphosting.com](https://aio.atbphosting.com/stremio/configure) |
| 7 | **Omni's** | [aiostreams.12312023.xyz](https://aiostreams.12312023.xyz/stremio/configure) |

Full list: [docs.aiostreams.viren070.me](https://docs.aiostreams.viren070.me/getting-started/public-instances/)

---

#### 3️⃣ Import the Template

1. Open your chosen AIOStreams host
2. Navigate to **Templates** → **Import**
3. Paste the raw URL from the table above (the template names link directly to the raw URL)
4. Click **Load Template**

> 💡 **Re-importing resets service toggles.** Your API keys are preserved but service enabled states return to template defaults. Re-enable your services after each re-import.

---

#### 4️⃣ Enable Your Services

**TorBox is pre-enabled.** Enter your API key in the Services section.

All other services are pre-loaded in the 12-service roster but toggled off — enable only what you subscribe to:

`TorBox` · `Real-Debrid` · `AllDebrid` · `Premiumize` · `DebridLink` · `Offcloud` · `Put.io` · `EasyNews` · `EasyDebrid` · `PikPak` · `Seedr` · `Debrider`

#### Hybrid Template — NZBGeek Setup

NZBGeek is a Usenet indexer addon, not a debrid service — its API key is entered separately in the **Addons** section, not the Services modal.

1. Load the template and save
2. Scroll to **Addons → NZBGeek → ⚙️**
3. Paste your API key from [nzbgeek.info](https://nzbgeek.info) → Account → API Key
4. Save

NZBGeek returns no results until this is done. All other addons work immediately.

---

#### 5️⃣ Save & Install

1. Click **Save** at the bottom of the configuration screen
2. AIOStreams generates a unique manifest URL

**Stremio:** Click **Install** — Stremio opens and prompts confirmation.

**WuPlay:** Copy the manifest URL, open WuPlay configurer → **Add-ons** → paste the URL.

---

#### 📱 Multi-Device Households

AIOStreams cannot detect which device is making a request. For households with a mix of devices, use **two separate Stremio accounts:**

**Low-End Account** — phones, tablets, budget TVs
→ 1080p SDR template — compatible with any hardware

**High-End Account** — Shield, 4K OLED, Apple TV 4K
→ 4K template — Remux, DV, HDR10+, TrueHD, Atmos

Both accounts use the same debrid credentials. Addons sync per-account.

See [DEVICE_PROFILES.md](DEVICE_PROFILES.md) for full setup.

---

---

## 3 — Formatters
Custom visual layouts that control how streams appear in your list. Swap between styles instantly without touching any template settings.

---

#### Available Formatters

#### 💎 Core Zenith Diamond
*Recommended — rich, information-dense*

The flagship formatter. Emoji-coded badges, smallcaps text, and structured metadata lines for instant technical confirmation at a glance.

- **Service pool** — `⚡ Instant • TB` / `⏳ Uncached • RD` at the start of every stream
- **Resolution badges** — 🟣 4K · 🔵 1080p · 🟢 720p
- **Quality tags** — 💎 REMUX · 💿 BLURAY · 🍿 WEB-DL · 📼 WEBRIP
- **Audio tags** — 🎶 ATMOS · 💎 TRUEHD · 🔷 DTS-HD MA
- **Special flags** — 👑 SEADEX BEST · ✅ OWNED · 📚 LIBRARY
- **4-line description** — age/type/addon → bitrate/size → video/encode/language → release group/regex score

#### 📺 Core Clean Stream
*Minimal — plain text*

Stripped-back layout matching a standard Stremio card. No emojis, no smallcaps — structured exactly like the native stream card.

- **Line 1** — `Quality • Encode`
- **Line 2** — `Audio Tags • Channels`
- **Line 3** — `Language`
- **Line 4** — `[ Size ] • Service`
- **Footer** — `Addon • Resolution • Age`

#### 🌙 Midnight Slate
*Brevity — dark, geometric, understated*

A new formatter built around a dark slate aesthetic. Geometric symbols replace emoji badges for a cleaner, more understated look. Designed to feel native to dark-theme setups without sacrificing information density.

![Midnight Slate Preview](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/raw/refs/heads/main/Assets/midnight_slate_preview.svg)

- **Cached indicator** — `✦` for instant cached · `✧` for uncached
- **Stream title** — truncated title with service tag `[TB]`, resolution, and quality inline
- **Line 1** — `◼ addon · ⬤ type · ⧗ age`
- **Line 2** — `⚡ bitrate · 💾 size · ☁ service`
- **Line 3** — `☀ visual · ⚙ encode · 🌐 language · 👥 release group`
- No smallcaps — clean lowercase metadata throughout

#### 🐅 Auburn Tiger Edition
*Community — high-contrast orange and blue*

A community formatter by RB3 using the Auburn Tigers colour scheme. High-visibility orange and navy geometric separators. Available in `Community-Templates/RB3/`.

---

#### Step 1 — Download Your Formatter

Go to the [`Formatters/`](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/tree/main/Formatters) folder and download your preferred `.json` file using the **raw** URL:

```
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Formatters/Core_Zenith_Diamond.json
```
```
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Formatters/Core_Clean_Stream.json
```
```
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Formatters/Midnight_Slate.json
```

> ⚠️ **Download from the raw URL, not the rendered GitHub page.** Copying text from the GitHub file view will include extra formatting that causes a "Failed to parse JSON" error on import.

---

#### Step 2 — Open the Formatter Import Menu

1. Open your **AIOStreams dashboard**
2. Navigate to the **Formatter** section
3. Tap the **Import/Export icon** in the bottom right corner (box with inward arrow)

---

#### Step 3 — Import the File

1. Select **Import from File** in the pop-up
2. Choose the `.json` formatter file you downloaded
3. The Name and Description fields populate automatically

---

#### Step 4 — Save and Refresh

1. Click **Save** at the bottom of the dashboard
2. Refresh Stremio or WuPlay — the new layout applies instantly

---

#### Tips

> **Core Zenith Diamond:** Turn **Show file name** and **Show bitrate OFF** in AIOStreams main settings. The formatter handles these natively — leaving them on duplicates the information in the stream card.

> **Export your own:** Tap the **Export** icon next to the import button to save your current formatter as a JSON file you can back up or share.

> **Parse error on import:** Always use the raw GitHub URL above. Do not copy the text from the GitHub file view — the rendered page adds characters that break the JSON parser.

---

---

## 4 — Device Profiles
AIOStreams cannot detect what device is making a request — every device looks identical to the server. A Shield Pro, a budget Android TV, and a phone all arrive at the same manifest URL with no identifying information. This means a single AIOStreams installation will serve the same streams to every device, regardless of whether they can play them.

The solution is **two separate Stremio accounts** — one for low-end devices, one for high-end devices — each with its own AIOStreams addon installed.

---

#### Why Two Accounts?

| | Single Account | Two Accounts |
|---|---|---|
| Phone gets a 4K REMUX | ❌ Buffering or no playback | ✅ Gets 1080p WEB-DL instead |
| Shield gets a 1080p WEB-DL | ❌ Underperforming | ✅ Gets 4K REMUX instead |
| Setup complexity | Simple | Slightly more steps, once |
| Debrid credentials | One set | Same credentials on both |

---

#### 🔵 Low-End Account
*Phones · Tablets · Budget Android TV boxes · Projectors · Older TVs*

#### Recommended Templates
- **[Core Nexus TorBox Exclusive (RPDB)](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Single/core-nexus-torbox-exclusive_rpdb.json)** — TorBox only, RPDB poster integration
- **[Core Nexus Dual Core 1080p](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Deprecated/Dual/core-nexus-dual-core-1080p.json)** — TorBox + Real-Debrid for maximum availability

#### What these builds do
- ✅ Targets WEB-DL and WEBRip sources
- ✅ Caps bitrate and file size — no multi-gigabyte downloads on a mobile connection
- ✅ Strips HDR, Dolby Vision, and Atmos — these require hardware decode support
- ✅ Blocks BluRay and Remux — too large and often unplayable on budget hardware
- ✅ Enforces AVC/HEVC — widely supported across all Android devices
- ❌ No 4K content served at all

#### Devices to sign this account into
- Android phones and tablets
- Budget Android TV boxes (X96, H96, MXQ, Ugoos AM6B at 1080p mode)
- Amazon Fire TV Stick (4K stick can still benefit from the 1080p build for reliability)
- Projectors without native 4K panels
- Older 1080p TVs

---

#### 🟣 High-End Account
*Nvidia Shield · Apple TV 4K · 4K OLED/QLED TVs · High-end Android TV*

#### Recommended Templates
- **[Core Nexus 4K Dual Core](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Deprecated/Dual/core-nexus-4k-dual-core.json)** — TorBox + Real-Debrid, maximum quality and coverage
- **[Core Nexus 4K HT TorBox](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Torbox/Single/core-nexus-4k-ht-torbox.json)** — TorBox only, home theater focused

#### What these builds do
- ✅ Targets 4K UHD sources
- ✅ Allows BluRay REMUX up to 150GB
- ✅ Passes Dolby Vision, HDR10+, and HDR10
- ✅ Passes TrueHD Atmos, DTS:X, and DTS-HD MA
- ✅ Prioritises AV1 and HEVC for efficiency at high resolutions
- ✅ Enforces minimum 5GB floor — filters out fake or mislabelled 4K
- ❌ Will not serve 1080p as a fallback for content with no 4K release *(configurable)*

#### Devices to sign this account into
- Nvidia Shield Pro / Shield TV
- Apple TV 4K (all generations)
- 4K OLED / QLED TVs with native Stremio or WuPlay apps
- High-end Android TV boxes (Ugoos AM6B, MECOOL KM7)
- Google TV Streamer

---

#### 🔀 Optional: Hybrid Account
*Users who want cached + uncached streams on a single device*

#### Recommended Template
- **[Core Nexus TB Hybrid 1080p](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/blob/main/Templates/Hybrid/core-nexus-tb-hybrid-1080p.json)** — TorBox + NZBGeek, cached and uncached

#### What this build does
- ✅ Shows both cached (instant) and uncached streams
- ✅ Usenet integration via NZBGeek for wider source coverage
- ✅ 1080p SDR — safe for most hardware
- ⚠️ Requires a NZBGeek API key to activate the full Usenet tier
- ⚠️ Uncached streams require TorBox to download the file before playback begins

---

#### ⚙️ How to Set It Up

#### Step 1 — Create your second Stremio account
Go to [stremio.com](https://www.stremio.com) and create a second account using a different email address. A free account is all you need.

#### Step 2 — Install the right template on each account
Sign into each account separately and follow the [Import Guide](./IMPORT_GUIDE.md) to install the appropriate template. Use the same debrid credentials on both accounts — your subscriptions are not account-locked.

#### Step 3 — Sign each device into the right account
- Sign your **phones, tablets, and budget TVs** into the Low-End account
- Sign your **Shield, Apple TV 4K, and premium TVs** into the High-End account

Stremio syncs addon installations per-account, so each device automatically gets the correct stream list the moment it signs in.

---

#### 💡 Tips

> **Same debrid credentials on both accounts.** TorBox and Real-Debrid API keys are not tied to Stremio accounts — you can enter the same keys on both AIOStreams installations without issue.

> **RPDB posters work per-account.** The TorBox Exclusive (RPDB) template includes a free-tier RPDB key. If you upgrade to a paid RPDB plan, enter your personal key on the low-end account's template for richer poster art.

> **WuPlay users.** WuPlay does not use Stremio accounts — it manages addons locally per device. Simply install the appropriate manifest URL on each device directly.

---

*Return to the [Main README](../README.md)*

---


## 5 — Stremio vs WuPlay

Both players work with Core Builds templates, but they behave differently in ways that matter. Here's what you need to know.

---

#### At a Glance

| Feature | Stremio | WuPlay |
|---|---|---|
| **Platform** | Windows, Mac, Linux, Android, iOS, Smart TV | Android, Fire TV, Android TV |
| **Stream type handling** | Some YouTube/external streams slip through | Suppresses these more reliably |
| **UI maturity** | Polished, well-established | Newer, actively developed |
| **Metadata** | Excellent (Cinemeta) | Good |
| **Deep links** | Standard | Extended |
| **Offline support** | Limited | Better |
| **Cost** | Free (Stremio+/Web is paid) | Free |

---

#### Stream Type Differences

The biggest practical difference between the two players is how they handle **YouTube and external-type streams**.

When Stremio's native catalog (Cinemeta) finds no streams for a title, it sometimes injects YouTube trailer links or external info cards alongside the AIOStreams results. These appear as clickable "streams" in your list but open a web browser instead of playing video.

**AIOStreams mitigation (v2.2.5+):**
- `Hard YouTube Kill` ESE blocks `type(streams, 'youtube')`, `type(streams, 'external')`, and keyword matches
- `excludedStreamSources` blocks YouTube source variants
- `hideErrors: true` suppresses AIOStreams' own error cards

WuPlay does not inject these Cinemeta trailer entries alongside addon results, so the problem simply does not occur. If you encounter YouTube links in WuPlay, the ESE fix will still catch them.

---

#### Real-Debrid Behaviour

**Stremio** interacts with RD through its standard addon API. RD's May 2026 server-side filter causes error cards to appear in the stream list when cached files are flagged — `hideErrors: true` suppresses these, but the underlying RD streams are gone.

**WuPlay** processes RD stream responses slightly differently, and community testing shows reduced impact from the RD filter. The Advanced dual-core builds are consistently reported as working better on WuPlay than on Stremio.

---

#### Which Should I Use?

**Use Stremio if:**
- You are on a platform where WuPlay is not available (Windows, Mac, Linux, iOS, Smart TV)
- You want the most stable, polished experience
- You primarily use TorBox-only templates (no RD dependency)

**Use WuPlay if:**
- You are on Android, Fire TV, or Android TV
- You use the Advanced dual-core (TorBox + RD) builds
- YouTube/external stream leakage has been a problem for you in Stremio
- You want better handling of niche stream types

---

#### Using Both

There is no conflict. You can install the same AIOStreams manifest in both players simultaneously. Many users run Stremio on desktop and WuPlay on a Fire TV Stick — the same template works across both.

---

#### Formatter Compatibility

Both players fully support AIOStreams formatters. The `name` and `description` fields render correctly in both. WuPlay may display slightly different line heights or wrapping on very long description lines, but all Core Builds formatters are tested on both platforms.

---

---

## 6 — Advanced Editing
The **Core Builds** are designed to be plug-and-play. However, if you want to adjust caching rules, tweak filtering, or edit the raw template JSON, this guide covers how to do it safely.

---

#### Step 1: Access Your AIOStreams Host

Open your preferred AIOStreams instance and navigate to your existing configuration. You can reach it via the **Configure** button in Stremio next to the AIOStreams addon, or by visiting your host directly and entering your password.

| Rank | Host | URL |
|------|------|-----|
| 🥇 | **ElfHosted** | `https://aiostreams.elfhosted.com` |
| 🥈 | **Yeb's** | `https://aiostreams.fortheweak.cloud` |
| 🥉 | **Midnight's** | `https://aiostreamsfortheweebsstable.midnightignite.me` |
| 4 | **Viren's** | `https://aiostreams.viren070.me` |
| 5 | **Kuu's** | `https://aiostreams.stremio.ru` |
| 6 | **ATBP Hosting** | `https://aio.atbphosting.com` |
| 7 | **Omni's** | `https://aiostreams.12312023.xyz` |

---

#### Step 2: Enable Advanced Mode

1. Look near the top of the configuration page — usually top-right or just below the main header
2. Find the toggle labelled **"Advanced Mode"** or **"Show Advanced Settings"**
3. Toggle it **ON**

Once enabled, the UI expands to show deeper developer settings.

---

#### Step 3: What Advanced Mode Unlocks

- **Raw JSON Editor** — directly edit `excludedStreamExpressions`, resolution limits, scraper timeouts, and any other config field
- **Granular Scraper Controls** — fine-tune how each addon (Comet, Meteor, MediaFusion, etc.) behaves within the build
- **Proxy Configuration** — direct access to MediaFlow proxy URLs and credentials
- **Synced URL Management** — view and edit the external regex and expression URLs your template pulls from

---

#### ⚠️ Editing Rules — Read Before Touching Anything

#### JSON Syntax is Strict
A single missing comma `,` or mismatched bracket `}` will break the entire template and prevent it from loading. Common mistakes:

```json
// ❌ WRONG — trailing comma before closing bracket
"excludedQualities": ["CAM", "SCR",]

// ✅ CORRECT
"excludedQualities": ["CAM", "SCR"]
```

#### Quality Values Must Match Exactly
AIOStreams only accepts specific enum strings for quality fields. Use these exact values — case counts:

| Correct ✅ | Wrong ❌ |
|---|---|
| `BluRay REMUX` | `Bluray REMUX` |
| `BluRay` | `Bluray` |
| `WEB-DL` | `WEBDL` |
| `WEBRip` | `Webrip` |
| `HC HD-Rip` | `HC HD-RIP` |

#### Stream Expression Functions Must Exist
AIOStreams SEL (Stream Expression Language) only recognises specific built-in functions. Common mistakes that break expressions silently:

| Correct ✅ | Wrong ❌ |
|---|---|
| `type(streams, 'youtube')` | `streamType(streams, 'youtube')` |
| `keyword(streams, 'WEB-DL')` | `filename(streams, 'WEB-DL')` |
| `quality(streams, 'BluRay')` | `quality(streams, 'Bluray')` |

#### Sort Keys Must Be Valid
The `sortCriteria` field only accepts recognised sort keys. These are **not** valid and will throw an import error:

- ❌ `season`
- ❌ `episode`

Valid keys include: `quality`, `resolution`, `cached`, `seeders`, `size`, `age`, `bitrate`, `releaseGroup`, `streamExpressionMatched`, `seadex`, and others listed in the AIOStreams schema.

#### Formatter Expressions — Use `||` Not `|`
In the formatter's name and description fields, condition separators must be double-pipe `||`. A single pipe `|` will cause the expression to fail and render raw template text.

```
// ❌ WRONG
{stream.quality::exists["BluRay"|"Unknown"]}

// ✅ CORRECT
{stream.quality::exists["BluRay"||"Unknown"]}
```

#### Formatter Language Conditionals — Both Branches Must Be Correct
When using `::>1`, `::==1`, and `::exists` together for language handling, the false branch of `::>1` must be an empty string `""` — not a duplicate of the true branch. Getting this wrong shows the wrong value for single-language streams:

```
// ❌ WRONG — false branch also says "MULTI", breaks single-language streams
{stream.languages::>1["MULTI"||"MULTI"]}

// ✅ CORRECT — false branch is empty, letting the ==1 block handle it
{stream.languages::>1["MULTI"||""]}
{stream.languages::==1["{stream.languages::join('')}"||""]}
{stream.languages::exists[""||"Unknown"]}
```

#### `stream.age` Already Includes Its Unit
In current versions of AIOStreams, `stream.age` returns the age value with a `d` suffix already appended (e.g. `10d`). Do not add another `d` in your formatter template or it will display `10dd`:

```
// ❌ WRONG — produces "10dd"
{stream.age::>0["• {stream.age}d"||"• New"]}

// ✅ CORRECT
{stream.age::>0["• {stream.age}"||"• New"]}
```

#### Services — All Opt-In, None Required
All templates ship with the full 12-service roster set to `enabled: false`. Do not set any service to `enabled: true` in the raw JSON — this forces the template to require that service and will break it for anyone who doesn't have it. Enable services through the UI only.

---

#### ✅ Before You Save — Validate Your JSON

If you make any manual edits, **always validate before saving**. Copy your edited JSON and paste it into:

- **[JSONLint](https://jsonlint.com/)** — catches syntax errors instantly
- **[JSON Formatter](https://jsonformatter.curiousconcept.com/)** — formats and validates

---

#### 💾 Backup First

Before changing anything in a working build, export or copy your current configuration JSON and save it somewhere safe. If something breaks, you can re-import the backup without losing your setup.

---

#### 🔗 Useful References

- [AIOStreams Documentation](https://docs.aiostreams.viren070.me) — full schema reference
- [SEL Function Reference](https://docs.aiostreams.viren070.me/configuration/sel) — all valid stream expression functions
- [JSONLint Validator](https://jsonlint.com/) — validate your JSON before importing

---

*Return to the [Main README](../README.md)*

---

## 7 — Resetting Your Instance
Sometimes a template import goes wrong, credentials get stuck in a broken state, or you simply want to start completely fresh. This guide covers every reset scenario from a soft config wipe to a full account deletion.

---

#### Before You Reset -- Back Up First

If your instance is still accessible, export your current configuration before doing anything else. You can always re-import a backup if the reset causes more problems than it solves.

1. Open your AIOStreams dashboard
2. Go to the **Template** section
3. Tap the **Export** icon (box with outward arrow)
4. Save the JSON file somewhere safe

---

#### Choosing the Right Reset

| Situation | What to do |
|---|---|
| Template imported wrong settings | Soft reset -- re-import over existing config |
| Config is broken but you can still log in | Soft reset or hard reset |
| Forgotten password | Hard reset -- Delete User |
| Stremio showing errors after config change | Re-install manifest only |
| Want to switch templates entirely | Soft reset -- re-import new template |
| Something is fundamentally broken | Hard reset -- Delete User |

---

#### Option 1 -- Soft Reset (Re-Import a Template)

Re-importing a template replaces your entire configuration without deleting your account or credentials. This is the quickest fix for most problems.

1. Open your AIOStreams dashboard
2. Go to the **Template** section
3. Tap the **Import** icon
4. Paste the raw GitHub URL for your chosen template or select a local file
5. Enter your credentials when prompted
6. Tap **Load Template**
7. Review that services and addons look correct
8. Tap **Save**
9. Copy the new manifest URL and reinstall in Stremio or WuPlay

> The re-import replaces all filter settings, addons, sort criteria, and formatter settings. Your password is not affected.

---

#### Option 2 -- Hard Reset (Delete User)

Deletes your entire account and configuration. Use this when a soft reset is not enough or when you have forgotten your password.

#### Step 1 -- Note your manifest URL (if possible)

If Stremio still has the addon installed, you will need to uninstall it after the reset. Having the old URL makes this easier, but it is not required.

#### Step 2 -- Delete your user account

1. Open your AIOStreams host in a browser
2. Scroll to the very bottom of the configuration page
3. Tap **Delete User**
4. Confirm the deletion

> This permanently removes your account, password, and all saved configuration. It cannot be undone.

#### Step 3 -- Create a new account

1. Refresh the page -- you will be returned to the initial setup screen
2. Enter a new password (or the same one)
3. Tap **Create User** or **Register**

#### Step 4 -- Re-import your template

Follow the steps in the [Import Guide](./IMPORT_GUIDE.md) to load a fresh template and enter your API keys.

#### Step 5 -- Uninstall the old addon from Stremio

1. Open Stremio
2. Go to **Addons**
3. Find the old AIOStreams entry and tap **Uninstall**
4. Tap **Install** on the new manifest URL from your fresh setup

---

#### Option 3 -- Password Reset

If you have forgotten your password and cannot log in, a full Delete User is the only option on most hosted instances -- there is no password recovery email flow. Follow Option 2 above.

> On self-hosted Docker instances, you can reset the password by clearing the relevant environment variable or database entry and restarting the container. Check your host's documentation for the exact procedure.

---

#### Reinstalling in Stremio After Any Reset

Any time you reset or change your AIOStreams configuration, your manifest URL changes. The old URL in Stremio will stop returning results. You must reinstall.

**Stremio:**
1. Go to Addons
2. Find the old AIOStreams entry -- tap Uninstall
3. Open your AIOStreams dashboard and copy the new manifest URL
4. Paste it into Stremio's addon search bar or tap Install from the dashboard

**WuPlay:**
1. Open WuPlay configurer
2. Navigate to Add-ons
3. Remove the old AIOStreams manifest URL
4. Paste the new URL and confirm

---

#### Reinstalling in Stremio After a Soft Reset

If you did a soft reset (re-imported a template) and your manifest URL did not change, you do not need to reinstall. Stremio will pick up the updated configuration automatically on the next stream request. A full app restart speeds this up.

---

#### Common Problems After a Reset

**Import fails with HTTP 404**
The template URL is wrong or the file does not exist at that path on GitHub. Check the URL carefully -- folder names and filenames are case-sensitive.

**Import fails with "Invalid template"**
The JSON file is malformed. Validate it at [jsonlint.com](https://jsonlint.com) before importing.

**Stremio still showing the old stream list**
The old manifest is still installed. Uninstall it from the Stremio addon manager and reinstall with the new URL.

**Credentials modal does not appear after re-import**
Some hosts cache the credential state. Try logging out and back in, or clearing your browser cache, then re-importing.

**NZBGeek still not working after reset (Hybrid template)**
The NZBGeek API key is not entered in the credentials modal -- it must be configured in the Addons section after loading. See the [Import Guide](./IMPORT_GUIDE.md) for the full NZBGeek setup step.

---

#### Host-Specific Notes

| Host | Delete User location | Password reset |
|---|---|---|
| ElfHosted | Bottom of config page | Delete User and re-register |
| Yeb's (ForTheWeak) | Bottom of config page | Delete User and re-register |
| Midnight's | Bottom of config page | Delete User and re-register |
| Viren's | Bottom of config page | Delete User and re-register |
| Kuu's | Bottom of config page | Delete User and re-register |
| Self-hosted Docker | Delete User in UI or wipe volume | Edit environment variables |

---

*Return to the [Main README](../README.md) -- [Import Guide](./IMPORT_GUIDE.md) -- [Advanced Editing](./ADVANCED_EDITING.md) -- [Troubleshooting](./TROUBLESHOOTING.md)*

---

## 8 — Troubleshooting
Quick fixes for the most common errors encountered when importing templates, saving configuration, or loading streams.

---


#### Clicking a Stream Opens the GitHub Page Instead of Playing

**What it means:** AIOStreams returned an informational entry rather than a real stream. Stremio requires all entries to be clickable, so clicking the info card opens the AIOStreams GitHub page. This is expected behaviour -- the info entry is not a real stream.

**Why it happens:** No real streams were found. The most common cause is that no debrid services are enabled.

**Fix:**
1. Open your AIOStreams dashboard
2. Go to the **Services** section
3. Enable at least one debrid service and enter its API key
4. Click **Save** and reinstall the manifest in Stremio

If services are already enabled and you still see the GitHub card, check that your API keys are valid and not expired.

---

#### "Failed to fetch manifest for MediaFusion RD: 400 - Bad Request"

**What it means:** AIOStreams tried to contact the MediaFusion server to build your personalised manifest but the request failed. This is almost always a transient server-side hiccup, not a problem with your configuration.

**Fix:** Click **Save** again. The second attempt succeeds in the vast majority of cases.

If it fails repeatedly:
1. Wait 60 seconds and try again -- MediaFusion may be momentarily overloaded
2. Check the [AIOStreams host status page](https://docs.aiostreams.viren070.me/getting-started/public-instances/) to confirm your instance is healthy
3. Check MediaFusion's own status -- ElfHosted's public instance occasionally undergoes maintenance

> This error does not mean your Real-Debrid credentials are wrong. It is a connectivity issue between AIOStreams and the MediaFusion server, not a credential validation failure.

---

#### "Failed to import template: HTTP error! status: 404"

**What it means:** The raw GitHub URL you pasted does not point to an existing file.

**Common causes:**
- The file has not been uploaded to the repository yet
- The folder path in the URL is wrong (folder names are case-sensitive on GitHub)
- The filename in the URL does not match the actual filename on GitHub

**Fix:** Double-check the URL matches the exact path in the repo. Raw URLs follow this pattern:
```
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/main/Templates/Torbox/Deprecated/Dual/core-nexus-4k-dual-core.json
```

Note: `Torbox` has a lowercase `b`. `Dual`, `Single`, and `Hybrid` are capitalised. Filenames are all lowercase with hyphens.

---

#### "Failed to import template: Invalid template"

**What it means:** The JSON file is malformed -- a missing comma, extra bracket, or other syntax error is preventing AIOStreams from parsing it.

**Fix:**
1. Download the template file
2. Paste its contents into [jsonlint.com](https://jsonlint.com)
3. Fix the highlighted error
4. Re-import the corrected file

---

#### "invalid attribute 'WEB-DL'" (Stream Expression Error)

**What it means:** A stream expression is using the `keyword()` function incorrectly. The `keyword()` function requires an attribute as its second argument (`filename`, `folderName`, `indexer`, `releaseGroup`, or `all`) before listing the keywords.

**Wrong:**
```
keyword(streams, 'WEB-DL', 'WEBRip', 'AMZN')
```
**Correct:**
```
keyword(streams, 'all', 'WEB-DL', 'WEBRip', 'AMZN')
```

**Fix:** Update to v2.1.2 of the Core Builds templates -- this was corrected in that release.

---

#### Stremio Showing a Wall of Red Errors After Saving

**What it means:** The streams are loading but the files have been flagged by your debrid service. This is most commonly the Real-Debrid "infringing file" issue where RD has blocked certain WEB-DL and streaming platform rips.

**Fix:** The Core Builds dual-service templates include an RD Infringing File Scrub that filters these results before they reach Stremio. If you are seeing red errors, confirm you are on v2.1.2 or later and that the MediaFusion and Real-Debrid presets are correctly configured.

---

#### Stremio Showing Old Streams After Saving New Config

**What it means:** The Stremio addon is still using a cached version of the old manifest. Your configuration has changed but Stremio has not picked up the new URL.

**Fix:**
1. Open Stremio -- go to **Addons**
2. Find the AIOStreams entry and tap **Uninstall**
3. Open your AIOStreams dashboard and copy the manifest URL
4. Paste it into Stremio's search bar or tap **Install** directly from the dashboard

A full app restart after reinstalling speeds up the refresh.

---


#### AnimeTosho or TorrentGalaxy Returning Errors or No Results

**AnimeTosho** is an anime-specific torrent source. It returns 0 results for movies and TV shows that are not anime -- this is expected and not a bug. It has been moved to opt-in as of v2.1.4.

**TorrentGalaxy** is periodically blocked by Cloudflare, causing it to return an HTML page instead of JSON results. This produces a `Partial Success` or `Unexpected token '<'` error in the scrape summary. It has been moved to opt-in as of v2.1.4.

Both addons are now **disabled by default**. Enable them in your addon settings only if you specifically want them -- AnimeTosho for anime content, TorrentGalaxy when it is not being blocked.

---

#### No Streams Appearing At All

Work through these in order:

1. **Are your debrid services enabled?** Open your AIOStreams dashboard and confirm at least one service has credentials entered and is toggled on.
2. **Is the manifest installed in Stremio?** Go to Addons and confirm AIOStreams appears in the installed list.
3. **Is your AIOStreams host online?** Check [docs.aiostreams.viren070.me](https://docs.aiostreams.viren070.me/getting-started/public-instances/).
4. **Is the content available in your debrid library?** Try a well-known popular title first to rule out a content availability issue.
5. **Are your ESEs filtering everything?** Open the AIOStreams dashboard, go to **Statistics**, and check the filter breakdown to see how many streams are being excluded at each stage.

---

#### NZBGeek Returns No Results (Hybrid Template)

**What it means:** The NZBGeek API key placeholder has not been replaced with your actual key.

**Fix:**
1. Open your AIOStreams dashboard
2. Go to **Addons** -- find **NZBGeek**
3. Tap the settings icon and replace the placeholder text with your API key from [nzbgeek.info](https://nzbgeek.info) under Account -- API Key
4. Tap **Save**

---

#### Still Stuck?

- See the [Reset Guide](./RESET_GUIDE.md) if your configuration is in a broken state and you need to start over
- See the [Advanced Editing Guide](./ADVANCED_EDITING.md) for JSON editing and validation tips
- Open an issue on the [GitHub repository](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/issues) with a description of the error

---

*Return to the [Main README](../README.md)*

---

## 9 — FAQ

Quick answers to the most common questions. If yours isn't here, open a [Discussion](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/discussions).

---

#### Import Errors

#### "Every group must have at least one addon"

You are importing an older template version. This was a known bug fixed in **v2.2.6** where a removed addon (`tam-mf`) was still referenced in the groups config. Re-import using the latest raw URL from the [Import Guide](README.md#1--importing-a-template).

#### "Template has 1 regex pattern that is not trusted"

You can proceed — click **Import Anyway**. This warning appears when a regex pattern in the template is not in the instance's whitelist. It does not affect functionality. The pattern is still applied; the instance admin just hasn't whitelisted its source URL.

#### "Failed to parse JSON" when importing a formatter

You copied the formatter text from the GitHub file view. GitHub adds hidden characters to rendered files that break the JSON parser. Always download from the **raw URL** — links are in the [Formatter Guide](README.md#2--formatters). Do not copy-paste.

#### Services reset to off after re-importing

Expected behaviour. Re-importing a template resets service toggles to the template defaults. Your API keys are preserved — just re-enable your services in the Services tab after each import.

---

#### No Streams

#### I get zero results after importing

Most likely cause: services not enabled. TorBox is pre-toggled on in all templates, but you still need to enter your API key in the **Services** tab. If TorBox is enabled and you still get nothing, check that `onlyShowCachedStreams` is working correctly — try a popular recent movie before assuming the template is broken.

#### I had streams before but now get zero after re-importing

Your services were reset when you re-imported. Re-enable TorBox (and any other services) in the Services tab and enter your API key again.

#### I only get a handful of streams for older TV shows

Normal for older content. Many classic TV episodes are under 512 MB and older encodes often have unrecognised audio or encode tags. Templates since v2.2.5 lower the size minimums and add `Unknown` fallbacks for audio and encode filters to address this.

---

#### Fake Links / Wrong Behaviour

#### Clicking a stream opens the AIOStreams GitHub page

Fixed in **v2.2.5**. The `Hard YouTube Kill` ESE now also blocks `type(streams, 'external')` streams — these are informational cards AIOStreams injects when errors occur. Re-import the latest template.

#### YouTube trailers are appearing in my stream list

Fixed in **v2.2.8**. Three layers now block YouTube content: the ESE catches type, external, source, and quality field variants; `excludedStreamSources` covers all case variants; `excludedStreamTypes` includes youtube. Re-import the latest template.

#### Wrong episode is playing

Fixed in **v2.2.3**. Two ESEs were added: `Kill Ambiguous Season Packs` blocks streams with only season info and no episode reference; `Kill Season Packs When Episode Streams Exist` blocks full packs when individual episode streams are available. Re-import the latest template.

---

#### Real-Debrid

#### RD streams show "File removed due to copyright infringement"

This is Real-Debrid's server-side enforcement — not a template issue. RD began filtering certain cached files in May 2026 based on filename keywords. `hideErrors: true` in all templates suppresses the error cards so they do not appear in your stream list. Nothing we can do about the underlying RD filter.

#### The Dual Core template shows fewer RD streams than before

Expected after May 2026. RD's server-side filter blocks many WEB-DL files. TorBox covers the gap for most content. The Advanced dual-core builds work best on **WuPlay** where the RD filter impact is less visible.

---

#### Formatters

#### The Zenith Diamond / Midnight Slate formatter isn't showing

After importing a new formatter, click **Save** and then **fully refresh** Stremio or WuPlay. Some clients cache the stream card layout and will not show the new formatter until the addon is reinstalled or the manifest refreshed.

#### My stream cards look identical before and after switching formatter

The formatter controls the **name** and **description** fields of each stream card. If AIOStreams is returning streams but the formatter is not rendering, check that the formatter JSON was imported correctly (no parse error on import) and that you saved after importing.

---

#### Platform Differences

#### Features work in WuPlay but not in Stremio

WuPlay and Stremio handle stream types differently. YouTube/external streams are suppressed more reliably in WuPlay. The `Hard YouTube Kill` ESE catches these in both, but some edge cases still slip through in Stremio. See the [WuPlay vs Stremio guide](README.md) for full details.

#### Statistics / scrape summary cards are showing

`statistics.enabled` was set to `true` in older template versions. Fixed in **v2.2.8** — re-import the latest template to disable the scrape summary display.

---



---

## 7 — Which Template?

Not sure where to start? Answer these three questions.

---

#### Step 1 — What plan do you have?

```
TorBox Pro    ──────────────► Go to Step 2A
TorBox Essential ──────────► Go to Step 2B
TorBox Essential + EasyNews ► Speed (EasyNews) tier
TorBox + Real-Debrid ───────► Advanced (Dual Core) tier
```

---

#### Step 2A — TorBox Pro

**What hardware are you streaming to?**

| Hardware | Template | Why |
|---|---|---|
| Shield, Apple TV 4K, OLED/QLED | **4K HT TorBox** | Full 4K HDR stack — DV, TrueHD, REMUX up to 150 GB |
| Phone, tablet, Fire Stick, budget TV | **TorBox Exclusive RPDB** | 1080p SDR — compatible with everything, RPDB poster art |
| TorBox Pro + NZBGeek subscription | **TB Hybrid 1080p** | Adds NZBGeek Usenet indexer for maximum source diversity |

---

#### Step 2B — TorBox Essential

**Do you prioritise speed or coverage?**

#### I want instant results (2-3 second load)

| Hardware | Template |
|---|---|
| Shield, Apple TV 4K, 4K display | **Speed 4K (TorBox)** |
| Phone, tablet, budget TV | **Speed 1080p (TorBox)** |
| Essential + EasyNews subscription | **Speed 4K/1080p (EasyNews)** |

#### I want maximum source coverage

| Hardware | Template |
|---|---|
| Shield, Apple TV 4K, 4K display | **4K Essential** |
| Phone, tablet, budget TV | **1080p Essential** |

---

#### Step 3 — Mixed household?

If you have a mix of devices (4K TV + phone, for example), use **two separate Stremio accounts**:

- **Account A** → 4K template on your high-end device
- **Account B** → 1080p template on phones, tablets, Fire Sticks

Both accounts use the same TorBox credentials. See [Device Profiles](README.md#3--device-profiles).

---

#### At a Glance

| Template | Plan | Resolution | Addons | Load Speed | Best For |
|---|---|---|---|---|---|
| 4K HT TorBox | Pro | 4K HDR | 8 | ~4.5s | Home cinema |
| TorBox Exclusive RPDB | Pro | 1080p SDR | 8 | ~4.5s | Budget hardware |
| TB Hybrid 1080p | Pro + NZBGeek | 1080p SDR | 9 | ~4.5s | Maximum sources |
| 4K Essential | Essential | 4K HDR | 8 | ~4.5s | 4K without Pro |
| 1080p Essential | Essential | 1080p SDR | 8 | ~4.5s | 1080p without Pro |
| Speed 4K (TorBox) | Essential | 4K HDR | 4 | ~2-3s | Speed priority |
| Speed 1080p (TorBox) | Essential | 1080p SDR | 4 | ~2-3s | Speed priority |
| Speed 4K (EasyNews) | Essential + EasyNews | 4K HDR | 4 | ~2-3s | Speed + Usenet |
| Speed 1080p (EasyNews) | Essential + EasyNews | 1080p SDR | 4 | ~2-3s | Speed + Usenet |
| Advanced 4K Dual Core | Pro + RD | 4K HDR | 8 | ~4.5s | TorBox + RD (WuPlay) |

---

#### TorBox Pro vs Essential — What Do You Actually Lose?

| Feature | Essential | Pro |
|---|---|---|
| Torrent caching | ✅ | ✅ |
| Shared torrent cache | ✅ | ✅ |
| Usenet downloads | ❌ | ✅ |
| `cacheAndPlay` (play while downloading) | ❌ | ✅ |
| `nzbFailover` (auto NZB retry) | ❌ | ✅ |
| Hybrid template | ❌ | ✅ |
| Speed tier | ✅ | ✅ |
| All other features | ✅ | ✅ |

For most users the Essential plan + a Speed or Essential template delivers an excellent experience. Pro is worth it if you specifically want Usenet coverage for niche or hard-to-find content.

---

---

## 8 — FAQ

Quick answers to the most common questions. If yours isn't here, open a [Discussion](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/discussions).

---

#### Importing

**"Every group must have at least one addon" on import**
This was a bug in templates prior to v2.2.6. A removed addon (MediaFusion) was still referenced in the groups config. Re-import using the latest template from the [import guide](README.md#1--importing-a-template).

**"Template has 1 regex pattern that is not trusted"**
One of the inline regex patterns isn't in your instance's whitelist. You can still import — tap **Import Anyway**. This warning doesn't affect functionality.

**"Failed to parse JSON" on formatter import**
You copied the formatter from the GitHub file view instead of downloading the raw file. Use the raw URL links in the [Formatter Guide](README.md#2--formatters) — they download the actual file, not the rendered page.

**My services got reset after re-importing**
This is expected behaviour. AIOStreams resets service toggles to template defaults on every import. Your API keys are preserved — just re-enable your services in the Services tab after each import. TorBox is pre-toggled on in all Core Builds templates.

**The BUILD badge shows "Repo or workflow not found"**
The GitHub Actions validation workflow hasn't been triggered yet. It runs automatically on the next commit that changes a JSON file. Push any template update and the badge will resolve.

---

#### Streams

**No streams showing at all**
Most likely cause: services aren't enabled. After importing, go to **Services** and make sure TorBox (and any other services you subscribe to) is toggled on with your API key entered.

**YouTube / trailer links appearing in my stream list**
This was fixed in v2.2.3+. The `Hard YouTube Kill` ESE now blocks streams by type, source, and quality field. Re-import the latest template. If you're on Stremio specifically, some trailer links come from Stremio's own catalog addon — these can't be filtered by AIOStreams.

**Clicking a stream opens the AIOStreams GitHub page**
Fixed in v2.2.3+. AIOStreams was injecting an informational entry as a stream when errors occurred. The `Hard YouTube Kill` ESE now also blocks `type: external` streams. Re-import the latest template.

**Wrong episode playing**
Fixed in v2.2.3+. Two ESEs (`Kill Ambiguous Season Packs` and `Kill Season Packs When Episode Streams Exist`) now use AIOStreams' `seasonPack()` function to prevent season pack torrents from playing as individual episodes. Re-import the latest template.

**Fewer Real-Debrid results than expected**
Real-Debrid introduced server-side keyword filtering in May 2026. Files with certain filename patterns (WEB-DL tags, streaming service identifiers) are blocked by RD before they ever reach AIOStreams. This is an RD policy issue, not a template issue. TorBox does not have this restriction and covers the gap.

**Streams load slowly**
Try a Speed tier template — Library, Search NZB (TorBox), Comet, and Zilean only, 3500ms timeouts, delivers results in 2-3 seconds. If you're on a standard template, the timeout ceiling is 4500ms (Knaben). Switching to a faster host also helps.

---

#### Formatters

**Which formatter should I use?**
- Want maximum information → **Omni Diamond Hybrid** or **Core Zenith Diamond**
- Want a clean dark look → **Midnight Slate**
- Want it to look like native Stremio → **Core Clean Stream**

**The formatter looks wrong / fields are missing**
Make sure **Show file name** and **Show bitrate** are turned OFF in AIOStreams settings when using Core Zenith Diamond or Omni Diamond Hybrid. These formatters handle bitrate natively — leaving the settings on duplicates the data.

---

#### Plans & Templates

**What's the difference between TorBox Pro and Essential?**
TorBox Essential is the entry-level plan — it gives you torrent caching but no Usenet access. TorBox Pro adds Usenet, meaning the Hybrid template and the `cacheAndPlay`/`nzbFailover` features work. See the [comparison guide](WHICH_TEMPLATE.md) for a full breakdown.

**Should I use the Speed tier or a standard template?**
Speed tier trades source coverage for load time. It uses 4 addons instead of 8-9, so it finds fewer total results but delivers them in 2-3 seconds. If TorBox has your content cached, Speed is excellent. If you regularly watch niche or older content that isn't well-cached, a standard template covers more ground.

**Can I use Real-Debrid with Core Builds?**
Yes — the Advanced (Dual Core) templates pair TorBox with RD. Due to RD's May 2026 filter enforcement, these work best on WuPlay. Stremio users may see reduced RD results for some content. See the [Advanced templates](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/tree/refs/heads/main/Templates/Torbox/Deprecated/Dual).

**What happened to the Dual Core templates?**
They were briefly deprecated due to RD's May 2026 server-side filter causing issues, then reclassified as **Advanced** after community reports of them working well on WuPlay. They're still available and maintained — just moved to `Templates/Torbox/Deprecated/Dual/` for now.

---

#### Stremio vs WuPlay

**Why does WuPlay work better with some templates?**
WuPlay handles stream types differently to Stremio. YouTube-typed streams that slip through ESE filtering in Stremio are automatically handled by WuPlay. RD's copyright filter errors also display more gracefully. See the [Stremio vs WuPlay guide](STREMIO_VS_WUPLAY.md) for a full comparison.

---

---

## 9 — Stremio vs WuPlay

Both players work with AIOStreams and Core Builds templates. They behave differently in a few important ways — knowing the differences helps you choose the right setup and debug issues faster.

---

#### Quick Comparison

| Feature | Stremio | WuPlay |
|---|---|---|
| Platform | Android, iOS, Windows, macOS, Linux, Smart TV | Android only |
| YouTube/trailer stream handling | Can slip through ESE filtering | Handled correctly — not displayed |
| RD copyright filter errors | Shows error cards (hidden by `hideErrors`) | Handles more gracefully |
| External link streams | Can appear as clickable entries | Blocked at player level |
| Stream type detection | Broader, some types bypass ESEs | More granular |
| Subtitles | Native + addon | Addon only |
| UI | Polished, catalogue-first | Stream-focused |
| RPDB poster art | ✅ | ✅ |

---

#### The YouTube / Trailer Link Issue

**Stremio** — Some streaming scrapers return YouTube-typed streams (trailers, promos). AIOStreams ESEs filter most of these, but certain stream types can bypass the filter depending on how the scraper labels them. The `Hard YouTube Kill` ESE in Core Builds targets type, external, source, keyword, and quality fields to catch as many variants as possible. A small number may still slip through on Stremio.

**WuPlay** — Handles YouTube and external-typed streams at the player level. These simply don't appear in the stream list regardless of what AIOStreams returns.

**Verdict:** If YouTube fake links are a persistent problem for you on Stremio, switching to WuPlay eliminates the issue entirely.

---

#### Real-Debrid & Copyright Filter Errors

In May 2026, Real-Debrid introduced server-side keyword filtering that blocks certain cached files (WEB-DL, streaming service tags). When AIOStreams tries to generate a stream URL for a blocked file, RD returns an error.

**Stremio** — Error cards appear in the stream list. Core Builds uses `hideErrors: true` to suppress these, but some error types still surface depending on the AIOStreams version.

**WuPlay** — Processes error responses differently. Blocked RD files either silently fail or show minimal UI feedback, keeping the stream list cleaner.

**Verdict:** If you use Real-Debrid and find your stream list cluttered with RD errors, WuPlay handles this more cleanly. The Advanced (Dual Core) templates are documented as working better on WuPlay for exactly this reason.

---

#### Stream Type Detection

AIOStreams classifies streams into types (`debrid`, `usenet`, `http`, `youtube`, `external`, `p2p`). ESEs filter based on these types.

**Stremio** — Stream type detection is sometimes inconsistent. A stream labelled as `youtube` by one scraper might be `http` in another context, causing some ESEs to miss it.

**WuPlay** — Stream type handling is more consistent with how AIOStreams expects it. Filters behave more predictably.

---

#### Which Should I Use?

**Use Stremio if:**
- You want the polished catalogue and UI
- You're on iOS, Windows, macOS, or Linux (WuPlay is Android-only)
- You're on a Smart TV
- You use subtitles heavily

**Use WuPlay if:**
- You're on Android and want cleaner stream lists
- You use Real-Debrid and find the error handling frustrating on Stremio
- YouTube/trailer links are appearing and you want them eliminated at the player level
- You're testing Advanced (Dual Core) templates

**You can use both** — install both players, point them at the same AIOStreams manifest. Use Stremio for browsing and WuPlay for the actual stream when needed.

---

#### Installing Your Manifest in WuPlay

1. Save your AIOStreams configuration and copy the manifest URL
2. Open WuPlay → tap the **+** icon
3. Paste the manifest URL
4. Tap **Add** — your streams are available immediately

---

---

*[Return to README](../README.md) · [CHANGELOG](../CHANGELOG.md)*
