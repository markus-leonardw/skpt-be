from openpyxl import Workbook

from kurikulum.enum.worksheet import Worksheet


def mapping(wb: Workbook):
    ws = wb[Worksheet.COURSE.value]

    course_data = []

    # Implement your mapping logic here
    # Iterate through rows, extract data, and append to course_data list

    return course_data