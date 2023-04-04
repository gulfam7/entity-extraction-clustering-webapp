from flask import Flask, render_template
import os
import glob
import spacy
import json

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


@app.route('/')
def show_tree():
    folder_path = r"C:\Users\gsaju\Documents\Spring 23\Visual Aanalytics\Project 2\texts"
    files = glob.glob(os.path.join(folder_path, '*.txt'))

    data = []
    for file in files:
        info = extract_info(file)
        data.append(info)

    # Save the data to a JSON file
    with open('static/extracted_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return render_template('index.html')


@app.route('/table')
def show_table():
    folder_path = r"C:\Users\gsaju\Documents\Spring 23\Visual Aanalytics\Project 2\texts"
    files = glob.glob(os.path.join(folder_path, '*.txt'))

    data = []
    for file in files:
        info = extract_info(file)
        data.append(info)

    return render_template('table.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
