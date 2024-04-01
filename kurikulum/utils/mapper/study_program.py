from openpyxl import Workbook, load_workbook
from kurikulum.enum.prefix import Prefix
from kurikulum.enum.worksheet import Worksheet
from kurikulum.utils.mapper.IRI import IRI

# study program
# return list of triple
def mapping(wb: Workbook):
    ws = wb[Worksheet.STUDYPROGRAM.value]
    min_row = 3
    max_row = wb['Sheet8']['B1'].value + 2

    study_program = []
    iri_study_program = IRI(Prefix.OBE, 'StudyProgram')

    for row in ws.iter_rows(min_row=min_row, max_row=max_row, values_only=True):
        iri_sp = IRI(Prefix.OBE, row[0])
        iri_name = IRI(Prefix.STRING, row[1])

        study_program.append([iri_sp, IRI(Prefix.RDF, 'type'), iri_study_program])
        study_program.append([iri_sp, IRI(Prefix.OBE, 'spName'), iri_name])
        
    return study_program
