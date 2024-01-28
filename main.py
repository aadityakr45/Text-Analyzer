from flask import Flask,render_template,request

app=Flask(__name__)
@app.get("/") #decorator
def showPage():
    return render_template("index.html")

@app.post("/analyze")
def analyze():
    text=request.form["text"]
    action=request.form["action"]
    answer=""
    if(action=="cntchr"):
        #count no of characters
        answer= f"The no of characters :- {len(text)}"
    if(action=="cntws"):
        #count no of white spaces
        answer= f"The no of white spaces are:- {text.count(' ')}"
    if(action=="ctuc"):
        #convert to upper case
        answer= f"The upper case of {text} is:- {text.upper()}"
    if(action=="ctlc"):
        #convert to lower case
        answer= f"The lower case of {text} is:- {text.lower()}"
    if(action=="ctcpl"):
        #convert to capitalize
        answer= f"The Capitalize form of {text} is:- {text.capitalize()}"
    if(action=="ctsc"):
        #convert to swapcase
        answer= f"The Swapcase of {text} is:- {text.swapcase()}"
    if(action=="ckap"):
        #check it only contains alphabates
        answer= f"Result is:- {text.isalpha()}"
    return render_template("index.html", output = answer)
app.run(debug=True)