from openpyxl import load_workbook
from kurikulum.utils.mapper.study_program import mapping as mapping_study_program
from kurikulum.utils.mapper.curriculum import mapping as mapping_curriculum
from kurikulum.utils.mapper.peo import mapping as mapping_peo
from kurikulum.utils.mapper.plo import mapping as mapping_plo
from kurikulum.utils.mapper.splo import mapping as mapping_splo
from kurikulum.utils.mapper.clo import mapping as mapping_clo
from kurikulum.utils.mapper.content import mapping as mapping_content
from kurikulum.utils.mapper.course import mapping as mapping_course


READ_FILE_DIR = './static/dummy_final.xlsx'
    
class Mapper:
    def __init__(self, file_path):
        self.file_path = file_path
        self.wb = self.load_file()
        self.study_program = None
        self.curriculum = None
        self.peo = None
        self.plo = None
        self.splo = None
        self.clo = None
        self.content = None
        self.course = None

    def load_file(self):
        try:
            wb = load_workbook(self.file_path, data_only=True, read_only=True)
            return wb
        except Exception as e:
            raise IOError(f"got error message: {e}")
        
    def construct_insert_query(self, triples):
        template = '''
PREFIX OBE: <http://www.semanticweb.org/ami/ontologies/2024/0/OBE#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
'''
        return template + self.get_rdf(triples)

    def get_rdf(self, triples):
        rdf = '\n'.join(f"{' '.join(map(str, triple))} ." for triple in triples)
        return rdf

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
    
    def construct_all_data(self):
        study_program = self.get_study_program_data()
        study_program_query = self.construct_insert_query(study_program)

        curriculum = self.get_curriculum_data()
        curriculum_query = self.construct_insert_query(curriculum)

        peo = self.get_peo_data()
        peo_query = self.construct_insert_query(peo)

        plo = self.get_plo_data()
        plo_query = self.construct_insert_query(plo)

        splo = self.get_splo_data()
        splo_query = self.construct_insert_query(splo)

        clo = self.get_clo_data()
        clo_query = self.construct_insert_query(clo)

        content = self.get_content_data()
        content_query = self.construct_insert_query(content)

        course = self.get_course_data()
        course_query = self.construct_insert_query(course)

        return {
            "study_program": study_program_query,
            "curriculum": curriculum_query,
            "peo": peo_query,
            "plo": plo_query,
            "splo": splo_query,
            "clo": clo_query,
            "content": content_query,
            "course": course_query
        }

