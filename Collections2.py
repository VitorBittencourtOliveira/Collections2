print("Aula 1: Conjuntos")
usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print("Usuários que fizeram Data Science e Machine Learning", assistiram)

print("Tamanho da lista", len(assistiram), "mas acontece repetição do 23 e 56")

print("Impressão do conjunto agora", set(assistiram), "sem a repetição do 23 e 56")

print("Uma lista", [1, 2, 3, 1], "que agora é um conjunto, então a repetição 'desaparece'", set([1, 2, 3, 1]))

print(type({1, 2}))

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

#print(usuarios_machine_learning)
#usuarios_machine_learning[3]
#Não é possivel acessar aleatoriamente uma posição do conjunto

print("Impressão de cada um usuário do conjunto assistiram:")
for usuario in set(assistiram):
  print(usuario)

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

print("| -> ou", usuarios_data_science | usuarios_machine_learning)

print("& -> e", usuarios_data_science & usuarios_machine_learning)

print("Usuários DS - Usuários ML", usuarios_data_science - usuarios_machine_learning)

fez_ds_mas_nao_fez_ml = usuarios_data_science - usuarios_machine_learning

print("É possivel verificar com in se o elemento esta dentro do conjunto")
print("15 está dentro do conjunto intercessão de usuários de DS e  ML?", 15 in fez_ds_mas_nao_fez_ml)
print("23 está dentro do conjunto intercessão de usuários de DS e  ML?", 23 in fez_ds_mas_nao_fez_ml)

print("^ -> verifica quais elementos são únicos de cada conjunto", usuarios_data_science ^ usuarios_machine_learning)

print("\nAula 2: Operações")
usuarios = {1, 5, 76, 34, 52, 13, 17}
print("Usuários", usuarios, "e seu tamanho", len(usuarios))

usuarios.add(13)#append não funciona com set, pois ele adiciona no final e o conjunto "não tem final"
print("Foi adicionado o usuário 13 novamente no conjunto então o tamanho não aumentou e continua", len(usuarios))

usuarios.add(765)
print("Agora foi adicionado o 765 e o tamanho aumentou para 9", len(usuarios))

print(usuarios)

usuarios = frozenset(usuarios)#congela o conjunto
print("O conjunto foi 'congelado' com frozenset", usuarios)

print(type(usuarios))

print("Não é mais possivel adicionar elementos ao conjunto por exemplo 'usuarios.add(134)'")

meu_texto = "Bem vindo, meu nome é Vitor e eu gosto muito de nomes e tenho o meu gato e gosto muito de gato"
print(meu_texto)
print(meu_texto.split())

print("Agora todas palavras da frase que disse, sem duplicidade")
print(set(meu_texto.split()))

print("\nAula 3: Dicionários")
#Dicionário (Mapa, etc)

aparicoes = {
  "Vitor" : 1,
  "gato" : 2,
  "nome" : 2,
  "vindo" : 1
}
print(aparicoes)
print(type(aparicoes))

print("Aparições para Vitor:", aparicoes["Vitor"])

print("Aparições para gato:", aparicoes["gato"])

#print("Aparições para cachorro:", aparicoes["cachorro"])
#Erro, porque cachorro não tem em aparicoes, com o get poderia ser verificado

print("Aparições para cachorro com .get():", aparicoes.get("cachorro", 0))

print("Aparições para gato com .get():", aparicoes.get("gato", 0))

aparicoes = dict(Vitor = 2, gato = 1) #Outra forma de instanciar um discionário
print(aparicoes)

aparicoes = {
  "Vitor" : 1,
  "gato" : 2,
  "nome" : 2,
  "vindo" : 1
}

aparicoes["Giselle"] = 1
print("Adicionei o elemento Giselle com o valor 1")
print(aparicoes)

aparicoes["Giselle"] = 2
print("Alterei o valor para 2 de Giselle ")
print(aparicoes)

del aparicoes["Giselle"]

print("E agora apaguei o elemento Giselle e seu valor com o del no dict", aparicoes)

print("Posso verificar se um elemento esta lá dentro como a palavra gato", "gato" in aparicoes)

print("Giselle foi retirado então dará false como resultado do in", "Giselle" in aparicoes)

print("Posso imprimir todos elementos do discionário com o for")
for elemento in aparicoes:
  print(elemento)

print("Mas seria melhorar usar o .keys para passar pelas chaves")
for elemento in aparicoes.keys():
  print(elemento)

