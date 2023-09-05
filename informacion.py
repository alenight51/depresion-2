from flask import Flask, render_template
app = Flask (__name__) 
@app.route("/Depresion")
def student_webpage():
    name = "👑🌸Alejandra🌸👑"
    return render_template("index.html", student_name = name)
app.run(debug = True)