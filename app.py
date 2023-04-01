from flask import Flask, render_template
from datetime import datetime
import sqlite3

app = Flask(__name__)

app.config.from_object(__name__)

@app.route('/')
def home():

  # Connect to the database
  con = sqlite3.connect('/Users/neto/ARDUINO/CounterSnapAll/followers.db')
  cur = con.cursor()

  # Create an empty list for the records
  records = []

  try:

    # Get all records
    all_stats = cur.execute('SELECT * FROM monthly_stats ORDER BY date DESC').fetchall()

    # Create an object ("dictionary" in Python) for each record
    for item in all_stats:
      dt = datetime.fromtimestamp(item[0])

      record = {
        'date': dt.strftime('%-d %b %H:%M'), # Format the date
        'emailC': item[1],
        'youtube': item[2],
        'youtubeL': item[3],
        'twitter': item[4],
        'instagram': item[5],
        'twitterL': item[6],
        'instagramL': item[7],
        'tiktokB': item[8],
        'tiktokL': item[9],
        'total': item[10]
      }
      
      # Add each record object to the list
      records.append(record)
    
  except Exception as e:
    pass
  
  # Disconnect from the database
  con.close()

  # Pass the list of objects to the template for rendering
  return render_template('stats.html', records=records)
  
