![Commit activity](https://img.shields.io/github/commit-activity/w/thibault-cne/wordle-and-solver)
![Licence](https://img.shields.io/github/license/thibault-cne/wordle-and-solver)
![Language](https://img.shields.io/badge/Solver-C-brightgreen)
![Language](https://img.shields.io/badge/Frontend-VueJS-brightgreen)
![Language](https://img.shields.io/badge/Backend-flask-brightgreen)

# project2-E19 : Wordle and Solver

# Table of Content

1. [Project presentation](#project-presentation)
2. [Installation guide](#installation-guide)
3. [Launch application](#launch-application)
4. [Warnings](#warnings)
5. [Known issues](#issues)


# Project presentation

## Overview
This project was done as part of the first year at Telecom Nancy. The goal was to built a wordle like application with flask framework. The second part was to built a Solver for this wordle game made in C. The goal was to use specific structures in C such as trees or linked, double linked lists.

[Here is a version of the subject](./Documents/Projet_P2I2_S2_2122_DP.pdf)

**Supervisors**

Olivier Festor <<olivier.festor@telecomnancy.eu>>  
Gérald Oster <<gerald.oster@telecomnancy.eu>>


**Group members**

* CHATARD Louis <<louis.chatard@telecomnancy.eu>>
* CHENEVIERE Thibault <<thibault.cheneviere@telecomnancy.eu>>
* CLERIOT Louis <<louis.cleriot@telecomnancy.eu>>
* MOY Kélian <<kelian.moy@telecomnancy.eu>>

# Installation guide

``` shell
$ git clone https://github.com/thibault-cne/wordle-and-solver
$ cd wordle-and-solver
```

## Install Docker

**MACOS**

``` shell
$ brew update
$ brew cask install docker
```

**Linux (Ubuntu, Debian, Linux Mint)**

``` shell
$ sudo apt update
$ sudo apt-install docker
```

# Launch application

## Web part

**Docker**

``` shell
$ cd Website
$ sudo docker-compose build
$ sudo docker-compose up
```

**Split backend/frontend images**

``` shell
$ cd Website/backend
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python3 tazmouApp.py
```

``` shell
$ cd Website/frontend
$ npm install package-lock.json
$ npm run serve
```

## Solver part
``` shell
$ cd Solver
$ make re
$ ./solver
```


# Warnings
Has I continue to maintain the website and the solver, both arent finished in their development.

# Issues
Their is still some issues especially on the solver part. I have problems on the way I cut the tree for calculation and for steps. If you have tips or any kind of advice, your welcome.
