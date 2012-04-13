from constants import *

def clone_and_push():
    os.system("hg clone %s %s" % (HG_REPO, REPO_PATH))
    os.system("rm -rf %s" % REPO_PATH)
