<p align="center">
  <img src="../Assets/formatters_banner.svg" alt="Core Formatters Banner">
</p>

# 🎨 Core Visual Formatters

Beyond just filtering streams, **Core Builds** includes custom UI formatters for AIOStreams. These formatters completely overhaul how your cached links are displayed inside Stremio and WuPlay, making it instantly clear what resolution, codec, and audio track you are selecting.

No more squinting at raw file names. Just clean, color-coded badging.

---

## 🌌 Omni Diamond Hybrid (v2.2.0)
**The Ultimate Metadata Tracker**

The newest flagship layout. This formatter marries the incredibly detailed metadata tracking of the Omni format with the clean `smallcaps` and emoji styling of the Zenith Diamond structure. 

![Omni Diamond Hybrid Preview](../Assets/omni_diamond_preview.svg)

**Key Features:**
* Advanced tags for Editions (IMAX, Director's Cut), Networks (HBO, Netflix), and Repacks.
* Smart Usenet Failover visually supported (⚡ for Instant Cached BitTorrent, ⏳ for Uncached NZBgeek downloads).
* Highly detailed audio, bitrate, and language tracking without breaking the layout.

---

## 💎 Core Zenith Diamond
**The Premium, High-Contrast Layout**

Designed for maximum readability from the couch. The Zenith Diamond formatter uses a sleek, high-contrast badging system that prioritizes resolution (4K/1080p) and visual formats (DV/HDR10+) so you know exactly what your hardware is about to decode.

![Core Zenith Diamond Preview](../Assets/zenith_diamond_preview.svg)

**Key Features:**
* Highlighted Remux and BluRay tags.
* Distinct badging for Dolby Vision vs. standard HDR.
* Clean, minimalist spacing to reduce UI clutter.

---

## 🐅 Auburn Tiger Edition
**The Bold, Thematic Layout**

Built for those who want a stylized, aggressive look to their stream lists. The Auburn Tiger Edition utilizes a custom color palette to make the absolute best cached links jump off the screen. 

![Auburn Tiger Preview](../Assets/auburn_tiger_preview.svg)

**Key Features:**
* Bold, thematic color coding for quick scanning.
* Prioritized high-end audio tags (Atmos, TrueHD, DTS:X) feature prominent highlights.
* Stripped down metadata for a punchier, faster-reading list.

---

## ⚙️ How to Apply a Formatter

You can apply these layouts without changing your underlying streaming template! 

1. Open the `.json` file for your chosen formatter in this folder.
2. Copy the entire raw code.
3. In your AIOStreams configuration panel, locate the **Formatter** section.
4. Select **Custom** and paste the JSON code into the custom formatter box.
5. Save your manifest and restart Stremio/WuPlay to see the new layout.

---
*Formatters designed by Brevity.*
