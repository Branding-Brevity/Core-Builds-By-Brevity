# Changelog

All notable changes to the **Core Builds** templates and formatters will be documented in this file.

> **Stability Notice:** Versions prior to `1.1.2` should be considered **unstable**. Early versions contained broken JSON, invalid enum values, non-functional stream expressions, and conflicting configuration systems. The first stable, publish-ready release across all four templates is `v1.1.2`.

---

## [1.2.0] - 2026-05-21

### Added
- **Any Host Template Suite:** Four new universal debrid templates — `core-nexus-anyhost-1080p`, `core-nexus-anyhost-1080p-dual`, `core-nexus-anyhost-4k`, `core-nexus-anyhost-4k-dual`. All 8 supported debrid services enabled by default (TorBox, Real-Debrid, AllDebrid, Premiumize, DebridLink, Offcloud, Put.io, EasyDebrid). TorBox-specific presets removed. Users activate whichever service they have — the rest are ignored.
- **Dual-Account Device Profiles:** Documented a dual-Stremio-account strategy for multi-device households. AIOStreams cannot detect devices natively — the recommended approach is two separate Stremio accounts. Low-End Account (phones, tablets, budget TVs) → 1080p SDR templates. High-End Account (Shield, 4K TVs) → 4K Unleashed templates.
- **AnimeTosho Preset:** Added across all 8 templates. Mirrors most anime from Nyaa.si and TokyoTosho, filling coverage gaps that SeaDex misses.
- **TorrentGalaxy Preset:** Added across all 8 templates. Active, debrid-only indexer with good variety.
- **Peerflix Preset:** Added across all 8 templates. Works with both debrid and P2P, fast, useful as a fallback source.
- **Core Clean Stream Formatter:** New minimal formatter (`Core_Clean_Stream.json`) matching a screenshot-style layout. Plain text, no smallcaps unicode. Four-line structure: `Quality • Encode` → `AudioTags • Channels` → `Language` → `[ Size ] • Service ONLY`.

### Changed
- **Addon Tier Hierarchy Enforced:** All 8 templates now follow a strict 3-speed tier structure. Fast group (≤4000ms): Library, Comet, TorBox Search, StremThru Torz (TB builds only). Medium group (5000ms): Meteor, Zilean, SeaDex, AnimeTosho, Searchⁿᶻᵇ, MediaFusion. Slow/fallback group (6000ms): TorrentGalaxy, Knaben, Peerflix. Results load progressively — no waiting for all sources to complete before seeing results.
- **Torrentio Removed:** Removed from all templates. Replaced by TorrentGalaxy and Peerflix for equivalent coverage without the rate-limit instability.
- **Comet Timeout Reduced:** Lowered from 5000ms to 4000ms — confirmed as the fastest premium debrid scraper, now correctly placed in the fast group.

---

## [1.1.3] - 2026-05-20

### Added
- **Core Nexus TB Hybrid 1080p:** New template (`core-nexus-tb-hybrid-1080p.json`) for TorBox users who want both cached and uncached stream access. Features `onlyShowCachedStreams: false`, `showP2PStreams: true`, and a `Low Seeders Uncached` ESE. Optimised for low-end hardware — SDR only, BluRay/Remux blocked, WEB-DL priority, 25Mbps bitrate cap, HEVC/AVC only, max 5.1 audio.
- **NZBGeek Integration:** Added NZBGeek as a dedicated newznab preset in the Hybrid template, positioned directly after Searchⁿᶻᵇ in the Usenet tier. Requires user API key to activate.
- **Torrentio Added:** Added Torrentio preset across all five templates for expanded index coverage at the time of this release (subsequently removed in v1.2.0).
- **Addon Tier Hierarchy Implemented:** All templates follow a 5-tier preset order — Tier 1 (Library, TorBox Search) → Tier 2 (StremThru Torz, Comet, Meteor) → Tier 3 (Zilean, SeaDex, Searchⁿᶻᵇ) → Tier 4 (Knaben, Torrentio, MediaFusion) → Tier 5 (OpenSubtitles V3+). Timeouts graded by tier (3000–6000ms).
- **4K TorBox Presets Completed:** Added Meteor, Comet, and Zilean to the 4K TorBox template — now on par with the 4K Dual Core for the first time.

### Fixed
- **`sortCriteria.series` Invalid Keys:** Removed `season` and `episode` from the series sort criteria across all five templates. These are not valid AIOStreams sort keys and were causing an `Invalid option` import error.
- **`groups.groupings` Undefined Condition:** Removed a broken grouping entry with an undefined `condition` field from all five templates, resolving the `groups.groupings.0.condition: Invalid input: expected string, received undefined` import error.

### Changed
- **Core Zenith Diamond Formatter Rebuilt:** Redesigned the formatter to mirror a screenshot-style structured layout. Service pool now shown as `[TB]` / `[RD]` using `::upper`. All quality and audio labels switched to uppercase. Description restructured into a clean 4-line hierarchy: age/type/addon → bitrate/size/seeds → video/encode/language → release/regex/seadex.
- **Stream Limits Raised:** `maxResults` increased to 25 (1080p) and 30 (4K). `maxResultsPerResolution` increased to 10 (1080p) and 12 (4K).
- **Year Matching Loosened:** `yearMatching.strict` set to `false`, tolerance widened from 1 to 2 years.
- **Digital Release Filter Widened:** Tolerance increased from 3 to 7 days.
- **Title Matching Threshold Lowered:** `similarityThreshold` reduced from `1.0` to `0.85`.
- **`preferredStreamTypes` Fixed (4K):** Both 4K templates corrected to `['usenet', 'debrid']` — consistent with 1080p templates and TorBox-first intent.

