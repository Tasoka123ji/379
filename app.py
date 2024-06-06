from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

def read_table_data():
    try:
        df = pd.read_csv('data.csv')
        return df.values.tolist()
    except FileNotFoundError:
        print('no')
        return [[f'Row {i+1} Col {j+1}' for j in range(3)] for i in range(14)]

def write_table_data(data):
    df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3'])
    df.to_csv('data.csv', index=False)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/index')
def index():
    table_data = read_table_data()
    return render_template('index.html', table_data=table_data)

@app.route('/edit', methods=['POST'])
def edit():
    table_data = []
    for i in range(14):
        row = [
            request.form.get(f'row{i}_col0'),
            request.form.get(f'row{i}_col1'),
            request.form.get(f'row{i}_col2')
        ]
        table_data.append(row)
    write_table_data(table_data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
