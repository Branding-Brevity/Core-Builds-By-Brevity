# 🛠️ Advanced Editing: Unlocking Deep Configuration

The **Core Builds** are designed to be frictionless and plug-and-play. However, if you want to look under the hood, adjust caching rules, or manually edit the raw template data, you will need to unlock **Advanced Mode** in AIOStreams.

Here is how to safely access and edit the deeper configuration layers.

## Step 1: Access Your AIOStreams Host
1. Open your preferred AIOStreams instance (e.g., your local dashboard or a hosted version like ForTheWeak).
2. Navigate to the **Configure** or **Template Importer** page where you normally paste the raw Core Build links.

## Step 2: Enable Advanced Mode
1. Look near the top of the configuration page (often in the top-right corner or right below the main header).
2. Locate the toggle switch labeled **"Advanced Mode"** or **"Show Advanced Settings"**.
3. Toggle it **ON**. 

## Step 3: What Advanced Mode Unlocks
Once enabled, the UI will expand to reveal deeper developer settings:

* **Raw JSON Editor:** You will now see the actual code block for the imported template. You can manually tweak `excludedStreamExpressions`, alter max resolution limits, or change scraper timeouts directly in the code.
* **Granular Scraper Toggles:** Instead of just turning services on or off, you can fine-tune exactly how each scraper (like Torrentio, MediaFusion, or Comet) behaves within the build.
* **Proxy Configuration:** Direct access to MediaFlow proxy URLs and password fields.

## ⚠️ Important Editing Rules
If you are tweaking the Core Builds via the raw JSON editor, keep these rules in mind:
* **Syntax Matters:** JSON is very strict. If you delete a comma `,` or a bracket `}` by accident, the entire template will break and fail to load in Stremio.
* **Validate Your Code:** If you make heavy edits, it is highly recommended to copy your code and paste it into a free site like [JSONLint](https://jsonlint.com/) to ensure there are no syntax errors before hitting save.
* **Backup First:** Before changing anything in a working Core Build, copy the original JSON and save it in a notepad file so you can easily revert if something goes wrong.

---
*Return to the [Main README](../README.md).*
