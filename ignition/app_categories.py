"""
Define the categorizations that the rest of the files will consider by. This
is designed so that only one file has to be modified in order to add, move,
or remove an app from a category.

We have two methods of categorization: by package manager, or by category.
"""

class App:
    def __init__(self, name, pkg_name, pkg_manager):
        """
        name        :   human-readable, capitalized name
        pkg_name    :   name of the package used by the package manager (can be space-separated to install multiple packages if all the packages use the same package manager and the package manager allows it)
        pkg_manager :   package manager to use (currently supported is apt, snap
        """

        self.name = name
        self.pkg_name = pkg_name
        self.pkg_manager = pkg_manager


class Category(list):
    """ Almost the exact same thing as a list, but with an additional .name attribute. """
    def __init__(self, name, apps):
        list.__init__(self, apps)
        self.name = name


categories = [
    Category("Basics", [
        App("Neofetch", "neofetch", "apt"),
        App("Gdebi", "gdebi", "apt"),
        App("Redshift", "redshift", "apt"),
        App("GNOME Tweaks", "gnome-tweaks", "apt"),
        App("Baobab", "baobab", "apt"),
        App("WINE", "wine", "apt"),
        App("Safe Eyes", "safeeyes", "apt")
    ]),
    Category("Launchers", [
        App("Synapse", "synapse", "apt"),
        App("Plank", "plank", "apt"),
        App("Cairo", "cairo-dock", "apt")
    ]),
    Category("Browsers", [
        App("Chromium (snap)", "chromium", "snap"),
        App("Chromium (apt)", "chromium-browser", "apt"), # already a transitional package to Snap
        App("Firefox", "firefox", "apt"),
        App("Midori (very light)", "midori", "snap")
    ]),
    Category("Cloud", [
        App("YakYak", "yakyak", "snap"),
    ]),
    Category("Games", [
        App("GNOME Games App", "gnome-games-app", "apt"),
        App("GNOME Games Suite", "gnome-games", "apt"),
        App("Steam", "steam", "apt"), # used to be via Gdebi, is this a problem?
        App("Super Tux Kart", "supertuxkart", "snap"),
        App("GNOME Breakout", "gnome-breakout", "apt")
    ]),
    Category("Office", [
        App("Libreoffice Suite", "libreoffice-common libreoffice-writer libreoffice-impress libreoffice-base libreoffice-calc libreoffice-math libreoffice-draw", "apt"),
        App("Abiword", "abiword", "apt"),
        App("Gnumeric", "gnumeric", "apt"),
        App("μPad", "micropad", "snap"),
        App("P3X Onenote", "p3x-onenote", "snap")
    ]),
    Category("Themes", [
        App("Papirus Icon Theme", "papirus-icon-theme", "apt"),
        App("Pocillo Icon Theme", "pocillo-icon-theme", "apt"),
        App("Faenza Icon Theme", "faenza-icon-theme", "apt"),
        App("XScreenSaver", "xscreensaver", "apt")
    ]),
    Category("Media", [
        App("VLC Media Player", "vlc", "apt"), # originally also was supposed to include DVD (.VOB) support
        App("Rhythmbox", "rhythmbox", "apt"),
        App("Spotify", "spotify", "snap"),
        App("PAVU Control", "pavucontrol", "apt"),
        App("GNOME Image Viewer", "eog", "apt"),
        App("GNOME Videos", "totem", "apt")
    ]),
    Category("Toys", [
        App("BB", "bb", "apt"),
    ]),
    Category("Terminals", [
        App("Tilix", "tilix", "apt"),
        App("Terminator", "terminator", "apt"),
        App("GNOME Terminal", "gnome-terminal", "apt"),
        App("Xfce Terminal", "xfce4-terminal", "apt"),
        App("LXTerminal", "lxterminal", "apt"),
        App("XTerm", "xterm", "apt"),
        App("MATE Terminal", "mate-terminal", "apt"),
        App("Konsole", "konsole", "apt")
    ]),
    Category("Programming", [
        App("Git", "git", "apt"),
        App("VS Code", "code", "snap"), # Do we need a --classic here?
        App("Atom", "atom", "snap"),
        App("Sublime", "sublime-text", "snap"),
        App("Android Studio", "android-studio", "snap"),
        App("Eclipse", "eclipse", "snap"),
        App("Gedit", "gedit", "apt"),
        App("Mousepad", "mousepad", "apt")
    ]),
    Category("Media Production", [
        App("GIMP Photo Editor", "gimp", "snap"),
        App("Blender", "blender", "snap"),
        App("Inkscape", "inkscape", "snap"),
        App("OpenShot", "openshot", "apt"),
        App("Kdenlive", "kdenlive", "snap"),
        App("Krita", "krita", "snap")
    ])
]

