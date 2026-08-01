import statistics



l = [2,9,1,19,10]
media  =  statistics.mean(l)
print(media)


# mediana - divido a minha frequancia 50 % 50%
mediana  =  statistics.median(l)
print(mediana)


# desvio padrão
# a relação de cada um dos dados em relação 
desvio = statistics.stdev(l)
print(desvio)


# moda
moda  =  statistics.mode(l)
print(moda)


# variancia 
variancia = statistics.variance(l)
print(variancia)

