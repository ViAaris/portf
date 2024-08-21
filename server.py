from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/submit_form', methods=['GET', 'POST'])
def write_to_csv():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "did not save to csv"
    else:
        return 'something is wrong'


def write_to_csv(data):
    with open('database.csv', newline='\n', mode='a') as database:
        data_to_csv = []
        csv_writer = csv.writer(database, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        for d in data:
            data_to_csv.append(data[d].strip('\n'))
        csv_writer.writerow(data_to_csv)


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/')
def hello():
    return render_template('index.html')

#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
