from flask import Flask

app = Flask(__name__)

@app.route("/")
def generateSentence(required):
  return str(required)

if __name__ == "__main__":
  app.run()
