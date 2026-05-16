# Changelog

All notable changes to the **Core Builds** templates and formatters will be documented in this file.

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
- 
