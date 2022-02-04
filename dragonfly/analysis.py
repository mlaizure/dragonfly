import git
import sys
import time
from git.exc import GitCommandError, NoSuchPathError, InvalidGitRepositoryError


def analysis(repo, branch='master'):
    """Takes repo and branch and analyzes commit messages."""
    """If words in msg match keywords, adds count to dictionary."""
    # Accesses git repo using repo name passed in.
    try:
        repo = git.Repo(repo)
    except (NoSuchPathError, InvalidGitRepositoryError):
        print("Uh oh! It looks like the repository you passed doesn't exist.")
        return
    num_fixes = {}

    # Accesses repo branch using branch name passed in or defaults to master.
    try:
        repo.git.checkout(branch)
    except GitCommandError:
        print("Oops! It seems the branch you passed doesn't exist.")
        return

    # Sets up loading bar.
    toolbar_width = 0
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))

    # For each commit message...
    for i, commit in enumerate(repo.iter_commits(branch)):
        time.sleep(0.001)
        keywords = ['fix', 'bug', 'issue']

        # if the commit message contains one of the keywords...
        if any(keyword in commit.message for keyword in keywords):
            change_types = ['A', 'C', 'D', 'R', 'M', 'T']

            # iterate through all possible change types.
            for t in change_types:
                if len(commit.parents) >= 1:
                    diffs = commit.diff(commit.parents[0]).iter_change_type(t)

                    # Gets file path using the diff.
                    for diff in diffs:

                        # Checks if file has a non-code-file extension.
                        if not is_ignored(diff.a_path):

                            # Adds one to dictionary if commit had keyword.
                            if diff.a_path in num_fixes.keys():
                                num_fixes[diff.a_path] += 1
                            else:
                                num_fixes[diff.a_path] = 1

        # Loading bar middle and end.
        sys.stdout.write("-")
        sys.stdout.flush()
    sys.stdout.write("] Analysis Complete!\n")

    # Dictionary with file names and key and num of matching commits as value.
    return num_fixes


def is_ignored(path):
    """Checks if file has non-code-file extension."""
    ignore_ext = ['.json', '.md', '.ps', '.eps', '.txt', '.xml', '.xsl',
                  '.rss', '.xslt', '.xsd', '.wsdl', '.wsf', '.yaml', '.yml',
                  '~', '#']
    for ext in ignore_ext:
        l = len(ext)
        if path[-l:] == ext:
            return True
    return False


if __name__ == '__main__':
    analysis()
