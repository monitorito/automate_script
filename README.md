# Script to automate Monitorito execution using Selenium

This repository contains a script to automate the execution of Monitorito. This script is written in Python and makes use of Selenium to open the extension of Monitorito (assumed to be already installed in your Chrome browser), select a mode (online or offline) and visit all the websites provided in a file. The following parameters need to be adjusted, so that the script works as expected:
* mode (this parameter defines whether the script will select the online or the offline mode of Monitorito, after opening it)
* chromeBinaryLocation (this parameter defines the location of the chrome binary)
* chromeUserDataDirectory (this paramter defines the location of the user data for Chrome, optional)
* extensionID (this parameter defines the extensionID, visible from the extensions panel of Chrome, used to open the correct URL pointing to the extension)