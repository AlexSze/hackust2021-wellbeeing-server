# Well-BEEing Server

Our team, Up To Data's submission to HackUST 2021

This is only the back-end server part of our submission to bridge the hardware and XiaoAi. Please refer to https://github.com/AlexSze/hackust2021-wellbeeing for the front-end application.

This repository is a Flask Server to communicate with the XiaoAi Platform. It responses to the requests from XiaoAi's application and make responses according to the intent of the request. It also controls the door (i.e. servo).

## Files

| Files                  | Function                                         |
| ---------------------- | ------------------------------------------------ |
| arduino_servo.ino      | Arduino microcontroller code to control the lock |
| run.sh                 | Run script to initialize the server              |
| server.py              | Main server script to interface with XiaoAi      |
| servo.py               | Library to interface with the microcontroller    |
| install.sh | Install script to put service in place |
| ngrok.service | ngrok service to open up a tunnel |
| ngrok.yml | ngrok configuration (authtoken needed) |
| wellbeeing.service | main service to interface with XiaoAi |

## Installation

Since this is built for deployment on a raspberry pi, username of `pi` is required in the current implementation

`sudo install.sh`

After running the script above, please insert your ngrok authtoken to `/home/pi/wellbeeing/ngrok.yml'

## Reference:
- https://flask.palletsprojects.com/en/1.1.x/
- https://developers.xiaoai.mi.com/documents/Home?type=/api/doc/render_markdown/SkillAccess/skill/fulu/HTTPS
