from __future__ import print_function

import json
from urllib.parse import urlencode
from urllib.request import urlopen

from flask import (
    Blueprint, request, make_response)

dialog = Blueprint('dialog', __name__)


@dialog.route('/pulseHook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    action = req.get("result").get("action")
    print("starting processRequest...", action)
    if action != "yahooWeatherForecast":
        return {"action": str(req)}
    result = {}
    data = json.loads(result)
    res = convert_web_hook(data)
    return res


def convert_web_hook(data):

    speech = "data fetched from your git"
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
    }


@dialog.route('/test', methods=['GET'])
def test():
    return "Hello there my friend !!"


@dialog.route('/static_reply', methods=['POST'])
def static_reply():
    speech = "Hello there, this reply is from the webhook !! "
    my_result = {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }
    res = json.dumps(my_result, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r
