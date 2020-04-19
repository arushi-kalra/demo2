from flask import Flask
app = Flask(__name__)
employee_info = {
    "emp1":
        {
            "name": "xyzsa",
            "sal": "10"
        },
    "emp2":
        {
            "name": "absac",
            "sal": "14"
        }
}
@app.route('/predict', methods=['GET'])
def predict():
    return employee_info


if __name__ == '__main__':
    app.run(debug=True)
