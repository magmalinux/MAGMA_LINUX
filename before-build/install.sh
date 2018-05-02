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
	sleep 1
	
	apt install chromium thunar openssh-server qterminal gnome kdenlive python-3
	apt remove nautilus gnome-terminal
	mv magma-theme /usr/share/desktop-base
	rm -r /usr/share/desktop-base/lines-theme
	rm -r /usr/share/desktop-base/joy-theme
	rm -r /usr/share/desktop-base/joy-inksplat-theme
	rm -r /usr/share/desktop-base/softwaves-theme
	rm -r /usr/share/desktop-base/spacefun-theme
	rm -r /usr/share/desktop-base/active-theme
	ln -d /usr/share/desktop-base/magma-theme /usr/share/desktop-base/active-theme
	mkdir /usr/share/version
	mv version.py /usr/version
	rm /etc/apt/sources.list
	mv sources.list /etc/apt/
	apt install breeze-icon-theme
	mv logo.png /usr/share/desktop-base
	apt update
	apt upgrade

	echo "If software does not work type (apt -f install)"
	echo "Done"
esac
