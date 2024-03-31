from openpyxl import Workbook

from kurikulum.enum.worksheet import Worksheet


def mapping(wb: Workbook):
    ws = wb[Worksheet.SPLO.value]

    splo_data = []

    # Implement your mapping logic here
    # Iterate through rows, extract data, and append to splo_data list

    return splo_data