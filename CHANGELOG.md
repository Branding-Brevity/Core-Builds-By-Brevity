# Changelog

## [2.2.9] - 2026-05-25

### Fixed
- **Essential Template Crash:** Patched `core-nexus-4k-essential-torbox.json` to fix critical `[ERR]` crashes.
    - Disabled `torbox-search` preset which was triggering 403 Forbidden errors for non-Usenet Essential accounts.
    - Removed Usenet source scraping from `meteor` preset to prevent backend API rejection.
- **Manual Newznab Preset:** Disabled redundant and unauthorized manual `newznab` preset in TorBox Pro templates that was causing search cycle failures.

### Added
- **RPDB Baking:** Integrated RPDB API key support directly into Essential templates for seamless poster art display.


All notable changes to the **Core Builds** templates and formatters will be documented in this file.

> **Stability Notice:** Versions prior to `1.1.2` should be considered **unstable**. Early versions contained broken JSON, invalid enum values, non-functional stream expressions, and conflicting configuration systems. The first stable, publish-ready release across all four templates is `v1.1.2`.

---

## [2.2.8] - 2026-05-24

### Fixed
- **`enhancePosters` disabled (All Templates):** Was set to `true` — disabled across all 12 templates. Poster enhancement adds unnecessary processing overhead and conflicts with RPDB poster service already configured.
- **`enhanceResults` disabled (All Templates):** Was set to `true` — disabled across all 12 templates. Stream result enhancement was adding latency without meaningful benefit for debrid-focused builds.
- **`precacheSingleStream` disabled (All Templates):** Hidden option was set to `true` — disabled across all 12 templates. This was silently initiating background single-stream pre-caches without user awareness, bypassing the `precacheSelector: []` setting.

### Changed
- **"TorBox Search" renamed to "Search NZB (TorBox)" in all documentation.** The official TorBox Stremio addon has been retired. The addon used in all Core Builds templates is AIOStreams' built-in `torbox-search` preset which queries TorBox's Newznab API endpoint directly — functionally a Newznab/NZB search, not the retired official addon. All README files and the homepage updated to reflect this accurately.

---

## [2.2.7] - 2026-05-24

### Changed
- **Dual Core templates reclassified — Advanced/Community (was Deprecated).** Community reports of flawless operation on WuPlay prompted a reclassification. The templates are confirmed working — the issues experienced were platform-specific (Stremio + RD's May 2026 server-side filter) rather than fundamental template problems. All v2.2.x fixes (groups error, audio Unknown, size minimums, YouTube ESE, service order) are applied and the templates remain in `Templates/Torbox/Deprecated/Dual/` for the time being. MediaFlow Proxy is recommended but not required. `[DEPRECATED]` prefix removed from template names.

---

## [2.2.6] - 2026-05-24

### Fixed
- **"Every group must have at least one addon" error (All Templates):** The `groups` config contained a reference to `"tam-mf"` (Tamtaro's MediaFusion preset ID) which was left over when MediaFusion was removed in v2.2.2. AIOStreams validated the group and found no matching addon, throwing a hard error on import. Groups disabled across all 9 active templates (`groups.enabled: false`). The grouping feature (dynamic addon switching based on cached stream count) can be re-enabled manually with a valid addon ID if needed.
- **Statistics display disabled (All Templates):** `statistics.enabled` set to `false` across all templates. The scrape summary cards were left enabled on 3 templates after the previous rebuild from the working base. Now consistently off.

### Changed
- **3 Working templates rebuilt from live base:** 4K Home Theater, TorBox Exclusive RPDB, and TB Hybrid 1080p were rebuilt using the confirmed-working GitHub versions as the base, with all v2.2.x fixes layered on top. This preserves `syncedIncludedStreamExpressionUrls` and `precacheSelector` values that were confirmed working, while applying all ESE, regex, timeout, service order, audio tag, encode, and size improvements from this session.

---

## [2.2.5] - 2026-05-24

### Deprecated
- **Dual Core Templates — all 3 builds deprecated.** Real-Debrid's May 2026 keyword filter ("filter-gate") combined with the MediaFlow proxy requirements introduced for multi-IP account protection have made dual-service builds inherently fragile. Symptoms included: zero results without a configured MediaFlow URL, RD streams being silently dropped at the proxy stage, copyright-flagged WEB-DL streams returning errors, and ongoing maintenance burden. The following templates are marked `[DEPRECATED]` in their metadata names and descriptions:
  - `core-nexus-4k-dual-core.json`
  - `core-nexus-dual-core-1080p.json`
  - `core-nexus-4k-essential-dual-core.json`

  The JSON files remain in the repository for advanced users who want to configure MediaFlow Proxy and accept the trade-offs. No further fixes will be issued. Migration paths to TorBox-only equivalents are listed in the README.

### Fixed
- **YouTube Kill ESE — triple-layered defense.** Reports of YouTube streams slipping through resulted in three new blocking layers: 1) ESE now checks `quality(streams, 'youtube')` in addition to type, external, and keyword; 2) `excludedStreamSources` now includes lowercase variants (`youtube`, `YOUTUBE`); 3) `excludedQualities` includes `youtube` and `YouTube` for streams where AIOStreams detects the quality field as YouTube.
- **`includedEncodes` — Unknown fallback added** to allow streams with unrecognised encode tags (common for older content) through the encode whitelist filter.
- **Size minimums lowered for TV series.** Global series minimum dropped from 1 GB to 100-150 MB to accommodate 25-minute TV episodes which are typically 150-400 MB at 720p and 500 MB-1.5 GB at 1080p.

