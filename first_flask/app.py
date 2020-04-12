from flask import *
from invertBinary import rotateBinary

app = Flask(__name__)

@app.route("/")
def upload():
    return render_template("fileUpload.html")

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        return render_template("success.html", name = f.filename) 
        rotateBinary(f.filename, "r") 

if __name__ == "__main__":
    app.run()