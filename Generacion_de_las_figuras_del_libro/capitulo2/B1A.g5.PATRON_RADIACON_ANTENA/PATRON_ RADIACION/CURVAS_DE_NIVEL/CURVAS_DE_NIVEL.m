clc
clear all

theta = [0:((10*pi)/180):2*pi];
rho0 = xlsread('CN0P');

polarplot(theta,rho0);


 hold on
 
 rho90 = xlsread('CN90P');
 polarplot(theta,rho90,'--');

rho180 = xlsread('CN180P');
polarplot(theta,rho180,'-.');

title('CURVAS DE NIVEL A 0°,90°,180°')


legend('Curva de nivel con Angulo Azimut (Phi=0°)', 'Curva de nivel con Angulo Azimut (Phi=90°)', 'Curva de nivel con Angulo Azimut (Phi=180°)')