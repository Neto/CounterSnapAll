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
        dataFirst = lastOne[30] #Number of Lines to Calculate Rate

        #Hours Dif in the last <daraFirst> entries
        timeLast = datetime.fromtimestamp(dataLast[0])
        timeFirst = datetime.fromtimestamp(dataFirst[0])
        dateDiff = ((timeLast - timeFirst).total_seconds())/3600

        #Hours to Goal Date
        timeMeta = "2022-09-30 23:59:59"
        timeMetaTS = datetime.strptime(timeMeta, "%Y-%m-%d %H:%M:%S").timestamp()
        timeFinal = datetime.fromtimestamp(timeMetaTS)

        # How many hours left
        diffFinal = ((timeFinal - timeLast).total_seconds())/3600



        totalLast = dataLast[8]
        totalSoon = dataFirst[8]
        totalLastF = float(totalLast.split('K')[0])
        totalSoonF = float(totalSoon.split('K')[0])
        #Followers in the last period
        diference = (totalLastF - totalSoonF)*1000
        
        totalLastI = totalLastF * 1000

        rateFollowers = diference/dateDiff
        estimatedFollGoal = int(diffFinal * rateFollowers + totalLastI)

        estimatedStr = float(estimatedFollGoal/1000)
        estimatedTX = str(estimatedStr)
        estimatedMil = estimatedTX.split(".")[0]
        estimatedDec = (estimatedTX.split(".")[1])[0]
        estFinal = estimatedMil + "." + estimatedDec + " K"

        print(estFinal)
        

    except Exception as err:
        print(f"Error: '{err}'")
  
      # Disconnect from the database
        con.close()

home()
