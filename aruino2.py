> conda activate arduino
(arduino) > python

Python 3.7.1 (default, Dec 10 2018, 22:54:23) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.

>>> import serial
>>> ser = serial.Serial('COM4', 9800, timeout=1)
>>> ser.write(b'H')
>>> ser.write(b'L')
>>> ser.write(b'H')
>>> ser.write(b'L')
>>> ser.close()
>>> exit()
