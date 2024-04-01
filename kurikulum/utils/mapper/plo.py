from openpyxl import Workbook

from kurikulum.enum.worksheet import Worksheet


def mapping(wb: Workbook):
    ws = wb[Worksheet.PLO.value]

    plo_data = []

    # Implement your mapping logic here
    # Iterate through rows, extract data, and append to plo_data list

    return plo_data