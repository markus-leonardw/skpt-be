from enum import Enum
from token import STRING

# Define an enumeration class
class Prefix(Enum):
    OBE = "OBE"
    OWL = "owl"
    RDF = "rdf"
    RDFS = "rdfs"
    STRING = "xsd:string"
    