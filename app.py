from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

def read_data(filename):
    with open(filename, 'r', encoding="utf_8") as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def write_data(data, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

@app.route("/index")
def index():
    return render_template("/index.html")

@app.route('/submit', methods=['POST'])
def submit():
    ratings = []
    for i in range(1, len(data) + 1):
        rating = request.form.get('rating' + str(i))
        if rating:
            ratings.append(int(rating))
        else:
            ratings.append(0)
    for i in range(len(data)):
        data[i].append(ratings[i])
    write_data(data, 'data.csv')
    return redirect('/thanks')

if __name__ == '__main__':
    data = read_data('text.csv')
    app.run()

