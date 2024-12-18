---
title: Daily work
tags:
  - daily
  - work
categories:
  - diaries
  - TODO
date:
---
*automatic update via todo-list*


---
## 2024/08/10 (10.4h)
### Doing tasks

### Done tasks
- ‼edit my blog and organize files (10.4h)

### Todo tasks in this week
- ‼模型描述: build the zero-evolution and add para; vim zhongqi_latex/src/03_model.tex and 00-daily*.md though
- learning model adding and config in revbayes
- make a model list for revbayes P3
- 输入文件格式，即数据来源
- 研究一下qmk，把轨迹球移动之后自动切换到第三层这件事给取消掉，再看看有什么可以配置玩的。
- align with magus？
- ON dating: run muscle in align and test mode via its online document.
- alignment is not much usefull on such huge dataset, why? or these gaps is normal on such taxa_num datasets? Filt them into small dataset will influent the pps_result?
- Can I get any acceptable pps_result?
- current running : mito_dataset. mft-ginsi/magus on dating; rb_pps on tower. check the result

### Memo & Comments
- #char_type:335069
- edit blog in autodaily, add TODOLIST/WISHLIST in hexo, edit via obsidian. 
- Write my thesis paper via mdbook; 
- Maybe I should use mdbook instead of beamer for presentation, not hexo for documentation, maybe. #mdbook #hexo #todo #obsidian #blog 
- Using todo list and hexo-blog via obsidian for daily work, using mdbook for presentation.


---
## 2024/08/10 (5.8h)
### Doing tasks

### Done tasks
- align with #magus ？ (0.0h) #alignment
- current running : mito_dataset. mft-ginsi/magus on dating; rb_pps on tower. check the result (2.3h) #alignment 
- my vpn maybe broken, check it. (0.5h) 
- config my workflow consist of todo/hexo/obsidian/mdbook/blog-README (3.0h)

### Todo tasks in this week
- ‼模型描述: build the zero-evolution and add para; vim zhongqi_latex/src/03_model.tex and 00-daily*.md though
- learning model adding and config in revbayes
- make a model list for revbayes P3
- 输入文件格式，即数据来源
- 研究一下qmk，把轨迹球移动之后自动切换到第三层这件事给取消掉，再看看有什么可以配置玩的。
- ON dating: run muscle in align and test mode via its online document.
- alignment is not much usefull on such huge dataset, why? or these gaps is normal on such taxa_num datasets? Filt them into small dataset will influent the pps_result?
- Can I get any acceptable pps_result?
- Edit TODO-list and mdbook-files for ensuring they are in correct format.

### Memo & Comments
- #char_type: 367368
- QiXi Festeval so that I did not much work today. 
- Well, it's weekend, just finish my workflow building tomorrow.


---
## 2024/08/12 (10.7h)
### Doing tasks

### Done tasks
- ‼ON dating: run muscle in align and test mode via its online document. (0.0h)
- ‼Edit TODO-list and mdbook-files for ensuring they are in correct format. (10.7h)

### Todo tasks in this week
- build my init dataset_list #fit_data
- rewrite align.sh #fit_test
- clear my basic rule of my model. #robustness_model

### Memo & Comments
#char_type : 403606; 
align.sh was wrong, I should align codon, not just nuc. maybe all align should be rerun, but i just need choose only one. it is not a big thing now.


---
## 2024/08/13 (8.6h)
### Doing tasks

### Done tasks
- ‼build a init dataset_list, maybe just hemiptera but i should make them into datasets, not library. #fit_data (6.3h) 
- get acc from shit_csv files. #fit_data (2.3h)

### Todo tasks in this week
- rewrite align.sh #fit_test
- clear my basic rule of my model. #robustness_model
- ‼download data from acc #fit_data

### Memo & Comments
#char_type : 434840;


---
## 2024/08/14 (8.1h)
### Doing tasks

### Done tasks
- ‼download data from acc (4.0h)
- align them into datasets. (4.1h)

### Todo tasks in this week
- rewrite align.sh #fit_test
- clear my basic rule of my model. #robustness_model
- align mito_2012/2019 cds #fit_data 

