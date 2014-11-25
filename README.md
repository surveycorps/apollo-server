apollo-server
=============
A small web server hosted on the Beaglebone black. This server handles requests from a companion phone app ([Apollo Launch](https://github.com/surveycorps/apollo-launch), parses the input JSON, and converts inputs into motor controls to relay to the microcontroller via the nRF24

Dependencies
===========
 - [Flask](http://flask.pocoo.org/) - Web server framework
 - [pynrf24](https://github.com/aehernandez/pynrf24) - Interfacing with microcontroller via the nRF24
 - [Adafruit BBIO](https://github.com/adafruit/adafruit-beaglebone-io-python)
