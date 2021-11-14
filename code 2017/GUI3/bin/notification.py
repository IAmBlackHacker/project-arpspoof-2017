import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify, GdkPixbuf

Notify.init("Arper")
image = GdkPixbuf.Pixbuf.new_from_file("logo.png")
def notification(text):
	summ = text[0]
	bod = text[1]
	notification = Notify.Notification.new(
		summ,
		bod,
		)
	notification.set_icon_from_pixbuf(image)
	notification.show()
	