from __future__ import print_function

import json

from flask import (
    Blueprint, request, make_response)

# from pulsa.han
#
# commitHandle = CommitHandler()
from handler.commitHandler import CommitHandler

commitHandle = CommitHandler()
dialog = Blueprint('dialog', __name__)


@dialog.route('/pulseHook', methods=['POST'])
def webhook():
    req = json.loads(request.get_data())

    print(req)

    res = commitHandle.process_request(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


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
