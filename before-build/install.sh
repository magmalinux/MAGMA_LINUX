dialog  --backtitle "Magma Build Setup"\
	--title "Before run"\
	--infobox "Run as root and make sure you have an internet connection!" 60 60
sleep 3
dhclient
apt update
apt upgrade
dialog  --backtitle "Magma Build Setup"\
	--title "Install Packages"\
	--yesno "Do you want to continue?" 10 30

case "$?" in
	'0')
	dialog  --backtitle "Magma Build Setup"\
		--title "Getting files ready"\
		--infobox "Setting Up System" 10 30
	echo "not ready"
esac
