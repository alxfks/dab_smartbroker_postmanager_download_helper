# MIT License
# 
# Copyright (c) 2021 afa @ https://github.com/alxfks
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.



#.............................................................................................................................................................................................................
#.............................................................................................................................................................................................................
# Acknowledgement
# "Skeleton code" from github project https://github.com/headEx74/Flatex-Documents-Download-Helper
#

# Goal
# 1. Unlimited (batch) download of PDF reports based on a predefined timeframe from DAB Postmanager site https://b2b.dab-bank.de/Tradingcenter/Postmanager/
# 2. Follow KISS principle.
#

# Requirements
# 1. Install Python 3 
#    a) https://www.python.org/downloads/ or https://docs.anaconda.com/anaconda/install/windows/
# 2. Install dependencies: 
#    a) run in cmd line "pip install -r requirements.txt"
# 3. Download relevant ChromeDriver version; e.g. if you use Chrome browser version 96.x.x.x download latest Chrome version 96 (https://chromedriver.chromium.org/downloads)
#    a) Extract the archive and copy file chromedriver.exe to a folder of your %PATH% environment, e.g. copy .exe file to C:\Windows (or create separate folder and add to %PATH% environment)
# 4. Use latest Chrome browser
#    a) https://www.google.com/chrome/
# 5. Configure Chrome to download files without issues
#    a) navigate to "chrome://settings/content/pdfDocuments", change "Default behavior" to "Download PDFs"
#    b) allow automatic and multiple downloads (https://www.howtogeek.com/428416/how-to-enabledisable-multiple-file-downloads-in-chrome/)
#    c) optional: install Chrome extension Smartbroker Enhancer (https://chrome.google.com/webstore/detail/smartbroker-enhancer/dckkmplockpdghpenceophfmgadbjhfi)
# 6. Close any Chrome instances and launch Chrome via cmd line
#    a) chrome.exe -remote-debugging-port=[your_prefered_not_used_port]
#      e.g. "C:\Program Files\Google\Chrome\Application\chrome.exe -remote-debugging-port=9998"
#    b) maximize Chrome window (full screen) 
# 7. Setup SmartBroker Postmanager
#    a) navigate to https://b2b.dab-bank.de/smartbroker/Postmanager/index.xhtml
#    b) login, scan QR code with SecurePlus App, confirm QR-TAN
#    c) login, scan QR code with SecurePlus App, confirm QR-TAN
#    d) optional: adjust your search -> timeframe, status and click "Dokumente suchen"
# 8. Download the PDF reports
#    a) run in cmd line "python smartbroker.py [your_prefered_not_used_port], e.g. "python smartbroker.py 9998"
#    b) don't use Chrome till download is completed (message in your cmd line window); each PDF takes approx. 1s to complete
#.............................................................................................................................................................................................................
#.............................................................................................................................................................................................................
# Test environment
#   Windows 10.0.19043 N/A Build 19043 (x64-based PC)
#   Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
#   Chrome Version 96.0.4664.110 (Official Build) (64-bit)
#............................................................................................................................................................................................................. 
#.............................................................................................................................................................................................................
# Similar projects
# https://github.com/mitsuhiko/flatex-pdf-download/blob/main/flatex-fetch.py
# https://github.com/pspeter/statement-dl/blob/master/src/statement_dl/flatex.py
#.............................................................................................................................................................................................................
#.............................................................................................................................................................................................................
 

import argparse
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support import expected_conditions
#from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class SmartBrokerBrowser:

    def __init__(self, port: int):
        self.chrome_options = Options()

        self.chrome_options.add_experimental_option( "debuggerAddress", f"127.0.0.1:{port}" )
        self.driver = webdriver.Chrome( options=self.chrome_options )

        # disable PDF preview, run chromedriver outside from PATH etc.
        #   https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions
        #   https://stackoverflow.com/questions/61168789/chromedriver-not-recognizing-options
        #   https://stackoverflow.com/questions/43149534/selenium-webdriver-how-to-download-a-pdf-file-with-python


    def download_documents(self):

        hwnd = self.driver.current_window_handle
        self.driver.switch_to.window(hwnd)

        i = 1
        rowCount = len(self.driver.find_elements( By.XPATH, "//tr/td[8]/div[2]/a") ) # KISS

        print("\tPostfach | number of docs/rows found: {}".format(rowCount))

        while i <= rowCount:
            print("\tPostfach | download pdf #{}".format(i))
            
            # KISS
            element = self.driver.find_element( By.XPATH, "//tr[{}]/td[8]/div[2]/a".format(i) )
            self.driver.execute_script( "arguments[0].click();", element )
            # if "click()" does not work use ActionChains or WebDriverWait
            # https://www.google.com/search?q=click+selenium+WebDriverWait+ActionChains+arguments[0].click()

            time.sleep(1)

            self.driver.switch_to.window(hwnd)
            i += 1    
        
        print("\Fantastic, download completed! Have a great day:-)")



if __name__ == '__main__':
    my_parser = argparse.ArgumentParser(prog        = 'smartbroker_postmanager_PDF_mass_downloader',
                                        description = 'Download automatically PDF reports from DAB Postfach via Selenium Chrome webdriver.'
                                                      'Please follow instructions (comment section or README.md).')
    my_parser.add_argument('port',
                           metavar = 'port',
                           type    = int,
                           help    = 'Define the debugging port of a running Chrome instance, e.g. must be 9998 if you launched Chrome via cmd line "chrome.exe -remote-debugging-port=9998"')

    args = my_parser.parse_args()

    print("\nSetup Selemium webdriver Chrome with debug port {}...".format(args.port))
    sm_browser = SmartBrokerBrowser(port=args.port)

    print("Downloading your PDF reports in a second ...\n")
    sm_browser.download_documents()
