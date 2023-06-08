import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck

screen = Wnck.Screen.get_default()
screen.force_update()