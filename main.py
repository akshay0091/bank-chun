from flask import Flask, render_template,request, url_for, redirect
import pickle
import sklearn
app = Flask(__name__)
model=pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        CreditScore = int(request.form['CreditScore'])
        Geography = request.form['Geography']
        if (Geography =="France"):
            Geography=0
        elif (Geography =="Spain"):
            Spain=1
        else:
            Geography=2

        Gender = request.form['Gender']
        if (Gender =="Male"):
            Male=0
        elif (Gender =="Female"):
            Female=1
        Age = int(request.form['Age'])
        Tenure = int(request.form['Tenure'])
        Balance = int(request.form['Balance'])
        credit = request.form['credit']
        if (credit =="yes"):
            credit=1
        elif (credit =="no"):
            credit=0
        active = request.form['active']
        if (active =="yes"):
            active=1
        elif (active =="no"):
            active=0
        EstimatedSalary = int(request.form['EstimatedSalary'])

        print(Geography)
        prediction = model.predict([[
            CreditScore,
            Geography,
            Gender,
            Age,
            Tenure,
            Balance,
            credit,
            active,
            EstimatedSalary,



        ]])
        number = int(prediction)
        print(prediction)
        if (number==0):
            output='No chance Exited'
        elif (number==1):
            output='Chances to Exited '
        else:
            output='diabetes'
            return output


        return redirect(url_for('result',output=output))
    return render_template('home.html')

@app.route('/result')
def result():

    output=request.args.get('output',None)
    return render_template('result.html',output=output)
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.debug = True
    app.run()