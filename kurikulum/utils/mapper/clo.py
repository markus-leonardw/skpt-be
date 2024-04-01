from openpyxl import Workbook

from kurikulum.enum.worksheet import Worksheet


def mapping(wb: Workbook):
    ws = wb[Worksheet.CLO.value]

    clo_data = []

    # Implement your mapping logic here
    # Iterate through rows, extract data, and append to clo_data list

    return clo_data