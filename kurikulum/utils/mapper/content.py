from configparser import MAX_INTERPOLATION_DEPTH
from xml.etree.ElementPath import prepare_predicate
from networkx import periphery
from openpyxl import Workbook

import kurikulum.const.predicate as predicate
from kurikulum.enum.prefix import Prefix
from kurikulum.enum.worksheet import Worksheet
from kurikulum.utils.mapper.IRI import IRI


def mapping(wb: Workbook):
    ws = wb[Worksheet.CONTENT.value]

    min_row = 4
    max_row = wb['Sheet8']['B7'].value + 3

    content = []
    iri_content = IRI(Prefix.OBE, 'Content')

    ws_knowledge_category = wb[Worksheet.KNOWLEDGECATEGORY.value]
    iri_knowledge_categories = [IRI(Prefix.OBE, cell[1]) for cell in ws_knowledge_category.iter_rows(min_row=2, max_row=5, values_only=True)]


    for row in ws.iter_rows(min_row=min_row, max_row=max_row, values_only=True):
        iri_ct = IRI(Prefix.OBE, row[0])
        iri_code = IRI(Prefix.STRING, row[0])
        iri_desc = IRI(Prefix.STRING, row[1])
        iri_factual = iri_knowledge_categories[0] if row[2] == 'Yes' else False
        iri_conceptual = iri_knowledge_categories[1] if row[3] == 'Yes' else False
        iri_procedural = iri_knowledge_categories[2] if row[4] == 'Yes' else False
        iri_metacognitive = iri_knowledge_categories[3] if row[5] == 'Yes' else False

        content.append([iri_ct, predicate.TYPE, iri_content])
        content.append([iri_ct, predicate.CODE, iri_code])
        content.append([iri_ct, predicate.DESCRIPTION, iri_desc])
        if iri_factual:
            content.append([iri_ct, predicate.HAS_KNOW_CAT, iri_factual])
        if iri_conceptual:
            content.append([iri_ct, predicate.HAS_KNOW_CAT, iri_conceptual])
        if iri_procedural:
            content.append([iri_ct, predicate.HAS_KNOW_CAT, iri_procedural])
        if iri_metacognitive:
            content.append([iri_ct, predicate.HAS_KNOW_CAT, iri_metacognitive])

        for clo in row[6:]:
            if clo == None or clo == '':
                continue
            iri_clo = IRI(Prefix.OBE, clo)
            content.append([iri_clo, predicate.HAS_CONTENT, iri_ct])

    return content