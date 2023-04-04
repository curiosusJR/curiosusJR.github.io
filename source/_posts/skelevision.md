---
title: Measure insect male external genitalia by skelevision protocol
tags:
  - null
categories:
  - null
date: 2023-04-03 20:47:49
---


[Skelevision](https://github.com/bcweeks/Skelevision) is a wonderful work which is a automatically protocol to measure birds bones using man-made labels. When I see those skeletal specimens, I think they are kind of similar to insect male external genitalia. I don't have any experience with machine learning but thanks to the detailed README file of [Skelevision](https://github.com/bcweeks/Skelevision), even it starts from installing conda, I can reproduce the whole  protocol to my computer and learn it.

# Pictures Preparation 

I was fortunate to have the pictures from a leafhopper subfamily taken by Dr. Liang Zonglei. These \*.tiff pictures's name are unformatted so let's begin with pics format converting and name formatting.

## Format converting
Using ffmpeg to convert the pics format. Tiff files are scattered accross various levels of folders so we need a little script to handle this.

**Tips:** If there are spaces in file name, use `rename \  _ **/* ` to convert spaces to '\_'.

```
k=0;
for i in `ls **/*.tif`; 
do 
ffmpeg -i $i $i.png; 
rm $i;-
mv $i.png ../format_convert/$k.png
((k=$k+1));
done;
```



## Databasing

***hold on***

# Annotate
Just like authors did in [their research](https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.13864) , I annotate pictures using [VGG](https://www.robots.ox.ac.uk/~vgg/software/via/). I tried to annotate 6 pictures and estimate the time I should use to train. 

Add selected pictures to VGG and draw 5 different regions each picture.  Press **[Enter]** to finish drawing the region or press [Esc] to cancel.  Define 5 attributes. 
Select type as `dropdown` from the list of available options and define option values as shown in screenshot below. Click the regions and define annotations. In the end, export annotations in coco format.

Use skelevision scripts shown in github to train pictures. cpu runs in 2 weeks.

**DATE: 2023.4.4 TO BE CONTINUE**
