from flask import Flask, request, Response
import Adafruit_BBIO.PWM as PWM 
import MotorCommand as M

led_pin = "P9_14"
PWM.start(led_pin, 0) 

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test/", methods=['POST'])
def test():
    print("got something")

    # Grab JSON file
    content = request.get_json(force=True)
    angle = content['angle']
    magnitude = content['mag']
    
    print("Sending Angle: %d, Mag: %d" % (angle,magnitude))

    motor_state = M.joystick_to_motors(angle, magnitude)
    M.send_motor_command(motor_state)

    return "Thanks for all the data!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

    # Initialize the nRF24 radio peripheral
    M.init_radio()
    
