import os
from subprocess import Popen, PIPE, STDOUT

from constants import *

def clone_and_push():
    if os.path.exists(REPO_PATH):
        pretty_run_in_repo("hg pull --force")
        pretty_run_in_repo("hg update")
    else:
        pretty_run("hg clone %s %s" % (HG_REPO, REPO_PATH))

        with open(REPO_PATH + "/.hg/hgrc", "a") as f:
            f.write("git = %s\n" % GIT_REPO)
            f.write("\n")
            f.write("[extensions]\n")
            f.write("hgext.bookmarks =\n")
            f.write("hggit =\n")

        pretty_run_in_repo("hg bookmark -r default master")

    pretty_run_in_repo("hg push --force git")

def pretty_run(cmd):
    print("-----> " + cmd)
    run(cmd)

def pretty_run_in_repo(cmd):
    cmd_in_repo = "cd %s && %s" % (REPO_PATH, cmd)

    print("-----> Inside repo: %s" % cmd)
    run(cmd_in_repo)

def run(cmd):
    p  = Popen(cmd, shell=True, bufsize=-1,
               stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

    for line in p.stdout:
        print("       " + line.rstrip('\n'))
    print("\n")

    p.stdout.close()
    p.stdin.close()
    p.wait()
