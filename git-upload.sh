#!/bin/bash/
if [$# == 1]
then
git config --global user.name bandiclv             
git add . 
#git commit -m "20180918"
git commit -m $1
git push origin master
fi 




