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

# taxon selections
taxon_selections = [
    "scientificName",
    "kingdom",
    "phylum",
    "class",
    "order",
    "family",
    "genus",
    "vernacularName",
]

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
    "latitude": QVariant.Double,
    "longitude": QVariant.Double,
    "occurrence_date": QVariant.String,
    "taxon_name": QVariant.String,
    "taxon_concept_lsid": QVariant.String,
    "id": QVariant.String,
    "data_resource": QVariant.String,
    "occurrence_status": QVariant.String,
    "data_provider": QVariant.String,
    "gbifID": QVariant.String,
    "datasetKey": QVariant.String,
    "occurrenceID": QVariant.String,
    "kingdom": QVariant.String,
    "phylum": QVariant.String,
    "class": QVariant.String,
    "order": QVariant.String,
    "family": QVariant.String,
    "genus": QVariant.String,
    "species": QVariant.String,
    "infraspecificEpithet": QVariant.String,
    "taxonRank": QVariant.String,
    "verbatimScientificName": QVariant.String,
    "verbatimScientificNameAuthorship": QVariant.String,
    "countryCode": QVariant.String,
    "locality": QVariant.String,
    "stateProvince": QVariant.String,
    "individualCount": QVariant.String,
    "publishingOrgKey": QVariant.String,
    "coordinateUncertaintyInMeters": QVariant.String,
    "coordinatePrecision": QVariant.String,
    "elevation": QVariant.String,
    "elevationAccuracy": QVariant.String,
    "depth": QVariant.String,
    "depthAccuracy": QVariant.String,
    "day": QVariant.String,
    "month": QVariant.String,
    "year": QVariant.String,
    "taxonKey": QVariant.String,
    "speciesKey": QVariant.String,
    "basisOfRecord": QVariant.String,
    "institutionCode": QVariant.String,
    "collectionCode": QVariant.String,
    "catalogNumber": QVariant.String,
    "recordNumber": QVariant.String,
    "identifiedBy": QVariant.String,
    "dateIdentified": QVariant.String,
    "license": QVariant.String,
    "rightsHolder": QVariant.String,
    "recordedBy": QVariant.String,
    "typeStatus": QVariant.String,
    "establishmentMeans": QVariant.String,
    "lastInterpreted": QVariant.String,
    "mediaType": QVariant.String,
    "issue": QVariant.String,
}

"""
/**********************************
Lat/long values for each atlas
**********************************/
"""
latitude_dict = {
    "Australia": "decimalLatitude",
    "Austria": "decimalLatitude", #"latitude",
    "Brazil": "latitude",
    "France": "latitude",
    "Flanders": "decimalLatitude",
    "Global": "decimalLatitude",
    "Guatemala": "latitude",
    "Kew": "decimalLatitude",
    "Spain": "decimalLatitude",
    "Sweden": "decimalLatitude",
    "United Kingdom": "decimalLatitude",
}

longitude_dict = {
    "Australia": "decimalLongitude",
    "Austria": "decimalLongitude", #"longitude",
    "Brazil": "longitude",
    "Flanders": "decimalLongitude",
    "Global": "decimalLongitude",
    "Kew": "decimalLongitude",
    "Spain": "decimalLongitude",
    "Sweden": "decimalLongitude",
    "United Kingdom": "decimalLongitude",
}

eventdate_dict = {
    "Australia": "eventDate",
    "Austria": "occurrence_date",
    "Brazil": "occurrence_date",
    "Flanders": "eventDate",
    "Global": "eventDate",
    "Kew": "eventDate",
    "Spain": "eventDate",
    "Sweden": "eventDate",
    "United Kingdom": "eventDate",
}

bor_dict = {
    "Australia": "basisOfRecord",
    "Austria": "basis_of_record",
    "Brazil": "basis_of_record",
    "Flanders": "basisOfRecord",
    "Global": "basisOfRecord",
    "Kew": "basisOfRecord",
    "Spain": "basisOfRecord",
    "Sweden": "basisOfRecord",
    "United Kingdom": "basisOfRecord",
}

occstatus_dict = {
    "Australia": "occurrenceStatus",
    "Austria": "occurrence_status",
    "Brazil": "occurrence_status",
    "Flanders": "occurrenceStatus",
    "Global": "occurrenceStatus",
    "Kew": "occurrenceStatus",
    "Spain": "occurrenceStatus",
    "Sweden": "occurrenceStatus",
    "United Kingdom": "occurrenceStatus",
}

occ_fields = {
    "Australia": ["basic", "dataProviderName", "stateConservation", "countryConservation"],
    "Austria": ["basic","data_resource","data_provider"], 
    "Brazil": [
        "latitude",
        "longitude",
        "occurrence_date",
        "taxon_name",
        "taxon_concept_lsid",
        "id",
        "data_resource",
        "occurrence_status",
        "data_provider",
    ],
    "Flanders": ["basic", "dataProviderName", "stateConservation", "countryConservation"],
    "Global": ["basic"],
    "Kew": ["basic"],
    "Spain": ["basic", "dataProviderName", "stateConservation", "countryConservation"],
    "Sweden": ["basic", "dataProviderName"],
    "United Kingdom": ["basic", "dataProviderName", "stateConservation", "countryConservation"],
}

taxon_fields_dict = {
    "Australia": taxon_selections + ["identifiers"],
    "Austria": [
        "taxon_name",
        "kingdom",
        "phylum",
        "class",
        "order",
        "family",
        "genus",
        "common_name",
    ],
    "Brazil": [
        "taxon_name",
        "kingdom",
        "phylum",
        "class",
        "order",
        "family",
        "genus",
        "common_name",
    ],
    "Flanders": taxon_selections,
    "Global": taxon_selections,
    "Kew": taxon_selections,
    "Spain": taxon_selections,
    "Sweden": taxon_selections,
    "United Kingdom": taxon_selections,
}