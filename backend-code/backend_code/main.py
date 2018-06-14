import awsgi
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return ("Everything is working greater", 200)

def lambda_handler(event, context):
    response = awsgi.response(app, event, context)
    response["isBase64Encoded"] = False
    cors_header = {
        "X-Requested-With": '*',
        "Access-Control-Allow-Headers": 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,x-requested-with',
        "Access-Control-Allow-Origin": '*',
        "Access-Control-Allow-Methods": 'POST,GET,OPTIONS'
    }

    response["headers"] = cors_header
    return response

