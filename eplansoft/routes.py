import os
from flask import render_template, request
from werkzeug.utils import secure_filename
from eplansoft import app

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        file = request.files["file-input"]
        file_size = len(file.read())

        file_description = {
            "file_name": file.filename,
            "file_type": file.content_type,
            "file_size": f"{file_size} bytes"
        }

        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return render_template("index.html", file_description=file_description)

    file_description = {
        "file_name": "No name entered",
        "file_type": "No file submitted",
        "file_size": "No file submitted"
    }

    return render_template("index.html", file_description=file_description)
