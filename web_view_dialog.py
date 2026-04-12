from qgis.PyQt.QtWidgets import QDialog, QVBoxLayout, QLabel

# Safe import
try:
    from PyQt5.QtWebEngineWidgets import QWebEngineView
    WEB_ENGINE_AVAILABLE = True
except ImportError:
    WEB_ENGINE_AVAILABLE = False


class WebViewDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quick Street Viewer")
        self.resize(900, 600)

        self.layout = QVBoxLayout()
        self.web_available = WEB_ENGINE_AVAILABLE

        if self.web_available:
            self.browser = QWebEngineView()
            self.layout.addWidget(self.browser)
        else:
            self.browser = None
            label = QLabel(
                "⚠ Web view not available.\n\n"
                "Street View will open in your default browser."
            )
            self.layout.addWidget(label)

        self.setLayout(self.layout)

    def load_url(self, url):
        if self.browser:
            self.browser.setUrl(url)