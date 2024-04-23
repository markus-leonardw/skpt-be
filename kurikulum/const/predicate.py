from kurikulum.enum.prefix import Prefix
from kurikulum.utils.mapper.IRI import IRI

# common
TYPE = IRI(Prefix.RDF, 'type')
DESCRIPTION = IRI(Prefix.OBE, 'description')

# study program
SP_NAME = IRI(Prefix.OBE, 'spName')
FAKULTAS = IRI(Prefix.OBE, 'faculty')
VISI = IRI(Prefix.OBE, 'vision')
MISI = IRI(Prefix.OBE, 'mission')
TUJUAN = IRI(Prefix.OBE, 'objective')

# curriculum
BELONGS_TO_SP = IRI(Prefix.OBE, 'belongsToSP')
CURRICULUM_NAME = IRI(Prefix.OBE, 'curriculumName')

# program educational objective
BELONGS_TO_CURR = IRI(Prefix.OBE, 'belongsToCurr')

# peo & plo
KKNI_RESPONIBILITY = IRI(Prefix.OBE, 'nqfAuthorityResposibility')
KKNI_KNOWLEDGE = IRI(Prefix.OBE, 'nqfKnowledge')
KKNI_WORKING = IRI(Prefix.OBE, 'nqfWorkingSkill')
SNDIKTI_ATTITUDE = IRI(Prefix.OBE, 'nsAttitude')
SNDIKTI_GENERIC = IRI(Prefix.OBE, 'nsGenericSkill')
SNDIKTI_KNOWLEDGE = IRI(Prefix.OBE, 'nsKnowledge')
SNDIKTI_SPECIFIC = IRI(Prefix.OBE, 'nsSpecificSkill')

# program learning outcome
PLO_PART_OF_PEO = IRI(Prefix.OBE, 'ploPartOfPeo')

# subprogram learning outcome
SPLO_PART_OF_PLO = IRI(Prefix.OBE, 'sploPartOfPlo')

# course learning outcome
CRITERIA = IRI(Prefix.OBE, 'Criteria')
CLO_PART_OF_PLO = IRI(Prefix.OBE, 'cloPartOfPlo')
CLO_PART_OF_SPLO = IRI(Prefix.OBE, 'cloPartOfSplo')
HAS_CONTENT = IRI(Prefix.OBE, 'hasContent')

# Content
HAS_KNOW_CAT = IRI(Prefix.OBE, 'hasKnownCat')

# Course
HAS_CLO = IRI(Prefix.OBE, 'hasCLO')

CODE = IRI(Prefix.OBE, 'code')
HAS_DOMAIN = IRI(Prefix.OBE, 'hasDomain')