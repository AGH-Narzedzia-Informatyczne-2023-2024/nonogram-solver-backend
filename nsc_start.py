from flask import Flask, json

homep = {"id" : "Welcome to colorfull nonogram solver!"}
api = Flask(__name__)

@api.route('/homep', methods=['GET'])
def get_homep():
  return json.dumps(homep)

if __name__ == '__main__':
    api.run()