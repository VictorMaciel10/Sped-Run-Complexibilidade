from __future__ import annotations
from sqlmodel import Session, select
from .database import engine, init_db
from .models import Question, Option

QUESTIONS = [
    {
        "text": "O que significa dizer que um problema é recursivamente enumerável (RE)?",
        "options": [
            ("Pode ser resolvido por um autômato finito", False),
            ("Toda entrada possui resposta garantida (sim ou não)", False),
            ("Existe uma Máquina de Turing que aceita todas as entradas do conjunto e pode não parar em outras", True),
            ("É sempre possível construir uma prova formal para cada instância", False),
            ("Pode ser resolvido em tempo polinomial", False),
        ],
    },
    {
        "text": "Por que o Problema da Parada é considerado indecidível?",
        "options": [
            ("Não existe Máquina de Turing capaz de verificar qualquer programa", False),
            ("A linguagem correspondente não é recursivamente enumerável", False),
            ("Qualquer algoritmo que o resolva pode ser traduzido para lógica proposicional", False),
            ("Sua prova de indecidibilidade depende de diagonalização, mostrando contradição em um suposto decidor", True),
            ("É um problema NP-completo", False),
        ],
    },
    {
        "text": "Na definição da classe SPACE(f(n)), o que ela representa?",
        "options": [
            ("Os problemas resolvidos com tempo f(n)", False),
            ("Os problemas que exigem tanto tempo quanto espaço", False),
            ("Os problemas que podem ser resolvidos com espaço assintótico máximo f(n)", True),
            ("Os problemas indecidíveis por qualquer Máquina de Turing", False),
            ("Problemas resolvidos por autômatos de pilha", False),
        ],
    },
    {
        "text": "O Teorema da Hierarquia de Tempo estabelece que:",
        "options": [
            ("Aumentar o tempo disponível sempre torna o problema mais difícil", False),
            ("Tempo e espaço são equivalentes para qualquer função assintótica", False),
            ("Há problemas que podem ser resolvidos em tempo f(n) mas não em tempo o(f(n) / log(f(n)))", True),
            ("P é estritamente contido em EXPTIME (provado)", False),
            ("Nenhum problema pode ser resolvido em tempo sublinear", False),
        ],
    },
    {
        "text": "Qual afirmação descreve corretamente um problema NP-completo?",
        "options": [
            ("É verificável em tempo exponencial", False),
            ("Todo problema em P pode ser reduzido em tempo polinomial para ele", False),
            ("É tanto NP quanto NP-difícil", True),
            ("Tem solução única para todas as instâncias", False),
            ("Sempre exige espaço exponencial", False),
        ],
    },
    {
        "text": "Qual é a função essencial das reduções polinomiais entre problemas?",
        "options": [
            ("Determinar qual problema é semanticamente mais simples", False),
            ("Mostrar que resolver um problema é pelo menos tão difícil quanto resolver outro", True),
            ("Permitir sempre encontrar uma solução ótima", False),
            ("Converter um problema indecidível em um decidível", False),
            ("Garantir que ambos os problemas pertencem à classe P", False),
        ],
    },
    {
        "text": "Como se interpreta a computação de uma Máquina de Turing Não Determinística (NTM)?",
        "options": [
            ("A NTM percorre todas as transições simultaneamente e exige memória infinita", False),
            ("Uma entrada é aceita se ao menos um dos ramos computacionais leva a um estado de aceitação", True),
            ("NTMs são mais poderosas que MTs determinísticas em termos de linguagens decidíveis", False),
            ("Uma NTM sempre para em tempo exponencial", False),
            ("NTM aceita apenas linguagens regulares", False),
        ],
    },
    {
        "text": "Qual afirmação é correta sobre a classe EXPTIME?",
        "options": [
            ("EXPTIME = P", False),
            ("Inclui problemas solucionáveis apenas por autômatos finitos", False),
            ("Contém problemas que requerem tempo exponencial para serem resolvidos por MT determinísticas", True),
            ("É estritamente menor que NP", False),
            ("É equivalente a PSPACE", False),
        ],
    },
    {
        "text": "Qual afirmação é verdadeira sobre linguagens indecidíveis?",
        "options": [
            ("Toda linguagem indecidível é não enumerável", False),
            ("Existe linguagem indecidível que é recursivamente enumerável", True),
            ("Nenhuma linguagem indecidível é reconhecida por Máquina de Turing", False),
            ("Toda linguagem indecidível é NP-difícil", False),
            ("Toda linguagem indecidível possui complemento decidível", False),
        ],
    },
    {
        "text": "Qual é o papel fundamental de uma Máquina de Turing Universal?",
        "options": [
            ("Executar apenas linguagens regulares com eficiência", False),
            ("Simular qualquer outra Máquina de Turing a partir de sua descrição codificada", True),
            ("Resolver problemas NP-completos em tempo linear", False),
            ("Verificar formalmente se um problema é indecidível", False),
            ("Reduzir problemas de EXPTIME para P", False),
        ],
    },
]


def run():
    init_db()
    with Session(engine) as s:
        # Se já existem, não reinsere
        if s.exec(select(Question)).first():
            print("Perguntas já existem.")
            return

        order = 1
        for q in QUESTIONS:
            qrow = Question(text=q["text"], order=order)
            s.add(qrow)
            s.flush()

            for text, correct in q["options"]:
                s.add(Option(question_id=qrow.id, text=text, is_correct=bool(correct)))

            order += 1

        s.commit()
        print("Perguntas inseridas!")


if __name__ == "__main__":
    run()
