from flask import Flask
from flask_restful import Resource,Api
app=Flask(__name__)
api=Api(app)
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
class Employee(Resource):

	def get(self):
		return employee_info

api.add_resource(Employee,"/info")
app.run(host='localhost', port=5000,debug=True)
