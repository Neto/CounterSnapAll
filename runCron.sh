#!/bin/sh
cd "$(dirname "$0")";
CWD="$(pwd)"
echo $CWD
/Library/Frameworks/Python.framework/Versions/3.11/bin/python3 /Users/neto/ARDUINO/CounterSnapAll/get_stats.py
/Library/Frameworks/Python.framework/Versions/3.11/bin/python3 /Users/neto/ARDUINO/CounterSnapAll/rateCalc.py