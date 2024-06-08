from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb+srv://antonyank36:Hunisi5@cluster0.vlmwoxw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.testdb
collection = db.users

@app.before_first_request
def create_tables():
    if collection.count_documents({}) == 0:
        # Initialize table data
        for i in range(14):
            collection.insert_one({
                'row': i,
                'col1': f'Row {i+1} Col 1',
                'col2': f'Row {i+1} Col 2',
                'col3': f'Row {i+1} Col 3'
            })
        print('yes')
@app.route('/')
def main():
    return render_template('main.html')

@app.route('/index')
def index():
    table_data = list(collection.find({}, {'_id': 0}).sort('row', 1))  # Exclude MongoDB's default _id field
    return render_template('index.html', table_data=table_data)

@app.route('/edit', methods=['POST'])
def edit():
    for i in range(14):
        collection.update_one(
            {'row': i},
            {'$set': {
                'col1': request.form.get(f'row{i}_col0'),
                'col2': request.form.get(f'row{i}_col1'),
                'col3': request.form.get(f'row{i}_col2')
            }}
        )
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

