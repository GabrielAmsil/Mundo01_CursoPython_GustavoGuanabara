medida = float(input('Uma distância em metros:'))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
print('A medida de {}m coresponde a {:.0f}km, {:.0f}hm, {:.0f}dam, {:.0f}dm, {:.0f}cm e {:.0f}mm'.format(medida, km, hm, dam, dm, cm, mm))
# Exercicio 008