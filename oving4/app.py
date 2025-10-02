from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''<h2>Welcome to the CTF Challenge!</h2>
    <form method="POST" action="/greet">
        Name: <input name="name">
        <input type="submit" value="Greet">
    </form>'''

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name', '')
    # VULNERABLE: User input is rendered directly in the template
    template = f"""<h2>Hello, {name}!</h2>"""
    return render_template_string(template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
