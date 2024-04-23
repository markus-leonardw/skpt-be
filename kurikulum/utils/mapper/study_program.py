from openpyxl import Workbook
from kurikulum.enum.prefix import Prefix
from kurikulum.enum.worksheet import Worksheet
import kurikulum.const.predicate as predicate
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
        fakultas = IRI(Prefix.STRING, row[2])
        visi = IRI(Prefix.STRING, row[3])
        misi = IRI(Prefix.STRING, row[4])
        tujuan = IRI(Prefix.STRING, row[5])
    
        study_program.append([iri_sp, predicate.TYPE, iri_study_program])
        study_program.append([iri_sp, predicate.SP_NAME, iri_name])
        study_program.append([iri_sp, predicate.FAKULTAS, fakultas])
        study_program.append([iri_sp, predicate.VISI, visi])
        study_program.append([iri_sp, predicate.MISI, misi])
        study_program.append([iri_sp, predicate.TUJUAN, tujuan])
        
    return study_program
