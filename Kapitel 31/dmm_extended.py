#------------------------------------------------------------
# Filename: dmm.py
# Support for data transfer from a digital multimeter (dmm).
# The public function read_dmm() returns a float number, which
# represents the numerical value shown on the display of
# the dmm.
# This works with dmms that send their data via usb->COM.
# This is the file that is published on PyPI.
# 
# More details are explained in:
# Python 3(6th edition), mitp 2016
# Chapter 31
#
# Michael Weigend, 13.8.2016
# 
#-------------------------------------------------------------
import serial

DIGIT = {'1111110':'0',
         '0110000':'1',
         '1101101':'2',
         '1111001':'3',
         '0110011':'4',
         '1011011':'5',
         '1011111':'6',
         '1110000':'7',
         '1111111':'8',
         '1111011':'9'}

def read_dmm(port=2, baudrate=2400, databits=8,
             stopbits=1, timeout=3):
    """ Liefert eine Gleitkommzahl, die den Zahlenwert
        angibt, der auf dem Display angezeigt wird"""
    ser = serial.Serial(port, baudrate, databits,
                        'N', stopbits, timeout) 
    data = ser.read(28)
    ser.close()
    d1 = [format(i, '#010b')[2:] for i in data]
    i = 0
    while not d1[i].startswith("0001"): i +=1
    d = d1[i:i+14]
    return _get_number(d)

def _get_digits(d):
    """ Das Argument d ist eine Liste von 14 Strings aus
        Nullen und Einsen. Zurückgegeben wird eine ganze Zahl,
        die die vier Ziffern des Displays repräsentiert."""
       
    A = d[1][7] + d[2][7] + d[2][5] + d[2][4] + \
        d[1][5] + d[1][6] + d[2][6]
    B = d[3][7] + d[4][7] + d[4][5] + d[4][4] + \
        d[3][5] + d[3][6] + d[4][6]
    C = d[5][7] + d[6][7] + d[6][5] + d[6][4] + \
        d[5][5] + d[5][6] + d[6][6]
    D = d[7][7] + d[8][7] + d[8][5] + d[8][4] + \
        d[7][5] + d[7][6] + d[8][6]
    return int(DIGIT[A] + DIGIT[B] + DIGIT[C] + DIGIT[D])

   
def _get_number(d):
    """ Das Argument d ist eine Liste von 14 Strings aus
        Nullen und Einsen. Zurückgegeben wird eine Zahl,
        (float) die den dargestellten Zahlenwert repräsentiert."""
        
    n = _get_digits(d)
    # Position des Punktes
    if d[7][4] == "1": n/=10
    elif d[5][4] == "1": n/=100
    elif d[3][4] == "1": n/= 1000
    # Präfix 
    if d[9][4] == "1": n /= 10**6      #Mikro
    elif d[9][5] == "1": n /= 10**9    #Nano  
    elif d[9][6] == "1": n *= 1000     #Kilo
    elif d[10][4] == "1": n /= 1000    #Milli
    elif d[10][6] == "1": n *= 10**6   #Mega
    # Minuszeichen
    if d[1][4] == "1": n *= -1
    return n
 
 
if __name__ == '__main__':
    for i in range(10):
        try:
            print(read_dmm())
        except:
            print("Error")



