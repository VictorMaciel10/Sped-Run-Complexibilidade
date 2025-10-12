from __future__ import annotations
from sqlmodel import Session, select
from .database import engine, init_db
from .models import Question, Option

QUESTIONS = [
    {
        "text": "Qual definição melhor descreve uma Máquina de Turing?",
        "options": [
            ("Um autômato finito com memória limitada", False),
            ("Um modelo computacional com fita infinita e cabeçote de leitura/escrita", True),
            ("Uma CPU real de arquitetura Von Neumann", False),
            ("Um algoritmo de ordenação ótimo", False),
            ("Uma pilha com duas cabeças", False),
        ],
    },
    {
        "text": "O que é a Tese de Church-Turing?",
        "options": [
            ("Toda linguagem regular pode ser reconhecida em tempo polinomial", False),
            ("Tudo que é computável efetivamente é computável por uma Máquina de Turing", True),
            ("P=NP", False),
            ("Todo problema indecidível é intratável", False),
            ("NP é o conjunto de problemas decidíveis em espaço polinomial", False),
        ],
    },
    {
        "text": "Sobre complexidade: o que significa O(n log n)?",
        "options": [
            ("Tempo cresce linearmente com n", False),
            ("Tempo cresce proporcional a n vezes log n", True),
            ("Tempo constante", False),
            ("Espaço exponencial", False),
            ("Tempo quadrático", False),
        ],
    },
    {
        "text": "Qual afirmação é correta sobre P e NP?",
        "options": [
            ("Todo problema em NP tem verificação polinomial", True),
            ("P é um subconjunto próprio de NP (provado)", False),
            ("P=NP foi provado em 2001", False),
            ("NP contém apenas problemas decidíveis em tempo exponencial", False),
            ("Problemas NP-completos são resolvidos em tempo linear", False),
        ],
    },
]

def run():
    init_db()
    with Session(engine) as s:
        if s.exec(select(Question)).first():
            print("Perguntas já existem.")
            return
        order = 1
        for q in QUESTIONS:
            qrow = Question(text=q["text"], order=order)
            s.add(qrow); s.flush()
            for text, correct in q["options"]:
                s.add(Option(question_id=qrow.id, text=text, is_correct=bool(correct)))
            order += 1
        s.commit()
        print("Perguntas inseridas!")

if __name__ == "__main__":
    run()