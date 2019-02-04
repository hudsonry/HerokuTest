from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
   return render_template("index.html")

@app.route("/page2")
def page_2():
   return render_template("page2.html")

if __name__ == "__main__":
   app.run(debug=True)
