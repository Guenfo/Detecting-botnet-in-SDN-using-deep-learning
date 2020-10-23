 
from flask import Flask ,render_template, url_for
from tensorflow.keras.models import load_model
import pandas as pd

app = Flask(__name__)
flow_model = load_model('3final.h5')
 

@app.route("/")
@app.route("/home")
def home():
	try:
            detect = False
            predict_flow_dataset = pd.read_csv('PredictANN.csv')
            X_predict_flow = predict_flow_dataset.iloc[:, :].values
            
            y_flow_pred = flow_model.predict(X_predict_flow)
            y_flow_pred = (y_flow_pred > 0.5)

            legitimate_trafic = 0
            ddos_trafic = 0
	
            for i in y_flow_pred:
                if i == 0:
                    legitimate_trafic = legitimate_trafic + 1
                else:
                    ddos_trafic = ddos_trafic + 1
                    
            
            
           
            if (float(legitimate_trafic)/(legitimate_trafic+ddos_trafic)*100) >= 70.00:
                detect = False
		
            else:
                detect = True

            
            return render_template('home.html', result=str(detect) , normal=legitimate_trafic, ddos=ddos_trafic, total=legitimate_trafic+ddos_trafic)

            
	except Exception as e:
            if not str(e).startswith("\'bool\'"):
            
                print (e)

                pass  
    	


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/other")
def other():
    return render_template('other.html')



if __name__ == '__main__':
    app.run(debug=True)
