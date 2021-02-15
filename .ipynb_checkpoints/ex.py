#1. Criando um mini sistema de controle de estoque

# Crie um sistema para ser usado pelo time de controle de estoque de um centro de distribuição.

# -Imagine que ao fim de todo dia, o time conta quantas unidades de produto existem no estoque. 
# Se tivermos um estoque abaixo do estoque permitido para aquela categoria do produto, o time deve 
# ser avisado (print) para fazer um novo pedido daquele produto.
# -Cada categoria de produto tem um estoque mínimo diferente, segundo a regra abaixo:

# -alimentos -> Estoque mínimo: 50
# -bebidas -> Estoque mínimo: 75
# -limpeza -> Estoque mínimo: 30

# Para isso vamos criar um programa que pede 3 inputs do usuário: nome do produto, categoria e 
# quantidade atual em estoque.

# Se o produto tiver abaixo do estoque mínimo da categoria dele, o programa deve printar a mensagem 
# "Solicitar {produto} à equipe de compras, temos apenas {unidades} em estoque"

# Exemplo: Se o usuário preenche os inputs com: bebidas, dolly, 90, o programa não deve exibir nenhuma mensagem.
# Agora, se o usuário preenche os inputs com: bebidas, guaraná, 60, o programa deve exibir a mensagem 
# "Solicitar guaraná à equipe de compras, temos apenas 60 unidades em estoque.

# Obs: lembre de usar o int() para transformar o número inserido pelo usuário no input de string para int.
# Obs2: Caso o usuário não preencha alguma das 3 informações, o programa deve exibir uma mensagem para avisá-lo 
# de preencher corretamente.


#######################

#Entrada programa: nome do produto; categoria; qtd atual em estoque
# 1. No final do dia, verificar qts unidades tem no estoque
# 2. Se estoque abaixo do nº permitido p/ categoria, imprimir na tela essa informação e solicitar reposição(novo pedido)
# 3. Regra de estoque mínimo p/ categoria
#       alimentos = 50 unid
#       bebidas = 75 unid
#       limpeza = 30 unid    


categoria = input('Entre com o nome da categoria do produto: ')
nomeProduto = input('Entre com o nome do produto desejado: ')
qtEstoqueAtual = input('Entre com a quantidade existente em estoque: ')

if nomeProduto and categoria and qtEstoqueAtual:
        qtEstoqueAtual = int(qtEstoqueAtual)
        if categoria == 'bebidas':
            if int(qtEstoqueAtual) < 75:
                print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque'.format(nomeProduto, qtEstoqueAtual))
            else:
                print('Temos estoque suficiente!')

        if categoria == 'alimentos':
            if int(qtEstoqueAtual) < 50:
                print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque'.format(nomeProduto, qtEstoqueAtual))
            else:
                print('Temos estoque suficiente!')

        if categoria == 'limpeza':
            if int(qtEstoqueAtual) < 30:
                print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque'.format(nomeProduto, qtEstoqueAtual))
            else:
                print('Temos estoque suficiente!')
else:
    print('Categoria não cadastrada, valor inexistente ou campo em branco, favor digitar corretamente!')
    


