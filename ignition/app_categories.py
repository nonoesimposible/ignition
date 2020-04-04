"""
Define the categorizations that the rest of the files will consider by. This
is designed so that only one file has to be modified in order to add, move,
or remove an app from a category.

We have two methods of categorization: by package manager, or by category.
"""

class Category(list):
    """ Almost the exact same thing as a list, but with an additional .name attribute. """
    def __init__(self, name, apps):
        list.__init__(self, apps)
        self.name = name


apps_by_pkg_manager = {
    "aptitude": [
        "neofetch",
        "redshift",
        "baobab",
        "wine",
        "safeeyes",
        "steamengine-locomotive",
        "gdebi",
        "gnome-tweaks",
        "virtualbox",
        "firefox",
        "synapse",
        "plank",
        "cario",
        "chromium",
        "thunderbird",
        "google-earth",
        "gnome-games",
        "gnome-breakout",
        "gnome-games-app",
        "libreoffice",
        "abiword",
        "gnumeric",
        "papirus-icon-theme",
        "pocillo-icon-theme",
        "faenza-icon-theme",
        "xscreensaver",
        "vlc",
        "rhythmbox",
        "pulseaudio",
        "gstreamer",
        "adobe-flash-player",
        "gnome-image-viewer",
        "totem",
        "bb",
        "aa",
        "tilix",
        "gnome-terminal",
        "xfce-terminal",
        "lxterminal",
        "xterm",
        "mate-terminal",
        "konsole",
        "git",
        "gedit",
        "mousepad",
        "openshot",
        "ubuntustudio"
    ],
    "snapd": [
        "chromium",
        "mailspring",
        "midori",
        "googletools",
        "yakyak",
        "ggmail",
        "supertuxkart",
        "openofficedesktopeditors",
        "micropad",
        "p3x-onenote",
        "projectlibre",
        "spotify",
        "code",
        "atom",
        "sublime",
        "androidstudio",
        "eclipse",
        "gimp",
        "blender",
        "inkscape",
        "kdenlive",
        "krita"
    ],
    "gdebi": [
        "ulauncher",
        "insync3",
        "steam",
        "minecraft",
        "apacheopenoffice"
    ],
    "custom": [
        "pling"
    ]
}

categories = [
    Category("Basics", [
        "All Basics",
        "Neofetch",
        "Gdebi",
        "Redshift",
        "Gnome Tweaks",
        "Baobab",
        "WINE",
        "Safe Eyes",
        "Steamengine Locomotive"
    ]),
    Category("Launchers", [
        "Synapse",
        "Plank",
        "ULauncher",
        "Cario"
    ]),
    Category("Browsers", [
        "Chromium",
        "Chromium on APT",
        "Firefox",
        "Midori (Very Light)"
    ]),
    Category("Cloud", [
        "Google Tools",
        "YakYak",
        "Gnome Gmail"
    ]),
    Category("Games", [
        "Gnome Games App",
        "Steam",
        "Minecraft",
        "Gnome Games Suite",
        "Super Tux Kart",
        "Gnome Breakout"
    ]),
    Category("Office", [
        "Libreoffice",
        "OPENOFFICE Desktop Editors",
        "Abiword",
        "Gnumeric",
        "Google Tools",
        "microPad",
        "P3X Onenote",
        "Apache OpenOffice",
        "ProjectLibre"
    ]),
    Category("Themes", [
        "Papirus Icon Theme",
        "Pocillo Icon Theme",
        "Faenza Icon Theme",
        "Pling Store",
        "XScreenSaver"
    ]),
    Category("Media", [
        "VLC Media Player",
        "Rhythmbox",
        "Spotify",
        "PAVU Control",
        "GStreamer Codecs",
        "Gnome Image Viewer",
        "Totem",
        "Flash Player"
    ]),
    Category("Toys", [
        "BB",
        "AA Lib"
    ]),
    Category("Terminals", [
        "Tilix",
        "Terminator",
        "Gnome Terminal",
        "Xfce Terminal",
        "LXTerminal",
        "XTerm",
        "MATE Terminal",
        "Konsole"
    ]),
    Category("Programming", [
        "GIT SCM",
        "VS Code",
        "Atom",
        "Sublime",
        "Android Studio",
        "Eclipse",
        "Gedit",
        "Mousepad"
    ]),
    Category("Media Production", [
        "GIMP Photo Editor",
        "Blender",
        "Inkscape",
        "Open Shot",
        "Kdenlive",
        "Krita",
        "Ubuntu Studio"
    ])
]

