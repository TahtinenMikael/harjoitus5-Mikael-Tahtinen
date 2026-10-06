from machine import Pin, PWM
from time import sleep

# Moottorit
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

e1.freq(1000) #Aseta PWM-taajuus 1000 Hz
e2.freq(1000) #Aseta PWM-taajuus 1000 Hz

# DEFINE RIVIT KERTOO OLEELLISET

def pysähdy():             # SEIS
    e1.duty_u16(0)  #moottorin nopeus (MAX 65534!!!)
    e2.duty_u16(0)
    sleep(0.5)


def eteenpäin(): #  ~50 cm
    m1.value(1)
    m2.value(0)
    e1.duty_u16(32767)   #moottorin nopeus (MAX 65534!!!)
    e2.duty_u16(32767)
    sleep(3)
    pysähdy()


def taaksepäin(): #  ~50 cm
    m1.value(0)
    m2.value(1)
    e1.duty_u16(32767)   #moottorin nopeus (MAX 65534!!!)
    e2.duty_u16(32767)
    sleep(3)
    pysähdy()


def käänny_vasemmalle(): # ~90ast
    m1.value(0)
    m2.value(0) 
    e1.duty_u16(50000)  #moottorin nopeus (MAX 65534!!!)
    e2.duty_u16(50000)
    sleep(3)
    pysähdy()


def käänny_oikealle(): # ~90ast
    m1.value(1)
    m2.value(1)
    e1.duty_u16(50000)  #moottorin nopeus (MAX 65534!!!)
    e2.duty_u16(50000)
    sleep(3)
    pysähdy()


def käänny_180():  # 180 astetta = kaksi 90 asteen käännöstä

    m1.value(0)
    m2.value(0)
    e1.duty_u16(50000)  #moottorin nopeus (MAX 65534!!!)
    e2.duty_u16(50000)
    sleep(6)
    pysähdy()

# ITSE SUUNTA KÄSKYT

sleep(12) 
taaksepäin()
käänny_oikealle() 
taaksepäin() 
käänny_oikealle()
taaksepäin()
käänny_vasemmalle()
taaksepäin()
käänny_vasemmalle()
eteenpäin()
käänny_180()
eteenpäin()
pysähdy()


sleep(1) # Odota