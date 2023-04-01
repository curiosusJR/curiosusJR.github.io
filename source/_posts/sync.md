---
title: sync
date: 2023-03-19 17:07:49
tags:
---

## build enviroment
1. install node, git and hexo;
2. git clone -b hexo https://github.com/curiosusJR/curiosusJR.github.io.git curiosus
3. cd cuirosus && sudo npm install # init config and packages

## github authentication
1. "hexo d" and "git push" commands MAYBE need to authenticate github by token, or token maybe disappear;
2.  only *repo* and *workflow* is necessary.
3. token for hexo: vim ./_config.yml
```
deploy:
  type: git
  repository: https://<token-for-hexo>@github.com/<user.name>/<repo.name>.git 
  branch: master
  name: <user.name>
  email: <email-address>
```

4. token for git: vim ./.git/config
```
[remote "origin"]
	url = https://<token-for-hexo>@github.com/<user.name>/<repo.name>.git 
```

## daily use
1. git pull # for latest data
2. git branch -vv # check branch matchup between local and remote
3. hexo n "\<title\>" # hexo g; hexo d; et.al 
**NOTE: "hexo d" update the master branch contain website in github**
4. git add . && git commit -m "<msg>" && git push # remember use command "git push" without "origin hexo" only when "git branch -vv" results a correct matchup. 
**NOTE: git push up date hexo branch contain source data**

# reference
1. https://www.jianshu.com/p/85f455afcfcf
2. https://www.jianshu.com/p/6ecb3adfefbd

# TODO
1. <https://linux.cn/article-13119-1.html> for RAW picture.
2. <https://zhuanlan.zhihu.com/p/34964970> for image format convert
