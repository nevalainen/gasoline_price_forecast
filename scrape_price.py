import urllib.request
from bs4 import BeautifulSoup
import json
import time

def update_json(price_file):
	status = False

	EXAMPLE_DATA = [
		'ABC, Karavaani Lasinristeys Punkantie 2 (E85 1.129), 130-tie, 3-tie15.04.1.3491.4391.249',
		'ShellExpress, Et. Viertotie Kaarlonkatu 115.04.1.3241.4241.214',
		'Neste, Et. Viertotie Kulmalan Puistokatu 1015.04.1.3491.4391.279',
		'St1, Lidl Petsamo Karankatu 1515.04.1.3291.4191.219',
		'Neste,  Kirjauksentie 214.04.1.3691.4691.279',
		'ABC,  Kinturintie 2, 3-tie, 54-tie15.04.1.3491.4391.249',
		'Teboil,  Sakonkatu 415.04.1.3251.4151.215',
		'Neste Oil Express, Et. Viertotie Torikatu 7-915.04.1.3241.4141.214',
		'Teboil Express, Et.Viertotie Kumerankatu 1115.04.1.3241.4141.214',
		'ABC, Prisma Voimalankatu 215.04.1.3491.4391.249'
	]

	with open(price_file) as loadfile:
		json_raw = json.load(loadfile)
	loadfile.close()

	#Make request for the page containing the price data, and converts it to 
	#BeautifulSoup object
	quote_page = 'https://www.polttoaine.net/Riihima_ki'
	req = urllib.request.Request(quote_page, headers={'User-Agent': 'Mozilla/5.0'})
	page = urllib.request.urlopen(req).read()
	soup = BeautifulSoup(page, 'html.parser')

	#This will search for the html table rows with class 'bg1 E10' and 'bg2 E10', where
	#the price data is stored in polttoaine.net
	trs = soup.find_all('tr', {'class': 'bg2 E10'}) + soup.find_all('tr', {'class': 'bg1 E10'})
	print("Scrapping data...")

	#Loops through "trs", which contains price from table in text format.
	#It compares the text to items in bensa_asemat, and when it finds the correct text, 
	#it parses the price data from the text row 
	for row in trs: ##Change to trs
		for i in json_raw:
			row_text = row.get_text()[2:] #Input text has two spaces at the beginning, [2:] "takes them off"
			length = len(json_raw[i]['addr'])
			if json_raw[i]['addr'] == row_text[0:length]:
				json_raw[i]['Diesel'] = row_text[-5:]
				json_raw[i]['98E'] = row_text[-10:-5]
				json_raw[i]['95E10'] = row_text[-15:-10]
				json_raw[i]['date'] = row_text[-21:-16]
				status = True

	with open(price_file, 'w') as outputfile:
		json.dump(json_raw, outputfile)

	outputfile.close()
	print("Done!")
	return status

if __name__ == '__main__':
	update_json('daatta.json')