#TODO: Passing the values and updating the cells in some more compact way

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import time
import sys, os

SHEET_NAME = ""

def add_values(sheet, row, timestamp, date, station, gasol1, gasol2, diesel):
	sheet.update_cell(row, 1, timestamp)
	sheet.update_cell(row, 2, date)
	sheet.update_cell(row, 3, station)
	sheet.update_cell(row, 4, gasol1)
	sheet.update_cell(row, 5, gasol2)
	sheet.update_cell(row, 6, diesel)


def update(input_file):
	auth_file = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'client_secret.json')
	# use creds to create a client to interact with the Google Drive API
	scope = ['https://spreadsheets.google.com/feeds',
	         'https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name(auth_file, scope)
	client = gspread.authorize(creds)

	# Find a workbook by name and open the first sheet
	# Make sure you use the right name here.
	sheet = client.open(SHEET_NAME).sheet1

	# Extract values and check the length of the list (=how many data records are included)
	list_of_hashes = sheet.get_all_records()
	next_row = len(list_of_hashes) + 2

	with open(input_file) as input_data:
		price_data = json.load(input_data)
	input_data.close()

	t = time.localtime()
	current_time = time.strftime("%H:%M:%S", t)
	print("Uploading data...")
	for i in price_data:
		add_values(sheet, next_row, current_time, price_data[i]['date'], i, price_data[i]['95E10'], price_data[i]['98E'], price_data[i]['Diesel'])
		next_row += 1
	print("Done!")
	
if __name__ == '__main__':
	update('data.json')