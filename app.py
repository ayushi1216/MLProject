# Flask App routing

from flask import Flask,render_template,request,redirect,url_for

# Create a simple Flask application
app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return "Welcome to my world"

@app.route("/index", methods=["GET"])
def index():
    return "Welcome to my index world kamran"


# Variable rule

@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the score is: "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the score is: "+ str(score)

@app.route('/calculate', methods=['POST', 'GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks = (maths+science+history)/3
        result = ""

        if average_marks>=50:
            result="success"
        else:
            result="fail"
        
      
        return render_template('result.html', results=average_marks)

if __name__ == "__main__":
    app.run(debug=True)

