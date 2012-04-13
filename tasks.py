from constants import *

def clone_and_push():
    print "cloning %s to %s" % (HG_REPO, REPO_PATH)
    os.system("hg clone %s %s" % (HG_REPO, REPO_PATH))
    print "removing %s" % REPO_PATH
    os.system("rm -rf %s" % REPO_PATH)
