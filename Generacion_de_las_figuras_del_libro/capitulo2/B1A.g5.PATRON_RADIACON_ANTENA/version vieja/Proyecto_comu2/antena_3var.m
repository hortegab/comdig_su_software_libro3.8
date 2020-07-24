clc
clear all ;
close all ;

arch = xlsread('comu');
%Esfera de radio unitario en coordenadas esf�ricas
phi = arch(2:28,1);
theta = arch(1,2:28);
r = arch(32:58,29);

%Construcci�n de malla
[phi,theta] = meshgrid(phi,theta);
r = meshgrid(r);

%La conversi�n se realiza despu�s de construir la malla
[X,Y,Z] = sph2cart(theta,phi,r);

mesh(X,Y,Z), axis equal

