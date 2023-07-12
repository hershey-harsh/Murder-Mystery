from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
  return render_template('home.html')


@app.route("/game")
def game():
  return render_template('game.html')


@app.route("/suspects")
def suspects():
  return render_template('suspects.html')

@app.route("/clues")
def clues():
  return render_template('clues.html')

@app.route("/victim")
def victim():
  return render_template('victim.html')

@app.route('/solve', methods=['GET', 'POST'])
def solve():
    if request.method == 'POST':
        selected_suspect = request.form.get('suspect')

        if selected_suspect == 'Emily Smith':
            result = 'Congratulations! You correctly identified the suspect.'
        else:
            result = 'Sorry, your selection was incorrect. Please try again.'
        
        return render_template('solve.html', result=result)
    
    return render_template('solve.html')

if __name__ == "__main__":
        app.run(host="0.0.0.0")
