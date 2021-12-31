# DAB | SmartBroker - Postmanager - download PDF reports with selenium & python

Automatic download of all PDF reports in "Postmanager inbox"

# Goal
1. Batch download of unlimited PDF reports based on a predefined timeframe from DAB PostfachManager site.
2. Follow KISS principle.


# Requirements
1. Install Python 3 
    a) https://www.python.org/downloads/ or https://docs.anaconda.com/anaconda/install/windows/
 2. Install dependencies: 
    a) run in cmd line "pip install -r requirements.txt"
 3. Download relevant ChromeDriver version; e.g. if you use Chrome browser version 96.x.x.x download latest Chrome version 96 (https://chromedriver.chromium.org/downloads)
    a) Extract the archive and copy file chromedriver.exe to a folder of your %PATH% environment, e.g. copy .exe file to C:\Windows (or create separate folder and add to %PATH% environment)
 4. Use latest Chrome browser
    a) https://www.google.com/chrome/
 5. Configure Chrome to download files without issues
    a) navigate to "chrome://settings/content/pdfDocuments", change "Default behavior" to "Download PDFs"
    b) allow automatic and multiple downloads (https://www.howtogeek.com/428416/how-to-enabledisable-multiple-file-downloads-in-chrome/)
    c) optional: install Chrome extension Smartbroker Enhancer (https://chrome.google.com/webstore/detail/smartbroker-enhancer/dckkmplockpdghpenceophfmgadbjhfi)
 6. Close any Chrome instances and launch Chrome via cmd line
    a) chrome.exe -remote-debugging-port=[your_prefered_not_used_port]
      e.g. "C:\Program Files\Google\Chrome\Application\chrome.exe -remote-debugging-port=9998"
    b) maximize Chrome window (full screen) 
 7. Setup SmartBroker Postmanager
    a) navigate to https://b2b.dab-bank.de/smartbroker/Postmanager/index.xhtml
    b) login, scan QR code with SecurePlus App, confirm QR-TAN
    c) login, scan QR code with SecurePlus App, confirm QR-TAN
    d) optional: adjust your search -> timeframe, status and click "Dokumente suchen"
 8. Download the PDF reports
    a) run in cmd line "python smartbroker.py [your_prefered_not_used_port], e.g. "python smartbroker.py 9998"
    b) don't use Chrome till download is completed (message in your cmd line window); each PDF takes approx. 1s to complete


# Test environment
- Windows 10.0.19043 N/A Build 19043 (x64-based PC)
- Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
- Chrome Version 96.0.4664.110 (Official Build) (64-bit)



# Acknowledgement
 "Skeleton code" from github project https://github.com/headEx74/Flatex-Documents-Download-Helper


# Similar projects
- https://github.com/mitsuhiko/flatex-pdf-download/blob/main/flatex-fetch.py
- https://github.com/pspeter/statement-dl/blob/master/src/statement_dl/flatex.py
