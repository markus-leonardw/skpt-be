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

    for row in ws.iter_rows(min_row=min_row, max_row=max_row, max_col=10, values_only=True):
        iri_peo = IRI(Prefix.OBE, row[0])
        iri_code = IRI(Prefix.STRING, row[0])
        iri_curr = IRI(Prefix.OBE, row[1])
        iri_desc = IRI(Prefix.STRING, row[2])

        peo.append([iri_peo, predicate.TYPE, iri_program_educational_objective])
        peo.append([iri_peo, predicate.CODE, iri_code])
        peo.append([iri_peo, predicate.BELONGS_TO_CURR, iri_curr])
        peo.append([iri_peo, predicate.DESCRIPTION, iri_desc])

        # nullable field
        column_to_predicate = {
            3: predicate.KKNI_RESPONIBILITY,
            4: predicate.KKNI_KNOWLEDGE,
            5: predicate.KKNI_WORKING,
            6: predicate.SNDIKTI_ATTITUDE,
            7: predicate.SNDIKTI_GENERIC,
            8: predicate.SNDIKTI_KNOWLEDGE,
            9: predicate.SNDIKTI_SPECIFIC
        }

        # Iterate over the relevant columns and append non-null IRIs to plo
        for column_index, predicate_value in column_to_predicate.items():
            iri = IRI(Prefix.STRING, row[column_index]) if row[column_index] else None
            if iri:
                peo.append([iri_peo, predicate_value, iri])

    return peo