---

## [1.1.2] - 2026-05-20

### Stability Notice
> ⚠️ Versions prior to `1.1.2` should be considered **unstable**. Earlier releases contained broken JSON, incorrect enum values, non-functional YouTube block (`streamType` instead of `type`), conflicting sort systems, dead config fields, and broken grouping conditions. `1.1.2` is the first version verified stable and publish-ready across all four templates.

### Added
- **New Scrapers:** Added `seadex`, `knaben`, and `mediafusion` presets across all templates from community optimised builds, significantly increasing source coverage for movies and TV shows.

### Changed
- **Stream Limits Raised:** `maxResults` increased from 15→25 (1080p) and 20→30 (4K). `maxResultsPerResolution` increased from 5→10 (1080p) and 8→12 (4K).
- **Year Matching Loosened:** `yearMatching.strict` set to `false`, tolerance widened from 1→2 years — catches valid streams that were being blocked by overly strict year filtering.
- **Digital Release Filter Widened:** Tolerance increased from 3→7 days, reducing missed new releases.
- **Title Matching Threshold Lowered:** `similarityThreshold` reduced from `1.0` to `0.85` — captures title variants previously excluded by requiring a perfect match.
- **`preferredStreamTypes` Fixed (4K):** Both 4K templates corrected from `['debrid', 'usenet']` to `['usenet', 'debrid']` — consistent with 1080p templates and TorBox-first intent.

---

## [1.1.1] - 2026-05-18

### Added
- **Series-Aware Sort:** Added `sortCriteria.series` across all templates with episode-aware ordering — `cached → expressionMatched → seeders`. Note: `season` and `episode` were initially added as sort keys but are not valid in AIOStreams — corrected in v1.1.3.
- **`deduplicator.excludeAddons`:** Added missing field across all templates for schema completeness.

### Changed
- **1080p Dual Core Proxy Fixed:** Added `proxiedServices: ['realdebrid']` to MediaFlow proxy config, matching 4K Dual Core. Both dual-core templates now consistently route RD traffic through MediaFlow for account protection.
- **`seederRangeTypes` Cleared:** Removed `['p2p']` from all templates — dead setting since p2p streams are excluded entirely.
- **`excludeUncachedFromStreamTypes` Cleared:** Removed redundant `['p2p']` filter — `onlyShowCachedStreams: True` already handles this.
- **`autoPlay.attributes` Updated:** Changed from `['resolution', 'quality', 'releaseGroup']` to `['resolution', 'quality', 'audioTags']` — audio tag matching is more relevant for auto-play stream selection.
- **Version bumped to `1.1.1`** across all templates.

---

## [1.1.0] - 2026-05-18

### Added
- **Tamtaro Trusted Regex URL:** Added `syncedExcludedRegexUrls` pointing to Tamtaro's whitelisted GitHub source across all templates. Brings in a comprehensive junk file extension block without triggering ElfHosted's forbidden URL error.
- **`addonCategoryColors`:** Added colour coding for addon categories across all templates — Debrid=emerald, Usenet=lime, HTTP=cyan, P2P=orange, Subs=purple, Mix=indigo.
- **`usePosterServiceForMeta: true`:** Enabled RPDB poster service for metadata lookups across all templates.
- **`preferredSubtitles: ['English']`:** Added explicit English subtitle preference across all templates.
- **`Upscaled 4k` ESE:** Added to both 4K templates to block content upscaled from lower resolutions falsely labelled as native 4K.
- **`Bad 4k Anime` ESE:** Added to both 4K templates for anime-specific 4K quality filtering.
- **`mergedCatalogs`:** Added missing field across all templates.

### Changed
- **ESEs Refreshed (2026-05-18):** Replaced all stream expressions with the latest versions. Key fix: `/*Hard YouTube Kill*/` corrected from `streamType()` to `type()` — the previous function name was invalid and the YouTube block was not firing.
- **`preferredStreamTypes` Reordered:** Changed from `['debrid', 'usenet']` to `['usenet', 'debrid']` — Usenet now correctly ranks above standard debrid cache for TorBox-first builds.
- **Statistics Enhanced:** Added `position: bottom`, `timing` to `statsToShow`, and `showFilterStatsOnNoStreams: true` across all templates.
- **Version Bumped to `1.1.0`** across all templates.

---

## [1.0.10] - 2026-05-18

### Changed
- **Template Metadata Overhaul:** Updated the `name` and `description` fields across all four templates to accurately reflect their specific configurations, resolutions, and service dependencies.
- **Unique Template IDs Assigned:** Replaced shared, duplicate IDs with unique, hyphenated IDs for each file. All four templates can now be loaded simultaneously without conflicting.

### Fixed
- **Hard YouTube Kill ESE Corrected:** Replaced invalid `streamType(streams, 'youtube')` with the correct `type(streams, 'youtube')` across all four templates. `streamType` is not a recognised AIOStreams function — the expression was failing silently instead of blocking YouTube streams.
- **RD Infringing File Scrub ESE Corrected:** Replaced the invalid `filename()` function with the native `keyword()` text-matching function in the Real-Debrid infringement block. The previous expression was throwing an `undefined variable: filename` error and breaking list evaluation.

---

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
