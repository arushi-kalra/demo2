from flask import Flask

app=Flask(__name__)

employee_info={
	"emp1":
	{
	"name":"xyz",
	"sal":"10"
	},
	"emp2":
	{
	"name":"abc",
	"sal":"14"
	}
}
@app.route('/predict',methods=['GET'])
def predict():
	return employee_info

app.run(port=33507,debug=True)
