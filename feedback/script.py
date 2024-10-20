from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
from docx  import Document # python-docx for DOCX files
import requests  # for fetching URLs
from bs4 import BeautifulSoup  # for parsing URLs (web pages)
import PyPDF2
import json
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

KB_FILE = 'knowledge_base.json'

# Function to check if a file is allowed (based on extension)
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to parse TXT
def parse_txt(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def update_knowledge_base(header, text):
    timestamp = datetime.now().isoformat()
    new_entry = {
        "header": header,
        "text": text,
        "timestamp": timestamp
    }

    if os.path.exists(KB_FILE):
        with open(KB_FILE, 'r', encoding='utf-8') as kb_file:
            knowledge_base = json.load(kb_file)
    else:
        knowledge_base = []

    knowledge_base.append(new_entry)

    with open(KB_FILE, 'w', encoding='utf-8') as kb_file:
        json.dump(knowledge_base, kb_file, ensure_ascii=False, indent=4)

# Function to parse a URL
def parse_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the title of the web page
        title = soup.title.string if soup.title else "No title"

        # Extract the visible text from the page
        for script in soup(["script", "style"]):  # Remove JavaScript and CSS styles
            script.extract()

        # Get text and strip extra spaces
        text = ' '.join(soup.stripped_strings)
        return {"header": title, "text": text}

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Route for rendering the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file uploads and parsing
@app.route('/upload_doc', methods=['POST'])
def upload_doc():
    # Check if the request has a file part
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    # Check if a file was uploaded and if it's allowed
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Parse the document based on its type
        file_extension = filename.rsplit('.', 1)[1].lower()
        if file_extension == 'txt':
            parsed_content = parse_txt(file_path)
        else:
            return jsonify({"error": "Unsupported file format"}), 400

        update_knowledge_base(filename, parsed_content)
        # Return the extracted content as JSON
        return jsonify({"header": filename, "text": parsed_content})

    else:
        return jsonify({"error": "Invalid file type"}), 400

# Route to handle URL parsing
@app.route('/parse_url', methods=['POST'])
def parse_url_request():
    # Get the URL from the form data (or JSON request)
    url = request.form.get('url') or request.json.get('url')

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    # Parse the URL and return the result
    parsed_data = parse_url(url)

    update_knowledge_base(parsed_data['header'], parsed_data['text'])
    return jsonify(parsed_data)

if __name__ == '__main__':
    app.run(debug=True)
