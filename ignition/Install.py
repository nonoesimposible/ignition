from os import * # Import bash run abilities
from os.path import expanduser
home = expanduser("~")

import gi # Import GTK Stuff
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

class Install():
    def __init__(self):
        print("Installer Ready")

    # Organize by package manager

    # APTITUDE
    def neofetch(self):
        print("Installing Neofetch via Aptitude")
        system("pkexec apt-get --yes install neofetch && exit")

    def redshift(self):
        print("Installing RedShift via Aptitude")
        system("pkexec apt-get --yes install redshift && exit")

    def baobab(self):
        print("Installing Baobab via Aptitude")

    def wine(self):
        print("Installing Wine Is Not an Emulator via Aptitude")

    def safeeyes(self):
        print("Installing Safe Eyes via Aptitude")
        system("pkexec apt-get --yes install safeeyes && exit")

    def sl(self):
        print("Installing Steamengine Locomotive via Aptitude")

    def gdebi(self):
        print("Installing Gdebi via Aptitude")
        system("pkexec apt-get --yes install gdebi && exit")

    def gnometweaks(self):
        print("Installing Gnome-Tweaks via Aptitude")
        system("pkexec apt-get --yes install gnome-tweaks && exit")

    def virtualbox(self):
        print("Installing Oracle VirtualBox via Aptitude")

    def firefox(self):
        print("Installing Firefox via Aptitude")
        system("pkexec apt-get --yes install firefox firefoxdriver firefox-globalmenu && exit")


    def synapse(self):
        print("Installing Synapse via Aptitude")
        system("pkexec apt-get --yes install synapse && exit")

    def plank(self):
        print("Installing Plank dock via Aptitude")

    def cario(self):
        print("Installing Cario dock via Aptitude")

    def chromiumapt(self):
        print("Installing Chromium via Aptitude")
        system("pkexec apt-get --yes install chromium-browser chromium-chromedriver chromium-codecs-ffmpeg chromium-bsu && exit")

    def thunderbird(self):
        print("Installing Thunderbird local email client via Aptitude")

    def googleearth(self):
        print("Installing Google Earth via Aptitude")

    def ggames(self):
        print("Installing the Gnome Games Suite via Aptitude")
        system("pkexec apt-get --yes install gnome-games && exit")

    def gnomebreakout(self):
        print("Installing Gnome Breakout via Aptitude")
        system("pkexec apt-get --yes install gnome-breakout && exit")

    def ggamesapp(self):
        print("Installing the Gnome Games App via Aptitude")
        system("pkexec apt-get --yes install gnome-games-app && exit")

    def libreofficeall(self):
        print("Installing full LibreOffice suite and accessories via Aptitude")
        print()
        self.libreoffice()
        self.libreofficeext()

    def libreoffice(self):
        print("Installing full LibreOffice suite via Aptitude")
        system("pkexec apt-get --yes install libreoffice-common libreoffice-writer libreoffice-impress libreoffice-base libreoffice-calc libreoffice-math libreoffice-draw && exit")

    def libreofficeext(self):
        print("Installing LibreOffice suite accessories via Aptitude")
        system("pkexec apt-get --yes install libreoffice-style-sifr libreoffice-java-common libreoffice-pdfimport libreoffice-systray && exit")

    def abiword(self):
        print("Installing Abiword via Aptitude")

    def gnumeric(self):
        print("Installing Gnumeric via Aptitude")

    def papirus(self):
        print("Installing Papirus Icon Theme via Aptitude")
        system("pkexec apt-get --yes install papirus-icon-theme && exit")

    def pocillo(self):
        print("Installing Pocillo Icon Theme via Aptitude")
        system("pkexec apt-get --yes install pocillo-icon-theme && exit")

    def faenza(self):
        print("Installing Faenza Icon Theme via Aptitude")
        system("pkexec apt-get --yes install faenza-icon-theme && exit")

    def xscreensaver(self):
        print("Installing XScreenSaver v_____ and all screensavers via Aptitude")

    def vlc(self):
        print("Installing VLC Media Player and DVD (.VOB) support via Aptitude")

    def rhythmbox(self):
        print("Installing Rhythmbox and all plugins via Aptitude")

    def pavucontrol(self):
        print("Installing Pulse Audio VolUme Control via Aptitude")

    def gstreamer(self):
        print("Installing all GStreamer Audio Codecs via Aptitude")

    def flashplayer(self):
        print("Installing Adobe Flash Player support for Chromium and Firefox via Aptitude")

    def gimageviewer(self):
        print("Installing Gnome Image Viewer via Aptitude")

    def totem(self):
        print("Installing Totem (Gnome Videos) via Aptitude")

    def bb(self):
        print("Installing BB from AA via Aptitude")

    def libaabin(self):
        print("Installing the AA Binary Executable Library from AA via Aptitude")

    def tilix(self):
        print("Installing Tilix via Aptitude")
        system("pkexec apt-get --yes install tilix && exit")

    def terminator(self):
        print("Installing Terminator via Aptitude")

    def gterminal(self):
        print("Installing Gnome Terminal via Aptitude")

    def xfceterminal(self):
        print("Installing Xfce4 Terminal via Aptitude")

    def lxterminal(self):
        print("Installing Lxterminal via Aptitude")

    def xterm(self):
        print("Installing XTerm via Aptitude")

    def mateterminal(self):
        print("Installing MATE Terminal via Aptitude")

    def konsole(self):
        print("Installing Konsole from KDE via Aptitude")

    def git(self):
        print("Installing Git Source Control Management via Aptitude")
        system("pkexec apt-get --yes install git && exit")

    def gedit(self):
        print("Installing Gedit via Aptitude")

    def mousepad(self):
        print("Installing Lxterminal via Aptitude")

    def openshot(self):
        print("Installing Open Shot media editor via Aptitude")

    def ubuntustudio(self):
        print("Installing Ubuntu Studio Installer via Aptitude")

    # SNAPD

    def chromium(self):
        print("Installing Chromium via snapd")
        system("pkexec snap install chromium && exit")

    def mailspring(self):
        print("Installing Mailspring via Snapd")

    def midori(self):
        print("Installing Midori via snapd")
        system("pkexec snap install midori && exit")

    def googletools(self):
        print("Installing Google Tools Desktop via Snapd")

    def yakyak(self):
        print("Installing YakYak via Snapd")

    def ggmail(self):
        print("Installing Gnome Gmail via Snapd")

    def supertuxkart(self):
        print("Installing SuperTuxKart via snapd")
        system("pkexec snap install supertuxkart && exit")

    def openofficedesktopeditors(self):
        print("Installing OPENOFFICE Desktop Editors via Snapd")

    def micropad(self):
        print("Installing microPad via Snapd")

    def p3xonenote(self):
        print("Installing P3X-Onenote via Snapd")
        system("pkexec snap install p3x-onenote && exit")

    def projectlibre(self):
        print("Installing Project Libre via Snapd")

    def spotify(self):
        print("Installing Spotify via Snapd")

    def code(self):
        print("Installing VS Code IDE via snapd")
        system("pkexec snap install code --classic && exit")

    def atom(self):
        print("Installing Atom IDE via snapd")
        system("pkexec snap install atom --classic && exit")

    def sublime(self):
        print("Installing Sublime Text IDE (Trial version) via Snapd")

    def androidstudio(self):
        print("Installing Android Studio from Google via Snapd")

    def eclipse(self):
        print("Installing Eclipse IDE via snapd")
        system("pkexec snap install eclipse --classic && exit")

    def gimp(self):
        print("Installing GIMP via Snapd")
    
    def blender(self):
        print("Installing Blender via Snapd")

    def inkscape(self):
        print("Installing Inkscape via Snapd")

    def kdenlive(self):
        print("Installing Kdenlive media editor from KDE via Snapd")

    def krita(self):
        print("Installing Krita via Snapd")

    # GDEBI

    def ulauncher(self):
        print("Installing ULauncher via Gdebi")

    def insync3(self):
        print("Installing Insync 3 via Gdebi")

    def steam(self):
        print("Installing Steam via wget and gdebi")
        system("wget https://steamcdn-a.akamaihd.net/client/installer/steam.deb && pkexec gdebi steam.deb && exit")

    def minecraft(self):
        print("Installing Minecraft via wget and gdebi")
        system("wget https://launcher.mojang.com/download/Minecraft.deb && pkexec gdebi Minecraft.deb && exit")

    def apacheopenoffice(self):
        print("Installing Apache Open Office suite via Gdebi")

    # CUSTOM

    def pling(self):
        print("Installing the Pling Store by this process:")
        print("    1.Download PlingStore_______.AppImage via wget")
        print("    2.Move it to /usr/share/")
        print("    3.Mark it as executable by chmod 777")
        print("    4.Add a .desktop file generated by Ignition to /usr/share/applications/")
        print()

