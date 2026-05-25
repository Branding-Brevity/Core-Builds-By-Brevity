import urllib.request

instances = {
    "ElfHosted": "https://aiostreams.elfhosted.com",
    "Yeb's": "https://aiostreams.fortheweak.cloud",
    "Midnight's": "https://aiostreamsfortheweebsstable.midnightignite.me"
}

status_report = "# Instance Status\n\n| Instance | Status |\n|---|---|\n"

for name, url in instances.items():
    try:
        code = urllib.request.urlopen(url, timeout=5).getcode()
        status = "🟢 Online" if code == 200 else "🟡 Degraded"
    except:
        status = "🔴 Offline"
    status_report += f"| {name} | {status} |\n"

with open('STATUS.md', 'w') as f:
    f.write(status_report)
    
