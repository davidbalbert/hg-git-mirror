import urlparse

from redis import Redis
from rq import use_connection, Queue
from flask import Flask

from tasks import clone_and_push
from constants import *

app = Flask(__name__)

# rq setup
redis = Redis(host=REDIS_URL.hostname, port=REDIS_URL.port, db=0, password=REDIS_URL.password)
use_connection(redis)
q = Queue()

app.debug = DEBUG

@app.route('/')
def index():
    return 'hg-git mirror v%s<br><br>\nmirroring %s<br>\nto %s' % (VERSION, HG_REPO, GIT_REPO)

@app.route('/hook', methods=["POST"])
def hook():
    q.enqueue(clone_and_push)
    return "push queued\n"

@app.route('/gittest')
def gittest():
    from tasks import run_with_private_key
    os.system("pwd")
    os.sysstem("find tmp")
    run_with_private_key("ssh -T git@github.com")
    return "results in the log"

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
