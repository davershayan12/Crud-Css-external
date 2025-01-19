from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/collaboration')
def collaboration():
    return render_template('colaboration.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/overvision')
def overvision():
    return render_template('overvision.html')

@app.route('/manageemployee')
def manageemployee():
    return render_template('manageemployee.html')

@app.route('/recruit', methods=['GET', 'POST'])
def recruit():
    if request.method == 'POST':
        # Handle form submission
        name = request.form['name']
        # Process the form data
        return redirect(url_for('index'))
    return render_template('recruit.html')

if __name__ == '__main__':
    app.run(debug=True)