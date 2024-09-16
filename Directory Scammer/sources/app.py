from flask import Flask, request, render_template_string, render_template
import sqlite3
import os

app = Flask(__name__)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error=error), 500

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    user_greeting = None
    if request.method == 'POST':
        #username = request.form['username']
        #password = request.form['password']
        #conn = None
        #try:    
        #    query = f"SELECT username, description FROM users WHERE username = '{username}' AND password = '{password}'"
        #    conn = sqlite3.connect('users.db')
        #    cursor = conn.cursor()
        #    cursor.execute(query)
        #    user = cursor.fetchall()
        #    if not user:
        #        return render_template('login.html', error="Неверное имя пользователя или пароль")
        #    user_greeting = f"Добро пожаловать, {user}!\n"
        #    return render_template('login.html', user=user_greeting)
        #except Exception as error:
            return render_template('login.html', error=error)
        #finally:
        #    conn.close()
    return render_template("login.html")
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dbadmin')
def config():
    flag='FLAG{TiilS:Fr1dge_PaTh}'
    return render_template("dbadmin.html", flag={os.environ.get('FLAGPATH', "FLAG is not set")})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=0)
    
