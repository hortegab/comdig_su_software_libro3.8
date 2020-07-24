clc 
clear all 

azimuth = xlsread('PHI_AZIMUT');
elevation = xlsread('THETA_ELEVATION');
r = xlsread('RHO_RATIO');

[azimuth,elevation] = meshgrid(azimuth,elevation);
r = meshgrid(r);

[X,Y,Z] = sph2cart(azimuth,elevation,r);

mesh(X,Y,Z), axis equal

title('PATRON DE RADIACION')

figure

plot(Z,Y)
title('PLANO DE ELEVACION')
grid on












