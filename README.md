# dragonfly

[![Pypi link](https://img.shields.io/pypi/v/git-dragonfly)](https://pypi.org/project/git-dragonfly/)
[![landing link](https://img.shields.io/badge/landing-page-blue)](https://mlaizure.github.io/dragonfly/)

![](assets/3-bug.png)

## What does dragonfly do?

* dragonfly will scan a git repository and return a json file filled with certain commit data

* The file will contain a json dictionary with files as the keys

* Each file will have a number, which is the total number of commits that had the words "fix", "bug", or "issue"

* dragonfly can also return a png file, containing a visualization of the json data

* dragonfly can also print the data to standard out

## Installation

```shell
pip3 install git-dragonfly
```

## System Requirements

You need to have at least version 3.6 of Python to install and use this software

## How to use

```shell
$ dragonfly --help
usage: dragonfly PATH_TO_REPO [BRANCH]

  Return commit data from given repository.

Options:
	--version   print version
	--help      print this message
	--terminal  print data in terminal
	--chart     generate pie chart of results
```

To scan a repository:

```shell
$ dragonfly ~/Absolute/path/to/repo
[----------------] Analysis Complete!
drgnfly_analysis.json file generated
$
$ ls
drgnfly_analysis.json
```

Want to scan a certain branch?

```shell
$ dragonfly ~/Absolute/path/to/repo [branch]
[-------------] Analysis Complete!
drgnfly_analysis.json file generated
$
$ ls
drgnfly_analysis.json

$
$ cat drgnfly_analysis.json
{"web_dynamic/static/scripts/4-hbnb.js": 2, "web_dynamic/static/scripts/2-hbnb.js": 3, "web_dynamic/static/scripts/3-hbnb.js": 2, "web_dynamic/static/styles/3-header.css": 2, "web_dynamic/templates/2-hbnb.html": 2, "web_dynamic/templates/3-hbnb.html": 2, "web_dynamic/templates/4-hbnb.html": 2}
$
```

## Options

To print the results of the analysis without generating a json file, type "--terminal" at the end

```shell
$ dragonfly ~/Absolute/path/to/repo [branch] --terminal
[-------------] Analysis Complete!
web_dynamic/static/scripts/2-hbnb.js   | 3
web_dynamic/static/scripts/4-hbnb.js   | 2
web_dynamic/static/scripts/3-hbnb.js   | 2
web_dynamic/static/styles/3-header.css | 2
web_dynamic/templates/2-hbnb.html      | 2
web_dynamic/templates/3-hbnb.html      | 2
web_dynamic/templates/4-hbnb.html      | 2
$
```

To generate a .png file containing a visual representation of the data, type "--chart" at the end

```shell
$ dragonfly ~/Absolute/path/to/repo [branch] --chart
[-------------] Analysis Complete!
pie_chart.png file generated
$
$ ls
pie_chart.png
```

Here is an example of the png file

![](assets/example_map.png)

NOTE: the numbers in each of the pie pieces are the percentages of commits that each file had with the keywords in their commit message. So "web_dynamic/static/scripts/2-hbnb.js" held 20% of all commits with the words 'bug', 'fix', or 'issue'.

## Contributions

Pull requests and issues are welcome. Please leave detailed comments about any changes you make.

## Related Projects

* [erikbern/git-of-theseus](https://github.com/erikbern/git-of-theseus)

* [ejwa/gitinspector](https://github.com/ejwa/gitinspector)

## About

* Dragonfly is a first year Portfolio Project for Holberton School.
* Our project timeline in a nutshell:
  * One week for high-level brainstorming and feature discussions
  * One week for breaking down features into tasks and scheduling and assigning those tasks
  * One week for MVP development - a command line application that analyzes a Git repository and outputs a JSON file with the results
  * One week for stretch goals - terminal output, data visualization, and pip packaging
* Our most difficult challenges during intial development
  * Finding well-documented libraries for gathering data from Git and visualizing that data
  * Learning customization of in-depth configuration in MatPlotLib
* Potential future features
  * Keyword customizaiton: allowing the user to add and change keywords in order to analyze different aspects of the code
  * Different styles of visualizations
  * Analysis of how bug-related commits i.e. code stability changes over time

## Authors

* Maddi Laizure - [Github](https://github.com/mlaizure) & [LinkedIn](https://www.linkedin.com/in/maddi-laizure/)

* Corbin Vandeventer - [Github](https://github.com/forstupidityonly) & [LinkedIn](https://www.linkedin.com/in/corbin-vandeventer-6551b71a9/)

* Finn Aspenson - [Github](https://github.com/faspen) & [LinkedIn](https://www.linkedin.com/in/finn-aspenson-0a23841b6/)

### Maddi Laizure

Hi! I’m Maddi, one of the developers for Dragonfly. This project was inspired by my husband, who is a long-time software developer. We were discussing the lack of tools available to get insight into code maturity. We came up with the idea of Dragonfly as an easy way to get a quick snapshot of where in your code you’ve had to fix the most bugs. Dragonfly’s analysis can help with targeting code refactorings, familiarizing a new developer with a code base, or getting a deeper look at code maturity.

## Licensing

* Dragonfly is licensed under the *MIT license*.

* License can be viewed [here](https://github.com/mlaizure/dragonfly/blob/main/LICENSE).
