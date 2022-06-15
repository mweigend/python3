#! /Python310/python.exe

#----------------------------------------------------
# Dateiname:  dmm.py
# Das Modul stellt die Funktion get_digits bereit,
# die die Ziffern des Displays des angeschlossenen
# Multimeters liefert.
#
# Python 3,  mitp Verlag
# Kap. 31
# Michael Weigend 11. 06. 2019
#----------------------------------------------------
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

def get_digits():
    """Liefert die Ziffern auf dem Display als Zahl"""
    ser = serial.Serial("COM9", 2400, 8, 'N', 1, timeout=3)   # 1. Argument: COM8
    data = ser.read(28)
    ser.close()
    d1 = [format(i, '#010b')[2:] for i in data]
    i = 0
    while not d1[i].startswith("0001"): i +=1
    d = d1[i:i+14]
       
    
    A = d[1][7] + d[2][7] + d[2][5] + d[2][4] + \
        d[1][5] + d[1][6] + d[2][6]
    B = d[3][7] + d[4][7] + d[4][5] + d[4][4] + \
        d[3][5] + d[3][6] + d[4][6]
    C = d[5][7] + d[6][7] + d[6][5] + d[6][4] + \
        d[5][5] + d[5][6] + d[6][6]
    D = d[7][7] + d[8][7] + d[8][5] + d[8][4] + \
        d[7][5] + d[7][6] + d[8][6]
    return int(DIGIT[A] + DIGIT[B] + DIGIT[C] + DIGIT[D])
       

if __name__ == '__main__':
    while True:
        try:
            n = get_digits()
            print(n)
        except:
            print ("error")

