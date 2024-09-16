from flask import Flask, request, render_template
import os, subprocess
app = Flask(__name__)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Шаблон HTML для вывода списка файлов

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        path = request.form['path']
        result = os.popen("ls " + path).read().strip()
        html = render_template("index.html", items=result)
        return html
    
    return render_template("index.html", items='')


if __name__ == '__main__':
    app.run(host='0.0.0.0')

