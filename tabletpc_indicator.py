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

def turnLeft(widget):
    os.system("xrandr --output eDP1 --rotate left")

def turnRight(widget):
    os.system("xrandr --output eDP1 --rotate right")

def turnInverted(widget):
    os.system("xrandr --output eDP1 --rotate inverted")

def turnNormal(widget):
    os.system("xrandr --output eDP1 --rotate normal")

def disableTouchpad(widget):
    os.system("gsettings set org.gnome.desktop.peripherals.touchpad send-events disabled")

def enableTouchpad(widget):
    os.system("gsettings set org.gnome.desktop.peripherals.touchpad send-events enabled")

def build_menu():
    menu = gtk.Menu()

    item_quit = gtk.MenuItem('Left')
    item_quit.connect('activate', turnLeft)
    menu.append(item_quit)

    item_quit = gtk.MenuItem('Right')
    item_quit.connect('activate', turnRight)
    menu.append(item_quit)

    item_quit = gtk.MenuItem('Inverted')
    item_quit.connect('activate', turnInverted)
    menu.append(item_quit)

    item_quit = gtk.MenuItem('Normal')
    item_quit.connect('activate', turnNormal)
    menu.append(item_quit)

    item_quit = gtk.MenuItem('Disable touchpad')
    item_quit.connect('activate', disableTouchpad)
    menu.append(item_quit)

    item_quit = gtk.MenuItem('Enable touchpad')
    item_quit.connect('activate', enableTouchpad)
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
