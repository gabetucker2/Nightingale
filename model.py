# imports
import parameters
import functions

import re

# decode priorAuth, patient, and prescriber data from CSV/PDF format to fields
priorAuthInputFields = functions.decodePDF(parameters.priorAuthInputPath)
patientFields = functions.decodeCSV(parameters.patientPath, parameters.patientRow)
prescriberFields = functions.decodeCSV(parameters.prescriberPath, parameters.prescriberRow)

functions.tryPrintFields(f"{parameters.priorAuthFormName} Original PriorAuth", priorAuthInputFields)
functions.tryPrintFields(f"Patient {parameters.patientRow}", patientFields)
functions.tryPrintFields(f"Prescriber {parameters.prescriberRow}", prescriberFields)

# normalize original priorAuth fields
priorAuthOutputFields = functions.decodePDF(parameters.priorAuthInputPath)
priorAuthOutputFieldsNormalized1 = {}

# * normalize strings
for PAKey in priorAuthOutputFields.keys():

    if not PAKey:
        PAKey = "None"

    # * normalize key names (remove special characters)
    oldKey = PAKey
    newKey = re.sub(r'[^a-zA-Z0-9# ]', '', PAKey)
    priorAuthOutputFieldsNormalized1[newKey] = ''

    # * tokenize (word1-word2)
    oldKey = newKey
    newKey = re.sub(r'[ ]', '-', newKey)
    priorAuthOutputFieldsNormalized1[newKey] = ''
    
    # * lowercase
    oldKey = newKey
    newKey = newKey.lower()
    priorAuthOutputFieldsNormalized1[newKey] = ''

# functions.tryPrintFields(f"{parameters.priorAuthFormName} Updated PriorAuth", priorAuthOutputFieldsNormalized1)

# * ensure there are no irrelevant terms like 'undefined' encoded
priorAuthOutputFieldsNormalized2 = dict(priorAuthOutputFieldsNormalized1)

for PAKey in priorAuthOutputFieldsNormalized1.keys():

    if any(term in PAKey.lower() for term in parameters.priorAuthTermBlacklist):
        
        priorAuthOutputFieldsNormalized2.pop(PAKey)


functions.tryPrintFields(f"{parameters.priorAuthFormName} Updated PriorAuth", priorAuthOutputFieldsNormalized2)

new_field_representation = {}

# ! using a hardcoded (bad) tentative method

for PAKey in priorAuthOutputFieldsNormalized2.keys():
    new_field_representation[PAKey] = functions.hardMatchPAKey(PAKey, patientFields, prescriberFields)

# ! using the procedural method BERT (which apparently doesn't work well)

# * similarity measurement with threshold to match patient/prescriber field keys to priorAuth field keys
# similarity_threshold = 0.99

# for PAKey in priorAuthOutputFieldsNormalized.keys():
#     most_similar_patient_key, patient_similarity = functions.find_most_similar_key(PAKey, patientFields)
#     most_similar_prescriber_key, prescriber_similarity = functions.find_most_similar_key(PAKey, prescriberFields)

#     # If the similarity is above the threshold, add it to the new representation
#     if patient_similarity < similarity_threshold and prescriber_similarity < similarity_threshold:
#         new_field_representation[PAKey] = (None, None)
#     elif patient_similarity > prescriber_similarity:
#         new_field_representation[PAKey] = ('patient', f"{most_similar_patient_key}, {patient_similarity}")
#     elif patient_similarity < prescriber_similarity:
#         new_field_representation[PAKey] = ('prescriber', f"{most_similar_prescriber_key}, {prescriber_similarity}")
    
functions.tryPrintFields(f"{parameters.priorAuthFormName} PriorAuth Match", new_field_representation)

# Create a mapping from original keys to transformed keys
original_to_transformed_key_map = {}

for original_key in priorAuthOutputFields.keys():
    
    if not original_key:
        original_key = "None"

    # Apply the same transformations that were used in the script
    transformed_key = re.sub(r'[^a-zA-Z0-9# ]', '', original_key)  # Remove special characters
    transformed_key = re.sub(r'[ ]', '-', transformed_key)       # Replace spaces with hyphens
    transformed_key = transformed_key.lower()                    # Convert to lowercase

    # Check if the transformed key is in the final new_field_representation (i.e., it wasn't removed)
    if transformed_key in new_field_representation:
        original_to_transformed_key_map[original_key] = transformed_key

functions.tryPrintFields("Original-Transformed Key Mapping", original_to_transformed_key_map)

# encode updated priorAuth fields into new PDF

functions.create_updated_pdf(parameters.priorAuthInputPath, new_field_representation, original_to_transformed_key_map, f"{parameters.outputPath}{parameters.outputName}.pdf")
