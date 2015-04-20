# python-lepton

Quick and dirty pure python library for capturing images from the Lepton over SPI (for example, on a Raspberry PI).

Requires `python-opencv` and `python-numpy`:

    $ sudo apt-get install python-opencv python-numpy

## Example programs

### picamera_overlay

Requires `python-picamera`, a Raspberry PI, and compatible camera such as http://www.adafruit.com/products/1367

    $ sudo apt-get install python-picamera

    $ ./picamera_overlay --help
    Usage: picamera_overlay [options]

    Options:
      -h, --help            show this help message and exit
      -f, --flip-vertical   flip the output images vertically
      -a ALPHA, --alpha=ALPHA
                            set lepton overlay opacity

### still_capture

Note that this program will output any image format that opencv knows about, just specify the output file format extension (e.g. `output.jpg` or `output.png`)

    $ ./still_capture --help
    Usage: still_capture [options] output_file[.format]

    Options:
      -h, --help           show this help message and exit
      -f, --flip-vertical  flip the output image vertically