import git
import sys
import time


def analysis(repo, branch='master'):
    repo = git.Repo(repo)
    num_fixes = {}

    repo.git.checkout(branch)

    toolbar_width = 0

    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))

    for i, commit in enumerate(repo.iter_commits(branch)):
        time.sleep(0.1)
        keywords = ['fix', 'bug', 'issue']
        if any(keyword in commit.message for keyword in keywords):
            change_types = ['A', 'C', 'D', 'R', 'M', 'T']
            for t in change_types:
                if len(commit.parents) >= 1:
                    diffs = commit.diff(commit.parents[0]).iter_change_type(t)
                    for diff in diffs:
                        if diff.a_path in num_fixes.keys():
                            num_fixes[diff.a_path] += 1
                        else:
                            num_fixes[diff.a_path] = 1
        sys.stdout.write("-")
        sys.stdout.flush()

#    print(num_fixes)
    sys.stdout.write("] Analysis Complete!\n")
    return num_fixes

if __name__ == '__main__':
    analysis()
