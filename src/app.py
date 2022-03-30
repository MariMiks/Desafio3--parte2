from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("index.html")

@app.route("/biografia")
def bio():
   return render_template("biografia.html")

@app.route("/contatos")
def contatos():
   return render_template("contatos.html")

@app.route("/publicidade")
def publi():
   return render_template("publicidade.html")

if __name__ == "__main__":
   app.run(debug=True)

