# 📥 Import Guide: Core Nexus Builds

This guide covers everything you need to successfully import and finalise your **Core Nexus** configuration. Follow the steps in order and you'll be up and running in under five minutes.

---

## 1️⃣ Pick Your Template

Before importing, choose the right build for your setup. If you're running on multiple devices, see the **Device Profiles** section at the bottom of this guide.

### 🔵 TorBox Builds
*Optimised for TorBox Usenet + torrent cache priority*

| Template | Resolution | Best For |
|---|---|---|
| `core-nexus-torbox-exclusive_rpdb.json` | 1080p SDR | Low-end devices, TorBox only |
| `core-nexus-4k-ht-torbox.json` | 4K HDR | Shield / 4K TVs, TorBox only |
| `core-nexus-dual-core-1080p.json` | 1080p SDR | Low-end devices, TorBox + RD |
| `core-nexus-4k-dual-core.json` | 4K HDR | Shield / 4K TVs, TorBox + RD |
| `core-nexus-tb-hybrid-1080p.json` | 1080p SDR | Low-end, cached + uncached (NZBGeek) |

### 🟢 Any Host Builds
*Works with any debrid service — TorBox, Real-Debrid, AllDebrid, Premiumize, and more*

| Template | Resolution | Best For |
|---|---|---|
| `core-nexus-anyhost-1080p.json` | 1080p SDR | Low-end devices, single debrid |
| `core-nexus-anyhost-4k.json` | 4K HDR | High-end devices, single debrid |
| `core-nexus-anyhost-1080p-dual.json` | 1080p SDR | Low-end devices, dual debrid |
| `core-nexus-anyhost-4k-dual.json` | 4K HDR | High-end devices, dual debrid |

---

## 2️⃣ Open an AIOStreams Host

Open one of the following trusted community hosts in your browser:

- **ForTheWeak:** `https://aiostreams.fortheweak.cloud`
- **MidnightIgnite:** `https://aiostreams.midnightignite.com`
- **ElfHosted:** `https://aiostreams.elfhosted.com`

Navigate to the **Template Import** menu and paste the raw GitHub URL for your chosen template. All raw links follow this pattern:

```
https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/main/Templates/TorBox/Single/core-nexus-torbox-exclusive_rpdb.json
```

---

## 3️⃣ Enter Your API Keys

The template requires a few API keys to function fully. Fill in only the services you use — leave everything else blank.

### Required
- **TorBox API Key** — found in your TorBox account settings
- **TMDB API Key** — a link to generate this for free is directly below the input field in the AIOStreams setup menu

### Optional (based on your services)
- **Real-Debrid API Key** — for dual-core builds only
- **AllDebrid / Premiumize / DebridLink** — for Any Host builds, add whichever you subscribe to
- **RPDB API Key** — already pre-filled with a free tier key in the template; leave it as-is unless you have your own

> 💡 **TVDB has been removed** from all Core Nexus templates. If the field appears, leave it blank.

---

## 4️⃣ Save & Install

Once all required fields are filled in, click **Save** at the bottom of the screen. AIOStreams will generate a unique manifest URL for your build.

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
