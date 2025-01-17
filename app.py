from flask import Flask, render_template, request
from searchName import searchName

app = Flask(__name__)


@app.route('/')
def index():
    # this stores the arguments into a variable
    sentence = request.args.get('sentence')
    # checks if the arguments actually exist
    if sentence:
        # filters for the periodic symbols in the name 
        periodicSentence = searchName(sentence)
        
        return render_template('index.html', periodicWords=periodicSentence)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
