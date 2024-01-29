from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_table', methods=['POST'])
def generate_table():
    try:
        number = int(request.form['number'])
        table_data = [(i, number * i) for i in range(1, 21)]
        return render_template('table.html', number=number, table_data=table_data)
    except ValueError:
        return render_template('error.html', message='Please enter a valid number.')

if __name__ == '__main__':
    app.run(debug=True)
    