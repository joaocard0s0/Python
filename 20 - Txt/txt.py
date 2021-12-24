arquivo = open('alunos.txt', 'r')
txt = arquivo.readlines()#transforma em uma lista
#arquivo.read() apenas le do jeito que esta
'''
#escrever no txt
novo = open('resumo.txt', 'w')

novo.write('para escrever é só digitar a variavel.write(e depois colocar o que quer aqui)')
novo.close()

with open('resumo.txt', 'a') as more:
    more.write('\nAgora eu posso escrever sem fechar\neu usei o a de append e o with open(x.txt, a) as x')
'''
#desafio minha resposta 
total = 500
site = 'hashtag_site_org'
youtube = 'hashtag_yt_org'
insta = 'hashtag_ig_org'
face = 'hashtag_igfb_org'
org = '_org'
total_organico = 0
total_site = 0
total_youtube = 0
total_insta = 0
total_face = 0

for x in txt:
    if org in x:
        total_organico += 1

for s in txt:
    if site in s:
        total_site += 1
for y in txt:
    if youtube in y:
        total_youtube += 1
for i in txt:
    if insta in i:
        total_insta += 1
for f in txt:
    if face in f:
        total_face += 1
with open('exercicio.txt', 'w') as ex:
    ex.write('Total alunos organicos : {}\n'.format(total_organico))
    ex.write('Total alunos anuncios : {}\n'.format(500 - total_organico))
    ex.write('Total alunos por site : {}\n'.format(total_site))
    ex.write('Total alunos por youtube : {}\n'.format(total_youtube))
    ex.write('Total alunos por intagram : {}\n'.format(total_insta))
    ex.write('Total alunos por facebook: {}\n'.format(total_face))



