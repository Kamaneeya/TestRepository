from flask import Flask , jsonify,request
app = Flask(__name__)

@app.route('/input' , methods = ['GET','POST'])
def index():
    if(request.method == 'POST'):
        req_Json = request.json
        num1 = req_Json['num1']
        num2 = req_Json['num2']
        st = check_if_number_exists(num1,num2) 
        return st      
    else:
        return "Request method is GET"
def check_if_number_exists(num1,num2):
    num1 = str(num1)
    num2 = str(num2)
    if(len(num1) != 8):
        return "Number 1 is not a 8 digit number"
    if(len(num2) != 1):
        return "Number 2 is not in range of 0-9 "
    if(num2 in num1):
        return "Number2 is present in Number1"
    else:
        return "Number2 is not present in Number1"

if __name__ == '__main__':
    app.run(debug=True)