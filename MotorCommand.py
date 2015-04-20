import math

def joystick_to_motors(angle, magnitude, quadrant=None):
    angle = float(angle)
    # if (quadrant == 1 or quadrant == 2):
    #     theta = int(round(abs((angle - 90)) / 2))
    # elif (quadrant == 3):
    #     theta = int(round(abs(angle - 90)/2))
    # elif (quadrant == 4):
    #     theta = int(round((-angle + 270)/2))
    # else:
    #     raise ValueError("No correct quadrant given. Valid values [1,2,3,4]")

    # Angle is specific to the android virtual joystick implementation
    if (quadrant is None):
        if (angle < 90 and angle >= 0): quadrant = 1
        elif (angle < 0 and angle >= -90): quadrant = 2
        elif (angle < -90 and angle >= -180): quadrant = 3
        elif (angle <= 180 and angle >= 90): quadrant = 4
        else: raise ValueError("Angle should be within the range [0, 180] and [0, -180]")

    k_left = 0
    k_right = 0


    if (quadrant == 1):
        theta = (angle*(10.0/9))
        k_left = 1
        dir_left = 0
        dir_right = 0
    elif (quadrant == 2):
        theta = abs(angle*(10.0/9))
        k_right = 1
        dir_left = 0
        dir_right = 0

    elif (quarant == 3):
        theta = (angle+180)*(10.0/9)
        k_right = 1
        dir_left = 1
        dir_right = 1
    elif (quadrant == 4):
        theta = (angle-90)*(10.0/9)
        k_left = 1
        dir_left = 1
        dir_right = 1
    else:
        raise ValueError("No correct quadrant given. Valid values [1,2,3,4]")

    motor_left = int(round(magnitude - k_left*magnitude*(theta/100)))
    motor_right = int(round(magnitude - k_right*magnitude*(theta/100)))

   # theta = math.radians(theta)
   # motor_left = round(magnitude * math.sin(theta) * math.sin(theta))
   # motor_right = round(magnitude * math.cos(theta) * math.cos(theta))

    return [motor_left, motor_right, dir_left, dir_right]

def init_radio():
    from nrf24 import NRF24
    import time

    pipes = [ [0xe7, 0xe7, 0xe7, 0xe7, 0xe7], [0xc2, 0xc2, 0xc2, 0xc2, 0xc2] ]

    radio = NRF24()
    radio.begin(0,0,"P9_114", "P9_16") #Set CE and IRQ pins
    radio.setRetries(15,15)

    # Number of bytes we're sending per payload
    radio.setPayloadSize(3)

    radio.setChannel(10)
    radio.setDataRate(NRF24.BR_250KBPS)
    radio.setPALevel(NRF24.PA_MAX)
    radio.openWritingPipe(pipes[1])
    radio.openReadingPipe(1,pipes[0])

def send_motor_command(motor_left, motor_right, motor_shell, dir_left,
dir_right, dir_shell):
    # Check if the user passed an array containing the values, instead of the
    # values themselves. Note: The correct style is to use variable length
    # arguments

    buffer = [chr(motor_left), chr(motor_right), chr(motor_shell),
              chr(dir_left << 2 | dir_right << 1 | dir_shell)]
    radio.write(buffer)


