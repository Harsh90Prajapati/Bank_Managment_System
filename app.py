from flask import Flask, request, render_template, jsonify
import bms

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/openAC', methods=['POST'])
def open_acc():
  content_type = request.headers.get('Content-Type')
  if (content_type == 'application/json'):
      data = request.json
      response = bms.OpenAcc(data['name'], data['acn'], data['dob'], data['address'], data['phone'], data['balance'])
      return jsonify(response)
  else:
      return 'Content-Type not supported!'

@app.route('/deposit', methods=['POST'])
def deposit():
  content_type = request.headers.get('Content-Type')
  if (content_type == 'application/json'):
      data = request.json
      response = bms.Deposit(data['acn'], data['amount'])
      return jsonify(response)
  else:
      return 'Content-Type not supported!'

@app.route('/withdraw', methods=['POST'])
def withdraw():
  content_type = request.headers.get('Content-Type')
  if (content_type == 'application/json'):
      data = request.json
      response = bms.Withdraw(data['acn'], data['amount'])
      return jsonify(response)
  else:
      return 'Content-Type not supported!'

@app.route('/checkbal', methods=['GET'])
def checkbal():
    args = request.args
    response = bms.CheckBal(args.get("acn"))
    return jsonify(response)

@app.route('/getcustomer', methods=['GET'])
def getcustomer():
    args = request.args
    response = bms.GetCustomerData(args.get("acn"))
    return jsonify(response)

@app.route('/closeAC', methods=['POST'])
def closeacc():  
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.json
        response = bms.CloseAcc(data["acn"])
        return jsonify(response)
    else:
      return 'Content-Type not supported!'

