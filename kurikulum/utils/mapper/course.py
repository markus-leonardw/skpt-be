from openpyxl import Workbook

import kurikulum.const.predicate as predicate
from kurikulum.enum.prefix import Prefix
from kurikulum.enum.worksheet import Worksheet
from kurikulum.utils.mapper.IRI import IRI


def mapping(wb: Workbook):
    ws = wb[Worksheet.COURSE.value]

    min_row = 3
    max_row = wb['Sheet8']['B7'].value + 2

    course = []
    iri_course = IRI(Prefix.OBE, 'Course')

    for row in ws.iter_cols(min_row=min_row, max_row=max_row, values_only=True):
        iri_cr = IRI(Prefix.OBE, row[0])
        iri_code = IRI(Prefix.STRING, row[0])
        iri_clo = IRI(Prefix.OBE, row[1])
        iri_desc = IRI(Prefix.STRING, row[2])

        course.append([iri_cr, predicate.TYPE, iri_course])
        course.append([iri_cr, predicate.CODE, iri_code])
        course.append([iri_cr, predicate.HAS_CLO, iri_clo])
        course.append([iri_cr, predicate.DESCRIPTION, iri_desc])

    return course