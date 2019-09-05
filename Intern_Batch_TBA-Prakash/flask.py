from flask import flask,render_template,request
app=Flask(__name__)
@app.route('/')
def hello_world():
   return render_template(“new2.html”)
app.run(debug=True)		
		
