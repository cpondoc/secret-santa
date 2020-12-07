from flask import Flask, render_template, redirect, url_for, send_from_directory
from main import create_dict
app = Flask(__name__)

def create_generation(names):
    pairings = create_dict(names, names .copy())
    print(pairings)
    return pairings

names = ['Chris', 'Alyssa', 'Aidan', 'Summer', "Miguel", "Alex", "Caesar"]
pairings = create_generation(names)

@app.route('/')
def hello_world():
    global pairings
    names = ['Chris', 'Alyssa', 'Aidan', 'Summer', "Miguel", "Alex", "Caesar"]
    duplicateNames = names.copy()
    return render_template('index.html', names=duplicateNames)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/generate')
def generate_new():
    global pairings
    names = ['Chris', 'Alyssa', 'Aidan', 'Summer', "Miguel", "Alex", "Caesar"]
    pairings = create_generation(names)
    return redirect('/')

@app.route('/match/<person>')
def find_match(person):
    names = ['Chris', 'Alyssa', 'Aidan', 'Summer', "Miguel", "Alex", "Caesar"]
    return render_template('match.html', person=person.capitalize(), match=pairings[person.capitalize()])