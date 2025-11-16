Relatório Pedagógico do Plugin Gamificado


1. Identificação do Plugin
Nome do jogo/plugin: 
R: Speed Run de Complexidade

Área da disciplina (Fundamentos, Análise de Algoritmos, Técnicas, Modelos Computacionais):

R: Fundamentos da Computação – Complexidade, Computabilidade e Modelos Computacionais

Grupo (nomes e RAs dos integrantes):

R: Victor de Souza Maciel – RGM: 45450811
R: Everton Matias Cordeiro de Brito – RGM: 34169342
R: Nathan de Olivera Gomes – RGM: 39997243

2. Objetivo Pedagógico
Descreva quais conceitos da disciplina o jogo trabalha e o que o aluno deverá aprender ou praticar ao jogar.

R: O objetivo principal do plugin é oferecer uma forma gamificada para que o aluno pratique conteúdos essenciais da disciplina de Modelos Computacionais e Complexidade de Algoritmos.
Onde o aluno revisa conceitos fundamentais como: Máquinas de Turing, Complexidade de Tempo e Espaço, Classes de Complexidade, Problemas Decidíveis e Indecidíveis

3. Descrição do Jogo
Explique em poucas linhas as regras básicas do jogo, duração média e como o aluno recebe feedback (nota, dicas, mensagens).

R:
O jogo apresenta ao aluno uma sequência de perguntas teóricas relacionadas à área de computabilidade e complexidade.
O fluxo do jogo funciona assim:
O aluno registra um usuário com login e senha.
Ao clicar em Launch, uma sessão é iniciada.
Cada pergunta aparece na tela com múltiplas alternativas; o aluno deve responder o mais rápido possível.
O tempo total é contado, e a pontuação é calculada de acordo com precisão e velocidade.
Ao finalizar todas as questões, o aluno recebe um relatório com:
Respostas corretas
Pontuação total
Tempo gasto
Detalhes da sessão

4. Conteúdo Relacionado à Disciplina
Liste os tópicos do plano de ensino relacionados ao jogo (ex.: notação assintótica, P vs NP, máquinas de Turing etc.) e explique como o jogo ajuda na compreensão desses conceitos.
R:
O jogo cobre os principais tópicos do plano de ensino, incluindo:
Máquinas de Turing (DTM/NTM)
Problema da Parada e Indecidibilidade
Linguagens Recursivas e Recursivamente Enumeráveis (R e RE)
Classes de Complexidade: P, NP, NP-Completo, PSPACE, EXPTIME
Hierarquia de Tempo e Espaço
Reduções Polinomiais e NP-dificuldade
Funções assintóticas e análises teóricas

5. Critérios de Pontuação
Explique como o jogo calcula a nota final, qual o mínimo para aprovação e se há penalidades (tempo, dicas, erros).

R: Cada resposta correta gera um score baseado no tempo de resposta (quanto mais rápido, mais pontos).
Respostas erradas não somam pontos.
O sistema atribui um bônus para sessões com todas as respostas corretas.
O score final é a soma de todas as questões respondidas corretamente, multiplicado por um fator inversamente proporcional ao tempo gasto.
Não há penalidade explícita por erro, mas responder errado reduz a chance de conseguir uma pontuação alta, reforçando o aprendizado por repetição.

6. Testes Realizados
Liste pelo menos 5 casos de teste planejados (ex.: acerto total, erro esperado, tempo limite, repetição com seed).

R: Casos de teste principais:
Acerto total:
Jogador responde todas as questões corretamente.
Score deve ser alto e sem erros.
Erro proposital:
Jogador responde incorretamente para validar se não soma score para respostas erradas.
Tempo extremo:
Jogador espera vários segundos antes de responder, verificando diminuição do score.
Sessão repetida:
Jogador inicia várias sessões em sequência para validar consistência do banco e IDs.
Seed e banco:
Reset do banco e inserção correta das perguntas via seed.
Verificação se o jogo realmente carrega as perguntas armazenadas.

7. Roteiro de Demonstração
Explique como será feita a apresentação final do plugin em sala (cenário feliz, cenário de erro). 

R:
Cenário feliz (funcionamento esperado):
Mostrar o README e explicar rapidamente como rodar o jogo.
Abrir o navegador em http://127.0.0.1:8000/static/index.html.
Criar usuário e clicar em Launch.
Responder algumas perguntas, exibindo tempo e score.
Finalizar sessão e mostrar o JSON com os resultados.
Abrir /docs (Swagger) para mostrar as rotas da API.
Encerrar discutindo a aplicabilidade pedagógica.

Cenário de erro (previsto e tratado):
Tentar logar com senha errada → deve aparecer erro de credenciais.
Tentar acessar /questions/next sem sessão → API deve retornar erro apropriado.
Mostrar que o sistema não inicia jogo sem usuário autenticado.
