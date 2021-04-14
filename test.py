from flask import Flask, request, make_response
import json
import random

from servo import *

def printJson(o):
  parsed = json.loads(json.dumps(o))
  print(json.dumps(parsed, indent=4, sort_keys=True))

def extractInfo(data):
  return {
      "session_id": data["session"]["session_id"],
      # "user_id": data["session"]["user"]["user_id"],
      # "request_id": data["request"]["request_id"]
  }

def getResponse(info, hasUnlocked):
  response = {  # example response
        "is_session_end":False,
        "version": "1.0",
        "response":{
          "confidence":0.8869365,
          "open_mic":True,
          "to_speak":{
            "type":0,
            "text":"海浪的声音来咯"
          },
          "to_display":{
            "type":0,
            "text":"海浪的声音来咯"
          },
          "log_info":{}        
        },
      }

  # copy session id from request
  # response["session_attributes"]["session"]["sessionID"] = info["session_id"]

  if hasUnlocked:
    response["response"]["to_speak"]["text"] = "正在解鎖"
  else:
    response["response"]["to_speak"]["text"] = "声音来咯?"

  print('------------------------response---------------------------')
  printJson(response)
  return response


app = Flask(__name__)

@app.route("/", methods=['POST'])
def webhook():
    print('=============================================================')
    try:
        data = request.get_json()
    except:
        content = {
            "code": 406,
            "status": "NOT_ACCEPTABLE",
            "message": "No given data",
        }
        return content, 406
    else:
        print('------------------------request--------------------------')
        printJson(data)

        requestInfo = extractInfo(data)

        hasUnlocked = toggleLock()
        content = getResponse(requestInfo, hasUnlocked)

        return content, 200

# do unlock action
# return whether has unlocked successfully
def toggleLock():
    if isLocked:
        print('unlock')
        unlock()
    else:
        print('lock')
        lock()
    return random.uniform(0, 1) > 0.5

app.run(debug=True, port=80)
