from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)
app.secret_key = "Secret Key"

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
        email = request.form['email']
        phone = request.form['phone']
        
        # Write the data to a CSV file
        with open('employees.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, phone])
        
        return redirect(url_for('employees'))
    return render_template('recruit.html')

@app.route('/employees')
def employees():
    employees_list = []
    with open('employees.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            employees_list.append(row)
    return render_template('employees.html', employees=employees_list)

if __name__ == "__main__":
    app.run(debug=True)