from collections import Counter 

dic = {'joao': 1, 'paulo':2, 'cardoso':3} 
ordem = Counter(dic)

print(ordem.most_common(2))
