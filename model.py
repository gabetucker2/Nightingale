# imports
import parameters
import functions

import re

# decode priorAuth, patient, and prescriber data from CSV/PDF format to fields
priorAuthInputFields = functions.decodePDF(parameters.priorAuthInputPath)
patientFields = functions.decodeCSV(parameters.patientPath)
prescriberFields = functions.decodeCSV(parameters.prescriberPath)

functions.tryPrintFields(f"{parameters.priorAuthFormName} Original PriorAuth", priorAuthInputFields)
functions.tryPrintFields(parameters.patientName, patientFields)
functions.tryPrintFields(parameters.prescriberName, prescriberFields)

# normalize original priorAuth fields
priorAuthOutputFields = functions.decodePDF(parameters.priorAuthInputPath)
priorAuthOutputFieldsNormalized = functions.decodePDF(parameters.priorAuthInputPath)

for PAKey in priorAuthOutputFields.keys():
    
    # * normalize key names (remove special characters)
    oldKey = PAKey
    newKey = re.sub(r'[^a-zA-Z# ]', '', PAKey)
    functions.replaceKey(priorAuthOutputFieldsNormalized, oldKey, newKey)

    # * tokenize (word1-word2)
    oldKey = newKey
    newKey = re.sub(r'[ ]', '-', newKey)
    functions.replaceKey(priorAuthOutputFieldsNormalized, oldKey, newKey)
    
    # * lowercase
    oldKey = newKey
    newKey = newKey.lower()
    functions.replaceKey(priorAuthOutputFieldsNormalized, oldKey, newKey)

functions.tryPrintFields(f"{parameters.priorAuthFormName} Updated PriorAuth", priorAuthOutputFieldsNormalized)

# * similarity measurement with threshold to match patient/prescriber field keys to priorAuth field keys
similarity_threshold = 0.995

new_field_representation = {}

for PAKey in priorAuthOutputFields.keys():
    most_similar_patient_key, patient_similarity = functions.find_most_similar_key(PAKey, patientFields)
    most_similar_prescriber_key, prescriber_similarity = functions.find_most_similar_key(PAKey, prescriberFields)

    # If the similarity is above the threshold, add it to the new representation
    if patient_similarity < similarity_threshold and prescriber_similarity < similarity_threshold:
        new_field_representation[PAKey] = (None, None)
    elif patient_similarity > prescriber_similarity:
        new_field_representation[PAKey] = ('patient', f"{most_similar_patient_key}, {patient_similarity}")
    elif patient_similarity < prescriber_similarity:
        new_field_representation[PAKey] = ('prescriber', f"{most_similar_prescriber_key}, {prescriber_similarity}")

functions.tryPrintFields(f"{parameters.priorAuthFormName} PriorAuth Match", new_field_representation)

# encode updated priorAuth form

