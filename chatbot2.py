from flask import Flask
from flask import render_template,jsonify,request
import nlu
import response_dict

app = Flask(__name__)
app.secret_key = '12345'

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/chat',methods=["POST"])
def chat():
    user_message = request.form["text"]
    intent, entities = nlu.classify(user_message)
    response_text = response_dict.reply(intent)
    return jsonify({"status":"success","response":response_text})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