### Memo & Comments
#char_type : 456049 ; 
- mafft-xinsi for rrna and mafft-linsi for cds? #alignment 


---
## 2024/08/15 (9.9h)
### Doing tasks
- align mito_2012/2019 cds #fit_data (10.0h)

### Done tasks
- rewrite align.sh #fit_test (1.0h)
- check linsi/ginsi/einsi diff. (0.7h)
- run GTR rb_pps_data in current dataset. #fit_test #pps (8.2h)

### Todo tasks in this week
- ‼clear my basic rule of my model. #robustness_model
- current running: Dating: rb_pps. tower: mito_9/2_annotate; check the result.

### Memo & Comments
#char_type : 486401; 
- whole mito data cannot be split into genes simply. maybe I just need to test the whole align and the partial gene data. It's not important so it will be ok. 
- maybe I need to cut some column via seqkit or seqconverter because of gaps and maybe I can get better dataset.


---
## 2024/08/15 (8.7h)
### Doing tasks

### Done tasks
- ‼align mito_2012/2019 cds #fit_data (0.0h)
- current running: Dating: rb_pps. tower: mito_9/2_annotate; check the result. (2.7h)
- try to cut gap column after align(triml seqkit seqconverter). #fit_test #alignment (0.0h)
- ‼find the way of getting char/vars in rb. #fit_test #pps #revbayes (0.0h)
- find the way to use super computer. (0.0h)
- rb_pps for genomic dataset, bact, ahe (0.0h)

### Todo tasks in this week
- ‼clear my basic rule of my model. #robustness_model
- understand the revbayes protocol
- current running: dating: bcod_rb_pps; tower: mito2019rna_align, bactCao_rbpps. check the result
- to be run: ahes_Cao_rbpps, mito2/9_rb_pps;
 
### Memo & Comments
#char_type : 522966;
- list models, check every datasets. I need a table.
- Beside revbayes, I need some other tests, maybe.
- I need test the best model they used or best model under model-finder, not just GTR.
- Covarian and GHOST, how to test?
- maybe I should learn about how to enter model file into revbayes first, then think about my model.

---
## 2024/08/17 (11.0h)
### Doing tasks

### Done tasks
- current running: dating: bcod_rb_pps; tower: mito2019rna_align, bactCao_rbpps. check the result (1.4h)
- list models i should test and find out how to test/ input them into revbayes. #fit_test  (9.6h)

### Todo tasks in this week
- ‼clear my basic rule of my model. #robustness_model
- understand the revbayes protocol
- to be run: ahes_Cao_rbpps, mito2/9_rb_pps;
- I need a stand table for dataset/model/vars check.

### Memo & Comments
#char_type : 541852

---
## 2024/08/18 (8.2h)
### Doing tasks

### Done tasks
- understand the revbayes protocol (0.0h)
- which covarian-like model i need to test? Should I discuss the "test conflict" between model fit and heterogenety test? #fit_test  (5.5h)
- how to sample from pps? (2.7h)

### Todo tasks in this week
- ‼clear my basic rule of my model. #robustness_model
- to be run: ahes_Cao_rbpps, mito2/9_rb_pps;
- I need a stand table for dataset/model/vars check.
- how to get dataset from treebase? #fit_data

### Memo & Comments
#char_type : 570013


---
## 2024/08/19 (5.6h)
### Doing tasks

### Done tasks
- to be run: ahes_Cao_rbpps, mito2/9_rb_pps; (1.9h)
- I need a stand table for dataset/model/vars check. (0.0h)
- rewrite auto.sh  (3.7h)

### Todo tasks in this week
- clear my basic rule of my model. #robustness_model
- how to get dataset from treebase? #fit_data
- genrate genral pps protocol. not only revbayes. and make a change with the protocol in pp calculation (maybe parameter selection or model mixture) #fit_test

### Memo & Comments
#char_type: 593248; 


---
## 2024/08/20 (7.6h)
### Doing tasks

### Done tasks
- generate a couse viewer for datasets. #fit_cause (7.6h)

