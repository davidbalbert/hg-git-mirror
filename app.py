from rq import use_connection, Queue
from flask import Flask

from tasks import clone_and_push
from constants import *

app = Flask(__name__)

# rq setup
use_connection()
q = Queue()

app.debug = DEBUG

@app.route('/')
def index():
    return 'hg-git mirror v%s<br><br>\nmirroring %s<br>\nto %s' % (VERSION, HG_REPO, GIT_REPO)

@app.route('/hook', methods=["POST"])
def hook():
    q.enqueue(clone_and_push)
    return "push queued"

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
