from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin
from smart_note_open_ai import Smart_note_open_ai


app = Flask(__name__)
CORS(app)

smart_note_open_ai = Smart_note_open_ai()


@app.before_request
def basic_authentication():
    if request.method.lower() == 'options':
        return Response()

@app.route('/getShortReply' , methods=['POST'])

def getShortReply():
    #print(request.get_json()['sentMessage'])
    quick_prompt = smart_note_open_ai.get_quick_prompt(request.get_json()['sentMessage'])
    json_prompt = quick_prompt['choices'][0]['text']
    return jsonify({'dropDownHTML': json_prompt}), 200

@app.route('/getLongReply' , methods=['POST'])

def getLongReply():
    print(request.get_json())
    long_reply = smart_note_open_ai.get_long_message(request.get_json()['quickReply'], request.get_json()['message'])
    json_long_message = long_reply['choices'][0]['text']
    return jsonify({'longReply': json_long_message}), 200