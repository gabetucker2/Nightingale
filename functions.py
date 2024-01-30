# imports
import parameters

import csv
import pdfrw
from transformers import BertTokenizer, BertModel
import torch
import numpy as np
from datetime import datetime

# functions
def replaceKey(dict, oldKey, newKey):
    dict[newKey] = dict.pop(oldKey)

def tryPrint(m):
    if parameters.consoleLogs:
        print(m)

def tryPrintFields(name, fields):
    if parameters.consoleLogs:
        print(f"------------------------------------------ {name} Data ------------------------------------------")
        for field, value in fields.items():
            print(f"-- {field}: {value}")

def decodePDF(filePath):
    form_data = {}
    pdf = pdfrw.PdfReader(filePath)

    # Check if the PDF has AcroForm (interactive form)
    if pdf.Root.AcroForm:
        for field in pdf.Root.AcroForm.Fields:
            if field.Kids:  # For fields that have children
                for subfield in field.Kids:
                    field_name = subfield.T if subfield.T else None
                    field_value = None # subfield.V[1:-1] if subfield.V else None # only strip parens from values
                    form_data[field_name] = field_value
            else:  # For fields that don't have children
                field_name = field.T if field.T else None
                field_value = None # field.V[1:-1] if subfield.V else None # only strip parens from values
                form_data[field_name] = field_value

    return form_data

def decodeCSV(filePath):
    with open(filePath, newline='') as csvfile:
        # Read the CSV file
        reader = csv.reader(csvfile)
        
        # Extract the rows
        rows = list(reader)
        
        # Check if there are at least two rows
        if len(rows) < 2:
            raise ValueError("CSV file must have at least two rows")
        
        # First row for keys, second row for values
        keys = rows[0]
        values = rows[1]

        # Combine keys and values into a dictionary
        form_data = dict(zip(keys, values))

        return form_data

def hardMatchPAKey(PAKey, patientFields, prescriberFields):
    
    if PAKey == 'date':
        return datetime.now().strftime("%Y-%m-%d")
    elif PAKey in parameters.hardMatchPatient.keys():
        return patientFields[parameters.hardMatchPatient[PAKey]]
    elif PAKey in parameters.hardMatchPrescriber.keys():
        return prescriberFields[parameters.hardMatchPrescriber[PAKey]]
    
def create_updated_pdf(input_pdf_path, updated_fields, original_to_transformed_key_map, output_pdf_path):
    # Load the PDF template
    template = pdfrw.PdfReader(input_pdf_path)
    print("PDF template loaded.")

    # Print all field names in the PDF
    print("All field names in the PDF:")
    for page in template.pages:
        annotations = page.get('/Annots')
        if annotations is not None:
            for annotation in annotations:
                if annotation.get('/T') is not None:
                    print(annotation.get('/T'))

    # Prepare a reverse mapping from transformed keys to original keys
    transformed_to_original_key_map = {v: k for k, v in original_to_transformed_key_map.items()}

    # Update the fields with the new values
    for transformed_key, field_value in updated_fields.items():
        if field_value is not None and transformed_key in transformed_to_original_key_map:
            original_key = transformed_to_original_key_map[transformed_key]
            print(f"Attempting to update field: {original_key} with value: {field_value}")

            field_found = False
            for page in template.pages:
                annotations = page.get('/Annots')
                if annotations is None:
                    continue
                for annotation in annotations:
                    if annotation.get('/T') == original_key:
                        annotation.update(pdfrw.PdfDict(V=field_value))
                        field_found = True
                        print(f"Field {original_key} updated.")
                        break

            if not field_found:
                print(f"Field {original_key} not found or not updated.")

    # Save the filled out PDF
    pdfrw.PdfWriter().write(output_pdf_path, template)
    print(f"PDF saved to {output_pdf_path}")

# tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
# model = BertModel.from_pretrained('bert-base-uncased')

# def get_embedding(text):
#     inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)
#     outputs = model(**inputs)
#     return outputs.pooler_output[0]

# def cosine_similarity(vec1, vec2):
#     return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# def find_most_similar_key(target_key, comparison_dict):
#     target_embedding = get_embedding(target_key).detach().numpy()
#     highest_similarity = -1
#     most_similar_key = None

#     for key in comparison_dict.keys():
#         key_embedding = get_embedding(key).detach().numpy()
#         similarity = cosine_similarity(target_embedding, key_embedding)
#         if similarity > highest_similarity:
#             highest_similarity = similarity
#             most_similar_key = key

#     return most_similar_key, highest_similarity
