from constants import *

def clone_and_push():
    if os.path.exists(REPO_PATH):
        os.system("cd %s && hg pull --force" % REPO_PATH)
        os.system("cd %s && hg update" % REPO_PATH)
    else:
        os.system("hg clone %s %s" % (HG_REPO, REPO_PATH))

        with open(REPO_PATH + "/.hg/hgrc", "a") as f:
            f.write("git = %s\n" % GIT_REPO)
            f.write("\n")
            f.write("[extensions]\n")
            f.write("hgext.bookmarks =\n")
            f.write("hggit =\n")

        os.system("cd %s && hg bookmark -r default master" % REPO_PATH)

    os.system("cd %s && hg push --force git" % REPO_PATH)
