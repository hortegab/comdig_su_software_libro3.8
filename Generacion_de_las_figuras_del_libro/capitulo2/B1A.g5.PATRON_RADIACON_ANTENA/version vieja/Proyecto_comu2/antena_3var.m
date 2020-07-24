clc
clear all ;
close all ;

arch = xlsread('comu');
%Esfera de radio unitario en coordenadas esféricas
phi = arch(2:28,1);
theta = arch(1,2:28);
r = arch(32:58,29);

%Construcción de malla
[phi,theta] = meshgrid(phi,theta);
r = meshgrid(r);

%La conversión se realiza después de construir la malla
[X,Y,Z] = sph2cart(theta,phi,r);

mesh(X,Y,Z), axis equal

