upload_price.py hoitaa koko homman, eli:
-> Hakee ensin hinnan scrape_price.py:ltä
-> Lataa ne google sheetiin upload_price.py:llä 


upload_price.py:
- Acts as a "master", that starts:
  - Price scraping
    - Gets price from polttoaine.net (a service/website that provides gasoline price data. 
    Price data is based on pricing data entered by users), and saves it to data.json

  - Google sheet updating
    - Gets the price data from data.json, and saves it to google sheet

How to commission:
- For spreadsheet authentication, client_secret.json is needed
- Change your sheet name in upload_gsheet.py
- Change value of PAGE_URL in scrape_price.py to the polttoaine.net page you want to get the price data