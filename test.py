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
  response["session_attributes"]["session"]["sessionID"] = info["session_id"]

  if hasUnlocked:
    response["response"]["to_speak"] = "海浪的声音"
  else:
    response["response"]["to_speak"] = "声音来咯?"

  print('----------------response---------------')
  print(response)
  return response


from flask import Flask, request, make_response
import random

app = Flask(__name__)

@app.route("/", methods=['POST'])
def webhook():
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
        print('----------------request-----------------')
        print(str(data))

        requestInfo = extractInfo(data)

        hasUnlocked = unlock()
        content = getResponse(requestInfo, hasUnlocked)

        return content, 200

# do unlock action
# return whether has unlocked successfully
def unlock():
  return random.uniform(0, 1) > 0.5  # dummy

app.run(debug=True, port=80)