# -*- coding: utf-8 -*-
import bmi

if bmi.BMI < 18.5:
    f = open("niedowaga.txt", "r", encoding='utf-8')
    print(f.read())
elif bmi.BMI < 25:
    f = open("norma.txt", "r")
    print(f.read())
elif bmi.BMI < 30:
    f = open("nadwaga.txt", "r")
    print(f.read())
else:
    f = open("otylosc.txt", "r")
    print(f.read())