### Todo tasks in this week
- clear my basic rule of my model. #robustness_model
- how to get dataset from treebase? #fit_data
- genrate genral pps protocol. not only revbayes. and make a change with the protocol in pp calculation (maybe parameter selection or model mixture) #fit_test

### Memo & Comments
#char_type : 614842
* 今天发现之前的p-value计算脚本出错了，sim和emp的比较错了一位，已经改正
* 理解了R做图的脚本，发现没啥用，不如直接用pvalue脚本
* 理解了pvalue脚本的输出，其中low和upper就是emp值在pp分布中的上和下的概率，但是这都包括了恰好等于的部分，所以mid是把恰好等于取一半的修正，然后效应量是计算“模拟行为多大程度改变了样本总体”，效应量越小越好，太大不好。


---
## 2024/08/30 (24.5h)
### Doing tasks

### Done tasks
- how to get dataset from treebase? #fit_data (0.0h)
- genrate genral pps protocol. not only revbayes. and make a change with the protocol in pp calculation (maybe parameter selection or model mixture) #fit_test (18.7h)
- why there are some 'nan' in eff-test?  (5.8h)

### Todo tasks in this week
- clear my basic rule of my model. #robustness_model
- ‼generate phylobayes approach. #fit_test

### Memo & Comments
#char_type : 666424


---
## 2024/08/31 (10.2h)
### Doing tasks

### Done tasks
- ‼generate phylobayes approach. #fit_test (10.2h)
- current run: pb_ances_test in tower and ahe_rb_pps in dating(because of memery limit in tower).  (0.0h)

### Todo tasks in this week
- clear my basic rule of my model. #robustness_model

### Memo & Comments
#char_type : 696500


---
## 2024/09/04 (18.2h)
### Doing tasks

### Done tasks
- clear my basic rule of my model. #robustness_model (0.1h)
- ‼what is next? how long will i run? how to compare?  (11.7h)
- learn covarion model and matrix in revbayes (2.9h)
- learn about Q matrix in markov process (3.5h)

### Todo tasks in this week
- download data from treebase, generate a protocol. #fit_data
- ‼Simulate data in various rate/composition parameters. #fit_data
- PhyloMAd? Is it generate a different test? well, actually I just need to calculate the posterior predictive distribution for now. If PhyloMAd just generate different statistics, I can study it later.

### Memo & Comments
#char_type : 769353 


---
## 2024/09/05 (3.0h)
### Doing tasks
- using parallel for pb_cm2. (-12.7h)

### Done tasks
- learn about covarion model (3.0h)

### Todo tasks in this week
- download data from treebase, generate a protocol. #fit_data
- ‼Simulate data in various rate/composition parameters. #fit_data
- PhyloMAd? Is it generate a different test? well, actually I just need to calculate the posterior predictive distribution for now. If PhyloMAd just generate different statistics, I can study it later.

### Memo & Comments
#char_type : 826647 


---
## 2024/09/08 (23.8h)
### Doing tasks

### Done tasks
- using parallel for pb_cm2. (0.0h)
- learn about covarion model (0.0h)
- check the cov model file (23.8h)

### Todo tasks in this week
- download data from treebase, generate a protocol. #fit_data
- ‼Simulate data in various rate/composition parameters. #fit_data
- PhyloMAd? Is it generate a different test? well, actually I just need to calculate the posterior predictive distribution for now. If PhyloMAd just generate different statistics, I can study it later.

### Memo & Comments
#char_type : 879369


---
## 2024/09/10 (13.7h)
### Doing tasks

### Done tasks
- build a mbl model file. (13.7h)
- 通过几个数据集计算phylobayes和revbayes的simulation是否有区别。后续全面转向phylobayes和其他语言吧，rev不靠谱。 (0.0h)

### Todo tasks in this week
- download data from treebase, generate a protocol. #fit_data
- ‼Simulate data in various rate/composition parameters. #fit_data
- PhyloMAd? Is it generate a different test? well, actually I just need to calculate the posterior predictive distribution for now. If PhyloMAd just generate different statistics, I can study it later.
- 构建mmms和ghost的实现？或者找办法模拟一下。

### Memo & Comments
#char_type : 907274


