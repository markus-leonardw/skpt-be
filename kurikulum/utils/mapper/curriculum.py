from openpyxl import Workbook, load_workbook
from kurikulum.enum.worksheet import Worksheet
    
def mapping(wb: Workbook):
    ws = wb[Worksheet.CURRICULUM.value]

    curriculum_data = []

    return curriculum_data

