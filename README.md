# [ph_sona_scraper]()

Philippine State of the Nation (SONA) Scraper

- A simple scrapy spider for scraping SONA texts delivered by Philippine presidents, from Manual L. Quezon (1935) to Benigno S. Aquino, III (2015), found at http://www.gov.ph/past-sona-speeches/.
- To launch the spider, please make sure you have scrapy installed and then cd to the root directory and run
  $ scrapy crawl sona
- As of initial commit, scraped data are not pipelined into a database, so you might want to replace the above command with the following instead:
  $ scrapy crawl sona -o filename.json
- Data fields include title, author (the name of the President), date, and body.
- Please watch out for unexpected strings in author and the main text fields. Still working on these.
- Please feel free to comment or suggest.