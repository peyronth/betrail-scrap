# Betrail Scraper

Betrail Scraper is a tool for scraping race results from various websites and exporting them to Excel files.

## Supported Websites

[See the list of supported websites.](https://github.com/peyronth/betrail-scrap/releases)

## Usage

1. **Download the Latest Version:**
   - Visit the [Releases](https://github.com/peyronth/betrail-scrap/releases) page.
   - Download the latest version of Betrail Scraper (betrail-scrap.zip).

2. **Installation:**
   - Unzip the downloaded file to a folder of your choice.

3. **Run Betrail Scraper:**
   - Execute `betrail-scrap.exe`.
   - Select your race and enter the URL.
   - Validate your selection.
   - Retrieve your Excel file from the `export` folder in the application.

## Contributing

To add a script for a new website:

1. **Create a New Branch:**
   - Create a new branch from `dev`: `script/[website-name]`.
   - Make your changes.

2. **Open a Pull Request:**
   - Open a pull request to the `dev` branch.
   - Await review and approval.

## Usage (Development)

For running the development version:

* **Run :**
   ```bash
   python main.py
   ```
* **Add a Script:**
   - Create a new script in the `scripts` folder. The script must be a single function that takes an url as parameter and returns the path to the exported Excel file.
   - Add the script to the scripts list in the `main.py` file.
   - Add the script to the scripts list in the `test.py` file.


