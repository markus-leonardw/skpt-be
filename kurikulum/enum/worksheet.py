from enum import Enum

# Define an enumeration class
class Worksheet(Enum):
    CLO = 'Course Learning Outcome'
    CONTENT = 'Content'
    COURSE = 'Course'
    CURRICULUM = 'Curriculum'
    PEO = 'Program Educational Objective'
    PLO = 'Program Learning Outcome'
    SPLO = 'Subprogram Learning Outcome'
    STUDYPROGRAM = 'Study Program'
    PLOPEO = 'Padanan PLO dengan PEO'
    PLODOMAIN = 'Padanan PLO dengan domain'
    SPLODOMAIN = 'Padanan SubPLO dengan domain'
    CLODOMAIN = 'Padanan CLO dan Domain'
    CLOPLO = 'Padanana CLO dengan PLO'
    CLOSPLO = 'Padanan CLO dengan SubPLO'

    LEARNINGDOMAIN = 'Learning Domain'
    COUNT = 'Sheet8'
    