from flask import Flask, json

homeData = {"id" : "Welcome to colorfull nonogram solver!"}
api = Flask(__name__)

@api.route('/', methods=['GET'])
def get_homeData():
  return json.dumps(homeData)

if __name__ == '__main__':
    api.run()
