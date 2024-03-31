from openpyxl import Workbook

from kurikulum.enum.worksheet import Worksheet


def mapping(wb: Workbook):
    ws = wb[Worksheet.CONTENT.value]

    content_data = []

    # Implement your mapping logic here
    # Iterate through rows, extract data, and append to content_data list

    return content_data