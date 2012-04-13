import os

from flask import Flask
app = Flask(__name__)

VERSION = "0.0.1"

HG_REPO = os.environ.get('HG_REPO')
GIT_REPO = os.environ.get('GIT_REPO')

app.debug = os.environ.get('DEBUG', False)

@app.route('/')
def index():
    return 'hg-git mirror v%s<br><br>\nmirroring %s<br>\nto %s' % (VERSION, HG_REPO, GIT_REPO)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
