from flask import Flask, render_template, redirect, url_for, send_from_directory
from main import create_dict, parse_document
app = Flask(__name__)

def create_generation(names):
    pairings = create_dict(names, names.copy())
    print(pairings)
    return pairings

test = parse_document()
print(test)

#names = ['Chris', 'Alyssa', 'Aidan', 'Summer', "Miguel", "Alex", "Caesar"]
#pairings = create_generation(names)

@app.route('/')
def hello_world():
    names = ['Chris', 'Alyssa', 'Aidan', 'Summer', "Miguel", "Alex", "Caesar"]
    return render_template('index.html', names=names)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/generate')
def generate_new():
    global test
    names = ['Chris', 'Alyssa', 'Aidan', 'Summer', "Miguel", "Alex", "Caesar"]
    test = create_dict(names, names.copy())
    return redirect('/')

@app.route('/match/<person>')
def find_match(person):
    global test
    return render_template('match.html', person=person.capitalize(), match=test[person.capitalize()])