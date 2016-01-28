from flask import Flask,render_template,request
from flask.ext.script import Manager
from subprocess import Popen, PIPE

app = Flask(__name__)
app.debug = True
manager = Manager(app)
classname='hello'
lang = {"Python":('ex.py','python ex.py'),"C":('hello.c','gcc hello.c;./a.out'),"Python3":('ex.py','python3 ex.py'),"C++":('hello.cpp','g++ hello.cpp;./a.out'),"Java":(classname+'.java','javac '+classname+'.java;java '+classname)}


@app.route("/",methods=['GET', 'POST'])
def index():

	if request.method == 'GET':
		return render_template("home.html",output_value = "",code_text="")
		
	if request.method == 'POST':
		inp=""
		code=""
		code = request.form.get('code')
		inp = request.form.get('input')
		language = request.form.get('lang')
		if language == 'Java':
			#Get class name of java file
			pass
		l = lang[language]
		with open(l[0],'w') as f:
			f.write(code)
		terminal_processes = Popen(l[1],shell=True,stdin=PIPE,stdout=PIPE)
		output = terminal_processes.communicate(inp)[0]
		return render_template("home.html",output_value=output,code_text=code)
    