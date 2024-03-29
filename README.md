# Gasoline price forecast

Application is used to get gasoline price data from Polttoaine.net, which is a service/website that provides gasoline price data. Price data is based on pricing data entered by users, so there might be some reliability issues related to data source, but in big picture/long run it seems to be good enough source for data.

![spreadsheet](price_sheet.PNG)



## Overview of files

upload_price.py:
- Acts as a "master", that starts:
  - scrape_price.py (Price scraping)
    - Gets price from polttoaine.net (), and saves it to data.json

  - upload_gsheet.py (Google sheet updating)
    - Gets the price data from data.json, and saves it to google sheet

So if you don't want to use Google Spreadsheet for data storage, the upload_gsheet.py can be replaced with some alternative script.

    

## Setup
- For spreadsheet authentication, client_secret.json is needed
- Change your sheet name in upload_gsheet.py
- Change value of PAGE_URL in scrape_price.py to the polttoaine.net page (=city) you want to get the price data

## Analyse outcome

Example of data utilizing can be seen in ABC-diesel-price.ipynp, which:
- Gets the data from spreadsheets
- Filters out one of the stations from the spreadsheet
- Saves the price difference between consecutive days, and presents that information in boxplot

The boxplot image below shows, whow much has diesel price changed compared to the day before. So as an example, on weekday #2 (Wednesday), the number is usually positive which means that prices tend to rise between Tuesday and Wednesday 
--> Refuel your vehicles on Tuesday!
![prices](Diesel-price-change.PNG)
