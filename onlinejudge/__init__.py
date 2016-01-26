from flask import Flask,render_template,request
from flask.ext.script import Manager
from subprocess import Popen, PIPE

app = Flask(__name__)
app.debug = True
manager = Manager(app)
classname='hello'
lang = {"Python":('ex.py','python ex.py'),"C":('hello.c','gcc hello.c;./a.out'),"C++":('hello.cpp','g++ hello.cpp;./a.out'),"Java":(classname+'.java','javac '+classname+'.java;java '+classname)}


@app.route("/",methods=['GET', 'POST'])
def index():

	if request.method == 'GET':
		return render_template("home.html",output_value = "")
		
	if request.method == 'POST':
		code = request.form.get('code')
		language = request.form.get('lang')
		if language == 'Java':
			#Get class name of java file
			pass
		l = lang[language]
		with open(l[0],'w') as f:
			f.write(code)
		terminal_processes = Popen(l[1],shell=True,stdout=PIPE)
		output = terminal_processes.communicate()[0]
		return render_template("home.html",output_value=output)
    