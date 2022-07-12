#!/usr/bin/python
import serial
import time
import os
import datetime
from flask import Flask, render_template
from datetime import datetime
import sqlite3

app = Flask(__name__)

@app.route('/')

def home():
    try:
# Connect to the database
        con = sqlite3.connect('followers.db')
        cur = con.cursor()
        lastOne = cur.execute('SELECT * FROM monthly_stats ORDER BY date DESC').fetchall()
        dataLast = lastOne[0]
        dataFirst = lastOne[-1] #Number of Lines to Calculate Rate

        #Hours Dif in the last <daraFirst> entries
        timeLast = datetime.fromtimestamp(dataLast[0])
        timeFirst = datetime.fromtimestamp(dataFirst[0])
        dateDiff = ((timeLast - timeFirst).total_seconds())/3600
        dateDiff = round(dateDiff, 1)
        
        print("Intervalo de Dias : ", (timeLast - timeFirst))
        print("Intervalo de Horas : ", dateDiff)
        
        #Hours to Goal Date
        timeMeta = "2022-09-30 23:59:59"
        timeMetaTS = datetime.strptime(timeMeta, "%Y-%m-%d %H:%M:%S").timestamp()
        timeFinal = datetime.fromtimestamp(timeMetaTS)

        # How many hours left
        diffFinal = ((timeFinal - timeLast).total_seconds())/3600
        diffFinal = round(diffFinal, 1)

        print("Horas restantes para a Meta : ", diffFinal)

        totalLast = dataLast[8]
        totalSoon = dataFirst[8]
        totalLastF = float(totalLast.split('K')[0])
        totalSoonF = float(totalSoon.split('K')[0])
        #Followers in the last period
        diference = (totalLastF - totalSoonF)*1000
        diference = round(diference, 2)
        print("Numero de Followers no período : ", diference)
        
        totalLastI = totalLastF * 1000

        rateFollowers = diference/dateDiff
        estimatedFollGoal = int(diffFinal * rateFollowers + totalLastI)
        print("Rate de Conquista de Followers no período : ", round((diference/dateDiff),2))

        estimatedStr = float(estimatedFollGoal/1000)
        estimatedTX = str(estimatedStr)
        estimatedMil = estimatedTX.split(".")[0]
        estimatedDec = (estimatedTX.split(".")[1])[0]
        estFinal = totalLast + " / " + estimatedMil + "." + estimatedDec + "K"
        print("TOTAL ESTIMADO EM 30 DE SETEMBRO: ", estFinal)
        estFinal = estFinal.encode("utf-8")
        find_ports()

        out = os.popen('ls /dev/tty.usb*').read()
        out1 = out.splitlines()
        
        find_ports.port1a = out1[0]
        find_ports.port2a = out1[1]
        find_ports.port3a = out1[2]

        os.system("fuser " + find_ports.port1a)
        os.system("fuser " + find_ports.port2a)
        os.system("fuser " + find_ports.port3a)
        time.sleep(2)
#The following line is for serial over GPIO
        port = find_ports.port3a # note I'm using Mac OS-X
        ard = serial.Serial(port,9600,timeout=5)
        time.sleep(3) # wait for Arduino
        ard.write(estFinal)
        time.sleep(2)
        ard.close

        os.system("fuser " + find_ports.port1a)
        os.system("fuser " + find_ports.port2a)
        os.system("fuser " + find_ports.port3a)
        raise SystemExit

    except Exception as err:
        estiText = "Erro no Cálculo"
        print(f"Error: '{err}'")
  
      # Disconnect from the database
        con.close()

def find_ports():
	out = os.popen('ls /dev/cu.usb*').read()
	out1 = out.splitlines()
	
	find_ports.port1a = out1[0]
	find_ports.port2a = out1[1]
	find_ports.port3a = out1[2]
        
home()