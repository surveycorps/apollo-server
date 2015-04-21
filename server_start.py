from flask import Flask, request, jsonify
import Adafruit_BBIO.PWM as PWM
import MotorCommand as M

led_pin = "P9_14"
PWM.start(led_pin, 0)

app = Flask(__name__)

command = M.Motor()


@app.route("/")
def hello():
    return "Hello World! My name is APRo."

@app.route("/test/", methods=['POST'])
def test():
    # Grab JSON file
    content = request.get_json(force=True)

    js_angle = content['joystick_angle']
    js_mag = content['joystick_mag']
    left, right, left_dir, right_dir = command.joystick_to_motors(js_angle, js_mag)

    shell = content['slider_mag']
    shell_dir = content['slider_dir']

    command.send_motor_command(left, right, shell, left_dir, right_dir, shell_dir)

    print("Angle: %d, Mag: %d, Shell: %d, Dir: %d" % (js_angle, js_mag,
                                                      shell, shell_dir))
    return jsonify(power="50")


@app.route("/status/", methods=['GET'])
def status():
    # Get Status Here
    return jsonify(status='OKAY')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

    # Initialize the nRF24 radio peripheral
