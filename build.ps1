$exclude = @("venv", "template_botcity.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "template_botcity.zip" -Force