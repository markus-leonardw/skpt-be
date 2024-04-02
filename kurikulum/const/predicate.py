from kurikulum.enum.prefix import Prefix
from kurikulum.utils.mapper.IRI import IRI


TYPE = IRI(Prefix.RDF, 'type')
BELONGS_TO_CURR = IRI(Prefix.OBE, 'belongsToCurr')
DESCRIPTION = IRI(Prefix.OBE, 'description')
BELONGS_TO_SP = IRI(Prefix.OBE, 'belongsToSP')
CURRICULUM_NAME = IRI(Prefix.OBE, 'curriculumName')
KKNI = IRI(Prefix.OBE, 'kkni')
PLO_PART_OF_PEO = IRI(Prefix.OBE, 'ploPartOfPeo')
HAS_DOMAIN = IRI(Prefix.OBE, 'hasDomain')