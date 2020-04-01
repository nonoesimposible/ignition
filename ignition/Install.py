from os import * # Import bash run abilities
from os.path import expanduser
home = expanduser("~")

import gi # Import GTK Stuff
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

from app_categories import apps_by_pkg_manager

class Install():
    def __init__(self):
        print("Installer Ready")

    def install(self, pkg_name):
        if pkg_name in apps_by_pkg_manager["aptitude"]:
            system("pkexec apt-get --yes install " + pkg_name + " && exit")
        elif pkg_name in apps_by_pkg_manager["snapd"]:
            system("pkexec snap install " + pkg_name + " && exit")
        else:
            print(f"Couldn't find package {pkg_name}. It's possible that it's an aptitude or Snap package with the wrong name, or it's Gdebi/custom installation package and is not supported by this branch yet.")
