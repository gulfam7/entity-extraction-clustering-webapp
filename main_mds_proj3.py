import numpy as np
from flask import Flask, render_template
import glob
import os
import spacy
import json
import pandas as pd
from sklearn.manifold import MDS
from sklearn.metrics import pairwise_distances
from sklearn.preprocessing import MinMaxScaler

def create_document_entity_matrix(data):
    # Initialize a list to store the entities count for each document
    entities_count = []

    for doc in data:
        names_count = len(doc['names'])
        locations_count = len(doc['locations'])
        dates_count = len(doc['dates'])
        orgs_count = len(doc['orgs'])

        entities_count.append([names_count, locations_count, dates_count, orgs_count])

    # Convert the list to a NumPy array and return it
    return np.array(entities_count)

def apply_mds(matrix, n_components=2):
    # Scale the matrix
    scaler = MinMaxScaler()
    scaled_matrix = scaler.fit_transform(matrix)

    # Calculate the pairwise dissimilarity matrix
    dissimilarity_matrix = pairwise_distances(scaled_matrix, metric='euclidean')

    # Apply classical MDS
    mds = MDS(n_components=n_components, dissimilarity='precomputed', random_state=42)
    mds_coordinates = mds.fit_transform(dissimilarity_matrix)

    return mds_coordinates

app = Flask(__name__)

# Load Spacy NLP model
nlp = spacy.load('en_core_web_sm')

def extract_info(file):
    with open(file, 'r') as f:
        text = f.read()
        doc = nlp(text)

        names = list(set(ent.text for ent in doc.ents if ent.label_ == 'PERSON'))
        locations = list(set(ent.text for ent in doc.ents if ent.label_ == 'GPE'))
        dates = list(set(ent.text for ent in doc.ents if ent.label_ == 'DATE'))
        orgs = list(set(ent.text for ent in doc.ents if ent.label_ == 'ORG'))

        file_name = os.path.splitext(os.path.basename(file))[0]

        extracted_data = {
            'file': file_name,
            'names': names,
            'locations': locations,
            'dates': dates,
            'orgs': orgs
        }

        return extracted_data




if __name__ == '__main__':
    app.run(debug=True)


# In your show_tree() or show_table() function, after extracting the data from the files:
data_matrix = create_document_entity_matrix(data)
mds_coordinates = apply_mds(data_matrix)

# Pass the MDS coordinates to the template, e.g., for the show_table() function:
return render_template('table.html', data=data, mds_coordinates=mds_coordinates)
