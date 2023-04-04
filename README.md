# entity-extraction-clustering-webapp
Clustering Visualization
This is a web-based tool for visualizing clusters of entities extracted from text files. It uses the Spacy NLP library to identify and extract person names, locations, dates, and organizations from a set of text files, and then displays the relationships between these entities in an interactive network graph.

Features
Entity extraction: The tool extracts entities from a set of text files using the Spacy NLP library, including person names, locations, dates, and organizations.
Clustering visualization: The extracted entities are clustered based on their co-occurrence patterns in the text files, and the resulting clusters are visualized as nodes in a network graph.
Interactive network graph: The network graph is fully interactive, allowing the user to zoom in and out, drag nodes around, and filter the display by entity type.
File metadata: The tool also displays metadata for each file, including its name and the entities extracted from it.
Usage
To use the tool, simply run the Flask web app and navigate to the home page. From there, you can view the extracted data in a table or as a network graph.

Installation
Clone the repository:
bash
Copy code
git clone https://github.com/[username]/clustering-visualization.git
Install the dependencies:
Copy code
pip install -r requirements.txt
Run the Flask app:
Copy code
python app.py
Navigate to http://localhost:5000/ in your web browser to view the tool.
Configuration
The tool is designed to work with a set of text files located in a specific directory. By default, the tool looks for files in the texts directory, but you can change this by modifying the folder_path variable in app.py.

License
This tool is released under the MIT License. See LICENSE for details.

Credits
This tool was created by Gulfam Ahmed Saju. It uses the Spacy NLP library for entity extraction and the Vis.js library for network graph visualization.
