#!/usr/bin/env python3
import datetime as dt
from time import sleep

def main():
    while True:
        now = dt.datetime.now()
        times = now.strftime("%H:%M:%S")
        print("Текущее время в ЧЧ:ММ:СС - ",times)
        sleep(5)

if __name__ == "__main__":
    main()