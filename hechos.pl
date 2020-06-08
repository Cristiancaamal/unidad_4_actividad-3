%HECHOS PARA LA DETECCIÓN DE PROBLEMAS POR SOFTWARE/
%% % tiene(X,Y): X tiene Y
tiene(ronaldo,virus ).
tiene(jesus,lentitud).
tiene(cristian,pantallanegra).
tiene(luis,reinicio).
tiene(diana,apagon).
tiene(eduardo, parosistema).
tiene(leonel,spam).
tiene(david,noresponde).


%HECHOS PARA LA DETECCIÓN DE PROBLEMAS POR HARDWARE/
%% % error(X,Y): X error de Y
error(ronaldo, pantallarota).
error(eduardo,cambiobateria).
error(cristian,fallateclado).
error(luis, puertos).
error(diana,fallasonido).
error(eduardo, discoduro).
error(leonel,fallacargador).
error(david,mojado).
error(maria, noenciede).

%REGLAS PARA LAS PROBLEMAS POR HARDWARE

reparacion(X,falla):- error(X,pantallarota);error(X, cambiobateria);error(X, puertos);error(X,fallasonido);error(X,fallacargador);error(X,fallateclado).

sinreparacion(X):-error(X,mojado);error(X,noenciede);error(X,discoduro).




%REGLAS PARA LAS PROBLEMAS POR SOFTWARE

equipodanado(X,falla):- tiene(X,virus),tiene(X,lentitud);tiene(X,pantallanegra);tiene(X,reinicio),tiene(X,apagon).


sindano(X):- tiene(X,spam);tiene(X,noresponde);tiene(X,parosistema).