from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/predict' , methods = ['POST'])
def submit():
    if request.method == "POST":
       username = request.form['username']
       age = request.form['age']
       sex = request.form['sex']
       cp = request.form['cp']
       trestbps = request.form['trestbps']
       chol = request.form['chol']
       fbs = request.form['fbs']
       restecg = request.form['restecg']
       thalach = request.form['thalach']
       exang = request.form['exang']
       oldpeak = request.form['oldpeak']
       slope = request.form['slope']
       ca = request.form['ca']
       thal = request.form['thal']
       
       
    return render_template("predict.html", n=username , a=age , s=sex , cp=cp , tr=trestbps , cl=chol , fbs=fbs , re=restecg , th=thalach , ex=exang , op=oldpeak , sl=slope , ca=ca , tl=thal)
        
        

if __name__ == "__main__":
     app.run(debug=True, port=8000)