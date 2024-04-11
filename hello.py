
from flask import Flask
import random
app = Flask(__name__)
@app.route("/")
def helloworld():
    return "Hello World!"

## 1st Excercise
@app.route("/randomTip")
def randomTip():
    tipc = random.uniform(.10,.15)
    text = (str(tipc*100)) + "%"
    return text

## 2nd Excercise
@app.route("/getHaircut")
def getHaircut():
    ## Initial haircut price  
    haircutp = 35
    r = random.uniform(.10,.15)
    tip = r*haircutp
    ## Round to limit to two decimal places
    fprice = round((haircutp + tip),2)
    text = str(fprice)
    return text

@app.route("/nyc") 
def hellonyc():
    return "Hello NYC!"

if __name__ == "__main__":
    app.run()