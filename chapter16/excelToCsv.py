#! python3
# write a program that reads all the Excel files in the current 
# working directory and outputs them as CSV files.
# The filenames of the CSV files should be <excel filename>_<sheet title>.csv,
# where <excel filename> is the filename of the Excel file without the file extension

import os, openpyxl, csv

for excel_file in os.listdir():
	if not excel_file.endswith('.xlsx'):
		continue
	wb = openpyxl.load_workbook(excel_file)
	for current_sheet in wb.sheetnames:
		current_sheet_obj = wb[current_sheet]
		csv_file = open(f"{excel_file.rstrip('.xls')}_{current_sheet}.csv", 'w', newline='')
		csv_writer = csv.writer(csv_file)
		for row in range(1,current_sheet_obj.max_row+1):
			row_contents=[]
			for column in range(1, current_sheet_obj.max_column+1):
				row_contents.append(current_sheet_obj.cell(row=row, column=column).value)
			csv_writer.writerow(row_contents)
	csv_file.close()
		
