# Changelog

All notable changes to the **Core Builds** templates and formatters will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.1] - 2026-05-17

### Removed
- **Scraper Debloat:** Removed `NZBGeek` and `Debridio` integrations entirely from both the 1080p and 4K templates to ensure a strictly TorBox-exclusive scraping experience.

### Changed
- **Setup Streamlined:** Updated the `IMPORT_GUIDE.md` and `WuPlay_Core_Nexus_Import_Guide_V2.pdf` to completely remove the legacy Debridio bypass instructions. Setup is now a frictionless 3-step process.

---

## [1.0.0] - 2026-05-17

### Added
- **Initial Release: Core Nexus 1080p SDR (TorBox Exclusive)**
  - Engineered for Android projectors and standard Google TV hardware.
  - Implemented strict 60 Mbps bitrate cap to prevent network choking.
  - Hard-blocked AV1, Dolby Vision, TrueHD, and DTS-HD MA formats to prevent black screens and audio drops.
- **Initial Release: Core Nexus 4K Home Theater**
  - Unleashed template built for Nvidia Shields and dedicated home theaters.
  - Removed bitrate ceilings (150 Mbps safety net).
  - Actively prioritizes Dolby Vision, HDR10+, AV1 encodes, TrueHD Atmos, and DTS:X.
- **Visual Formatters:** Added the `Core Zenith Diamond` and `Auburn Tiger Edition` UI configurations for clean, hardware-specific badging.
- **Documentation:** Added PDF and Markdown setup guides for WuPlay integration, alongside repository branding and raw import links.