---

## [2.2.4] - 2026-05-24

### Changed
- **Timeout Optimisation (All Standard Templates):** All 8 standard templates have had addon timeouts tightened to reduce maximum stream load time. Knaben was the primary bottleneck at 6000ms — every stream list waited up to 6 seconds for it regardless of other addons. Updated values:

  | Addon | Before | After |
  |---|---|---|
  | Library | 3000ms | 2000ms |
  | TorBox Search | 4000ms | 3500ms |
  | StremThru Torz | 4000ms | 3500ms |
  | Zilean | 5000ms | 3500ms |
  | SeaDex | 5000ms | 3500ms |
  | Meteor | 5000ms | 4000ms |
  | newznab | 5000ms | 4000ms |
  | OpenSubtitles V3+ | 4000ms | 3000ms |
  | Knaben | 6000ms | 4500ms |

  Maximum load time across any standard template is now 4500ms, down from 6000ms. Speed tier templates unchanged at 3500ms flat.

---

## [2.2.3] - 2026-05-23

### Removed
- **`Uncensored` Regex Pattern (All Universal Templates):** Removed from `rankedRegexPatterns` across all 12 universal templates. The pattern had a score of 0 (no ranking contribution), was exclusively associated with adult anime content, and added no benefit to any standard build. Also removed from `regexes-scored.json`.
- **AnimeTosho (All Templates):** Confirmed fully absent from all template preset lists. Previously disabled in v2.1.4, the preset entry has been cleaned from all templates.

### Fixed
- **Season Pack Episode Matching (All Templates):** Two new ESEs added to resolve wrong episode playback:
  - `Kill Ambiguous Season Packs` — blocks streams with only season info and no episode reference using `seasonPack(streams, 'onlySeasons')`. These are the primary cause of wrong episode playback where debrid services default to file 1.
  - `Kill Season Packs When Episode Streams Exist` — blocks full season pack streams when at least one episode-specific stream is available, using `seasonPack(streams, 'seasonPack')`.

---

## [2.2.2] - 2026-05-23

### Fixed
- **YouTube Kill Strengthened (All Templates):** The previous `type(streams, 'youtube')` expression only caught streams explicitly typed as youtube. In standard Stremio, YouTube links can arrive typed as `http` with a YouTube URL, bypassing the filter entirely. The expression now targets all three vectors: `type(streams, 'youtube')`, `keyword(streams, 'all', 'youtube.com', 'youtu.be', 'trailer')`, and a regex exclusion matching YouTube watch/embed URL patterns. Tested to block trailer and promo links in both Stremio and WuPlay.

