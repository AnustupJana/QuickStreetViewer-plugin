from qgis.gui import QgsMapToolEmitPoint, QgsVertexMarker
from qgis.PyQt.QtCore import QUrl
from qgis.PyQt.QtGui import QDesktopServices, QColor
from qgis.PyQt.QtWidgets import QApplication
from qgis.utils import iface
from qgis.core import (
    QgsCoordinateTransform,
    QgsProject,
    QgsCoordinateReferenceSystem
)


class MapClickTool(QgsMapToolEmitPoint):
    def __init__(self, canvas, dialog):
        self.canvas = canvas
        self.dialog = dialog
        super().__init__(self.canvas)

        self.last_url = None

        # 🔴 Marker setup
        self.marker = QgsVertexMarker(self.canvas)
        self.marker.setColor(QColor(255, 0, 0))
        self.marker.setIconSize(10)
        self.marker.setPenWidth(3)

    def canvasReleaseEvent(self, event):
        point = self.toMapCoordinates(event.pos())

        # Move marker to clicked point
        self.marker.setCenter(point)

        # CRS transform to WGS84
        crs_src = self.canvas.mapSettings().destinationCrs()
        crs_dest = QgsCoordinateReferenceSystem("EPSG:4326")

        transform = QgsCoordinateTransform(crs_src, crs_dest, QgsProject.instance())
        wgs_point = transform.transform(point)

        lat = wgs_point.y()
        lon = wgs_point.x()

        # 📋 Copy to clipboard (6 decimal format)
        coord_text = f"{lat:.6f}, {lon:.6f}"
        QApplication.clipboard().setText(coord_text)

        # 🔔 Show message in QGIS
        iface.messageBar().pushMessage(
            "Quick Street Viewer",
            f"Copied: {coord_text}",
            level=0,
            duration=3
        )

        # 🌍 Street View URL
        url_str = f"https://www.google.com/maps/@?api=1&map_action=pano&viewpoint={lat},{lon}"
        url = QUrl(url_str)

        # ✅ If WebEngine available → update same window
        if self.dialog.web_available:
            self.dialog.load_url(url)

        else:
            # 🚫 Prevent duplicate tab spam
            if url_str == self.last_url:
                return

            self.last_url = url_str
            QDesktopServices.openUrl(url)