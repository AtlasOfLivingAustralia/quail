from qgis.PyQt.QtCore import QVariant

"""
/*****************
Tick box values
*****************/
"""
# Authoritative lists of threatened species available in the ALA
threatenedLists = {
    "ACT": "dr649",
    "EPBC": "dr656",
    "NSW": "dr650",
    "NT": "dr651",
    "QLD": "dr652",
    "SA": "dr653",
    "TAS": "dr654",
    "VIC": "dr655",
    "WA": "dr2201",
}

# Authoritative lists of sensitive species available in the ALA
sensitiveLists = {
    "ACT": "dr2627",
    "NSW": "dr487",
    "NT": "dr492",
    "QLD": "dr493",
    "SA": "dr884",
    "TAS": "dr491",
    "VIC": "dr490",
    "WA": "dr467",
}

# Authoritative lists of migratory species available in the ALA
migratoryLists = {
    "Bonn": "dr18987",
    "CAMBA": "dr18989",
    "JAMBA": "dr18988",
    "ROKAMBA": "dr18990",
}

# Authoritative lists of non-native species available in the ALA
nonNativeLists = {"NonNative All": "dr32213"}

"""
/*****************
Attribute values
*****************/
"""

# declare dictionary of all possible attributes to add to the layer
attributes_dict = {
    "decimalLatitude": QVariant.Double,
    "decimalLongitude": QVariant.Double,
    "eventDate": QVariant.String,
    "scientificName": QVariant.String,
    "taxonConceptID": QVariant.String,
    "recordID": QVariant.String,
    "dataResourceName": QVariant.String,
    "occurrenceStatus": QVariant.String,
    "dataProviderName": QVariant.String,
    "stateConservation": QVariant.String,
    "countryConservation": QVariant.String,
}