### Removed
- **MediaFusion (All Templates):** Removed from all 18 templates. MediaFusion's public ElfHosted instance is currently broken and returning inconsistent or empty results. The addon slot has been freed -- users who self-host a working MediaFusion instance can re-add it manually in their addon settings.

---

## [2.2.8] - 2026-05-24

### Fixed
- **`enhancePosters` disabled (All Templates):** Was set to `true` — disabled across all 12 templates. Poster enhancement adds unnecessary processing overhead and conflicts with RPDB poster service already configured.
- **`enhanceResults` disabled (All Templates):** Was set to `true` — disabled across all 12 templates. Stream result enhancement was adding latency without meaningful benefit for debrid-focused builds.
- **`precacheSingleStream` disabled (All Templates):** Hidden option was set to `true` — disabled across all 12 templates. This was silently initiating background single-stream pre-caches without user awareness, bypassing the `precacheSelector: []` setting.

### Changed
- **"TorBox Search" renamed to "Search NZB (TorBox)" in all documentation.** The official TorBox Stremio addon has been retired. The addon used in all Core Builds templates is AIOStreams' built-in `torbox-search` preset which queries TorBox's Newznab API endpoint directly — functionally a Newznab/NZB search, not the retired official addon. All README files and the homepage updated to reflect this accurately.

---

## [2.2.7] - 2026-05-24

### Changed
- **Dual Core templates reclassified — Advanced/Community (was Deprecated).** Community reports of flawless operation on WuPlay prompted a reclassification. The templates are confirmed working — the issues experienced were platform-specific (Stremio + RD's May 2026 server-side filter) rather than fundamental template problems. All v2.2.x fixes (groups error, audio Unknown, size minimums, YouTube ESE, service order) are applied and the templates remain in `Templates/Torbox/Deprecated/Dual/` for the time being. MediaFlow Proxy is recommended but not required. `[DEPRECATED]` prefix removed from template names.

---

## [2.2.6] - 2026-05-24

### Fixed
- **"Every group must have at least one addon" error (All Templates):** The `groups` config contained a reference to `"tam-mf"` (Tamtaro's MediaFusion preset ID) which was left over when MediaFusion was removed in v2.2.2. AIOStreams validated the group and found no matching addon, throwing a hard error on import. Groups disabled across all 9 active templates (`groups.enabled: false`). The grouping feature (dynamic addon switching based on cached stream count) can be re-enabled manually with a valid addon ID if needed.
- **Statistics display disabled (All Templates):** `statistics.enabled` set to `false` across all templates. The scrape summary cards were left enabled on 3 templates after the previous rebuild from the working base. Now consistently off.

### Changed
- **3 Working templates rebuilt from live base:** 4K Home Theater, TorBox Exclusive RPDB, and TB Hybrid 1080p were rebuilt using the confirmed-working GitHub versions as the base, with all v2.2.x fixes layered on top. This preserves `syncedIncludedStreamExpressionUrls` and `precacheSelector` values that were confirmed working, while applying all ESE, regex, timeout, service order, audio tag, encode, and size improvements from this session.

---

## [2.2.5] - 2026-05-24

### Deprecated
- **Dual Core Templates — all 3 builds deprecated.** Real-Debrid's May 2026 keyword filter ("filter-gate") combined with the MediaFlow proxy requirements introduced for multi-IP account protection have made dual-service builds inherently fragile. Symptoms included: zero results without a configured MediaFlow URL, RD streams being silently dropped at the proxy stage, copyright-flagged WEB-DL streams returning errors, and ongoing maintenance burden. The following templates are marked `[DEPRECATED]` in their metadata names and descriptions:
  - `core-nexus-4k-dual-core.json`
  - `core-nexus-dual-core-1080p.json`
  - `core-nexus-4k-essential-dual-core.json`

  The JSON files remain in the repository for advanced users who want to configure MediaFlow Proxy and accept the trade-offs. No further fixes will be issued. Migration paths to TorBox-only equivalents are listed in the README.

### Fixed
- **YouTube Kill ESE — triple-layered defense.** Reports of YouTube streams slipping through resulted in three new blocking layers: 1) ESE now checks `quality(streams, 'youtube')` in addition to type, external, and keyword; 2) `excludedStreamSources` now includes lowercase variants (`youtube`, `YOUTUBE`); 3) `excludedQualities` includes `youtube` and `YouTube` for streams where AIOStreams detects the quality field as YouTube.
- **`includedEncodes` — Unknown fallback added** to allow streams with unrecognised encode tags (common for older content) through the encode whitelist filter.
- **Size minimums lowered for TV series.** Global series minimum dropped from 1 GB to 100-150 MB to accommodate 25-minute TV episodes which are typically 150-400 MB at 720p and 500 MB-1.5 GB at 1080p.

