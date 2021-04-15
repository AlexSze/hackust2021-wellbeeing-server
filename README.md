# hackust2021-wellbeeing-server

## Files

| Files                  | Function                                         |
| ---------------------- | ------------------------------------------------ |
| arduino_servo.ino      | Arduino microcontroller code to control the lock |
| run.sh                 | Run script to initialize the server              |
| server.py              | Main server script to interface with XiaoAi      |
| servo.py               | Library to interface with the microcontroller    |

to be updated

## Installation

Since this is built for deployment on a raspberry pi, username of `pi` is required in the current implementation

`sudo install.sh`

After running the script above, please insert your ngrok authtoken to `/home/pi/wellbeeing/ngrok.yml'

