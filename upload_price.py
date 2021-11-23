import scrape_price
import upload_gsheet
import os, sys

def main():
	json_file = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'data.json')
	
	if scrape_price.update_json(json_file) == False:
		print("Price scraping unsuccesful! Try again")
		exit(-1)

	if upload_gsheet.update(json_file) == False:
		print("Sheets updating unsuccesful! Try again")
		exit(-1)

	print("Data collected and updated!")


if __name__ == '__main__':
	main()