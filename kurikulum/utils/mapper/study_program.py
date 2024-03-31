from openpyxl import Workbook, load_workbook
from kurikulum.enum.worksheet import Worksheet

# study program
# return list of triple
def mapping(wb: Workbook):
    ws = wb[Worksheet.STUDYPROGRAM.value]

    study_program = []

    for row in ws.iter_rows(min_row=3, values_only=True):
        study_program.append(row)
        print(row)
    return study_program

