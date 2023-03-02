from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

def read_data(filename):
    with open(filename, 'r', encoding="utf_8") as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

@app.route("/")
def index():
    return render_template("index.html", data=text)

@app.route("/thanks", methods=["GET"])
def nextpage():
    return render_template("thanks.html")

@app.route('/submit', methods=['POST'])
def submit():
    ratings = []
    for i in range(1, len(text)+1):
        rating = request.form.get('rating' + str(i))
        if rating:
            ratings.append(int(rating))
        else:
            ratings.append(0)
    with open("data.csv", 'a+',  encoding='utf_8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows([ratings])
    return redirect('/thanks')

if __name__ == '__main__':
    text = read_data('sen.csv')
    app.run()

