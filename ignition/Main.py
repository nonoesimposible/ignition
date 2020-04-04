#!/bin/env python3
from os import * # Import bash run abilities
from os.path import expanduser
home = expanduser("~")
import inspect

import gi # Import GTK Stuff
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

from app_categories import categories

class HomeWindow(Gtk.ApplicationWindow):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ignition")
        # system("mkdir ~/.local/share/ignition/")
        # self.appdata = home+"/.local/share/ignition/"

        tabs = Gtk.Notebook.new()

        prevbutton = []
        for category in categories:
            tabgrid = Gtk.Grid.new()

            # print(gridlist)

            row = 0
            col = 0

            for item in category:
                button = Gtk.Button.new() 
                button.set_label(item.name)
                button.connect("clicked", self.install, item)
                if col == 0:
                    # print("Attach")
                    tabgrid.attach(button, col, row, 2, 1)
                else:
                    # print("Attach Next To")
                    tabgrid.attach_next_to(button, prevbutton, Gtk.PositionType.RIGHT, 2, 1)

                prevbutton = button

                if col >= 7:
                    row = row + 1
                    col = 0
                else:
                    col = col + 1

            tabs.insert_page(tabgrid, Gtk.Label.new(category.name), -1)

        self.add(tabs)

    # Currently button is not used. I need to look up Python syntax to make that cleaner.
    def install(self, button, item):

        if item.pkg_manager == "apt":
            print(f"pkexec apt-get --yes install {item.pkg_name} && exit")
            # system("pkexec apt-get --yes install " + pkg_name + " && exit")
        elif item.pkg_manager == "snap":
            print(f"pkexec snap install {item.pkg_name} && exit")
            # system("pkexec snap install " + pkg_name + " && exit")
        else:
            print(f"Something myseterious went wrong when trying to install {item.name}.")

win = HomeWindow()

win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
