from openpyxl import load_workbook
from kurikulum.utils.mapper.study_program import mapping as mapping_study_program
from kurikulum.utils.mapper.curriculum import mapping as mapping_curriculum
from kurikulum.utils.mapper.peo import mapping as mapping_peo
from kurikulum.utils.mapper.plo import mapping as mapping_plo
from kurikulum.utils.mapper.splo import mapping as mapping_splo
from kurikulum.utils.mapper.clo import mapping as mapping_clo
from kurikulum.utils.mapper.content import mapping as mapping_content
from kurikulum.utils.mapper.course import mapping as mapping_course


READ_FILE_DIR = './static/bulk_insert_template_filled.xlsx'

def load_file():
    try:
        wb = load_workbook(READ_FILE_DIR, data_only=True, read_only=True)
        print("success!!!")

        return wb
    except Exception as e:
        raise IOError(f"got error message: {e}")
    
class Mapper:
    def __init__(self):
        self.wb = load_file()
        self.study_program = None
        self.curriculum = None
        self.peo = None
        self.plo = None
        self.splo = None
        self.clo = None
        self.content = None
        self.course = None

    def get_study_program_data(self):
        if self.study_program is None:
            self.study_program = mapping_study_program(self.wb)
        return self.study_program
    
    def get_curriculum_data(self):
        if self.curriculum is None:
            self.curriculum = mapping_curriculum(self.wb)
        return self.curriculum

    def get_peo_data(self):
        if self.peo is None:
            self.peo = mapping_peo(self.wb)
        return self.peo

    def get_plo_data(self):
        if self.plo is None:
            self.plo = mapping_plo(self.wb)
        return self.plo

    def get_splo_data(self):
        if self.splo is None:
            self.splo = mapping_splo(self.wb)
        return self.splo

    def get_clo_data(self):
        if self.clo is None:
            self.clo = mapping_clo(self.wb)
        return self.clo

    def get_content_data(self):
        if self.content is None:
            self.content = mapping_content(self.wb)
        return self.content

    def get_course_data(self):
        if self.course is None:
            self.course = mapping_course(self.wb)
        return self.course
