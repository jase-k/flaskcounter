from flask import Flask, render_template, request, redirect, session # don't forget to import redirect!
    

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes



@app.route('/')
def create_user():
    if 'count' in session:
        print("key found")
        session["count"] = session['count'] +1
        return render_template("index.html")
    else:
        print("added key")
        session["count"] = 0
        return render_template("index.html")

@app.route('/add1')
def addTwo():
    if 'count' in session:
        print("key found")
    else:
        print("added key")
        session["count"] = 0
    session["count"] = session['count'] +1
    return redirect('/')
    
# adding this method
@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')




if(__name__ == "__main__"):
    app.run(debug=True)