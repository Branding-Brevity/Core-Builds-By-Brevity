# 🐅 WuPlay Setup: Core Nexus TorBox Exclusive 

This guide covers the necessary steps to successfully import and finalize your **Core Nexus TorBox Exclusive** configuration. Because this template relies on advanced smart logic, deduplication, and customized caching, there are a few specific API requirements to clear during the setup phase.

---

## 1️⃣ Select a Host & Load the Template
Before you can import the template, you need to open an AIOStreams web host (instance). Here is a list of trusted community hosts you can use:

* **ForTheWeak:** `https://aiostreams.fortheweak.cloud`
* **MidnightIgnite:** `https://aiostreams.midnightignite.com`
* **ElfHosted:** `https://aiostreams.elfhosted.com`

Once you load your preferred host, navigate to the **Template Import** menu. When prompted, enter your specific template ID to pull the customized configuration:

`core-nexus-torbox-exclusive--2026-05-15.23-43-04-azcri48`

---

## 2️⃣ Secure the Poster API Keys
To power the advanced digital release filters and ensure your library art loads correctly, the system requires API keys for **TMDB** and **TVDB**. *(Note: Your RPDB key is already baked directly into this custom template, so you can leave that field as-is!)*

> 💡 **Where to find them:** You do not need to search the web for these. Look directly underneath the respective text input boxes for TMDB and TVDB in the AIOStreams setup menu. There are built-in hyperlinks sitting right beneath the fields that will take you exactly where you need to go to generate your free keys.

---

## 3️⃣ Bypass and Remove Debridio
The template package includes the Debridio integration by default, which throws an error if left blank during the import process. If you do not use Debridio, you must bypass it to save the configuration.

1. **The Bypass:** Click into the Debridio API Key box and type literally anything (e.g., `skip`, `1234`, or random letters). This tricks the validation check and allows you to proceed.
2. **The Removal:** Once you have bypassed the prompt and successfully saved your configuration, open your newly generated AIOStreams configuration panel. Navigate to the **Add-ons** section, locate the Debridio instance, and delete it completely.

---

## 4️⃣ Save and Install to WuPlay
Once all the mandatory fields are satisfied (including your bypassed Debridio text), click **Save** at the bottom of the screen.

AIOStreams will generate a unique UUID and a final manifest URL for your build. **Copy this manifest link**, then open your WuPlay configurer, navigate to the **Add-ons** section, and paste the link to finalize your setup.

