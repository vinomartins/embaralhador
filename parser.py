from random import choice
import re
from typing import List
import pandas as pd

def expand_items(items: List[str]) -> List[str]:
    result = []

    for item in items:
        # Case: number with letter range, like 3[b-f]
        match = re.match(r"^(\d+)\[([a-z])-([a-z])\]$", item)
        if match:
            num, start, end = match.groups()
            result.extend([f"{num}{chr(c)}" for c in range(ord(start), ord(end)+1)])
            continue

        # Case: numeric range, like 2-6
        match = re.match(r"^(\d+)-(\d+)$", item)
        if match:
            start, end = map(int, match.groups())
            result.extend([str(n) for n in range(start, end+1)])
            continue

        # Case: plain number
        result.append(item)

    return result

def problemsDataFrame(alunos, text_area_input):
    # text_area_input = "12, 1-9, 2[a-f]\n2, 4, 5"
    # alunos = "joao\nPedro\nDaniel"


    lines = text_area_input.split('\n')
    print(lines)


    problems = []

    for line in lines:
        line = line.replace(' ', '')
        options = line.split(',')
        problems.append(expand_items(options))

    alunos = alunos.split('\n')
    problemas = []

    for aluno in alunos:
        problemasDoAluno = []
        for problem in problems:
            p  = choice(problem)
            count = 0
            while (p in problemasDoAluno) and (count < 5):
                print(count)
                p = choice(problem)
                count += 1
            problemasDoAluno.append(p)
        problemas.append(", ".join(problemasDoAluno))



    df = pd.DataFrame({'Aluno': alunos, 'Problemas':problemas})

    return df
