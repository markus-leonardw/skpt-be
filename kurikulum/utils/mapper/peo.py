from openpyxl import Workbook, load_workbook

from kurikulum.enum.worksheet import Worksheet
    
def mapping(wb: Workbook):
    ws = wb[Worksheet.PEO.value]

    peo_data = []

    # Implement your mapping logic here
    # Iterate through rows, extract data, and append to peo_data list

    return peo_data