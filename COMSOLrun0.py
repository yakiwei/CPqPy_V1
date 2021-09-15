# ------------------------------calculate first step in COMSOL-----------



inputcomsolstr0 = """

function out = model
%
% pesti00000.m
%
% Model exported on Jan 12 2021, 21:54 by COMSOL 5.2.1.152.

import com.comsol.model.*
import com.comsol.model.util.*

model = ModelUtil.create('Model');

model.modelPath('F:\Pycharm\COMSOL_phreeqc');

model.label(['pesti.mph']);

model.comments(['Pesticide Transport and Reaction ieAmination of soil through Aldicarb transport and reaction.']);

model.param.set('k_1', '0.36[1/d]', 'Rate constant, reaction 1');
model.param.set('k_2', '0.024[1/d]', 'Rate constant, reaction 2');
model.param.set('k_3', '0.2[1/d]', 'Rate constant, reaction 3');
model.param.set('k_4', '0.01[1/d]', 'Rate constant, reaction 4');
model.param.set('k_5', '0.0524[1/d]', 'Rate constant, reaction 5');
model.param.set('rho', '1e3[kg/m^3]', 'Fluid density');
model.param.set('thetas_1', '0.339', 'Porosity, layer 1');
model.param.set('thetas_2', '0.399', 'Porosity, layer 2');
model.param.set('thetar_1', '0.001', 'Residual saturation, layer 1');
model.param.set('thetar_2', '0.001', 'Residual saturation, layer 2');
model.param.set('Ss_1', '0.339[1/m]/(g_const*rho)', 'Storage coefficient, layer 1');
model.param.set('Ss_2', '0.399[1/m]/(g_const*rho)', 'Storage coefficient, layer 2');
model.param.set('Ks_1', '0.454[m/d]', 'Saturated hydraulic conductivity, layer 1');
model.param.set('Ks_2', '0.298[m/d]', 'Saturated hydraulic conductivity, layer 2');
model.param.set('alpha_1', '1.39[1/m]', 'Parameter alpha, layer 1');
model.param.set('alpha_2', '1.74[1/m]', 'Parameter alpha, layer 2');
model.param.set('n_1', '1.6', 'Parameter n, layer 1');
model.param.set('n_2', '1.38', 'Parameter n, layer 2');
model.param.set('Hp0', '0.01[m]', 'Pressure head in the ring');
model.param.set('N0', '0.01*Ks_1*rho', 'Leak from the base');
model.param.set('c0', '1[mol/m^3]', 'Solute concentration in the ring');
model.param.set('rhob', '1300[kg/m^3]', 'Bulk density');
model.param.set('kp_a', '1e-4[m^3/kg]', 'Partition coefficient, aldicarb');
model.param.set('kp_asx', '0.5e-4[m^3/kg]', 'Partition coefficient, aldicarb sulfoxide');
model.param.set('kp_asn', '2e-4[m^3/kg]', 'Partition coefficient, aldicarb sulfone');
model.param.set('Dl', '3.74e-3[m^2/d]', 'Diffusion coefficient, liquid phase');
model.param.set('Dg', '0.432[m^2/d]', 'Diffusion coefficient, gas phase');
model.param.set('alphar', '0.005[m]', 'Longitudinal dispersivity');
model.param.set('alphaz', '0.001[m]', 'Transverse dispersivity');
model.param.set('kg_a', '1.33e-7', 'Volatilization');
model.param.set('kg_asn', '1.33e-3', 'Volatilization');
model.param.set('d_s', '0.05[m]', 'Thickness of the concentration boundary layer');

model.modelNode.create('comp1');

model.geom.create('geom1', 2);

model.file.create('res2');

model.geom('geom1').axisymmetric(true);

model.mesh.create('mesh1', 'geom1');

model.geom('geom1').create('r1', 'Rectangle');
model.geom('geom1').feature('r1').set('size', {'1.25' '0.9'});
model.geom('geom1').feature('r1').set('pos', {'0' '-1.3'});
model.geom('geom1').create('r2', 'Rectangle');
model.geom('geom1').feature('r2').set('size', {'1.25' '0.4'});
model.geom('geom1').feature('r2').set('pos', {'0' '-0.4'});
model.geom('geom1').create('pt1', 'Point');
model.geom('geom1').feature('pt1').setIndex('p', '0.25', 0, 0);
model.geom('geom1').feature('pt1').setIndex('p', '0', 1, 0);
model.geom('geom1').run;

model.variable.create('var1');
model.variable('var1').model('comp1');
model.variable('var1').set('r_1', 'k_1*c_a', 'Rate expression 1');
model.variable('var1').set('r_2', 'k_2*c_asx', 'Rate expression 2');
model.variable('var1').set('r_3', 'k_3*c_a', 'Rate expression 3');
model.variable('var1').set('r_4', 'k_4*c_asx', 'Rate expression 4');
model.variable('var1').set('r_5', 'k_5*c_asn', 'Rate expression 5');

model.view.create('view2', 3);

model.physics.create('dl', 'RichardsEquation', 'geom1');
model.physics('dl').create('remm2', 'RichardsEquationModel', 2);
model.physics('dl').feature('remm2').selection.set([2]);
model.physics('dl').create('init2', 'init', 2);
model.physics('dl').feature('init2').selection.set([2]);
model.physics('dl').create('ph1', 'PressureHead', 1);
model.physics('dl').feature('ph1').selection.set([5]);
model.physics('dl').create('mf1', 'MassFlux1', 1);
model.physics('dl').feature('mf1').selection.set([2]);
model.physics.create('tds', 'DilutedSpeciesPorousMedia', 'geom1');
model.physics('tds').field('concentration').field('c_a');
model.physics('tds').field('concentration').component({'c_a' 'c_asx' 'c_asn'});
model.physics('tds').create('out1', 'Outflow', 1);
model.physics('tds').feature('out1').selection.set([2 7 8]);
model.physics('tds').create('conc1', 'Concentration', 1);
model.physics('tds').feature('conc1').selection.set([5]);

model.mesh('mesh1').create('ftri1', 'FreeTri');
model.mesh('mesh1').feature('ftri1').create('size1', 'Size');
model.mesh('mesh1').feature('ftri1').feature('size1').selection.geom('geom1', 2);
model.mesh('mesh1').feature('ftri1').feature('size1').selection.set([2]);

model.view('view1').axis.set('abstractviewrratio', '0.8259299993515015');
model.view('view1').axis.set('abstractviewlratio', '-0.8259299397468567');
model.view('view1').axis.set('abstractviewxscale', '0.003854447742924094');
model.view('view1').axis.set('abstractviewbratio', '-0.05000004544854164');
model.view('view1').axis.set('xmax', '2.247722625732422');
model.view('view1').axis.set('xmin', '-0.9977223873138428');
model.view('view1').axis.set('abstractviewyscale', '0.0038544475100934505');
model.view('view1').axis.set('ymax', '0.13630735874176025');
model.view('view1').axis.set('ymin', '-1.4363073110580444');
model.view('view1').axis.set('abstractviewtratio', '0.05000004544854164');

model.physics('dl').feature('remm1').set('rho', 'rho');
model.physics('dl').feature('remm1').set('thetas', 'thetas_1');
model.physics('dl').feature('remm1').set('thetar', 'thetar_1');
model.physics('dl').feature('remm1').set('ktype', 'conductivity');
model.physics('dl').feature('remm1').set('Ks', {'Ks_1'; '0'; '0'; '0'; 'Ks_1'; '0'; '0'; '0'; 'Ks_1'});
model.physics('dl').feature('remm1').set('Storage', 'userdef');
model.physics('dl').feature('remm1').set('S', 'Ss_1');
model.physics('dl').feature('remm1').set('alpha', 'alpha_1');
model.physics('dl').feature('remm1').set('n_es', 'n_1');
model.physics('dl').feature('init1').set('InitType', 'Hp');
model.physics('dl').feature('init1').set('Hp', '-(z+1.2)');
model.physics('dl').feature('remm2').set('rho', 'rho');
model.physics('dl').feature('remm2').set('thetas', 'thetas_2');
model.physics('dl').feature('remm2').set('thetar', 'thetar_2');
model.physics('dl').feature('remm2').set('ktype', 'conductivity');
model.physics('dl').feature('remm2').set('Ks', {'Ks_2'; '0'; '0'; '0'; 'Ks_2'; '0'; '0'; '0'; 'Ks_2'});
model.physics('dl').feature('remm2').set('Storage', 'userdef');
model.physics('dl').feature('remm2').set('S', 'Ss_2');
model.physics('dl').feature('remm2').set('alpha', 'alpha_2');
model.physics('dl').feature('remm2').set('n_es', 'n_2');
model.physics('dl').feature('init2').set('InitType', 'Hp');
model.physics('dl').feature('init2').set('Hp', '-(z+1.2)-0.2*(z+0.4)');
model.physics('dl').feature('ph1').set('Hp0', 'Hp0');
model.physics('dl').feature('mf1').set('N0', '-N0');
model.physics('tds').prop('TransportMechanism').set('AdsorptionInPorousMedia', '1');
model.physics('tds').prop('TransportMechanism').set('VolatilizationInPartiallySaturatedPorousMedia', '1');
model.physics('tds').prop('TransportMechanism').set('DispersionInPorousMedia', '1');
model.physics('tds').feature('pmtp1').set('epsilon_p', 'thetas_1');
model.physics('tds').feature('pmtp1').set('rho', 'rhob');
model.physics('tds').feature('conc1').set('species', {'1'; '1'; '1'});
model.physics('tds').feature('conc1').set('c0', {'c0'; '0'; '0'});

model.mesh('mesh1').feature('size').set('hauto', 2);
model.mesh('mesh1').feature('ftri1').feature('size1').set('custom', 'on');
model.mesh('mesh1').feature('ftri1').feature('size1').set('hmaxactive', true);
model.mesh('mesh1').feature('ftri1').feature('size1').set('hmax', '0.025');
model.mesh('mesh1').run;

model.frame('material1').sorder(1);

model.physics('dl').feature('remm1').set('rho_mat', 'userdef');
model.physics('dl').feature('remm2').set('rho_mat', 'userdef');
model.physics('tds').feature('pmtp1').set('epsilon_p_mat', 'userdef');
model.physics('tds').feature('pmtp1').set('rho_mat', 'userdef');
model.physics('tds').feature('pmtp1').set('minput_velocity_src', 'root.comp1.dl.u');

model.study.create('std2');
model.study('std2').create('time', 'Transient');

model.sol.create('sol2');
model.sol('sol2').study('std2');
model.sol('sol2').attach('std2');
model.sol('sol2').create('st1', 'StudyStep');
model.sol('sol2').create('v1', 'Variables');
model.sol('sol2').create('t1', 'Time');
model.sol('sol2').feature('t1').create('fc1', 'FullyCoupled');
model.sol('sol2').feature('t1').create('d1', 'Direct');
model.sol('sol2').feature('t1').feature.remove('fcDef');

model.result.dataset.create('dset2', 'Solution');
model.result.dataset.create('rev1', 'Revolve2D');
model.result.dataset('rev1').set('data', 'dset2');
model.result.dataset.remove('dset1');
model.result.create('pg5', 'PlotGroup3D');
model.result.create('pg6', 'PlotGroup2D');
model.result.create('pg7', 'PlotGroup3D');
model.result.create('pg8', 'PlotGroup2D');
model.result.create('pg9', 'PlotGroup1D');
model.result('pg5').create('surf1', 'Surface');
model.result('pg6').create('surf1', 'Surface');
model.result('pg7').create('surf1', 'Surface');
model.result('pg8').create('surf1', 'Surface');
model.result('pg9').create('lngr1', 'LineGraph');
model.result('pg9').feature('lngr1').set('data', 'dset2');
model.result('pg9').feature('lngr1').set('xdata', 'expr');
model.result('pg9').feature('lngr1').selection.set([1 3]);
model.result.export.create('data1', 'Data');
model.result.export.create('data2', 'Data');
model.result.export.create('data3', 'Data');
model.result.export.create('data4', 'Data');

model.study('std2').feature('time').set('tlist', 'range(###)');

model.sol('sol2').attach('std2');
model.sol('sol2').feature('v1').set('clist', {'range(###)'});
model.sol('sol2').feature('t1').set('tlist', 'range(###)');
model.sol('sol2').feature('t1').set('maxorder', '2');
model.sol('sol2').feature('t1').feature('fc1').set('jtech', 'once');
model.sol('sol2').feature('t1').feature('fc1').set('damp', '0.9');
model.sol('sol2').feature('t1').feature('fc1').set('maxiter', '8');
model.sol('sol2').runAll;

model.result.dataset('rev1').label('Revolution 2D');
model.result.dataset('rev1').set('genpoints', {'0' '0'; '0' '1'});
model.result.dataset('rev1').set('startangle', '-90');
model.result.dataset('rev1').set('revangle', '225');

model.result.export('data1').set('timeinterp', 'on');
model.result.export('data1').set('unit', {'mol/m^3' 'mol/m^3' 'mol/m^3'});
model.result.export('data1').set('descr', {'Concentration' 'Concentration' 'Concentration'});
model.result.export('data1').set('expr', {'c_a' 'c_asn' 'c_asx'});
model.result.export('data1').set('t', '0');
model.result.export('data1').set('filename', 'F:\Pycharm\COMSOL_phreeqc\Result\outcon0.txt');
model.result.export('data2').set('timeinterp', 'on');
model.result.export('data2').set('unit', {'mol/m^3' 'mol/m^3' 'mol/m^3'});
model.result.export('data2').set('descr', {'Concentration' 'Concentration' 'Concentration'});
model.result.export('data2').set('expr', {'c_a' 'c_asn' 'c_asx'});
model.result.export('data2').set('t', '#');
model.result.export('data2').set('filename', 'F:\Pycharm\COMSOL_phreeqc\Result\outcono.txt');
model.result.export('data3').set('descr', {'Pressure head'});
model.result.export('data3').set('timeinterp', 'on');
model.result.export('data3').set('filename', 'F:\Pycharm\COMSOL_phreeqc\Result/flowho.txt');
model.result.export('data3').set('unit', {'m'});
model.result.export('data3').set('t', '#');
model.result.export('data3').set('expr', {'dl.Hp'});
model.result.export('data4').set('descr', {'Liquid volume fraction'});
model.result.export('data4').set('timeinterp', 'on');
model.result.export('data4').set('filename', 'F:\Pycharm\COMSOL_phreeqc\Result/flowtheo.txt');
model.result.export('data4').set('unit', {'1'});
model.result.export('data4').set('t', '#');
model.result.export('data4').set('expr', {'dl.theta'});

model.result.export('data1').run
model.result.export('data2').run
model.result.export('data3').run
model.result.export('data4').run


out = model;

    """
