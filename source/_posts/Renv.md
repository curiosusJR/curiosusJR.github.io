---
title: R语言环境变量
tags:
  - config
  - Rstudio
  - Renv
  - Rmarkdown
  - Beamer
categories:
  - blogs
date: 2023-04-07 20:47:49
---

之前也遇到过R语言环境变量配置方面的问题，最近又遇到，每次都要花一些时间搜索，这种重复工作很令人沮丧，在此简单记录：
![](Pasted%20image%2020241217141314.png)


用R markdown转bemaer tex的时候，我希望能对tex文件直接编辑，使其更灵活、更符合我的需求，而转换中用的knit会自动删除tex文件，此处需要在头部的yaml中声明。这里Rstudio会自动翻译yaml头部声明，提供可视化的option选项，在knit旁边的设置（齿轮图标）中，然而，只有当yaml格式符合标准时，option选项才会出现，如果没有option选项，请重新生成默认的yaml头部声明，此时设置菜单中会出现“output options”，其中在“Advanced”选项卡中勾选“Keep tex source file”选项。该操作等价于头部声明：
```yaml
output: 
  beamer_presentation: 
    keep_tex: yes
```

