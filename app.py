from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
 return "<h1>App experta en clona una ia</h1><p>Gen14 Experto clona una ia</p><a href='https://www.binance.com/activity/referral-entry/CPA?ref=CPA_00RDO84IBV'>Bono</a>"
if __name__=="__main__": app.run(host="0.0.0.0",port=int(__import__("os").getenv("PORT",10000)))