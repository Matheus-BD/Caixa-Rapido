# Caixa Rapido

## Cenário prático: sistema de caixa rápido

Você foi contratado para iniciar o desenvolvimento do sistema de um "Caixa Rápido" de uma loja de eletrônicos. O sistema precisa processar a venda de três produtos diferentes. Para cada produto, o operador de caixa informará o nome, o valor original e a porcentagem de desconto a ser aplicada. O sistema deve calcular o valor final de cada item e, ao final, exibir um pequeno recibo. Para evitar escrever a mesma fórmula matemática três vezes, você criará uma função reutilizável responsável apenas por calcular os descontos.


- 1. Qual foi a maior dificuldade que você encontrou ao tentar ler e entender um código que foi escrito por outra pessoa e não por você mesmo?

R: A maior dificuldade foi entender a função de cada função e como elas se relacionam, principalmente os parâmetros base, desc e fin. Foi necessário acompanhar o código desde a entrada dos dados até o cálculo do desconto e a exibição do resultado.

- 2. Por que formular um feedback assertivo (fazendo perguntas ou sugestões, em vez de dar ordens) pode trazer melhores resultados técnicos para uma equipe de desenvolvimento?

R: Porque perguntas e sugestões permitem que o programador entenda o problema e pense em uma solução, evitando conflitos. Além disso, facilita a troca de ideias e pode ajudar a equipe a encontrar formas melhores de organizar e melhorar o código.

- 3. Descreva qual foi a sugestão mais valiosa que você recebeu do seu colega durante a revisão e como ela melhorou a qualidade da sua modularização (funções e parâmetros).

R: A sugestão mais valiosa foi separar as responsabilidades do código em funções. No código, cal_final() ficou responsável pelo cálculo do preço com desconto e exibir() pela apresentação dos resultados. Isso deixou o código mais organizado, fácil de entender e permitiu que cada função recebesse apenas os parâmetros necessários para realizar sua tarefa.
