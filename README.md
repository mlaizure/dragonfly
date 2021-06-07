# dragonfly
![](assets/2-bug.png)

##What does dragonfly do?

* dragonfly will scan a git repository and return a json file filled with certain commit data

* The file will contain a json dictionary with files as the keys

* Each file will have a number, which is the total number of commits that had the words "fix", "bug", or "issue"

## How to use

```shell
$ dragonfly --help
usage: dragonfly ABSOLUTE_PATH_TO_REPO [BRANCH]

  Return commit data from given repository.

Options:
	--version	print version
	--help     print this message
```

To scan a repository:

```shell
$ dragonfly ~/Absolute/path/to/repo
$
$ ls
drgnfly_analysis.json
```

Want to scan a certain branch?

```shell
$ dragonfly ~/Absolute/path/to/repo [branch]
$
$ ls
drgnfly_analysis.json
```

## Authors

Maddi Laizure

Corbin Vandeventer

Finn Aspenson
