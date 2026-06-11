# Renders the social og-image (1200x630) and apple-touch-icon (180x180)
# from their HTML sources via headless Edge — the same trick the one-pager
# PDF uses. Re-run whenever assets/og/*.html or the fonts change.
$edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
$root = Split-Path -Parent $PSScriptRoot
$rootUrl = ($root -replace '\\','/')

& $edge --headless --disable-gpu --screenshot="$root\assets\img\og-image.png" --window-size=1200,630 "file:///$rootUrl/assets/og/og.html" 2>$null | Out-Null
& $edge --headless --disable-gpu --screenshot="$root\assets\img\apple-touch-icon.png" --window-size=180,180 "file:///$rootUrl/assets/og/icon.html" 2>$null | Out-Null

Get-Item "$root\assets\img\og-image.png","$root\assets\img\apple-touch-icon.png" |
  Select-Object Name, @{n='KB';e={[math]::Round($_.Length/1KB,1)}}
