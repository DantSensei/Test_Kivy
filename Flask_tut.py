from flask import Flask, redirect, url_for, render_template 

app = Flask(__name__)

@app.route("/<name>") #redirection 

#You make functions to display different sites 
def home(name):
    return render_template("index.html", content ="Testing")


'''
@app.route("/<name>")
def user(name): 
    return f"Hello {name}!"

@app.route("/admin")
def admin(): 
    return redirect(url_for("home"))
'''

if __name__ == "__main__": 
    app.run(debug=True)



'''
In index 

<!DOCTYPE html>
<html>
<head>
    <title>Home page</title>  
    </head>
    <body>
        <h1>Home Page! </h1>
        <p>{{content}}</p>
        <p>{{r}} </p>
        {% for x in content %}
            
            <p>
                {{x}}
            </p>
            
        {% endfor%}
    </body>
</html>

'''