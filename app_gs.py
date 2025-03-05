import json
from fastapi import FastAPI
import gs
from datetime import datetime

def main():
    lists1 = gs.main()
    lists2 = [x for x in lists1 if datetime.strptime(x['ocDate'], "%m/%d/%Y").date() == datetime.today().date()]
    print(type(lists1))
    print(type(lists2))
    
    outputData = lists2[0]
    print(type(outputData))
    
    return outputData

