produtos = ['','uva','pera','maçã','banana']
valores = [0,10.50,5.0,15.25,10.0]
carrinho = []
total = []

produ0 = int(input(f''' 
                       escolha um a partir do indice:  
{produtos[1]} - {produtos.index(produtos[1])} - R$ {valores[1]}
{produtos[2]} - {produtos.index(produtos[2])} - R$ {valores[2]}
{produtos[3]} - {produtos.index(produtos[3])} - R$ {valores[3]}
{produtos[4]} - {produtos.index(produtos[4])} - R$ {valores[4]}



'''))

carrinho.append(produtos[produ0])
total.append(valores[produ0])
produ1 = int(input(f''' 
                       escolha um a partir do indice:  
{produtos[1]} - {produtos.index(produtos[1])} - R$ {valores[1]}
{produtos[2]} - {produtos.index(produtos[2])} - R$ {valores[2]}
{produtos[3]} - {produtos.index(produtos[3])} - R$ {valores[3]}
{produtos[4]} - {produtos.index(produtos[4])} - R$ {valores[4]}



'''))
carrinho.append(produtos[produ1])
total.append(valores[produ1])
produ2 = int(input(f''' 
                       escolha um a partir do indice:  
{produtos[1]} - {produtos.index(produtos[1])} - R$ {valores[1]}
{produtos[2]} - {produtos.index(produtos[2])} - R$ {valores[2]}
{produtos[3]} - {produtos.index(produtos[3])} - R$ {valores[3]}
{produtos[4]} - {produtos.index(produtos[4])} - R$ {valores[4]}


'''))
carrinho.append(produtos[produ2])
total.append(valores[produ2])


print('Carrinho', carrinho)

print('R$', sum(total))