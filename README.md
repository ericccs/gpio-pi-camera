# gpio-pi-camera
Security camera for Raspberry Pi with PIR sensor and led indicator.

###Recipe:
- Raspberry Pi
- Pi Camera
- PIR sensor
- led indicator
- resistors
- Python
- picamera library
- GPIO library

### Instruction:
1. Mix raspberry pie with Python with pi camera
2. Attach the PIR sensor, and to GPIO
3. Attach the led indicator to GPIO
4. Clone this repo
5. Install libraries:

    sudo apt-get install python-picamera python3-picamera

    pip install RPi.GPIO

6. Install script by copying bin/cameraPirSensor.sh script to /etc/init.d/

### Commands
    /etc/init.d/cameraPirSensor.sh start
    /etc/init.d/cameraPirSensor.sh stop
    /etc/init.d/cameraPirSensor.sh restart
    /etc/init.d/cameraPirSensor.sh reload
    /etc/init.d/cameraPirSensor.sh force-reload
    /etc/init.d/cameraPirSensor.sh status
    