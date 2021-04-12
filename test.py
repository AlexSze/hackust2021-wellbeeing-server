# example request data:
# {
#   "version": "1.0",
#   "session": {
#     "is_new": false,
#     "session_id": "530xxxxxxx",
#     "application": { "app_id": "xxxxxxxxxx" },
#     "user": {
#       "user_id": "Z05hZ==",
#       "is_user_login": true,
#       "gender": "unknown"
#     }
#   },
#   "request": {
#     "type": 0,
#     "request_id": "1b2f490768a8d09d859a3",
#     "timestamp": 1572508188915,
#     "intent": {
#       "query": "听30分钟海浪声",
#       "score": 0.800000011920929,
#       "complete": true,
#       "domain": "openplatform",
#       "confidence": 1,
#       "skillType": "Custom",
#       "sub_domain": "1004244",
#       "app_id": "xxxxxxx",
#       "request_type": "Start",
#       "need_fetch_token": false,
#       "is_direct_wakeup": false,
#       "slots": "{\"intent_name\":\"set_whitenoise\",\"slots\":[{\"name\":\"whitenoise\",\"value\":\"海浪\",\"raw_value\":\"海浪声\"},{\"name\":\"time\",\"value\":\"{\\\"start\\\":\\\"2019-10-31T15:49:48\\\",\\\"end\\\":\\\"2019-10-31T16:19:48\\\"}\",\"raw_value\":\"30分钟\"}]}"
#     },
#     "locale": "zh-CN",
#     "slot_info": {
#       "intent_name": "set_whitenoise",
#       "slots": [
#         { "name": "whitenoise", "value": "雨声", "raw_value": "海浪声" },
#         {
#           "name": "time",
#           "value": "{\"start\":\"2019-10-31T15:09:48\",\"end\":\"2019-10-31T16:29:48\"}",
#           "raw_value": "30分钟"
#         }
#       ]
#     }
#   },
#   "query": "听30分钟海浪声",
#   "context": { "device_id": "OQ+VrIRwXudjS+uT9KOuAA==", "in_exp": false }
# }
def extractInfo(data):
  return {
      "session_id": data["session"]["session_id"],
      # "user_id": data["session"]["user"]["user_id"],
      # "request_id": data["request"]["request_id"]
  }


# example response data:
# {
#   "is_session_end":false,
#   "version": "1.0",
#   "response":{
# 	"confidence":0.8869365,
# 	"open_mic":true,
# 	"to_speak":{
# 		"type":0,
# 		"text":"海浪的声音来咯"},
# 	"to_display":{
# 		"type":0,
# 		"text":"海浪的声音来咯"},
# 	  "log_info":{}
# 	},
#   "session_attributes":{
# 	"noticeFlag":1,
# 	"replyKeyWord":"",
# 	"turn":3,
# 	"miniSkillInfo":{"name":"LONGTAIL"},
# 	"session":{
# 		"sessionID":"f7579e8e-982e-4d4b-9387-980a3b09edef",
# 		"skillName":"",
# 		"skillSubName":"",
# 		"turn":0,
# 		"data":[{"query":"海浪声","reply":"海浪的声音来咯",
# 		"engine":"LONGTAIL"}]
# 		},
# 	"longtailEngine":"SKILL",
# 	"replace":false,
# 	"latitude":40.61924,"longtitude":120.73009}
# 	}
# }
def getResponse(info, hasUnlocked):
  response = {
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
      # "session_attributes":{
      #   "noticeFlag":1,
      #   "replyKeyWord":"",
      #   "turn":3,
      #   "miniSkillInfo":{"name":"LONGTAIL"},
      #   "session":{
      #     "sessionID":"f7579e8e-982e-4d4b-9387-980a3b09edef",
      #     "skillName":"",
      #     "skillSubName":"",
      #     "turn":0,
      #     "data":[{"query":"海浪声","reply":"海浪的声音来咯",
      #     "engine":"LONGTAIL"}]
      #     },
      #   "longtailEngine":"SKILL",
      #   "replace":False,
      #   "latitude":40.61924,"longtitude":120.73009
      #   }
      }

  # response["session_attributes"]["session"]["sessionID"] = info["session_id"]

  if hasUnlocked:
    response["response"]["to_speak"] = "海浪的声音"
  else:
    response["response"]["to_speak"] = "声音来咯?"

  print('reeeesponse-------------')
  print(response)
  return response


from flask import Flask, request, make_response
# from flask_ngrok import run_with_ngrok
import random

app = Flask(__name__)
# run_with_ngrok(app)

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
        print(str(data))

        requestInfo = extractInfo(data)

        hasUnlocked = unlock()
        content = getResponse(requestInfo, hasUnlocked)

        return content, 200


# do unlock
# return whether has unlocked successfully
def unlock():
  return random.uniform(0, 1) > 0.5

app.run(debug=True, port=80)
