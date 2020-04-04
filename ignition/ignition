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
from Install import *

class HomeWindow(Gtk.ApplicationWindow):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ignition")
        # system("mkdir ~/.local/share/ignition/")
        # self.appdata = home+"/.local/share/ignition/"

        installer = Install()

        tabs = Gtk.Notebook.new()

        prevbutton = []
        for category in categories:
            name = category.name
            tabgrid = name
            tabgrid = Gtk.Grid.new()

            # print(gridlist)

            row = 0
            col = 0

            for item in category:
                button = Gtk.Button.new() 
                button.set_label(item)
                # button.connect("clicked", installer.allitemmethod)
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

            tabs.insert_page(tabgrid, Gtk.Label.new(name), -1)

        self.add(tabs)

    # def install(self, button, name):
    #     print("Install called")


win = HomeWindow()

win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
