from qgis.PyQt.QtWidgets import QAction, QMessageBox
from qgis.PyQt.QtGui import QIcon
import os

from .map_click_tool import MapClickTool
from .web_view_dialog import WebViewDialog


class QuickStreetViewer:
    def __init__(self, iface):
        self.iface = iface
        self.canvas = iface.mapCanvas()
        self.action = None
        self.mapTool = None
        self.dialog = None
        self.shown_msg = False

    def initGui(self):
        icon_path = os.path.join(os.path.dirname(__file__), 'icon.png')

        self.action = QAction(QIcon(icon_path), "Quick Street Viewer", self.iface.mainWindow())
        self.action.triggered.connect(self.run)

        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&Quick Street Viewer", self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        self.iface.removePluginMenu("&Quick Street Viewer", self.action)

    def run(self):
        if self.dialog is None:
            self.dialog = WebViewDialog()

        self.dialog.show()

        # Show info only once
        if not self.shown_msg:
            if not self.dialog.web_available:
                QMessageBox.information(
                    self.iface.mainWindow(),
                    "Quick Street Viewer",
                    "Web view is not available.\n\n"
                    "The plugin will open locations in your browser instead.\n\n"
                    "For best experience, install PyQtWebEngine."
                )
            self.shown_msg = True

        self.mapTool = MapClickTool(self.canvas, self.dialog)
        self.canvas.setMapTool(self.mapTool)