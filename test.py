from flask import Flask, request, make_response
import json
import random

from servo import unlock, lock

isLocked = True

def printJson(o):
  parsed = json.loads(json.dumps(o))
  print(json.dumps(parsed, indent=4, sort_keys=True))

def extractInfo(data):
  return {
      "session_id": data["session"]["session_id"],
      # "user_id": data["session"]["user"]["user_id"],
      # "request_id": data["request"]["request_id"]
      "intent_name": data["request"]["slot_info"]["intent_name"],
  }

def getResponse(info, hasDone):
  response = {  # example response
        "is_session_end":False,
        "version": "1.0",
        "response":{
          "confidence":0.8869365,
          "open_mic":True,
          "to_speak":{
            "type":0,
            "text":""
          },
          "to_display":{
            "type":0,
            "text":""
          },
          "log_info":{}        
        },
      }

  # copy session id from request
  # response["session_attributes"]["session"]["sessionID"] = info["session_id"]

  # Make response text from intent and hasDone status
  intent = info["intent_name"]
  response_text = ""
  if intent == "Mi_Welcome":
    response_text = "歡迎使用，請在緊急時大喊「救命」來發出求救信號。"
  elif intent == "Mi_Default":
    response_text = "請在緊急時大喊「救命」來發出求救信號。"
  elif intent == "unlock":
    if hasDone:
      response_text = "正在解鎖。請說「取消」來重新上鎖。"
    else:
      response_text = "抱歉，無法解鎖。"
  elif intent == "lock":
    if hasDone:
      response_text = "正在重新上鎖。"
    else:
      response_text = "抱歉，無法上鎖。"
  else:
    response_text = "抱歉，聽不懂。"
  response["response"]["to_speak"]["text"] = response_text
  response["response"]["to_display"]["text"] = response_text

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

        # Do lock / unlock
        hasDone = None
        intent = requestInfo["intent_name"]
        if intent == "unlock":
          print('unlock')
          hasDone = unlock()
          # hasDone = True
        elif intent == "lock":
          print('lock')
          hasDone = lock()
          # hasDone = True

        # toggleLock()
        
        content = getResponse(requestInfo, hasDone)

        return content, 200

# do unlock action
# return whether has unlocked successfully
def toggleLock():
  global isLocked
  if isLocked:
    print('unlock')
    unlock()
  else:
    print('lock')
    lock()

app.run(debug=True, port=80)
