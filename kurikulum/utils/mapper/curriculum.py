from openpyxl import Workbook
import kurikulum.const.predicate as predicate
from kurikulum.enum.prefix import Prefix
from kurikulum.enum.worksheet import Worksheet
from kurikulum.utils.mapper.IRI import IRI
    
def mapping(wb: Workbook):
    ws = wb[Worksheet.CURRICULUM.value]
    min_row = 3
    max_row = wb['Sheet8']['B2'].value + 2

    curriculum = []
    iri_curriculum = IRI(Prefix.OBE, 'Curriculum')

    for row in ws.iter_rows(min_row=min_row, max_row=max_row, values_only=True):
        iri_curr = IRI(Prefix.OBE, row[0])
        iri_sp = IRI(Prefix.OBE, row[1])
        iri_name = IRI(Prefix.STRING, row[2])

        curriculum.append([iri_curr, predicate.TYPE, iri_curriculum])
        curriculum.append([iri_curr, predicate.BELONGS_TO_SP, iri_sp])
        curriculum.append([iri_curr, predicate.CURRICULUM_NAME, iri_name])

    return curriculum

