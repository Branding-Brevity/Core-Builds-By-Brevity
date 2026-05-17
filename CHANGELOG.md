# Changelog

All notable changes to the **Core Builds** templates and formatters will be documented in this file.

---

## [1.0.6] - 2026-05-17

### Removed
- **TVDB Integration:** Removed `tvdbApiKey` from the TorBox Exclusive template to streamline the configuration and eliminate an unused API dependency.
- **Custom Inline Regex Patterns:** Cleared `excludedRegexPatterns` from the TorBox Exclusive template to comply with ElfHosted's instance-level regex restrictions. Blu-ray and Remux filtering remains enforced via `excludedQualities` and `excludedStreamExpressions`.

### Changed
- **Quality Block Casing Fixed:** Corrected `Bluray` â†’ `BluRay` and `Bluray REMUX` â†’ `BluRay REMUX` in `excludedQualities` to match AIOStreams' accepted enum values. Removed invalid `Remux` entry which is not a recognised quality option.

---

## [1.0.5] - 2026-05-17

### Added
- **Hosted Regex Sync:** Created `Regex/excluded-regex-patterns.json` in the repository to serve as a trusted external regex source. The TorBox Exclusive template now pulls patterns via `syncedExcludedRegexUrls`, eliminating the untrusted regex warning on import.
- **Blu-ray & Remux Regex Block:** Added a case-insensitive regex pattern to the hosted excluded patterns file targeting all Blu-ray and Remux filename variants (`BluRay`, `Blu-ray`, `BDRip`, `BDRemux`, `BDMux`, `BD25/50/66/100`, `REMUX`, `COMPLETE.BLURAY`) for low-end hardware protection.
- **Hard Quality Block:** Added `Bluray`, `Bluray REMUX`, and `Remux` to `excludedQualities` and a top-priority `excludedStreamExpressions` kill rule in the TorBox Exclusive template to enforce the low-end hardware profile at both the quality and stream filtering layers.

### Changed
- **JSON Integrity Fixed:** Resolved invalid JSON errors across `core-nexus-torbox-exclusive_rpdb.json` (trailing comma) and `core-nexus-dual-core-1080p.json` (trailing comma + ~90 duplicate keys). Both templates now pass clean validation.
- **Addon Cleanup:** Removed `NZBGeek`, `Debridio`, and all three StremThru-wrapped addons (`Debrid Search`, `Torrentio`, `Baguettio`) from the TorBox Exclusive template. Template reduced from 13 to 8 native presets.
- **README Banner Fixed:** Corrected broken image path in `Community-Templates/Templates/RB3/Readme.md` from a relative `./Assets/` reference to a full raw GitHub URL, ensuring the Auburn Tiger banner renders correctly from any folder depth.
- **Addon Description Updated:** Removed stale `Debridio` reference from the TorBox Exclusive `addonDescription` field.

---

## [1.0.4] - 2026-05-17

### Added
- **RD Safety Scrub:** Implemented custom `excludedStreamExpressions` logic in the Dual Core templates. This automatically hides `WEB-DL`, `WEBRip`, and streaming platform tags (`AMZN`, `NF`, `DSNP`, etc.) from Real-Debrid results, ensuring only safe, playable BluRay/Remux links are pulled.
- **MediaFlow Proxy Integration:** Hardcoded Real-Debrid traffic in the Dual Core templates to route through the MediaFlow proxy to protect account standing against IP bans.

### Changed
- **Safe Editions Created:** Replaced the standard Dual Core templates with the new `-safe.json` variants to directly mitigate the May 2026 RD "infringing file" errors.
- **Configuration Cleanup:** Removed legacy and unused service references (NZBGeek, Debridio) from the Dual Core structures for lighter template execution.

---

## [1.0.2] - 2026-05-17

### Added
- **Repository Organization:** Restructured the `/Templates` folder into `/Single-Service` and `/Dual-Service` subdirectories for better navigation.
- **Formatter Guide:** Added a new step-by-step guide for importing standalone UI layouts.

### Changed
- **README Update:** Updated all "Quick Start" raw import links to reflect the new folder hierarchy.

---

## [1.0.1] - 2026-05-17

### Removed
- **Scraper Debloat:** Removed `NZBGeek` and `Debridio` from all templates to ensure a frictionless, TorBox-exclusive experience.

### Changed
- **Setup Streamlined:** Updated the `IMPORT_GUIDE.md` and PDF to a simplified 3-step process.

---

## [1.0.0] - 2026-05-17

### Added
- **Initial Release:** Launched 1080p and 4K flagship templates for both Single-Service and Dual-Service users.
- **Visual Formatters:** Introduced the `Core Zenith Diamond` and `Auburn Tiger Edition` UI configurations.