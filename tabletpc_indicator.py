import signal
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
import os, xinput

APPINDICATOR_ID = 'tabletpcindicator'

def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('tabletpc.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    gtk.main()

def rotateScreen(direction):
    os.system("xrandr --output eDP1 --rotate " + direction)

def setTouchpadStatus(status):
    os.system("gsettings set org.gnome.desktop.peripherals.touchpad send-events " + status)

def build_menu():
    menu = gtk.Menu()

    item_quit = gtk.MenuItem('Left')
    item_quit.connect('activate', lambda x: rotateScreen("left"))
    menu.append(item_quit)

    item_quit = gtk.MenuItem('Right')
    item_quit.connect('activate', lambda x: rotateScreen("right"))
    menu.append(item_quit)

    item_quit = gtk.MenuItem('Inverted')
    item_quit.connect('activate', lambda x: rotateScreen("inverted"))
    menu.append(item_quit)

    item_quit = gtk.MenuItem('Normal')
    item_quit.connect('activate', lambda x: rotateScreen("normal"))
    menu.append(item_quit)

    item_quit = gtk.MenuItem('Disable touchpad')
    item_quit.connect('activate', lambda x: setTouchpadStatus("disabled"))
    menu.append(item_quit)

    item_quit = gtk.MenuItem('Enable touchpad')
    item_quit.connect('activate', lambda x: setTouchpadStatus("enabled"))
    menu.append(item_quit)

    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)

    menu.show_all()
    return menu

def quit(source):
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
