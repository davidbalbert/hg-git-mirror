import os
import base64
import urlparse

VERSION = "0.0.1"

HG_REPO = os.environ.get('HG_REPO')
GIT_REPO = os.environ.get('GIT_REPO')

if not GIT_REPO.startswith("git+ssh://"):
    # we have a standard format git remote
    GIT_REPO = "git+ssh://" + "/".join(GIT_REPO.split(":"))

REPO_NAME = HG_REPO.split("/")[-1]
REPO_PATH = "tmp/%s" % REPO_NAME

DEBUG = os.environ.get('DEBUG', False)

PRIVATE_KEY = base64.b64decode(os.environ.get('PRIVATE_KEY'))

REDIS_URL = os.environ.get('REDISTOGO_URL')
urlparse.uses_netloc.append('redis')
REDIS_URL = urlparse.urlparse(REDIS_URL)
