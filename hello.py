from flask import Flask
app = Flask(__name__)
@app.route("/")
def helloworld():
    return "Hello World!"

##1st Excercise
@app.route("/CalcTip")
def CalcTip():
    tip = random.uniform(.10,.15)
    return tip

## 2nd Excercise
@app.route("/getHaircut")
def getHaircut():
    haircutp = 35
    r = random.uniform(.10,.15)
    tip = r*haircutp
    fprice = haircut + tip
    return fprice

@app.route("/nyc")
def hellonyc():
    return "Hello NYC!"

if __name__ == "__main__":
    app.run()