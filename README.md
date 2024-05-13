# tamilmvScrapper

## Overview
The `tamilmvScrapper` is a Python-based tool designed to scrape HD movie links from "https://www.1tamilmv.nexus". It leverages `requests` and `BeautifulSoup` to navigate through web pages and extract relevant movie data, focusing on efficiency and respecting site load through controlled request intervals.

## Key Features
- **Targeted Scraping**: Users can specify the name of the movie to fetch relevant HD links efficiently.
- **Pagination Handling**: Supports scraping across multiple pages to gather comprehensive movie link data.
- **Respectful Scraping**: Implements a delay between requests to minimize the impact on the host server.

## Technical Details
- **Language**: Python
- **Libraries**: `requests`, `BeautifulSoup` (for HTML parsing), `tqdm` (for progress bars)

## Installation
Ensure you have Python and pip installed on your system to setup and run this scraper.

### Steps to Set Up
1. Clone the repository:
   ```bash
   git clone https://github.com/afsalahamed07/tamilmvScrapper.git
   cd tamilmvScrapper
   ```

2. Install the necessary Python packages:
   ```bash
   pip install requests beautifulsoup4 tqdm
   ```

## Usage
To start scraping movie links, run the script and follow the prompts to enter the movie name and the number of pages you wish to scrape.

```bash
python scrapper.py
```

You will be asked to:
- Enter the name of the movie.
- Specify how many pages you want to scrape.

The script will then display the movie titles along with their respective links in the console.

## How It Works
- **Session Initialization**: A `requests.Session` is used to persist certain parameters across requests.
- **Fetching Content**: Web pages are fetched using the specified user-agent headers to emulate a browser visit.
- **Parsing HTML**: Extracts relevant movie data from the structured markup using `BeautifulSoup`.
- **Filtering Data**: Filters movies by name to ensure relevance to user input.
- **Output**: Provides a simple, clear output of movie titles and their links in the console.

## Project Status
This project is currently maintained in a public repository, accessible for educational and research purposes. It is regularly updated to adapt to changes in the source website's structure and policies.


## Disclaimer
The `tamilmvScrapper` is intended for educational and research purposes only. Users should ensure they comply with legal stipulations regarding data scraping and usage in their respective jurisdictions.
