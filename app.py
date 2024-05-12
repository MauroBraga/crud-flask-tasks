from flask import  Flask, request

app = Flask(__name__)


tasks = []

@app.route('/tasks',methods=['Post'])
def create_task():
    data = request.get_json()
    print(data)
    return 'Test'


if __name__ == "__main__":
  app.run(debug=True)