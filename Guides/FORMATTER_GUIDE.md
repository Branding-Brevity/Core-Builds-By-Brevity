# 🎨 Formatter Guide: Visual Customisation

The **Core Builds** repository includes custom visual layouts (Formatters) that control how streams appear in your list. Swap between styles instantly using the AIOStreams Formatter Import tool.

---

## Available Formatters

### 💎 Core Zenith Diamond
*Recommended — rich, information-dense*

The flagship formatter. Uses emoji-coded resolution badges, smallcaps text, and structured metadata lines to give you instant technical confirmation at a glance.

- **Service pool** shown as `[TB]` / `[RD]` at the start of every stream
- **Resolution badges:** 🟣 4K UHD · 🔵 1080P · 🟢 720P
- **Quality tags:** 💎 REMUX · 💿 BLURAY · 🍿 WEB-DL · 📼 WEBRIP
- **Audio tags:** 🎶 ATMOS · 💎 TRUEHD · 🔷 DTS-HD MA
- **Special flags:** 👑 PREMIUM · 🏆 SEADEX BEST · ✅ OWNED · 📚 LIBRARY
- **4-line description:** age/type/addon → bitrate/size/seeds → video/encode/language → release/regex/seadex

### 📺 Core Clean Stream
*Minimal — clean, plain text*

A stripped-back formatter matching a standard Stremio screenshot layout. No emojis, no smallcaps — plain readable text structured exactly like the native Stremio stream card.

- **Line 1:** `Quality • Encode`
- **Line 2:** `AudioTags • Channels`
- **Line 3:** `Language`
- **Line 4:** `[ Size ] • Service ONLY`
- **Footer:** `[Service] Addon • Resolution (Visual Tags) • Age`

### 🐅 Auburn Tiger Edition
*Community — high-contrast orange & blue*

A community formatter by RB3 using the Auburn Tigers colour scheme. High-visibility orange and navy geometric separators for maximum readability. Available in the `/Community-Templates/RB3/` folder.

---

## 🛠️ Step 1: Download Your Formatter

Navigate to the [`/Formatters`](../Formatters) folder and download the `.json` file for your preferred style:

- [`Core_Zenith_Diamond.json`](../Formatters/Core_Zenith_Diamond.json)
- [`Core_Clean_Stream.json`](../Formatters/Core_Clean_Stream.json)

---

## ⚙️ Step 2: Open the Formatter Import Menu

1. Open your **AIOStreams Dashboard**
2. Go to the **Formatter** section
3. In the bottom right corner, tap the **Import/Export icon** (the box with the arrow pointing inward)

---

## 📄 Step 3: Import the File

1. When the pop-up appears, select **Import from File**
2. Select the `.json` formatter file you downloaded
3. The Name and Description fields will automatically populate with the formatter code

---

## 💾 Step 4: Save & Refresh

1. Click **Save** at the bottom of your AIOStreams dashboard
2. Refresh **WuPlay** or **Stremio** — your new visual style applies instantly to the stream list

---

## 🔧 Tips

> **UI Settings:** For the Core Zenith Diamond formatter, make sure **Show file name** and **Show bitrate** are toggled **OFF** in your main AIOStreams settings. The formatter handles these natively — leaving them on will duplicate information in the stream card.

> **Export your own:** If you've made custom tweaks, tap the **Export** icon next to the import button to save your current setup as a JSON file you can share or back up.

---

*Return to the [Main README](../README.md)*
