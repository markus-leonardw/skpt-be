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
        iri_code = IRI(Prefix.STRING, row[0])
        iri_curr = IRI(Prefix.OBE, row[1])
        iri_desc = IRI(Prefix.STRING, row[2])
        iri_kkni_responsibility = IRI(Prefix.STRING, row[3])
        iri_kkni_knowledge = IRI(Prefix.STRING, row[4])
        iri_kkni_working = IRI(Prefix.STRING, row[5])
        iri_sndikti_attitude = IRI(Prefix.STRING, row[6])
        iri_sndikti_generic = IRI(Prefix.STRING, row[7])
        iri_sndikti_knowledge = IRI(Prefix.STRING, row[8])
        iri_sndikti_specific = IRI(Prefix.STRING, row[9])


        peo.append([iri_peo, predicate.TYPE, iri_program_educational_objective])
        peo.append([iri_peo, predicate.CODE, iri_code])
        peo.append([iri_peo, predicate.BELONGS_TO_CURR, iri_curr])
        peo.append([iri_peo, predicate.DESCRIPTION, iri_desc])
        peo.append([iri_peo, predicate.KKNI_RESPONIBILITY, iri_kkni_responsibility])
        peo.append([iri_peo, predicate.KKNI_KNOWLEDGE, iri_kkni_knowledge])
        peo.append([iri_peo, predicate.KKNI_WORKING, iri_kkni_working])
        peo.append([iri_peo, predicate.SNDIKTI_ATTITUDE, iri_sndikti_attitude])
        peo.append([iri_peo, predicate.SNDIKTI_GENERIC, iri_sndikti_generic])
        peo.append([iri_peo, predicate.SNDIKTI_KNOWLEDGE, iri_sndikti_knowledge])
        peo.append([iri_peo, predicate.SNDIKTI_SPECIFIC, iri_sndikti_specific])

    return peo