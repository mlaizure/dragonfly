import git


def analysis(repo, branch='master'):
    repo = git.Repo(repo)
    num_fixes = {}

    repo.git.checkout(branch)

    for i, commit in enumerate(repo.iter_commits(branch)):
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

#    print(num_fixes)
    return num_fixes

if __name__ == '__main__':
    analysis()
