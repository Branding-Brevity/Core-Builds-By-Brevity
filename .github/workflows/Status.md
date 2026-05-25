name: Check Instance Status

on:
  schedule:
    - cron: '*/30 * * * *'
  workflow_dispatch:

jobs:
  check-status:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Ping Instances and Update Status
        run: |
          import urllib.request

          instances = {
            "ElfHosted": "https://aiostreams.elfhosted.com",
            "Yeb's": "https://aiostreams.fortheweak.cloud",
            "Midnight's": "https://aiostreamsfortheweebsstable.midnightignite.me"
          }
          
          # Start building the table
          status_report = "# Instance Status\n\n| Instance | Status |\n|---|---|\n"
          
          for name, url in instances.items():
            try:
              # Timeout after 5 seconds to keep the build fast
              code = urllib.request.urlopen(url, timeout=5).getcode()
              status = "🟢 Online" if code == 200 else "🟡 Degraded"
            except:
              status = "🔴 Offline"
            status_report += f"| {name} | {status} |\n"

          # Write to the dedicated file
          with open('STATUS.md', 'w') as f:
            f.write(status_report)
        shell: python

      - name: Commit and Push
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          if [[ -n "$(git status --porcelain STATUS.md)" ]]; then
            git add STATUS.md
            git commit -m "chore: update status report"
            git push
          fi
