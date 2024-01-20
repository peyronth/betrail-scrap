import os
from scriptlist import supportedWebsites as supportedWebsites
from scriptlist import supportedHtmlFormats as supportedHtmlFormats

testResults = {}

# For each website, test the script with the exampleUrl and check if an excel file is created at returned path
for webSiteName in supportedWebsites:
    print("Testing " + webSiteName + "...")
    currentWebsite = webSiteName
    currentUrl = supportedWebsites[currentWebsite]["exampleUrl"]
    # Launch the script
    returnedPaths = supportedWebsites[currentWebsite]["script"](currentUrl)
    # Check if the file is created
    testResult = False
    for path in returnedPaths:
        if os.path.isfile(path):
            testResult = True
        else:
            testResult = False
            break
    testResults[currentWebsite] = testResult


# Save results as markdown table in versions/compatibility.md and rename actual compatibility.md
import datetime
import shutil
import pandas as pd
from datetime import date

# Create a dataframe with the test results for url scrap
filename = "versions/compatibility.md"
df_url_scrap = pd.DataFrame(testResults.items(), columns=['Website', 'Compatibility'])
df_url_scrap['Compatibility'] = df_url_scrap['Compatibility'].replace({True: ':white_check_mark:', False: ':x:'})
df_url_scrap = df_url_scrap.sort_values(by=['Website'])

# Create a markdown table for html scrap
df_html_scrap = pd.DataFrame(supportedHtmlFormats.items(), columns=['Website', 'Compatibility'])
df_html_scrap['Compatibility'] = ':white_check_mark:'

markdown = "# Compatibility\n\n" + \
    "> Last update: " + date.today().strftime("%d/%m/%Y") + "\n\n" + \
    "## Url scrap\n\n" + \
    df_url_scrap.to_markdown(index=False) + \
    "\n\n" + \
    "## Html scrap\n\n" + \
    df_html_scrap.to_markdown(index=False)


if os.path.isfile(filename):
    shutil.move(filename, "versions/compatibility_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".md")
# Save the table in versions/compatibility.md
with open(filename, "w") as file:
    file.write(markdown)
   

