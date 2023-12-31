from flask import Flask, request, jsonify


from creator.__main__.openai import text_complition


app = Flask(__name__)


@app.route('/')
def home():
    return 'All is well...'


@app.route('/dialogflow/es/receiveMessage', methods=['POST'])
def esReceiveMessage():
    try:
        data = request.get_json()
        # You can use this action to do different things
        #action = data['queryResult']['action']
        query_text = data['queryResult']['queryText']

        result = text_complition(query_text)

        if result['status'] == 1 :
            return jsonify(
                {
                    'fulfillmentText': result['response']
                }
            )
    except:
        pass
    return jsonify(
        {
            'fulfillmentText': 'Something went wrong.'
        }
    )
