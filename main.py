from flask import Flask, jsonify
from flask_restful import  Api
import pandas as pd
app = Flask(__name__)
api = Api(app)

@app.route("/")
@app.route("/elements")
@app.route("/elements/<int:thumbnail_width>")
def hello(thumbnail_width=0):
    return "Witam użytkowniku, aby korzystać z tego API proszę podaj parametry thumbnail_width oraz thumbnail_height w formacie takim jak\
            : localhost:5000/elements/{thumbnail_width}/{thumbnail_height}"    

@app.route('/elements/<int:thumbnail_width>/<int:thumbnail_height>', methods=['GET'])
def elements(thumbnail_width=0,thumbnail_height=0):
    data = pd.read_excel('Task3DataSet.xlsx')  # read excel file
    if((thumbnail_width != 0) & (thumbnail_height !=0)):
        data = data[(data.thumbnail_width==thumbnail_width) & (data.thumbnail_height==thumbnail_height)]
        data=data.T.to_dict()
        if len(data) == 0:
            return "Nie znaleziono żadnego elementu. Proszę podaj ponownie parametry thumbnail_width oraz thumbnail_height w formacie takim jak\
            : localhost:5000/elements/{thumbnail_width}/{thumbnail_height}"
        else:
            return jsonify(data)
    else:
        return "Proszę podaj parametry thumbnail_width oraz thumbnail_height w formacie takim jak\
            : localhost:5000/elements/{thumbnail_width}/{thumbnail_height}"