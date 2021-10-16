FROM ubuntu:20.04

MAINTAINER Devin Caplow-Munro "decamun@gmail.com"

#install initial things
RUN \
    apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install git curl unzip man wget telnet

#set up django and dependencies
#more probably to come here...
RUN apt-get -y install python3-pip
RUN python3 -m pip install Django


#clone 1F2FRFBF repo


#set up ZSH for ease of use
RUN apt-get -y install zsh
# terminal colors with xterm
ENV TERM xterm
# set the zsh theme
ENV ZSH_THEME agnoster
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true
WORKDIR /root
ENV HOME /root

# don't do this for now
# ADD folder/.bashrc /root/.bashrc


#run this when the image starts
CMD ["zsh"]
