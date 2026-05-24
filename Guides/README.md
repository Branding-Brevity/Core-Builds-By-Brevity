<p align="center">
  <img src="https://github.com/Branding-Brevity/Core-Builds-By-Brevity/raw/refs/heads/main/Assets/master_guide_banner.svg" alt="Core Builds Guide Banner" width="100%"/>
</p>

# 📖 Core Builds by Brevity — Complete Guide

Everything you need to set up, customise, and maintain your build.

---

## Contents

1. [Importing a Template](#1--importing-a-template)
2. [Formatters](#2--formatters)
3. [Device Profiles](#3--device-profiles)
4. [Advanced Editing](#4--advanced-editing)
5. [Resetting Your Instance](#5--resetting-your-instance)
6. [Troubleshooting](#6--troubleshooting)

---

## 1 — Importing a Template
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

## 2 — Formatters
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

## 3 — Device Profiles
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

## 4 — Advanced Editing
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

## 5 — Resetting Your Instance
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

## 6 — Troubleshooting
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

*[Return to README](../README.md) · [CHANGELOG](../CHANGELOG.md)*
