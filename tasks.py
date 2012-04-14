from constants import *

def clone_and_push():
    if os.path.exists(REPO_PATH):
        run_in_repo("hg pull --force")
        run_in_repo("hg update")
    else:
        os.system("hg clone %s %s" % (HG_REPO, REPO_PATH))

        with open(REPO_PATH + "/.hg/hgrc", "a") as f:
            f.write("git = %s\n" % GIT_REPO)
            f.write("\n")
            f.write("[extensions]\n")
            f.write("hgext.bookmarks =\n")
            f.write("hggit =\n")

        run_in_repo("hg bookmark -r default master")

    run_in_repo("hg push --force git")

def run_in_repo(cmd):
    os.system("cd %s && %s" % (REPO_PATH, cmd))
