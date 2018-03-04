
import os

from PyQt5.QtCore import pyqtSlot, QSize
from PyQt5.QtWidgets import QSlider
from PyQt5 import QtCore

from qutebrowser.mainwindow.statusbar import percentage

NYAN_MAX_WIDTH=150

class NyanPercentage(QSlider):

	"""Reading percentage displayed in the statusbar."""

	def __init__(self, parent=None):
		"""Constructor. Set percentage to 0%."""
		super().__init__(parent)
		self.set_perc(0, 0)
		self.raw = False
		self.setOrientation(QtCore.Qt.Horizontal)

		dir_path = os.path.dirname(os.path.realpath(__file__))
		nyan_img_path = os.path.join(dir_path, "./img/nyan.svg")
		nyan_rainbow_path = os.path.join(dir_path, "./img/rainbow.svg")

		self.setStyleSheet("""
			QSlider::groove {{
				border: 1px none;
				height: 16px;
				margin: 0 12px;
			}}

			QSlider::sub-page:horizontal {{
				border-image: url({});
			}}

			QSlider::handle:horizontal {{
				image: url({});
				width: 30px;
				margin: -24px -12px;
			}}

			QTSlider::sub-page:horizontal {{
				background: #0000FF;
			}}
        """.format(nyan_rainbow_path, nyan_img_path))

		self.setMaximumWidth(150)

	@pyqtSlot(int, int)
	def set_perc(self, x, y):  # pylint: disable=unused-argument
		"""Setter to be used as a Qt slot.

		Args:
			x: The x percentage (int), currently ignored.
			y: The y percentage (int)
		"""
		if y is None:
			# We don't know, the pos, set to 0
			self.setValue(0)
		else:
			self.setValue(y)

	def on_tab_changed(self, tab):
		"""Update scroll position when tab changed."""
		self.set_perc(*tab.scroller.pos_perc())


def init_nyan():
	# This is really bad, but we need nyans
	percentage.Percentage = NyanPercentage


init_nyan()
