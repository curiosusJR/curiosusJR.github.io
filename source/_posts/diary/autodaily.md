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

