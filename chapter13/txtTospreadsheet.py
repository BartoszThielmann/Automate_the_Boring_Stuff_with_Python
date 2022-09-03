#! python3
# text files to spreadsheet
# the text files need to be in the same directory as the program

from pathlib import Path
import openpyxl

wb = openpyxl.Workbook()
sheet = wb['Sheet']
p = Path.cwd()
content = []
for filepath_obj in p.glob('*.txt'):
	current_file = open(filepath_obj)
	content.append(current_file.readlines())

for files in range(0, len(content)):
	for line in range(0, len(content[files])):
		if content[files][line].endswith('\n'):
			content[files][line] = content[files][line].rstrip('\n')
		sheet.cell(row = line+1, column = files+1).value=content[files][line]
		
wb.save('txt_spreadsheet.xlsx')
