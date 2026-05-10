from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from visuals import visuals
app = Flask(__name__)
v = visuals()
df = None
columns = []
chart_file = None
chart_type_global = None   
# HOME PAGE (To UPLOAD an excel file , The column headers are selected for Category and Value )
@app.route("/", methods=["GET", "POST"]) #route for the home page
def home(): #function to 
    try:
        global df, columns
        if request.method == "POST":
            file = request.files.get("file")
            if file:
                df_local = v.analysis(file)
                if df_local is None:
                    df = None            
                    columns = []
                    return render_template("home.html", a="Only Excel files allowed", columns=columns)
                df = df_local
                columns = df.columns.tolist()
                return redirect(url_for("next"))
        return render_template("home.html", a="", columns=columns)
    except Exception:
        return render_template("home.html", a="Something went wrong! Try again", columns=columns)
# CHART PAGE
@app.route("/index", methods=["GET", "POST"])
def next():
    try:
        global df, columns, chart_file, chart_type_global
        chart_file = None
        if request.method == "POST":
            chart_type_global = request.form.get("chart_type")  
            x = request.form.get("x_col")
            y = request.form.get("y_col")
            label = request.form.get("x_col")
            value = request.form.get("y_col")
            title = request.form.get("title")
            if chart_type_global == "line":
                chart_file = v.line_chart(df, x, y, title)
            elif chart_type_global == "bar":
                chart_file = v.bar_chart(df, x, y, title)
            elif chart_type_global == "hist":
                chart_file = v.histogram(df, x, title)
            elif chart_type_global == "pie":
                chart_file = v.pie_chart(df, x, y, title)
                if chart_file is None:
                    chart_file = None
            elif chart_type_global == "scatter":
                chart_file = v.scatter_chart(df, x, y, title)
        return render_template(
            "index.html",
            columns=columns,
            chart_file=chart_file,
            chart_type=chart_type_global   
        )
    except Exception:
        return render_template(
            "index.html",
            a="Something went wrong! Try again",
            columns=columns,
            chart_file=None,
            chart_type=chart_type_global
        )
if __name__ == "__main__":
    app.run(debug=True)