---

## [2.2.4] - 2026-05-24

### Changed
- **Timeout Optimisation (All Standard Templates):** All 8 standard templates have had addon timeouts tightened to reduce maximum stream load time. Knaben was the primary bottleneck at 6000ms — every stream list waited up to 6 seconds for it regardless of other addons. Updated values:

  | Addon | Before | After |
  |---|---|---|
  | Library | 3000ms | 2000ms |
  | TorBox Search | 4000ms | 3500ms |
  | StremThru Torz | 4000ms | 3500ms |
  | Zilean | 5000ms | 3500ms |
  | SeaDex | 5000ms | 3500ms |
  | Meteor | 5000ms | 4000ms |
  | newznab | 5000ms | 4000ms |
  | OpenSubtitles V3+ | 4000ms | 3000ms |
  | Knaben | 6000ms | 4500ms |

  Maximum load time across any standard template is now 4500ms, down from 6000ms. Speed tier templates unchanged at 3500ms flat.

---

## [2.2.3] - 2026-05-23

### Removed
- **`Uncensored` Regex Pattern (All Universal Templates):** Removed from `rankedRegexPatterns` across all 12 universal templates. The pattern had a score of 0 (no ranking contribution), was exclusively associated with adult anime content, and added no benefit to any standard build. Also removed from `regexes-scored.json`.
- **AnimeTosho (All Templates):** Confirmed fully absent from all template preset lists. Previously disabled in v2.1.4, the preset entry has been cleaned from all templates.

### Fixed
- **Season Pack Episode Matching (All Templates):** Two new ESEs added to resolve wrong episode playback:
  - `Kill Ambiguous Season Packs` — blocks streams with only season info and no episode reference using `seasonPack(streams, 'onlySeasons')`. These are the primary cause of wrong episode playback where debrid services default to file 1.
  - `Kill Season Packs When Episode Streams Exist` — blocks full season pack streams when at least one episode-specific stream is available, using `seasonPack(streams, 'seasonPack')`.

---

## [2.2.2] - 2026-05-23

### Fixed
- **YouTube Kill ESE Strengthened (All Templates):** The existing `type(streams, 'youtube')` expression correctly blocked YouTube streams in WuPlay but failed to catch them in base Stremio where YouTube/trailer streams may be identified differently. Added extended keyword coverage: `youtu`, `yt.be`, `YouTube` (capital Y), `Official Trailer`, `Official Video`, `Watch on YouTube`, `HD Trailer`, `Teaser`, `Promo`, `youtube.com/watch`, `youtube.com/embed`. Any stream matching these patterns is now dropped before it reaches the sort step.

### Removed
- **MediaFusion (All Templates):** Removed from all 18 templates due to ongoing reliability issues. MediaFusion was set to `enabled: true` across standard templates. It is now absent from the preset list entirely. Users who wish to use MediaFusion can add it manually via the AIOStreams addon settings.

---

## [2.2.1] - 2026-05-23