---
## 2024/09/11 (0.0h)
### Doing tasks

### Done tasks

### Todo tasks in this week
- download data from treebase, generate a protocol. #fit_data
- ‼Simulate data in various rate/composition parameters. #fit_data
- PhyloMAd? Is it generate a different test? well, actually I just need to calculate the posterior predictive distribution for now. If PhyloMAd just generate different statistics, I can study it later.
- 构建mmms和ghost的实现？或者找办法模拟一下。
- JC_mbl的文件还差一点，就是var输出的时候格式有一点不对，pps跑不起来，应该是branchlenth输出不应该是向量的问题吧，test.var3可以跑，查看一下原因。

### Memo & Comments
#char_type : 929101


---
## 2024/09/17 (0.0h)
### Doing tasks
- ‼Simulate data in various rate/composition parameters. #fit_data (-19.8h)

### Done tasks
- PhyloMAd? Is it generate a different test? well, actually I just need to calculate the posterior predictive distribution for now. If PhyloMAd just generate different statistics, I can study it later. (0.0h)
- 构建mmms和ghost的实现？或者找办法模拟一下。 (0.0h)
- JC_mbl的文件还差一点，就是var输出的时候格式有一点不对，pps跑不起来，应该是branchlenth输出不应该是向量的问题吧，test.var3可以跑，查看一下原因。 (0.0h)

### Todo tasks in this week
- download data from treebase, generate a protocol. #fit_data
- read lie markov model paper. 

### Memo & Comments
#char_type : 968136


---
## 2024/09/19 (0.0h)
### Doing tasks
- ‼Simulate data in various rate/composition parameters. #fit_data (-21.9h)
- read “alisim not good enough” paper (-22.4h)

### Done tasks
- read lie markov model paper.  (0.0h)

### Todo tasks in this week
- download data from treebase, generate a protocol. #fit_data

### Memo & Comments
#char_type : 983605


---
## 2024/09/22 (0.0h)
### Doing tasks
- ‼Simulate data in various rate/composition parameters. #fit_data (-12.9h)

### Done tasks
- read “alisim not good enough” paper (0.0h)

### Todo tasks in this week
- download data from treebase, generate a protocol. #fit_data
- read fbd paper and learn about it.

### Memo & Comments
#char_type : 992598 


---
## 2024/09/24 (0.0h)
### Doing tasks

### Done tasks

### Todo tasks in this week
- download data from treebase, generate a protocol. #fit_data
- Simulate data in various rate/composition parameters. #fit_data
- ‼read fbd paper and learn about it.

### Memo & Comments
#char_type : 1020221


---
## 2024/09/27 (0.0h)
### Doing tasks
- ‼read fbd paper and learn about it. (-13.9h)

### Done tasks

### Todo tasks in this week
- download data from treebase, generate a protocol. #fit_data
- Simulate data in various rate/composition parameters. #fit_data

### Memo & Comments
#char_type : 1037327


---
## 2024/09/29 (0.0h)
### Doing tasks

### Done tasks
- ‼read fbd paper and learn about it. (0.0h)

### Todo tasks in this week
- download data from treebase, generate a protocol. #fit_data
- Simulate data in various rate/composition parameters. #fit_data
- ‼learn about alisim in jc_cov or something(ghost?). #fit_data

### Memo & Comments
#char_type : 1043569


---
## 2024/10/07 (0.0h)
### Doing tasks
- ‼learn about alisim in jc_cov or something(ghost?). #fit_data (-13.9h)

### Done tasks

### Todo tasks in this week
- download data from treebase, generate a protocol. #fit_data
- Simulate data in various rate/composition parameters. #fit_data
- edit bin/simulator.sh in mac:workplace/test/. #fit_data

### Memo & Comments
#char_type : 1059768


---
## 2024/10/14 (4.4h)
### Doing tasks

### Done tasks
- download data from treebase, generate a protocol. #fit_data (0.0h)
- Simulate data in various rate/composition parameters. #fit_data (0.0h)
- ‼learn about alisim in jc_cov or something(ghost?). #fit_data (4.4h)
- edit bin/simulator.sh in mac:workplace/test/. #fit_data (0.0h)
- test if alisim is same as revbayes pps. #fit_data (0.0h)
- covarion model format translate via phylogears #fit_data (0.0h)

