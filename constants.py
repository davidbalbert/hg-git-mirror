import os

VERSION = "0.0.1"

HG_REPO = os.environ.get('HG_REPO')
GIT_REPO = os.environ.get('GIT_REPO')

REPO_NAME = HG_REPO.split("/")[-1]
REPO_PATH = "tmp/%s" % REPO_NAME

DEBUG = os.environ.get('DEBUG', False)
