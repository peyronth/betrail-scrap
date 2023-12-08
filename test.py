import os

import scripts.chronorace as chronorace
import scripts.kikourou as kikourou
import scripts.sportmaniacs as sportmaniacs


# Table referencing for each website, webSiteName, scriptPath and exampleUrl.
supportedWebsites = {
    'chronorace' : {"script": chronorace.chronorace, "exampleUrl": "https://prod.chronorace.be/Classements/Classement.aspx?eventId=1188318666566175&IdClassement=17573"},
    'kikourou' : {"script": kikourou.kikourou, "exampleUrl": "http://www.kikourou.net/resultats/resultat-154252-la_course_nature_des_3_etangs_-_18_km-2020.html"},
    'sportmaniacs' : {"script": sportmaniacs.sportmaniacs, "exampleUrl": "https://sportmaniacs.com/es/races/gtpe-2023-gran-trail-picos-de-europa/64976d6e-e580-48b6-ba51-6641ac1f1c02/results#rankings"}
}

testResults = {}

# For each website, test the script with the exampleUrl and check if an excel file is created at returned path
for webSiteName in supportedWebsites:
    print("Testing " + webSiteName + "...")
    currentWebsite = webSiteName
    currentUrl = supportedWebsites[currentWebsite]["exampleUrl"]
    # Launch the script
    returnedPath = supportedWebsites[currentWebsite]["script"](currentUrl)
    # Check if the file is created
    testResult = False
    if isinstance(returnedPath, str) and os.path.isfile(returnedPath):
        testResult = True
    testResults[webSiteName] = testResult

# Save results as markdown table in versions/compatibility.md and rename actual compatibility.md
import datetime
import shutil
import pandas as pd

# Create a dataframe with the test results
filename = "versions/compatibility.md"
df = pd.DataFrame(testResults.items(), columns=['Website', 'Compatibility'])
# Convert boolean to string and replace true by U+2705 and false by U+274C
df['Compatibility'] = df['Compatibility'].replace({True: ':white_check_mark:', False: ':x:'})
# Sort by website name
df = df.sort_values(by=['Website'])
# Convert to markdown table
table = df.to_markdown(index=False)
# Rename actual compatibility.md
if os.path.isfile(filename):
    shutil.move(filename, "versions/compatibility_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".md")
# Save the table in versions/compatibility.md
with open(filename, "w") as file:
    file.write(table)
   

