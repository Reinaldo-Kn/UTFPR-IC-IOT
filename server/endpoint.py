from flask import Flask
import serial

app = Flask(__name__)
ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)

@app.route('/temp')
def get_temperature():
    temperature = ser.readline().decode('utf-8').strip().split()[0]
    return temperature

if __name__ == '__main__':
    app.run(debug=True, port=8082)