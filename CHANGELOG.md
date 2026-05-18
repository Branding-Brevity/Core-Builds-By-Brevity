# Changelog

All notable changes to the **Core Builds** templates and formatters will be documented in this file.

---
## [1.0.10] - 2026-05-18

### Changed
- **Template Metadata Overhaul:** Updated the `name` and `description` fields across all four templates (`core-nexus-4k-dual-core`, `core-nexus-4k-ht-torbox`, `core-nexus-dual-core-1080p`, `core-nexus-1080p-torbox-exclusive`) to accurately reflect their specific configurations, resolutions, and service dependencies.
- **Unique Template IDs Assigned:** Replaced the shared, duplicate ID with unique, hyphenated IDs for each file. This ensures all four templates can be loaded into AIOStreams simultaneously without conflicting or overwriting one another.

### Fixed
- **Hard YouTube Kill ESE Corrected:** Replaced invalid `streamType(streams, 'youtube')` with the correct `type(streams, 'youtube')` in the `/*Hard YouTube Kill*/` excluded stream expression across all four templates. `streamType` is not a recognised AIOStreams function — the expression was throwing an `undefined variable` evaluation error and failing silently instead of blocking YouTube streams.
- **RD Infringing File Scrub ESE Corrected:** Replaced the invalid `filename()` function with the native `keyword()` text-matching function in the Real-Debrid infringement block. The previous expression was throwing an `undefined variable: filename` error and breaking the list evaluation.
  
## [1.0.9] - 2026-05-18

### Added
- **YouTube Triple-Layer Block:** Added `/*Hard YouTube Kill*/` ESE and `excludedStreamSources: ['YouTube', 'AI Enhanced']` across all templates. AI-enhanced YouTube links were bypassing the existing `excludedStreamTypes` filter by registering under a different source — now blocked at all three layers.
- **Statistics Enabled:** Turned on `statistics` across all templates to allow users to self-diagnose stream and filter issues without needing support.
- **RD Library Catalog:** Added Real-Debrid library catalog to `catalogModifications` in the Dual Core 1080p template — previously only TorBox library was listed.

### Changed
- **Sort Conflict Resolved:** Removed `sortBy: rank` from all templates. `sortCriteria` (cached → expressionMatched → seeders → size) now handles sorting exclusively without conflict.
- **Digital Release Filter Tightened:** Reduced `digitalReleaseFilter.tolerance` from 8 days to 3 days across all templates for more accurate new release matching.
- **4K Preload Increased:** Updated `preloadStreams.selector` on both 4K templates to preload 2 cached streams instead of 1, improving playback start times for large 4K files.
- **Descriptions Updated:** Rewrote `addonDescription` for both 1080p templates to accurately reflect their low-end hardware focus, SDR-only output, and BluRay/Remux blocking.
- **Template Versions Bumped:** All `appliedTemplates` references updated to `1.0.9`.

---

## [1.0.8] - 2026-05-17

### Added
- **Hard CAM Kill ESE:** Added `/*Hard CAM Kill*/` as the first stream expression across all four templates, creating a double-layer block alongside `excludedQualities`. Catches `CAM`, `SCR`, `TS`, `TC`, and `HC HD-Rip` at the stream level before any other filter fires.
- **4K Dual Core Template:** Created `core-nexus-4k-dual-core.json` — a dedicated 4K template for TorBox + Real-Debrid users, branched from the 4K HT build with RD service, Meteor, Comet RD, and Zilean presets added, and the RD Infringing File Scrub ESE included.

### Changed
- **Language Matching Fixed (All Templates):** Tightened language settings across all four templates — `includedLanguages`, `requiredLanguages`, and `preferredLanguages` now explicitly enforce English-first with `Original`, `Dual Audio`, `Multi`, `Dubbed`, and `Unknown` as fallbacks. Removed null `prioritisedLanguages` field.
- **Dual Core 1080p Built:** Created `core-nexus-dual-core-1080p.json` from the optimised TorBox Exclusive base, adding Real-Debrid service, Library, Meteor, Comet RD, Zilean, and OpenSubtitles V3+ presets, and the RD Infringing File Scrub ESE.

---

## [1.0.7] - 2026-05-17

### Added
- **Tamtaro ESE Integration:** Added 5 stream expressions from Tamtaro's extended ESE set — `G's Low Bitrate`, `ongoingSeasonPack`, `Low Seeders`, `Extra SeaDex`, and `Final Limit (All)` — bringing the TorBox Exclusive template to 10 active expressions.
- **Missing Config Fields:** Added `externalDownloads: false`, `autoRemoveDownloads: false`, and `excludeUncachedMode: or` to align with Tamtaro's complete setup standard.

### Changed
- **Performance Optimisation:** Set `maxResults: 15`, `maxResultsPerResolution: 5`, `onlyShowCachedStreams: true`, and `showP2PStreams: false` for faster stream loading on low-end hardware.
- **Result Limit Aligned:** Corrected `resultLimits.global` from `45` to `15` to match `maxResults` — both result limiting systems are now consistent.
- **Timeout Reduction:** Reduced all preset timeouts from 7000–8000ms to 5000ms and subtitles to 4000ms for snappier stream list load times.
- **Service Trim:** Removed 15 disabled service entries, leaving only TorBox. Template now contains no dead service config.
- **Title Matching Hardened:** Switched `titleMatching` from `contains` (0.9 similarity) to `exact` (1.0 similarity) to eliminate false stream matches.
- **Deduplicator Upgraded:** Changed `multiGroupBehaviour` from `conservative` to `aggressive` for cleaner result deduplication.
- **Year Matching Expanded:** Extended `yearMatching` to cover `series` and `anime` request types in addition to `movie`.
- **Stream Type Cleanup:** Removed `p2p` from `preferredStreamTypes` and `torrent` from `cacheAndPlay.streamTypes` — now strictly `debrid` and `usenet` only.
- **Audio Channel Order Fixed:** Corrected `preferredAudioChannels` from `[2.0, 5.1]` to `[5.1, 2.0]` to properly prioritise surround sound.
- **Proxy Config Cleaned:** Removed dead MediaFlow proxy config that was not proxying any services or addons.
- **Template Metadata Updated:** `appliedTemplates` now correctly references `core-nexus-torbox-exclusive v1.0.6` instead of the legacy dual-debrid source template.
- **UX Polish:** Disabled `showChanges` and `areYouStillThere` prompts. Set `serviceWrap.reconfigureService` to `false`.

---

## [1.0.6] - 2026-05-17

### Removed
- **TVDB Integration:** Removed `tvdbApiKey` from the TorBox Exclusive template to streamline the configuration and eliminate an unused API dependency.
- **Custom Inline Regex Patterns:** Cleared `excludedRegexPatterns` from the TorBox Exclusive template to comply with ElfHosted's instance-level regex restrictions. Blu-ray and Remux filtering remains enforced via `excludedQualities` and `excludedStreamExpressions`.

### Changed
- **Quality Block Casing Fixed:** Corrected `Bluray` → `BluRay` and `Bluray REMUX` → `BluRay REMUX` in `excludedQualities` to match AIOStreams' accepted enum values. Removed invalid `Remux` entry which is not a recognised quality option.

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
