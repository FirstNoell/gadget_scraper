Mighty Gadget Article Scraper
This project is a Scrapy spider integrated with Selenium that scrapes articles from mightygadget.co.uk and saves each article into a separate Microsoft Word (.docx) file.

Features
Extracts articles' title, URL, summary, and full content.

Follows pagination to scrape multiple pages.

Saves each article as a .docx file in a dedicated folder.

Automatically sanitizes filenames to avoid OS errors.

Built with Scrapy, scrapy-selenium, and python-docx.

Output
Each article is saved in a folder called gadget_articles/, with the following format:

Copy
Edit
gadget_articles/
├── Article_Title_1.docx
├── Article_Title_2.docx
├── ...
Each .docx file contains:

Title (as heading)

URL (article link)

Summary

Full text content

How It Works
Starts at the home page of mightygadget.co.uk.

Waits for article elements to load using Selenium.

Extracts metadata from each post.

Visit each article link to scrape the full content.

Creates and saves a .docx file per article using python-docx.

Continues to the next page via pagination.

Requirements
Python 3.7+

Scrapy

scrapy-selenium

Selenium WebDriver (e.g. ChromeDriver)

python-docx

Install dependencies with:

pip install scrapy scrapy-selenium selenium python-docx
