from openpyxl import Workbook, load_workbook
from kurikulum.enum.prefix import Prefix
from kurikulum.enum.worksheet import Worksheet
from kurikulum.utils.mapper.Node import IRI

# study program
# return list of triple
def mapping(wb: Workbook):
    ws = wb[Worksheet.STUDYPROGRAM.value]

    study_program = []
    iri_study_program = IRI(Prefix.OBE, 'StudyProgram')

    for row in ws.iter_rows(min_row=3, values_only=True):
        study_program.append([IRI(Prefix.OBE, row[0]), IRI(Prefix.RDF, 'type'), iri_study_program])
        study_program.append([IRI(Prefix.OBE, row[0]), IRI(Prefix.OBE, 'spName'), IRI(Prefix.STRING, row[1])])
    return study_program
