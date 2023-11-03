# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    ascii_art = '''
        AAA     ZZZZZZ  UU   UU  BBBBB   IIII
       A   A       ZZ   UU   UU  BB  BB   II 
      AAAAAAA     ZZ    UU   UU  BBBBB    II 
     AAA   AAA   ZZ      UUUUU   BB  BB   II 
    AAA     AAA ZZZZZZ    UUU    BBBBB   IIII 
    '''
    return ascii_art + '''

        Hello, World! Welcome to the Tech-Trendz web application.

        Many thanks to you future cloud engineers for helping us get started.
        GO AZUBI AFRICA!!!!
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
