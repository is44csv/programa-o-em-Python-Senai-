# ***DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.***  
# ***1 - Função -  cumprimentar o cliente***
# ***2 - Função - restaurante***
# ***3 - Sugestão utilize listas  e loops***




def cumprimentar(nome):
    return f'SEJA BEM VINDO! {nome}'


def restaurante():
    lista_compras = {'meus_produtos':[],'valores_produtos':[]} 
    cumprimentar('Ana')
    p =  input('Deseja comprar? ')
    
    while p  == 'sim':
        
        produ = {
        'lista_prod' :['','1 - SALADA', '2 -  MACARRONADA', '3 - SANDUICHE', '4  - SORVETE'],
        'valores' : [0,25.55,30.60,80.0,35.70]
        }


          
        print(produ)
        


        try:
            produto = int(input('Digite o id do produto: '))
            if produto:
                m_prod = produ['lista_prod'][produto]
                lista_compras['meus_produtos'].append(m_prod)
                lista_compras['valores_produtos'].append(produ['valores'][produto])
                print(lista_compras)
                p =  input('Deseja continuar? ')
        except ValueError:
            print(f'escolha um produto através do indice 1 - 2  -3 - 4')    
    else:
        total =  sum(lista_compras['valores_produtos'])
        print('R$', round(total, 2))
        print('obrigada volte sempre')    


restaurante()   

def comparar(n1,n2):


    if n1 % 2==0 and n2 % 2 == 1:
        print('N1 é par')
    elif  n1 % 2 == 1 and n2 % 2 == 0:
        print('N2 É PAR ')   
    elif n1  % 2 ==0 and n2 % 2 == 0:
        print('Ambos são pares')
    else:
        print('Nenhum, é par ')       


comparar(5,21)    





# DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.



def descobrir(ano, ano_nascimento,mes_atual, mes_nascimento):
    idade  =  ano - ano_nascimento
    if mes_atual > mes_nascimento:
        print('A pessoa tem', idade)
    else:
        idade_1 = idade - 1
        print(idade_1)    


descobrir(2026,2000,7,10)




def copa(ano):
    lista =  [1958, 1962, 1970, 1994 , 2002]
    if ano in lista:
        print('No ano citado o Brasil ganhou a copa')
    else:
        print('No ano citado o Brasil não Ganhou ')    


copa(1994)
