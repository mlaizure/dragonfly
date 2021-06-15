# holberton ubuntu version
FROM ubuntu:16.04
# python 3.7 and pip
RUN apt-get update && apt-get install -y software-properties-common && add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && apt-get install -y python3.7 python3.7-dev python3-pip
RUN ln -sfn /usr/bin/python3.7 /usr/bin/python3 && ln -sfn /usr/bin/python3 /usr/bin/python && ln -sfn /usr/bin/pip3 /usr/bin/pip
# git command line tool
RUN apt-get install -y git
# Git module from git python
RUN pip install GitPython
# matplotlib
RUN python -m pip install -U matplotlib
# dragonfly
RUN pip install git-dragonfly
