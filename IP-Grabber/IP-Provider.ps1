$pubIP = (Invoke-WebRequest ifconfig.me/ip).Content.Trim()

echo $pubIP | tee $env:TEMP\___

exit 0