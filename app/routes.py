from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kimaiga'}
    return '''
<html>
    <head>
        <title>Home Page - The Rhapsody</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''