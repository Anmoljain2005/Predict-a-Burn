from flask import Flask, request, render_template,jsonify
from flask_cors import CORS,cross_origin
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

@app.route('/')
@cross_origin()
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
@cross_origin()
def predict_datapoint():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        data = CustomData(
            Height = float(request.form.get('Height')),
            Weight = float(request.form.get('Weight')),
            Duration = float(request.form.get('Duration')),
            Heart_Rate = float(request.form.get('Heart_Rate')),
            Body_Temp = float(request.form.get('Body_Temp')),
            Age = int(request.form.get('Age')),
            Gender = request.form.get('Gender').lower()
        )

        pred_df = data.get_data_as_dataframe()
        
        print(pred_df)

        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(pred_df)
        results = round(pred[0],2)
        return render_template('index.html',results=results,pred_df = pred_df)
    
@app.route('/predictAPI',methods=['POST'])
@cross_origin()
def predict_api():
    if request.method=='POST':
        data = CustomData(
            Height = float(request.form.get('Height')),
            Weight = float(request.form.get('Weight')),
            Duration = float(request.form.get('Duration')),
            Heart_Rate = float(request.form.get('Heart_Rate')),
            Body_Temp = float(request.form.get('Body_Temp')),
            Age = int(request.form.get('Age')),
            Gender = request.form.get('Gender').lower()
        )

        pred_df = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(pred_df)

        dct = {'Calories':round(pred[0],2)}
        return jsonify(dct)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True) 
    