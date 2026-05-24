# 🎨 Formatter Guide — Core Builds by Brevity

Custom visual layouts that control how streams appear in your list. Swap between styles instantly without touching any template settings.

---

## Available Formatters

### 💎 Core Zenith Diamond
*Recommended — rich, information-dense*

The flagship formatter. Emoji-coded badges, smallcaps text, and structured metadata lines for instant technical confirmation at a glance.

- **Service pool** — `⚡ Instant • TB` / `⏳ Uncached • RD` at the start of every stream
- **Resolution badges** — 🟣 4K · 🔵 1080p · 🟢 720p
- **Quality tags** — 💎 REMUX · 💿 BLURAY · 🍿 WEB-DL · 📼 WEBRIP
- **Audio tags** — 🎶 ATMOS · 💎 TRUEHD · 🔷 DTS-HD MA
- **Special flags** — 👑 SEADEX BEST · ✅ OWNED · 📚 LIBRARY
- **4-line description** — age/type/addon → bitrate/size → video/encode/language → release group/regex score

### 📺 Core Clean Stream
*Minimal — plain text*

Stripped-back layout matching a standard Stremio card. No emojis, no smallcaps — structured exactly like the native stream card.

- **Line 1** — `Quality • Encode`
- **Line 2** — `Audio Tags • Channels`
- **Line 3** — `Language`
- **Line 4** — `[ Size ] • Service`
- **Footer** — `Addon • Resolution • Age`

### 🌙 Midnight Slate
*Brevity — dark, geometric, understated*

A new formatter built around a dark slate aesthetic. Geometric symbols replace emoji badges for a cleaner, more understated look. Designed to feel native to dark-theme setups without sacrificing information density.

![Midnight Slate Preview](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/raw/refs/heads/main/Assets/midnight_slate_preview.svg)

- **Cached indicator** — `✦` for instant cached · `✧` for uncached
- **Stream title** — truncated title with service tag `[TB]`, resolution, and quality inline
- **Line 1** — `◼ addon · ⬤ type · ⧗ age`
- **Line 2** — `⚡ bitrate · 💾 size · ☁ service`
- **Line 3** — `☀ visual · ⚙ encode · 🌐 language · 👥 release group`
- No smallcaps — clean lowercase metadata throughout

### 🐅 Auburn Tiger Edition
*Community — high-contrast orange and blue*

A community formatter by RB3 using the Auburn Tigers colour scheme. High-visibility orange and navy geometric separators. Available in `Community-Templates/RB3/`.

---

## Step 1 — Download Your Formatter

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

## Step 2 — Open the Formatter Import Menu

1. Open your **AIOStreams dashboard**
2. Navigate to the **Formatter** section
3. Tap the **Import/Export icon** in the bottom right corner (box with inward arrow)

---

## Step 3 — Import the File

1. Select **Import from File** in the pop-up
2. Choose the `.json` formatter file you downloaded
3. The Name and Description fields populate automatically

---

## Step 4 — Save and Refresh

1. Click **Save** at the bottom of the dashboard
2. Refresh Stremio or WuPlay — the new layout applies instantly

---

## Tips

> **Core Zenith Diamond:** Turn **Show file name** and **Show bitrate OFF** in AIOStreams main settings. The formatter handles these natively — leaving them on duplicates the information in the stream card.

> **Export your own:** Tap the **Export** icon next to the import button to save your current formatter as a JSON file you can back up or share.

> **Parse error on import:** Always use the raw GitHub URL above. Do not copy the text from the GitHub file view — the rendered page adds characters that break the JSON parser.

---

*[README](../README.md) · [Import Guide](IMPORT_GUIDE.md) · [Troubleshooting](TROUBLESHOOTING.md)*
