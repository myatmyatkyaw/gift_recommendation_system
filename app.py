from flask import Flask,request,render_template,redirect
import joblib
import numpy as np
import pandas
import sklearn
import pickle
#from sklearn.preprocessing import MinMaxScaler, StandardScaler
#from sklearn.ensemble import RandomForestClassifier

#importing model
#model = pickle.load(open('Pickle_RL_Model.pkl','rb'))
# sc = pickle.load(open('standscaler.pkl','rb'))
# ms = pickle.load(open('minmaxscaler.pkl','rb'))

#creating flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tab1')
def tab1():
    return render_template('tab1.html')

@app.route("/predict",methods=['POST'])
def brain():
    age = int(request.form['age'])
    sex = int(request.form['sex'])
    openness = int(request.form['openness'])
    conscientiousness = int(request.form['conscientiousness'])
    extraversion = int(request.form['extraversion'])
    agreeableness = int(request.form['agreeableness'])
    neuroticism = int(request.form['neuroticism'])
    event = int(request.form['event'])


    feature_list = [age, sex, openness, conscientiousness, extraversion, agreeableness, neuroticism, event]
    #single_pred = np.array(feature_list).reshape(1, -1)
    if age>18 and age<=79:
        joblib.load('Pickle_RL_Model_Two.pkl','r')
        model = joblib.load(open('Pickle_RL_Model_Two.pkl','rb'))

        arr = [feature_list]
        acc = model.predict(arr)
        brain = str(acc)
    # scaled_features = ms.transform(single_pred)
    # final_features = sc.transform(scaled_features)
    #prediction = model.predict(single_pred)

    
    # df_dict = {1: "Clothing", 2: "Book", 3: "Accessory", 4: "Gadget", 5: "Game"}
    

    # if acc[0] in df_dict:
    #     df = df_dict[acc[0]]
    #     result = "{} is the best gift to be given".format(df)
    # else:
    #     result = "Sorry, we could not determine the best gift to be given with the provided data."
    return render_template('index.html', brain1 = brain)
    


# python main
if __name__ == "__main__":
    app.run(debug=True)