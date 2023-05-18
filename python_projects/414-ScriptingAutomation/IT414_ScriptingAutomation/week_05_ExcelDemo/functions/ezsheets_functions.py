#IT 414 - EZsheets Tutorial
import ezsheets
import webbrowser

"""
#Creating a new spreadsheet and printing the ID
my_new_spreadsheet = ezsheets.createSpreadsheet("Sales Data")
print(my_new_spreadsheet.spreadsheetId)
"""
def createEZSheets(product_list, quantity_list):
    """"""
    my_spreadsheet = ezsheets.Spreadsheet("1-PYtFz7ywOW4WlgqvZn5llAoEY-mfBZ7mitHaetxFBQ")
    my_url = my_spreadsheet.url

    curr_sheet = my_spreadsheet[0]
    rows = curr_sheet.getRows()

    row_count = 1
    col_count = 0

    rows[0][0] = "Product"
    rows[0][1] = "Quantity"



    while row_count < len(product_list):
        rows[row_count][col_count] = product_list[row_count]
        row_count += 1


    row_count = 1
    col_count = 1

    while row_count < len(quantity_list):
        rows[row_count][col_count] = quantity_list[row_count]
        row_count += 1
    
    curr_sheet.updateRows(rows)

    webbrowser.open(my_url)
