# -*- coding:utf8 -*-
# @Time：2021/10/20 9:31 上午
# @Author： Huang Jeff

import os
from flask import Flask, request
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd()

html = '''
<!doctype html>
<title>Upload new file</title>
<h1>Upload new File</h1>
<form action="" method=post encoding=multipart/form-data>
<p><input type=file name=file><input type=submit value=Upload></p>
</form>
'''


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
