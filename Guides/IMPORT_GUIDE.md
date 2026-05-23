# 📥 Import Guide: Core Nexus Builds

This guide covers everything you need to successfully import and finalise your **Core Nexus** configuration. Follow the steps in order and you'll be up and running in under five minutes.

---

## 1️⃣ Pick Your Template

Before importing, choose the right build for your setup. If you're running on multiple devices, see the **Device Profiles** section at the bottom of this guide.

| Template | Resolution | Services | Best For |
|---|---|---|---|
| `core-nexus-torbox-exclusive_rpdb.json` | 1080p SDR | TorBox only | Low-end devices, RPDB poster integration |
| `core-nexus-4k-ht-torbox.json` | 4K HDR | TorBox only | Shield / 4K TVs, home theater |
| `core-nexus-dual-core-1080p.json` | 1080p SDR | TorBox + Real-Debrid | Low-end devices, dual-cache failover |
| `core-nexus-4k-dual-core.json` | 4K HDR | TorBox + Real-Debrid | Shield / 4K TVs, maximum coverage |
| `core-nexus-4k-essential-dual-core.json` | 4K HDR | TorBox Essential + Real-Debrid | Shield / 4K TVs, no Usenet required |
| `core-nexus-tb-hybrid-1080p.json` | 1080p SDR | TorBox + NZBGeek | Users with a Usenet indexer subscription |

> All five templates include the full **12-service roster** pre-loaded. Enable only the services you actually subscribe to — the rest are ignored.

---

## 2️⃣ Open an AIOStreams Host

Open one of the following community hosts in your browser. A live status page is available at [status.dinsden.top](https://status.dinsden.top/status/aiostreams).

| Rank | Host | URL |
|------|------|-----|
| 🥇 | **ElfHosted** | `https://aiostreams.elfhosted.com` |
| 🥈 | **Yeb's** | `https://aiostreams.fortheweak.cloud` |
| 🥉 | **Midnight's** | `https://aiostreamsfortheweebsstable.midnightignite.me` |
| 4 | **Viren's** | `https://aiostreams.viren070.me` |
| 5 | **Kuu's** | `https://aiostreams.stremio.ru` |
| 6 | **ATBP Hosting** | `https://aio.atbphosting.com` |
| 7 | **Omni's** | `https://aiostreams.12312023.xyz` |

Navigate to the **Template Import** menu and paste the raw GitHub URL for your chosen template. Raw links follow this pattern:

```
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Templates/Torbox/Dual/core-nexus-4k-dual-core.json
```

**Full raw URLs:**

| Template | Raw URL |
|---|---|
| TorBox Exclusive (RPDB) | `.../Templates/Torbox/Single/core-nexus-torbox-exclusive_rpdb.json` |
| 4K HT TorBox | `.../Templates/Torbox/Single/core-nexus-4k-ht-torbox.json` |
| Dual Core 1080p | `.../Templates/Torbox/Dual/core-nexus-dual-core-1080p.json` |
| Dual Core 4K | `.../Templates/Torbox/Dual/core-nexus-4k-dual-core.json` |
| TB Hybrid 1080p | `.../Templates/Hybrid/core-nexus-tb-hybrid-1080p.json` |

*(Prepend `https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/` to each path)*

---

## 3️⃣ Enable Your Services

All 12 debrid services are pre-loaded in every template, all set to **disabled by default**. Toggle on only the services you subscribe to — everything else stays off and is ignored.

**Available services:** TorBox · Real-Debrid · AllDebrid · Premiumize · DebridLink · Offcloud · Put.io · EasyNews · EasyDebrid · PikPak · Seedr · Debrider

> 💡 **4K Essential Dual Core** is identical to the flagship 4K Dual Core but with Usenet removed. Use this if you are on the TorBox Essential plan which does not include Usenet access. All 4K quality targets, RD scrub, and SeaDex enforcement are unchanged.

> 💡 For the **TB Hybrid** template, you will also need a **NZBGeek API key** to activate the Usenet indexer tier. If you don't have one, every other addon in the template still works without it.

> ⚠️ **TB Hybrid — Extra Step Required:** The NZBGeek API key cannot be entered in the credentials modal above. After clicking **Load Template** and saving, go to the **Addons** section, find the **NZBGeek** preset, and paste your API key there. NZBGeek will return no results until this is done. Your NZBGeek API key is found in your account settings at [nzbgeek.info](https://nzbgeek.info).

---

### 🔀 TB Hybrid — NZBGeek Additional Setup

The NZBGeek API key **cannot** be entered in the standard credentials modal — AIOStreams only shows recognised debrid services and TMDB in that screen. NZBGeek is a newznab addon and requires a separate step after the template loads.

**After clicking Load Template and saving:**

1. Stay on your AIOStreams dashboard and scroll to the **Addons** section
2. Find the **NZBGeek** addon in the list
3. Click the ⚙️ settings icon next to it
4. Replace the placeholder text with your actual NZBGeek API key
   - Your NZBGeek API key is found at [nzbgeek.info](https://nzbgeek.info) → Account → API Key
5. Click **Save**

> ⚠️ Until the API key is entered, NZBGeek will be active but return no results. Every other addon in the hybrid template — TorBox Search, Comet, Meteor, Zilean, Knaben, MediaFusion — works immediately without it.

> 💡 **TVDB has been removed** from all Core Nexus templates. If the field appears, leave it blank.

---

## 4️⃣ Save & Install

Once your services are configured, click **Save** at the bottom of the screen. AIOStreams will generate a unique manifest URL for your build.

**For Stremio:** Click the **Install** button that appears after saving. Stremio will open and prompt you to confirm.

**For WuPlay:** Copy the generated manifest URL, open your WuPlay configurer, navigate to **Add-ons**, and paste the link to finalise your setup.

---

## 📱 Device Profiles — Multi-Device Households

AIOStreams cannot detect what device is making a request — every device looks identical to the server. The recommended approach for households with mixed devices is **two separate Stremio accounts**:

### 🔵 Low-End Account
*Phones · Tablets · Budget Android TV · Projectors*

Sign into this account on low-end devices and install a **1080p SDR** template. The 1080p builds cap bitrate, block BluRay/Remux, and strip HDR/DV tags — safe for any hardware.

### 🟣 High-End Account
*Nvidia Shield · 4K OLED/QLED TVs · Apple TV 4K*

Sign into this account on high-end devices and install a **4K Unleashed** template. The 4K builds allow Remux, DV, HDR10+, TrueHD, and Atmos — maximum quality with no caps.

Both accounts use the same debrid credentials. Stremio addons sync per-account, so each device gets exactly the right streams.

---

*Return to the [Main README](../README.md)*
