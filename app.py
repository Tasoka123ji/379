from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

table_data = [[f'Row {i+1} Col {j+1}' for j in range(3)] for i in range(14)]

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/index')
def index():
    return render_template('index.html', table_data=table_data)

@app.route('/edit', methods=['POST'])
def edit():
    global table_data
    for i in range(14):
        table_data[i][0] = request.form.get(f'row{i}_col0')
        table_data[i][1] = request.form.get(f'row{i}_col1')
        table_data[i][2] = request.form.get(f'row{i}_col2')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