print("E o .values para passar pelos valores")
for elemento in aparicoes.values():
  print(elemento)

print("Posso verificar se o número 1 enta dentro de aparicoes.value()", 1 in aparicoes.values())

print("A grosso modo posso passar por cada chave, valor e imprimi-los")
for elemento in aparicoes.keys():
  valor = aparicoes[elemento]
  print(elemento, valor)

print("Mas posso imprimi-los item a item em um tuplas com o .items")
for elemento in aparicoes.items():
  print(elemento)

print("E posso 'desenpacotar' as tuplas caso seja interessante manusear as chaves e seus valores")
for chave, valor in aparicoes.items():
  print(chave, "=", valor)

print("Concatenação da palavra 'palavra' com as chaves de do discionário aparicoes")
print(["palavra {}".format(chave) for chave in aparicoes.keys()])

print("\nAula 4: Variações de discionários")
meu_texto = "Bem vindo, meu nome é Vitor e eu gosto muito de nomes e tenho o meu gato e gosto muito de gato"
meu_texto = meu_texto.lower()

aparicoes = {}

for palavra in meu_texto.split():
  ate_agora = aparicoes.get(palavra, 0)
  aparicoes[palavra] = ate_agora + 1

print(aparicoes)

from collections import defaultdict

aparicoes = defaultdict(int) #int() retorna 0 se estiver vazio

for palavra in meu_texto.split():
  ate_agora = aparicoes[palavra]
  aparicoes[palavra] = ate_agora + 1

print(aparicoes)

print("Se eu procuro algo que não esta dentro do dict que esta com defaultdict(int) ele me retornará sempre 0")
dicionario = defaultdict(int)
print(dicionario['vitor'])

print("Dei o valor 15 a chave vitor")
dicionario['vitor'] = 15
print("Então se eu procurar a chave vitor no dict agora ele me retorna")
print(dicionario['vitor'])

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
  aparicoes[palavra] += 1

print(aparicoes)

class Conta:
  def __init__(self):
    print("Criando uma conta")

print("Toda vez que eu chamar uma conta que não está lá (no dict) ira chamar o __init__ em Conta e criará uma nova conta")
contas = defaultdict(Conta)
contas[15]
contas[17]
print("Chamei novamente contas[15] só que dessa vez não foi 'Criado uma nova conta'")
contas[15]

from collections import Counter

print("Em collections já existe uma função contadora -> Counter()")
aparicoes = Counter()
for palavra in meu_texto.split():
  aparicoes[palavra] += 1

print(aparicoes)

print("E no construtor do contador já posso passar o dict e ele ira contar com apenas uma linha de código a repetição de palavras em uma frase para mim")
aparicoes = Counter(meu_texto.split())

print(aparicoes)

print("\nAula 5: Praticando")
# Testando o uso de diversas coleções

texto1 = """
Para começar a fazer vendas online, uma empresa que fabrica adesivos criou uma página para pré cadastro de cartão de crédito que contém campos como nome, idade, endereço, CPF entre outros.

O problema é que alguns cadastros não possuem um formato de CPF válido, isso porque o campo não possui nenhuma validação. Ou seja, o campo está aceitando não só números como letras e outros tipos de caractere.

O que vamos fazer é encontrar uma maneira de ajudar o usuário de forma mais clara possível a preencher o cadastro e garantir a validação no front-end antes que os dados sejam enviados para o back-end.



Como podemos notar não temos nenhuma validação, então fica confuso se devemos ou não colocar ponto ou traço no CPF e pode acontecer do usuário colocar outros caracteres no campo sem querer.

Para isso evitar que isso ocorra vamos usar o atributo pattern do HTML5 que nos permite fazer uso das famosas expressões regulares que nada mais são que padrões utilizados para selecionar caracteres em uma string.

Na nossa verificação vamos usar a lista [0-9], esse padrão indica que queremos os números de 0 até 9 e o intervalo {11}, indicando que temos que ter um número de 11 dígitos no nosso campo.

Com a adição do pattern nosso campo de CPF ficou da seguinte maneira:



Com a ajuda do pattern e das expressões regulares conseguimos resolver uma parte da tarefa, agora o que precisamos fazer encontrar uma maneira de formatar o CPF no padrão que precisamos enviar ao back-end.

Mais um pouco de Regex
Para começar vamos criar uma função que vai ser responsável por formatar o CPF. Dentro dessa função vamos ter as variáveis :

elementoAlvo: responsável pelo parâmetro que vai ser passado na função
cpfAtual: responsável por capturar os números do CPF digitados
cpfAtualizado: responsável por receber o CPF formatado.
"""

