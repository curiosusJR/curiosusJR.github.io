---
title: sync
date: 2023-03-19 17:07:49
tags:
---

## build enviroment
1. install node, git and hexo;
2. git clone -b hexo https://github.com/curiosusJR/curiosusJR.github.io.git curiosus
3. cd cuirosus && sudo npm install # init config and packages

## daily use
1. git pull # for latest data
2. git branch -vv # check branch matchup between local and remote
3. hexo n "" # hexo g; hexo d; et.al 
**NOTE: "hexo d" update the master branch contain website in github**
4. git add . && git commit -m "<msg>" && git push # remember use command "git push" without "origin hexo" only when "git branch -vv" results a correct matchup. 
**NOTE: git push up date hexo branch contain source data**

# reference
1. https://www.jianshu.com/p/85f455afcfcf
2. https://www.jianshu.com/p/6ecb3adfefbd

