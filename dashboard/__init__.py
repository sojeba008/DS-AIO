from flask import Flask, render_template, request
import uuid
#from werkzeug import secure_filename
app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
def index():
    return render_template('init.html')


@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/page/')
def page():
    return render_template('template.html')



@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save('uploads/'+(f.filename))
      return 'file uploaded successfully. Your ID is '+str(uuid.uuid4())
if __name__ == "__main__":
        app.run()