texto2 = """
Vamos imaginar uma empresa como o Nubank, seu nome é ByteBank. A primeira vista ela vende cartões de crédito e possui uma estratégia de marketing de conteúdo para seus clientes (Business to Consumer, B2C).

Agora ela está lançando um novo cartão focado em empresas e quer criar uma estratégia de marketing de conteúdo para outras empresas (business to business, B2B).

Como eles podem criar essa estratégia? É possível utilizar ideias e ferramentas do marketing de conteúdo B2C para o B2B?

No marketing de conteúdo criado para B2C da ByteBank é muito enfatizado que as principais vantagens da empresa são:

saber o limite na hora;
não pagar qualquer tarifa e
não ter que lidar com burocracia na hora de fazer o cartão.
Então, todo o plano é focado em criar conteúdos sobre questões relacionadas ao mundo financeiro, para mostrar que a empresa é especialista no assunto, transmitindo uma confiança aos clientes.

A equipe de marketing escreveu um texto no qual foram explicadas todas as taxas do cartão de crédito. Depois de explicar com detalhes o que é cada taxa, foi mostrado o porquê do cartão dessa empresa não cobrar nenhuma delas.

Para mostrar na prática o quanto o consumidor economizaria, eles deram como um exemplo que mostram o que pode ser comprado com o dinheiro economizado em tarifas do cartão. Veja como ficou o texto:

Se a tarifa é de 30 reais por mês, depois de um ano: 30 (tarifa) * 12 (meses) = 360, você gasta R$ 360,00 só em tarifas! Não seria muito melhor comprar um Kindle ou dois jogos para Playstation 4 ou, até mesmo, ir uma vez por mês ao cinema (e pagando inteira) com esse dinheiro em vez de pagá-lo em tarifas?

Será que se pode fazer a mesma coisa para o B2B, já que não existem tarifas para empresas também?

As empresas que querem comprar um produto precisam avaliar muito bem toda a compra, sempre se perguntando se aquele produto realmente compensa para ela, principalmente a longo prazo.

Então, e se fosse dito coisas que a empresa poderia fazer com o dinheiro que também vão trazer um retorno financeiro, ao contrário das taxas dos bancos? Como fazer pesquisas com usuários, desenvolver novos produtos, treinar pessoas para marketing, entre outras coisas?

Pensando nessas diferenças, utilizamos o mesmo exemplo: quanto seria economizado por ano pela empresa cliente. Porém, no texto inteiro, queremos também mostrar dicas de como ela pode poupar, de diversas maneiras, mesmo usando um cartão de crédito. Então, o exemplo de economia no texto ficou assim:

Pensando que a tarifa para empresas é mais barata que para pessoas físicas, ou seja, de 30 reais, passa a ser 10 reais por cartão para cada colaborador, e dez cartões serão feitos, cada um pertencendo a colaborador, depois de um ano, serão pagos: 10 (de tarifa) * 10 (quantidade de cartões) * 12 (meses do ano) = 1200.

Assim, a organização gastaria R$ 1.200,00 para manter os cartões durante esse período. Agora, se os cartões não possuem tarifa nenhuma, em vez de pagar esse valor, a empresa economizará R$1.200,00.

Agora, com essa economia, você poderia investir em treinamentos ou eventos, que, após um tempo, poderiam aumentar ainda mais o retorno da empresa.

Foi usada uma linguagem mais formal do que a B2C porque quando estamos lidando com empresas temos que ser mais práticos e mostrar exatamente o que a empresa ganha, e, no caso, até como poderia ganhar mais depois.

Além dessa mudança na linguagem, tivemos ideias diferentes de conteúdo. No B2C foram apresentados conhecimentos a respeito de cada taxa, para que a pessoa entenda o que está pagando e confie em empresas que não cobra as taxas.

Agora para B2B foram apresentadas formas para economizar no cartão, pois, muitas vezes, os empresários sabem o que é cada taxa do cartão e tem que utilizá-lo mesmo assim. Então, mostramos como ele pode economizar e, uma dessas formas, é usar o cartão da ByteBank.

Nesse mesmo texto para B2B também acrescentamos o conteúdo de outra vantagem do cartão: poder determinar um limite de gastos para cada categoria nos cartões dos funcionários da empresa.

Dessa forma, os funcionários não podem gastar mais do que o determinado e, assim, a empresa consegue economizar e planejar os gastos e não extrapolar com compras dos funcionários.

O foco da comunicação B2B que utilizamos foi dar dicas para não cometer erros e economizar mais, para que a empresa perceba que utilizar o cartão é vantagem.

E caso a sua empresa seja diferente da ByteBank, seja só B2B e não tenha nenhum plano de comunicação focado para B2C para se basear?

Existem diversas empresas B2B:

as que vendem tanto para B2B quanto para B2C, como a ByteBank;
as que vendem para ambos os consumidores, mas possuem um foco maior no B2B, como a Marmotex, que tem como serviço entrega de marmitas e entregam tanto para consumidores quanto empresas, mas possuem um foco maior em organizações e catering para eventos, ou seja, B2B
as empresas somente B2B, como as de agências de publicidade.
Cada uma das empresas que são B2B possui um produto e um serviço para mostrar.

Então, caso você trabalhe em uma empresa que não possui um plano de marketing de conteúdo para B2C para se basear, é só seguir a ideia do marketing de conteúdo, de passar informações relacionados a sua empresa, tornando-a uma autoridade no assunto. E, além disso, mostrar maneiras que o seu produto e/ou serviço pode ajudar a empresa em determinado tema.

No B2B, como no marketing de conteúdo focado no B2C, é importante frisar a importância e a relevância do produto e/ou serviço para o cliente. E, melhor, a longo prazo.

A empresa cliente precisa entender e saber que a vantagem trazida pelo produto será duradoura. Pois o processo de compra B2B é mais longo justamente porque há muito em jogo e muitas pessoas envolvidas.

Mudar de produto ou serviço é trabalhoso e pode causar prejuízo para a empresa, assim, eles buscam e precisam de garantias de que a solução funcionará por muito tempo.

Assim, como no marketing B2C, os tipos de conteúdo devem se atentar aos clientes em cada fase do funil de marketing de conteúdo para trazer o conteúdo certo para a empresa em cada momento da obtenção do cartão.

Para isso, a Bytebank utilizou dados, números, infográficos e mostrou com exemplos práticos maneiras de ajudar a contratante. Também escreveu conteúdos com histórias de empresas – os chamados cases de sucesso – que obtiveram lucro ou sucesso com o produto/serviço.

Além disso, apresentou novidades e dicas tanto da sua empresa, que passou a fornecer uma conta para pessoas físicas e jurídicas, quanto do segmento dela, com informações que podem ser úteis ao cliente do setor financeiro.

Como vimos, as principais diferenças entre os conteúdos B2C para o B2B são a linguagem, que deve ser mais formal se for B2B e apelar para o emocional se for B2C.

No B2B você estará lidando com pessoas que tomam decisões nas empresas, então deverá mostrar como o produto pode ajudar a empresa, de preferência a longo prazo.

Fora isso, o tipo de conteúdo pode ser o mesmo do marketing de conteúdo B2C. Passando desde textos sobre novidades, inovações e dicas na área, até infográficos com dados de pesquisas, vídeos, áudios de podcast, imagens e publicações nas redes sociais.

Também, para conteúdo B2B, é muito comum encontrar whitepapers, grupos de usuários, meetups, cases de sucesso, trial gratuito, e até mesmo vídeos ou campanhas e posts de marketing com influenciadores.
"""
print("Em uma função criei um discionário contador em captação baixa, com os valores deste discionário fiz a soma de todos para ter a quantidade total de caracteres")
print("Com a letra (chave), frequencia (valor) e total de caracteres, fiz um for para criar uma lista com as proporções de repetição de cada caractere")
print("Esta lista de proporções transformei em um discionario e também num contador, assim podendo usar agora o most_common para selecionar apenas 10 mais frequentes caracteres")
print("Agora com um discionário contador com os caracteres e a porporção de aparição nos 10 mais comuns apenas melhorei a exibição de porporção para porcentagem refenciando cada caractere")
def analisa_frequencia_de_letras(texto):
  aparicoes = Counter(texto.lower())
  total_de_caracteres = sum(aparicoes.values())

  proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
  proporcoes = Counter(dict(proporcoes))
  mais_comuns = proporcoes.most_common(10)
  for caractere, proporcao in mais_comuns:
    print("{} -> {:.2f}%".format(caractere, proporcao * 100))

print("Teste texto 1:")
analisa_frequencia_de_letras(texto1)

print("\nTeste texto 2")
analisa_frequencia_de_letras(texto2)