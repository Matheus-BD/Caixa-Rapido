# Caixa Rapido

## Cenário prático: sistema de caixa rápido

Você foi contratado para iniciar o desenvolvimento do sistema de um "Caixa Rápido" de uma loja de eletrônicos. O sistema precisa processar a venda de três produtos diferentes. Para cada produto, o operador de caixa informará o nome, o valor original e a porcentagem de desconto a ser aplicada. O sistema deve calcular o valor final de cada item e, ao final, exibir um pequeno recibo. Para evitar escrever a mesma fórmula matemática três vezes, você criará uma função reutilizável responsável apenas por calcular os descontos.

## Perguntas. Aula 3

1. Vantagem da função reutilizável: Explique, com suas próprias palavras, qual foi a principal vantagem observada ao utilizar a função calcularValorFinal múltiplas vezes no algoritmo principal, em comparação com reescrever a fórmula de desconto para cada um dos três produtos.
R.: A principal vantagem é evitar a repetição desnecessária de código.

2.Facilidade em mudanças (regra de negócio): Imagine que a regra de negócio da loja mudou e agora todo desconto calculado deve incluir também uma taxa administrativa fixa de R$ 2,00. Como a estrutura modularizada, que você criou, facilita essa alteração no código?
R.: Usando uma função para fazer o calculo eu apenas precisso ir lá na parte da função no meu codigo e apenas alterar ela em vez de mudar meu codigo inteiro.

3.Diferença de funcionamento: Qual a diferença prática de funcionamento percebida entre a função que realizou o cálculo do desconto (utilizando o comando Retorne) e o módulo exibirRecibo que formatou os dados na tela?
R.:Função (calcularValorFinal): Executa um cálculo e devolve um valor ao programa usando o comando Retorne. O resultado pode ser guardado em uma variável ou usado em outras operações. função (exibirRecibo): Apenas executa um bloco de ações (como mostrar mensagens na tela com o print), sem a necessidade de devolver nenhum valor ao programa.

## Perguntas. Aula 4
1. Qual foi a maior dificuldade que você encontrou ao tentar ler e entender um código que foi escrito por outra pessoa e não por você mesmo?
R.: A maior dificuldade foi entender a função de cada função e como elas se relacionam, principalmente os parâmetros base, desc e fin. Foi necessário acompanhar o código desde a entrada dos dados até o cálculo do desconto e a exibição do resultado.

2. Por que formular um feedback assertivo (fazendo perguntas ou sugestões, em vez de dar ordens) pode trazer melhores resultados técnicos para uma equipe de desenvolvimento?

R.: Porque perguntas e sugestões permitem que o programador entenda o problema e pense em uma solução, evitando conflitos. Além disso, facilita a troca de ideias e pode ajudar a equipe a encontrar formas melhores de organizar e melhorar o código.

3. Descreva qual foi a sugestão mais valiosa que você recebeu do seu colega durante a revisão e como ela melhorou a qualidade da sua modularização (funções e parâmetros).

R.: A sugestão mais valiosa foi separar as responsabilidades do código em funções. No código, cal_final() ficou responsável pelo cálculo do preço com desconto e exibir() pela apresentação dos resultados. Isso deixou o código mais organizado, fácil de entender e permitiu que cada função recebesse apenas os parâmetros necessários para realizar sua tarefa.