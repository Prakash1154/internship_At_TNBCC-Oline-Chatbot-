from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/')
def cal():
    return render_template("cal.html")

@app.route('/cal' ,methods=['GET','POST'])
def getvalue():
     val1=int(request.form['val1'])
     val2=int(request.form['val2'])
     val3=int(request.form['val3'])
     if val3==1:
        res=val1+val2
     if val3==2:
        res=val1-val2
     if val3==3:
        res=val1*val2
     if val3==4:
        res=val1/val2
     if val3==5:
        res=val1%val2
     return render_template("cal.html", res=res)
if __name__ == '__main__':
    app.run()
