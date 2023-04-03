---
title: How to sync blogs between different devices 
date: 2023-04-1 17:07:49
categories:
- blogs
tags: 
- blog 
- sync
---


## build enviroment
1. install node, git and hexo;
2. git clone -b hexo https://github.com/curiosusJR/curiosusJR.github.io.git curiosus
3. cd cuirosus && sudo npm install # init config and packages

## github authentication
1. "hexo d" and "git push" commands need to authenticate github by token;
2.  only *repo* and *workflow* is necessary.

**NOTE: token should not be upload to remote repository, means .gitignore should include files below**

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

5. valid .gitignore after changing it by delet local cache:
```
git rm -r --cached .
git add .
git commit -m 'update .gitignore'
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

