from flask import Flask
from main import predict

app = Flask(__name__)

@app.route("/<length>")
def generateSentence(length):
  return predict(int(length))

if __name__ == "__main__":
  app.run()
