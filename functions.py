# imports
import parameters

import csv
import pdfrw

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
                    field_name = subfield.T[1:-1] if subfield.T else None
                    field_value = subfield.V[1:-1] if subfield.V else None
                    form_data[field_name] = field_value
            else:  # For fields that don't have children
                field_name = field.T[1:-1] if field.T else None
                field_value = field.V[1:-1] if field.V else None
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

from transformers import BertTokenizer, BertModel
import torch
import numpy as np

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)
    outputs = model(**inputs)
    return outputs.pooler_output[0]

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def find_most_similar_key(target_key, comparison_dict):
    target_embedding = get_embedding(target_key).detach().numpy()
    highest_similarity = -1
    most_similar_key = None

    for key in comparison_dict.keys():
        key_embedding = get_embedding(key).detach().numpy()
        similarity = cosine_similarity(target_embedding, key_embedding)
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_key = key

    return most_similar_key, highest_similarity
