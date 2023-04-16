from flask import Flask, render_template, request
import pickle
import numpy as np
import warnings
import random
warnings.filterwarnings("ignore")
crop = ['rice', 'maize', 'jute', 'cotton', 'coconut', 'papaya', 'orange', 'apple', 'muskmelon', 'watermelon', 'grapes', 'mango',
        'banana', 'pomegranate', 'lentil', 'blackgram', 'mungbean', 'mothbeans', 'pigeonpeas', 'kidneybeans', 'chickpea', 'coffee', 'Anything']

app = Flask(__name__)
model = pickle.load(open('recommendation2.pkl', 'rb'))
pred_model = pickle.load(open('yieldPred.sav', 'rb'))


@app.route('/', methods=['GET'])
@app.route('/homes', methods=['GET'])
def Home():
    return render_template('home.html')


@app.route('/Major_Crop', methods=['GET'])
def Major_Crops():
    return render_template('Major_Crops.html')

@app.route('/AboutRice', methods=['GET'])
def AboutRice():
    return render_template('AboutRice.html')



@app.route('/AboutWheat', methods=['GET'])
def AboutWheat():
    return render_template('AboutWheat.html')

@app.route('/Selling', methods=['GET'])
def Selling():
    return render_template('Selling.html')

@app.route('/Soil_testing', methods=['GET'])
def Soil_testing():
    return render_template('Soil_testing.html')

@app.route('/AboutJute', methods=['GET'])
def AboutJute():
    return render_template('AboutJute.html')
@app.route('/AboutMaize', methods=['GET'])
def AboutMaize():
    return render_template('AboutMaize.html')
@app.route('/AboutPulses', methods=['GET'])
def AboutPulses():
    return render_template('AboutPulses.html')
@app.route('/AboutSugarcane', methods=['GET'])
def AboutSugarcane():
    return render_template('AboutSugarcane.html')


@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')


@app.route('/Nutrient_Management', methods=['GET'])
def Nutrient():
    return render_template('Nutrient_Management.html')


@app.route("/prediction", methods=['POST', 'GET'])
def prediction():
    if request.method == 'POST':
        N = int(request.form['N'])
        P = int(request.form['P'])
        K = int(request.form['K'])
        Temp = float(request.form['Temp'])
        Hum = float(request.form['Hum'])
        Ph = float(request.form['Ph'])
        Rain = float(request.form['Rain'])

        prediction = model.predict([[N, P, K, Temp, Hum, Ph, Rain]])
        # print(prediction)
        # output=prediction
        index = 22
        for i in range(22):
            if prediction[0][i] == 1:
                index = i
                break
        return render_template('prediction.html', prediction_text="You Can Grow {}".format(crop[index]))
    else:
        return render_template('prediction.html', prediction_text="")


@app.route("/yield_pred", methods=['POST', 'GET'])
def yield_pred():
    if request.method == 'POST':
        State = str(request.form['State'])
        Season = str(request.form['Season'])
        Crop = str(request.form['Crop'])
        Area = int(request.form['Area'])

        prediction = pred_model.predict([[random.randint(0,27), random.randint(0,1), random.randint(0,2), Area]])
        # print(prediction)
        # output=prediction
        return render_template('yield_pred.html', prediction_text="Total Growth in Quintals: {}".format(int(prediction)))
    else:
        return render_template('yield_pred.html', prediction_text="")


@app.route('/Schemes', methods=['GET'])
def Schemes():
    return render_template('Schemes.html')


@app.route('/Loans', methods=['GET'])
def Loans():
    return render_template('Loans.html')


@app.route('/About_us', methods=['GET'])
def About_us():
    return render_template('About_us.html')


if __name__ == "__main__":
    app.run(debug=True)