### Todo tasks in this week
- sync my simulator.sh into tower. #fit_data

### Memo & Comments
#char_type : 1104641


---
## 2024/10/16 (1.7h)
### Doing tasks

### Done tasks
- sync my simulator.sh into tower. #fit_data (1.0h)
- zhongqii files. (0.0h)
- Liang Zonglei\`s bpp. (0.7h)
- learn about \<expected pps\> article.  (0.0h)

### Todo tasks in this week
- R script learning #fit_cause

### Memo & Comments
#char_type : 1115319

---
## 2024/10/31 (12.6h)
### Doing tasks

### Done tasks
- R script learning #fit_cause (3.5h)
- HPC learn. (7.7h)
- combine data and inf into one script. (1.4h)
- parallel auto in hpc. (0.0h)
- test mpi time used (0.0h)
- test parallel and mpi time used  (0.0h)

### Todo tasks in this week
- inferrence in R. #fit_cause
- learn about R analysis.
- error cascades pippeline. 
- short seqs run under a suitable cores number. 
- sims run experimental design.

### Memo & Comments
#char_type : 1381138


---
## 2024/11/06 (0.0h)
### Doing tasks
- build a donelist pipeline between hpc and tower (-13.6h)

### Done tasks
- short seqs run under a suitable cores number.  (0.0h)
- storage usage in hpc report; (0.0h)
- archive xz in auto.sh; (0.0h)
- done file list check between hpc and tower (0.0h)
- old done output. xz and tar. (0.0h)

### Todo tasks in this week
- ‼inferrence in R. #fit_cause
- learn about R analysis.
- error cascades pippeline. 
- ‼Based on F81 Model sets, design sims run experimental.
- read science causual infer paper. 
-  file translation;

### Memo & Comments
#char_type : 1540811


---
## 2024/12/01 (0.0h)
### Doing tasks

### Done tasks
- ‼inferrence in R. #fit_cause (0.0h)
- learn about R analysis. (0.0h)
- read science causual infer paper.  (0.0h)
-  file translation; (0.0h)
- build a donelist pipeline between hpc and tower (0.0h)
- read causal inference. (0.0h)
- learn about tree comparation. rf distance; quartet distance. alias. (0.0h)
- ‼make a plot for zhongqii ppt. (0.0h)
- change the color of heatmap_smooth (0.0h)
- edit the code of raw_summary.txt.fmt in R.  (0.0h)
- fig 4 add motation. (0.0h)

### Todo tasks in this week
- error cascades pippeline. 
- ‼Based on F81 Model sets, design sims run experimental.
- make a base matrix for analysis. 
- my pps rev code. make topology prior be the same. test its influence in a small dataset. 
- ‼read hohna paper 2023: model selection is no
- read yang ziheng paper : 2005 branch length prior influences. 
- add convergence evaluation

### Memo & Comments
#char_type : 1879514


---
## 2024/12/13 (0.0h)
### Doing tasks

### Done tasks

### Todo tasks in this week
- error cascades pippeline. 
- ‼Based on F81 Model sets, design sims run experimental.
- make a base matrix for analysis. 
- my pps rev code. make topology prior be the same. test its influence in a small dataset. 
- ‼read hohna paper 2023: model selection is no
- read yang ziheng paper : 2005 branch length prior influences. 
- add convergence evaluation
- change ppt $problem to a frame. 
- year summary. make a plan for next-step working.

### Memo & Comments
#char_type : 2015115


---
## 2024/12/15 (0.0h)
### Doing tasks

### Done tasks
- make a base matrix for analysis.  (0.0h)
- change ppt $problem to a frame.  (0.0h)
- year summary. make a plan for next-step working. (0.0h)
- learn about argc (0.0h)
- make ai server env (0.0h)

### Todo tasks in this week
- error cascades pippeline. 
- ‼Based on F81 Model sets, design sims run experimental.
- my pps rev code. make topology prior be the same. test its influence in a small dataset. 
- ‼read hohna paper 2023: model selection is no
- read yang ziheng paper : 2005 branch length prior influences. 
- add convergence evaluation

### Memo & Comments
#char_type : 2063913




---
## 2024/12/16 (0.0h)
### Doing tasks

### Done tasks

### Todo tasks in this week
- "build your own group". send a email to Prof. Luo Arong
- year-end summary slides for group willing.
- ‼integrate aichat and todo and my hexo blog together

### Memo & Comments
#char_type : 2085460


#ai_shell: 
你的工作包括文件和目录操作（如复制、移动）、配置文件编辑、脚本编写与调试、以及使用`aichat`等工具处理任务管理、信息查询等相关事务。
 #aichat: 
这两天的工作内容基本没有变化，包括向罗教授发送邮件、为意愿小组制作年终总结幻灯片以及将AI聊天工具、待办事项和Hexo博客整合在一起。

---
## 2024/12/18 (0.0h)
### Doing tasks

### Done tasks
- ‼integrate aichat and todo and my hexo blog together (0.0h)
- revbayes in rstudio and rmarkdown for beamer (0.0h)

### Todo tasks in this week
- year-end summary slides for group will.
- statistics cor re-check
- clear the purpose that contacting Prof. Luo
- With the purposes, make a list that i need to do before sending email

### Memo & Comments
#char_type : 2115970


#ai_shell: 
It looks like you have a variety of commands and operations that are intended for use in a shell environment. To address your request, I'll provide explanations for some of the commands, clean up the sequence where possible, and add guidance on how to effectively use `aichat`.

Firstly, let's focus on cleaning and correcting some of the commands:

1. **Shell Commands**:
   - `cd` command: This changes the directory in your shell.
     ```sh
     cd workplace/blog/hexo/source/_posts/
     ```
   - `ls` command: This lists the files in a directory.
     ```sh
     ls diary/autodaily.md
     ```
   - `mkdir` command: This creates a new directory.
     ```sh
     mkdir year-end
     ```
   - `iqtree` commands: These are for running phylogenetic analyses using IQ-TREE. 
     ```sh
     iqtree --alisim alignment -m JC2 -t RANDOM{yh/20} --length 1000 --redo
     ```

2. **Using `aichat`**:
   - `aichat` seems to be a command-line utility that you are using for generating text or code. Ensure that it is properly installed and configured in your environment.
   - The `-r %code%` flag suggests that you might want to generate some code, but `%code%` might need to be replaced with the specific coding task you want.

Here's a revised sequence of commands focused on running phylogenetic analysis using IQ-TREE and utilizing `aichat` for possibly generating or analyzing code:

```sh
# Move to the workspace directory
cd workplace/year-end

