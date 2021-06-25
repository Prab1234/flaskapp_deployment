from flask import Flask
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])

def heading():
    return "<h1> This is the flask app to be deployed </h1>"


if __name__=='__main__':
    app.run()