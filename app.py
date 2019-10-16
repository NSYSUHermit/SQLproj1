from flask import flask
app = flask(_name_) #_name_ 代表目前執行的模組 

@app.route("/") # decorator 附加功能
def home():
    return "Hello Flask"

if _name_ == "_main_": #如果主程式執行
    app.run()#立即啟動伺服器