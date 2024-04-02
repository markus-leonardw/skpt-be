from openpyxl import Workbook, load_workbook

import kurikulum.const.predicate as predicate
from kurikulum.enum.prefix import Prefix
from kurikulum.enum.worksheet import Worksheet
from kurikulum.utils.mapper.IRI import IRI
    
def mapping(wb: Workbook):
    ws = wb[Worksheet.PEO.value]
    min_row = 3
    max_row = wb['Sheet8']['B3'].value + 2

    peo = []
    iri_program_educational_objective = IRI(Prefix.OBE, 'ProgramEducationalObjective')

    for row in ws.iter_rows(min_row=min_row, max_row=max_row, values_only=True):
        iri_peo = IRI(Prefix.OBE, row[0])
        iri_curr = IRI(Prefix.OBE, row[1])
        iri_desc = IRI(Prefix.STRING, row[2])

        peo.append([iri_peo, predicate.TYPE, iri_program_educational_objective])
        peo.append([iri_peo, predicate.BELONGS_TO_CURR, iri_curr])
        peo.append([iri_peo, predicate.DESCRIPTION, iri_desc])

    return peo