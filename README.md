# Quick Street Viewer QGIS Plugin
![Diagram of the System](https://github.com/AnustupJana/QuickStreetViewer-plugin/blob/main/icon.png?raw=true)

## Overview

The **Quick Street Viewer** plugin for QGIS is a lightweight and efficient tool that allows users to instantly open any clicked location in Google Street View. It simplifies field verification and location inspection workflows by combining map interaction with real-world visualization. Additionally, the plugin automatically copies the clicked coordinates, making it easy to reuse them in other platforms or applications.

## Features
- Open Google Street View instantly with a single click on the map.
- Automatically copy clicked coordinates (Latitude, Longitude) to clipboard.
- Display marker on clicked location for visual reference.
- Embedded Street View inside QGIS (if WebEngine is available).
- Smart browser fallback when WebEngine is not installed.
- Prevents multiple tab openings (avoids browser clutter).
- Real-time update of location without reopening new windows.

## Requirements
- **QGIS Version**: 3.0 or later.
- **Operating System**: Windows, macOS, or Linux.
- **Dependencies**:
  - No mandatory external libraries required.
  - Optional: `PyQtWebEngine` for embedded Street View inside QGIS.

## Installation

1. **From QGIS Plugin Repository**:
   - In QGIS, go to `Plugins > Manage and Install Plugins`.

   ![Diagram of the System](https://github.com/AnustupJana/QuickStreetViewer-plugin/blob/main/doc/1st.png?raw=true)

   - Search for "Quick Street Viewer".

   ![Diagram of the System](https://github.com/AnustupJana/QuickStreetViewer-plugin/blob/main/doc/2nd.png?raw=true)

   - Click `Install Plugin`.

2. **From ZIP File**:
   - Download the plugin ZIP file from the GitHub repository.
   - In QGIS, go to `Plugins > Manage and Install Plugins > Install from ZIP`.
   - Select the downloaded ZIP file and click `Install Plugin`.

3. **From Source (for developers)**:
   - Clone or download this repository:
     ```bash
     git clone https://github.com/YOUR_USERNAME/QuickStreetViewer.git
     ```
   - Copy the plugin folder to your QGIS plugins directory:
     - Windows: `C:\Users\<YourUsername>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins`
     - Linux: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins`
     - macOS: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins`

4. **Enable the Plugin**:
   - In QGIS Plugin Manager, search for **Quick Street Viewer**.
   - Check the box to enable the plugin.

5. **Verify Installation**:
   - Look for the **Quick Street Viewer** icon in the toolbar or Plugins menu.

---

## Usage

1. **Launch the Plugin**:
   - Click the **Quick Street Viewer** icon from the toolbar or Plugins menu.

   ![Diagram of the System](https://github.com/AnustupJana/QuickStreetViewer-plugin/blob/main/doc/3rd.png?raw=true)

2. **Click on Map**:
   - Click anywhere on the QGIS map canvas.

3. **Automatic Actions**:
   - Opens Google Street View for the selected location.
   - Copies coordinates to clipboard.
   - Displays a marker at the clicked point.

   ![Diagram of the System](https://github.com/AnustupJana/QuickStreetViewer-plugin/blob/main/doc/4th.png?raw=true)

4. **View Result**:
   - If WebEngine is available → Street View opens inside QGIS.
   - Otherwise → Opens in default web browser.

---

## Example Output
28.613939, 77.209021


---

## Development
- **Author**: Anustup Jana  
- **Email**: anustupjana21@gmail.com  
- **Version**: 1.0  
- **Started**: April 2026  
- **License**: GNU General Public License v2.0 or later  

---

## Issues and Support
- Report bugs or suggest features via the [issue tracker](https://github.com/AnustupJana/QuickStreetViewer-plugin/issues).
- For queries, contact: anustupjana21@gmail.com

---

## License
This plugin is licensed under the **GNU General Public License v2.0 or later**.  
See the [LICENSE](https://github.com/AnustupJana/QuickStreetViewer-plugin/blob/main/LICENSE) file for details.