# Simulate alignment data and analyze it using IQ-TREE with alisim model
iqtree --alisim alignment -m JC2 -t RANDOM{yh/20} --length 1000 --redo

# List files to verify presence of generated alignment file
ls

# Run IQ-TREE analysis on the newly generated alignment file
iqtree -s alignment.phy -m MFP -B 1000 --redo

# Use aichat to analyze or generate some code related toIQ-TREE output or another task
aichat -r "Analyze the IQ-TREE results and suggest improvements in model selection"

# Exit current session if needed
exit
```

To ensure everything works as expected:
- Make sure `iqtree` is installed on your system.
- Ensure that `aichat` is correctly set up, including any API keys or credentials required.

If you have specific tasks for `aichat`, such as generating a script or analyzing results, replace the prompt with the precise instructions you want to provide. For instance:

```sh
# Generate a Bash script to automate IQ-TREE analysis using alisim model
aichat -r "Generate a Bash script for automated IQ-TREE analysis using alisim model"
```

For more detailed help with `aichat` itself, check its documentation or use:

```sh
aichat -h
```

If you have specific questions about any part of the commands or need further assistance, feel free to ask!
 #aichat: 
这两天的工作变化集中在完成了将AI聊天、待办事项与Hexo博客集成的任务，同时在年终总结幻灯片和统计检查方面有所进展，并开始整理与教授罗泳涌联系的目的及其所需准备的事项。
