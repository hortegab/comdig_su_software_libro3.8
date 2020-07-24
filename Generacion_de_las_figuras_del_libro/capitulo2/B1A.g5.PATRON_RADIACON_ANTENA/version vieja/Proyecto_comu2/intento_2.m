clc
clear all
close all
arch = xlsread('comu');
x=arch(32:58,1)
y= arch(32:58,2)
polarplot(x,y, 'g', 'linewidth',2)
hold on
x=arch(32:58,1);
y= arch(32:58,3);
polarplot(x,y)
hold on
x=arch(32:58,1);
y= arch(32:58,4);
polarplot(x,y)
hold on
x=arch(32:58,1);
y= arch(32:58,5);
polarplot(x,y)
hold on
x=arch(32:58,1);
y= arch(32:58,6);
polarplot(x,y, 'm', 'linewidth',2)
hold on
x=arch(32:58,1);
y= arch(32:58,7);
polarplot(x,y)
hold on
x=arch(32:58,1);
y= arch(32:58,8);
polarplot(x,y)
hold on
x=arch(32:58,1);
y= arch(32:58,9);
polarplot(x,y)
hold on
x=arch(32:58,1);
y= arch(32:58,10);
polarplot(x,y,'r','linewidth',2)
% hold on
% x=arch(32:58,1);
% y= arch(32:58,11);
% polarplot(x,y)
% hold on
% x=arch(32:58,1);
% y= arch(32:58,12);
% polarplot(x,y)
% hold on
% x=arch(32:58,1);
% y= arch(32:58,13);
% polarplot(x,y)
% hold on
% x=arch(32:58,1);
% y= arch(32:58,14);
% polarplot(x,y)
% x=arch(32:58,1);
% y= arch(32:58,15);
% polarplot(x,y, 'b','linewidth',2)





