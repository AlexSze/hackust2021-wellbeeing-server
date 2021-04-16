# Well-BEEing Server

Our team, Up To Data's submission to HackUST 2021

This is only the back-end server part of our submission to bridge the hardware and XiaoAi, please refer to https://github.com/AlexSze/hackust2021-wellbeeing for the front-end application.

This repository is a Flask Server to communicate with the XiaoAi Platform. It responses to the requests from XiaoAi's application and make responses according to the intent of the request. It also controls the door (i.e. servo).

| Files                  | Function                                         |
| ---------------------- | ------------------------------------------------ |
| arduino_servo.ino      | Arduino microcontroller code to control the lock |
| run.sh                 | Run script to initialize the server              |
| server.py              | Main server script to interface with XiaoAi      |
| servo.py               | Library to interface with the microcontroller    |

## Reference:
- https://flask.palletsprojects.com/en/1.1.x/
- https://developers.xiaoai.mi.com/documents/Home?type=/api/doc/render_markdown/SkillAccess/skill/fulu/HTTPS
