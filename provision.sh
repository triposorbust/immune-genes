#!/bin/sh

sudo apt-get update
sudo apt-get -y install g++
sudo apt-get -y install gdb
sudo apt-get -y install emacs
sudo apt-get -y install make
sudo apt-get -y install git

sudo apt-get -y install python-numpy
sudo apt-get -y install python-scipy
sudo apt-get -y install python-matplotlib
sudo apt-get -y install ipython
sudo apt-get -y install ipython-notebook
sudo apt-get -y install python-pandas
sudo apt-get -y install python-sympy
sudo apt-get -y install python-nose

sudo apt-get -y install leiningen
sudo apt-get -y install r-base
echo 'install.packages(c("ggplot2", "scales", "ggmap", "googleVis", "igraph"), repos="http://cran.us.r-project.org")' | sudo R --no-save

touch ~/.matplotlib/matplotlibrc
echo "backend: Agg" >> ~/.matplotlib/matplotlibrc

exit 0
