# AIOStreams Instance Status

Live status for all known public AIOStreams instances. Checked every 30 minutes via GitHub Actions.

> ⚠️ **Green = host is reachable.** Does not guarantee the instance accepts new configs or that your template will import correctly. Always test with a fresh import.

---

## 🟢 Stable Instances

<!-- STATUS_STABLE_START -->
*Status loading — check back in a moment.*
<!-- STATUS_STABLE_END -->

---

## 🌙 Nightly Instances

<!-- STATUS_NIGHTLY_START -->
*Status loading — check back in a moment.*
<!-- STATUS_NIGHTLY_END -->

---

## 📋 Instance Notes

| Host | Notes |
|---|---|
| **ElfHosted** | Most stable. Public instance is debrid-only — perfect for Core Builds. No P2P/HTTP streams. |
| **Yeb's** | Run by an AIOStreams Discord admin. Reliable uptime, fast. |
| **Midnight's** | Run by the TorBox community manager. Optimised for TorBox setups. |
| **Viren's** | Developer's own instance. Nightly only — tracks main branch. |
| **Kuu's** | Community-run. Both stable and nightly available. |
| **ATBP** | Community-run. Good uptime track record. |
| **Omni's** | Community-run. |

---

## 🔗 Self-Hosting

Run your own private AIOStreams instance with Docker:

```bash
docker run -p 3000:3000 viren070/aiostreams
```

Full self-hosting docs: [docs.aiostreams.viren070.me](https://docs.aiostreams.viren070.me/getting-started/self-hosting/)

To enable the Core Builds Filtering System synced URLs on a self-hosted instance:

```env
WHITELISTED_SYNCED_URLS=https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Filtering/Core-Builds-ESEs.json,https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Filtering/Core-Builds-PSEs.json,https://raw.githubusercontent.com/Branding-Brevity/Core-Builds-By-Brevity/refs/heads/main/Filtering/Core-Builds-ISEs.json
```

---

## ➕ Missing an Instance?

[Open an issue →](https://github.com/Branding-Brevity/Core-Builds-By-Brevity/issues/new?title=Add+Instance:+&labels=instance)

---

*Status auto-updated every 30 minutes by GitHub Actions. Badges powered by [shields.io](https://shields.io).*
