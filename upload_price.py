import scrape_price
import upload_gsheet

def main():
	json_file = 'daatta.json'
	if scrape_price.update_json(json_file) == False:
		print("Price scraping unsuccesful! Try again")
		exit(-1)

	if upload_gsheet.update(json_file) == False:
		print("Sheets updating unsuccesful! Try again")
		exit(-1)

	print("Data collected and updated!")


if __name__ == '__main__':
	main()