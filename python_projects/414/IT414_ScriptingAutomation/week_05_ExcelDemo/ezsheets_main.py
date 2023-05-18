#IT 414 - EZsheets Tutorial
import ezsheets
import webbrowser

"""
#Creating a new spreadsheet and printing the ID
my_new_spreadsheet = ezsheets.createSpreadsheet("sales_data")
print(my_new_spreadsheet.spreadsheetId)
"""

my_spreadsheet = ezsheets.Spreadsheet("1-PYtFz7ywOW4WlgqvZn5llAoEY-mfBZ7mitHaetxFBQ")
my_url = my_spreadsheet.url

curr_sheet = my_spreadsheet[0]
rows = curr_sheet.getRows()

rows[0][0] = "Title"
rows[0][1] = "Arthor"
rows[0][2] = "Price"
rows[1][0] = "Ender's Game"
rows[1][1] = "Orson Scott Card"
rows[1][2] = "7.99"
rows[2][0] = "Harry Potter and the Little Chimp"
rows[2][1] = "J.K. Rowling"
rows[2][2] = "18.99"

curr_sheet.updateRows(rows)


webbrowser.open(my_url)
