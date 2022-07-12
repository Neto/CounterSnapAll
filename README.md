
SCRAPPING QUALCOMM'S SNAPDRAGON SOCIAL NETWORK FOLLOWERS IN BRAZIL AND LATAM

Automatically collect these data:

- eMails on RD Platform
- YouTube Subscribers (BRAZIL & LATAM)
- Twitter Followers (BRAZIL & LATAM)
- Instagram Followers (BRAZIL & LATAM)

    app.py

Is the main app that takes care of the flask instance that publishes the webpage (.htm on /templates ; .css on /static)
The favicon and the graphic must be hosted outside the .venv enviroment.
I use tmux to keep flask hosting the page even after closing the terminal.

    get_stats.py

This is the file doing all the hard work.
It uses:
Selenium and Geckdriver (with Firefox) to scrape Twitter account.
Playwright and BeautifulSoup to scrape RD Station using a dummy account.
Sqlite3 to build, update and query followers database.
Instaloader to scrape Instagram total followers of each account.
Matplotlib and Pandas to build and save the graph.

    getGraphic.py

Is a separate module to update the graphic from the current followers.db, without adding one more record.

    rateCalc.py

Is a gimmick that will calculate the average of followers acquisition and send it to an Arduino LCD through MacOS serial port.


This app was writen in Python3 on Visual Studio Code on the winter of 2022.

© Spinoff Digital, https://www.spinoff.digital, Brazil - Mentor Neto
