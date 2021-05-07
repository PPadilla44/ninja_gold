from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key = "bleh"
@app.route("/")
def main_page():
    if not 'msgs' in session:
        session['msgs'] = []
    if not 'gold' in session:
        session['gold'] = 0
    print(session)
    return render_template("index.html")
@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")
@app.route("/process_money", methods=["POST"])
def proccess_money():
    user_input = request.form['building']
    if user_input == "farm":
        gained = random.randint(10, 20)
        session['gold'] += gained
        session['msgs'].insert(0,f"Earned {gained} gold from the farm!")
    elif user_input == "cave":
        gained = random.randint(5, 10)
        session['gold'] += gained
        session['msgs'].insert(0,f"Earned {gained} gold from the cave!")
    elif user_input == "house":
        gained = random.randint(2, 5)
        session['gold'] += gained
        session['msgs'].insert(0,f"Earned {gained} gold from the house!")
    elif user_input == "casino":
        casino_money = random.randint(0, 50)
        if random.randint(0, 1) == 1:
            session['gold'] += casino_money
            session['msgs'].insert(0,f"Entered a casino and gained {casino_money} gold!")
        else:
            session['gold'] -= casino_money
            session['msgs'].insert(0,f"Entered a casino and lost {casino_money} gold...")
    print(user_input)
    return redirect ("/")


if __name__ == "__main__":
    app.run(debug=True)