### Added
- **Core Nexus 4K Essential (`core-nexus-4k-essential-torbox.json`):** Full-featured 4K build for TorBox Essential users with no Usenet access. Based on the 4K HT TorBox template with `newznab` removed, `preferredStreamTypes` set to `['debrid']` only, and `nzbFailover`/`cacheAndPlay` disabled. Full 9-addon stack retained. Targets 2160p with Dolby Vision, HDR10+, TrueHD/Atmos, 5-150 GB. SeaDex enforced for anime. Upload to `Templates/Torbox/Single/`.
- **Core Nexus 1080p Essential (`core-nexus-1080p-essential-torbox.json`):** Full-featured 1080p SDR build for TorBox Essential users with no Usenet access. Based on the TorBox Exclusive template with the same Essential modifications. Targets WEB-DL/WEBRip, blocks BluRay/Remux/4K/HDR, 1-25 GB. Full 9-addon stack retained. Upload to `Templates/Torbox/Single/`.

---

## [2.2.0] - 2026-05-23

### Added
- **Speed Tier — 4 New Templates:** A new template category for users prioritising instant autoplay (2-3 second stream load) over maximum source coverage. All four speed templates use only Library, TorBox Search, Comet, and Zilean — the four fastest scrapers — with 3500ms timeouts, 10 global results, 4 per resolution, and a 5-key sort. All other Core Builds features remain: scored regex ranking, Tamtaro ESEs, episode matching, `cacheAndPlay`, `hideErrors`, and `nzbFailover`.

  | Template | Resolution | Services |
  |---|---|---|
  | `Speed/EasyNews/core-nexus-speed-1080p` — **Core Nexus Speed 1080p (EasyNews)** | 1080p SDR | TorBox Essential + EasyNews |
  | `Speed/EasyNews/core-nexus-speed-4k` — **Core Nexus Speed 4K (EasyNews)** | 4K HDR | TorBox Essential + EasyNews |
  | `Speed/TorBox/core-nexus-speed-1080p-torbox` — **Core Nexus Speed 1080p** | 1080p SDR | TorBox Essential only |
  | `Speed/TorBox/core-nexus-speed-4k-torbox` — **Core Nexus Speed 4K** | 4K HDR | TorBox Essential only |

  4K speed templates include: Dolby Vision and HDR10+ priority, TrueHD/Atmos audio chain, 5-150 GB file range, SeaDex best-release for anime.
  1080p speed templates include: SDR only, BluRay and Remux blocked, 1-25 GB file range.
  TorBox-only variants set `preferredStreamTypes: [debrid]` and disable Usenet-specific failover.

---

## [2.1.8] - 2026-05-23

### Changed
- **Per-Resolution Regex Pattern Optimisation (1080p Templates):** The 18 regex patterns that can never match any stream in 1080p templates have been removed from `rankedRegexPatterns`. These are patterns for Remux T1/T2/T3, UHD BluRay T1/T2/T3, HD BluRay T1/T2/T3, and DV (Disk) -- all target qualities or resolutions that are explicitly excluded before regex evaluation runs, making them dead weight. 1080p templates now carry 131 patterns instead of 149. 4K templates retain all 149 -- everything is potentially relevant. File size reduction: ~9 KB per 1080p template.
- **`preferredRegexPatterns` Per-Resolution (1080p Templates):** Previous preferred patterns (Remux T1, UHD BluRay T1, FraMeSToR) were all for excluded qualities -- they could never boost any stream. Replaced with Web T1 patterns (Radarr, Sonarr, Web T1) and top web-relevant groups (126811, FLUX, SiC, hallowed, BHDStudio) -- groups that actually release the WEB-DL content these templates target.

---

## [2.1.7] - 2026-05-23

### Added
- **`seasonEpisodeMatching`:** Added across all 12 templates — `enabled: true, strict: true, requestTypes: [movie, series, anime]`. Ensures the correct episode is matched rather than a loose title-only match. Was missing entirely from all previous versions.
- **`nzbFailover`:** `enabled: true, position: last` -- automatic NZB failover when a Usenet download fails, falling back to the next available source. Particularly relevant for the Hybrid template.
- **`cacheAndPlay`:** `enabled:
