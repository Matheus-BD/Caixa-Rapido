# Caixa Rapido - Aula 3

## Cenário prático: sistema de caixa rápido

Você foi contratado para iniciar o desenvolvimento do sistema de um "Caixa Rápido" de uma loja de eletrônicos. O sistema precisa processar a venda de três produtos diferentes. Para cada produto, o operador de caixa informará o nome, o valor original e a porcentagem de desconto a ser aplicada. O sistema deve calcular o valor final de cada item e, ao final, exibir um pequeno recibo. Para evitar escrever a mesma fórmula matemática três vezes, você criará uma função reutilizável responsável apenas por calcular os descontos.

## Questionario.
1. Vantagem da função reutilizável: Explique, com suas próprias palavras, qual foi a principal vantagem observada ao utilizar a função calcularValorFinal múltiplas vezes no algoritmo principal, em comparação com reescrever a fórmula de desconto para cada um dos três produtos.
R.: A principal vantagem é evitar a repetição desnecessária de código.

2.Facilidade em mudanças (regra de negócio): Imagine que a regra de negócio da loja mudou e agora todo desconto calculado deve incluir também uma taxa administrativa fixa de R$ 2,00. Como a estrutura modularizada, que você criou, facilita essa alteração no código?
R.: Usando uma função para fazer o calculo eu apenas precisso ir lá na parte da função no meu codigo e apenas alterar ela em vez de mudar meu codigo inteiro.

3.Diferença de funcionamento: Qual a diferença prática de funcionamento percebida entre a função que realizou o cálculo do desconto (utilizando o comando Retorne) e o módulo exibirRecibo que formatou os dados na tela?
R.:Função (calcularValorFinal): Executa um cálculo e devolve um valor ao programa usando o comando Retorne. O resultado pode ser guardado em uma variável ou usado em outras operações. função (exibirRecibo): Apenas executa um bloco de ações (como mostrar mensagens na tela com o print), sem a necessidade de devolver nenhum valor ao programa.

# Aula 4

## Checkilits
[x] As variáveis globais foram declaradas corretamente, ou há variáveis "sobrando"?
[x] A função de cálculo possui os parâmetros definidos corretamente na sua assinatura?
[x] As operações matemáticas utilizam os parâmetros internos da função, e não as variáveis globais de fora?
[x] O comando Retorne foi utilizado adequadamente?
[x] Os nomes das funções e das variáveis deixam claro qual é a responsabilidade delas?

## feedback assertivo
1. Utilizar Lista para armazenar os produtos informados
2. Criar um loop infinito para a entrada de produtos