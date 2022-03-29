"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

DISSES = [
  'you\'re stupid', 'you don\'t know how to code', 'Ballonicorn doesn\'t like you', 'you\'re bad', 'you need to excercise more'
]



@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
    <html>
    Hi! This is the home page.<br>
    <a href="/hello">Hello</a>
    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""
    options = []
    for compliment in AWESOMENESS:
        option = f'<option value="{compliment}"">{compliment}</option>'
        options.append(option)
      
    doptions = []
    for diss in DISSES:
        option = f'<option value="{diss}"">{diss}</option>'
        doptions.append(option)
        
    # choice = choice(["compliment", "diss"])
    # if choice == "compliment":
    #   pick = choice(AWESOMENESS)
    # else:
    #   pick = choice(DISS)
        
    return f"""
  
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet /diss">
          What's your name? <input type="text" name="person">
        </form>
          
          <form action="/greet">
      
            
            <label for="compliment-select">Choose your compliment:</label>
            <select name="compliment" id="compliment-select">
              {options[0]}
              {options[1]}
              {options[2]}
              {options[3]}
              {options[4]}
              {options[5]}
              {options[6]}
              {options[7]}
              {options[8]}
              {options[9]}
              {options[10]}
              {options[11]}
              {options[12]}
              {options[13]}
            </select>
            <input type="submit" value="Submit">
          </form>
      
      
        <form action="/diss">
          <label for="diss-select">Choose your insult:</label>
          <select name="diss" id="diss-select">
            {doptions[0]}
            {doptions[1]}
            {doptions[2]}
            {doptions[3]}
            {doptions[4]}
          </select>
          <input type="submit" value="Submit">
        </form>
        
      </form>
      
          
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""
    
    
    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """
    
    
@app.route('/diss')
def diss_person():
  
    player = request.args.get("person")
    
    diss = request.args.get("diss")
    
        
        
    return f"""
      <!doctype html>
      <html>
        <head>
          <title>An insult</title>
        </head>
        <body>
          Hi, {player}! I think you're {diss}!
        </body>
      </html
      """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")


