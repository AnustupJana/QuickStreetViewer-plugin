# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QuickStreetViewer
                                 A QGIS plugin
 Click on map to open Google Maps and Street View instantly
 ***************************************************************************/
"""
def classFactory(iface):
    from .quick_street_viewer import QuickStreetViewer
    return QuickStreetViewer(iface)