from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://antonyank36:Hunisi5@cluster0.vlmwoxw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.testdb
collection = db.users

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/araqich1')
def index2():
    return render_template('arakich1.html')



# tankers 

@app.route('/tankers')
def index1():
    collection = db.users
    table_data = list(collection.find({}, {'_id': 0}).sort('row', 1))  # Exclude MongoDB's default _id field
    return render_template('tankers.html', table_data=table_data)

@app.route('/edit_tankers', methods=['POST'])
def edit_tankers():
    db = client.testdb
    collection = db.users
    for i in range(14):
        collection.update_one(
            {'row': i},
            {'$set': {
                'col1': request.form.get(f'row{i}_col0'),
                'col2': request.form.get(f'row{i}_col1'),
                'col3': request.form.get(f'row{i}_col2')
            }}
        )
    return redirect(url_for('index1'))





# Restoran araqum 

@app.route('/Restoran_araqum')
def Restoran_araqum():
    collection = db.Restoran
    table_data = list(collection.find({}, {'_id': 0}).sort('row', 1))  # Exclude MongoDB's default _id field
    return render_template('Restoran_araqum.html', table_data=table_data)


@app.route('/edit_Restoran', methods=['POST'])
def edit_restoran():
    db = client.testdb
    collection = db.Restoran
    for i in range(14):
        collection.update_one(
            {'row': i},
            {'$set': {
                'col1': request.form.get(f'row{i}_col0'),
                'col2': request.form.get(f'row{i}_col1'),
                'col3': request.form.get(f'row{i}_col2')
            }}
        )
    return redirect(url_for('Restoran_araqum'))



#Keteri Araqum
@app.route('/keteri_araqum')
def keteri_araqum():
    db = client.testdb
    collection = db.Keter
    table_data = list(collection.find({}, {'_id': 0}).sort('row', 1))  # Exclude MongoDB's default _id field
    return render_template('keteri_araqum.html', table_data=table_data)

@app.route('/edit_keter', methods=['POST'])
def edit_keter():
    db = client.testdb
    collection = db.Keter
    for i in range(14):
        collection.update_one(
            {'row': i},
            {'$set': {
                'col1': request.form.get(f'row{i}_col0'),
                'col2': request.form.get(f'row{i}_col1'),
                'col3': request.form.get(f'row{i}_col2')
            }}
        )
    return redirect(url_for('keteri_araqum'))



if __name__ == '__main__':
    app.run(debug=True)

