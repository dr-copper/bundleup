import os
import boto3
import pandas
from flask import Flask, flash, render_template, request, redirect, abort, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
#import necessary dictionaries 

#create low level functional client 
client=boto3.client(
    's3',
    aws_access_key_id = 'AKIATMGB4WODG3M6B3B5',
    aws_secret_access_key = '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',
    region_name = 'us-east-1' 
    )

#create high level object oriented interface 
resource = boto3.resource(
    's3',
    aws_access_key_id = 'AKIATMGB4WODG3M6B3B5',
    aws_secret_access_key = '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',
    region_name = 'us-east-1' 
    )

# Fetch the list of existing buckets
clientResponse = client.list_buckets()
    
# Print the bucket names one by one
print('Printing bucket names...')
for bucket in clientResponse['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')

app = Flask(__name__, template_folder='.')
app.config['MAX_CONTENT_LENGTH'] = 26000 * 1024 * 1024 #accept files up to 25GB in size
app.config['UPLOAD EXTENSIONS'] = ['.tgz'] #rejects any non-matching file type
app.config['UPLOAD_PATH'] = os.path.join(os.path.dirname(__file__), 'uploads')

CORS(app, support_credentials=True) #enable CORS for all routes

@app.route("/login")
@cross_origin(support_credentials=True) #sending cookies along the payload back and forth
def login():
    return jsonify({'success': 'ok'})

@app.route('/') 
def index(): #function will accept GET requests
    return render_template('templates/index.html')

def allowed_file(filename):
    print(filename)
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in {'tgz'} #1st layer of filetype validation / procedure A check

def upload_file(file):
    file.save(os.path.join(app.config['UPLOAD_PATH'], file.filename)) #setup upload folder

@app.route('/', methods=['POST'])
def upload_files():
    if 'file' not in request.files:
        flash('No file part')

    file = request.files['user_file'] #get name of uploaded file

    if file.filename != '' and file.filename.endswith('.docx'): #2nd layer of filetype validation / procedure B check
        file_ext = os.path.splitext(file.filename)[1]
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename): # check if filetype is allowed
        print('Hello')
        filename = secure_filename(file.filename) #make filename safe, remove unsupported chars / prevents possible exploit 
        upload_file(file) # file.save(os.path.join(app.config['UPLOAD_PATH'], file.filename)) #setup upload folder
        return redirect(request.url)
    return '', 204 

@app.route('/uploads', methods=['GET'])
def uploads():
    pass
    # return file.

def create_upload_folder():
    print(app.config['UPLOAD_PATH'])
    if not os.path.exists(app.config['UPLOAD_PATH']):
        os.makedirs(app.config['UPLOAD_PATH'])

@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413

if __name__ == "__main__":
    create_upload_folder()
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host='0.0.0.0', port=5000, debug=True)
