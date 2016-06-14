## ph_sona_scraper
This is a simple scrapy spider for scraping State of the Nation Address (SONA) texts delivered by Philippine presidents, from Manual L. Quezon (1935) to Benigno S. Aquino, III (2015), found  at http://www.gov.ph/past-sona-speeches/.

## Running the spider
To launch the spider, please make sure you have scrapy installed and then cd to the root directory and run
```
$ scrapy crawl sona
```

As of initial commit, scraped data are not pipelined into a database, so you might want to replace the above command with the following instead:
```
$ scrapy crawl sona -o filename.json
```

## Scraped Data
1. `author`: The name of the President who delivered the speech. Names of speechwriters, if any, are not available.
2. `title`: The title of the speech as it appears on the reference table, not the speech's page itself.
3. `delivered`: datetime format showing when the speech had been delivered, (GMT+00).
4. `text`: The entire text of the speech.

Please watch out for unexpected strings in the `author` and the `text` fields. Still working on these.

## Contributing
Please feel free to contribute as you see fit.