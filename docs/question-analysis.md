# Question Analysis — contrato de interpretação

## Objetivo

Transformar o enunciado original em uma representação explícita do que a questão informa, solicita e exige para ser resolvida.

## Saída esperada

A saída deve seguir `schemas/question-analysis.schema.json`.

Campos essenciais:
- `question_id`: identificador estável da questão.
- `subject`: `mathematics` ou `physics`.
- `topic` e `subtopic`: classificação mais específica possível.
- `question_type`: `multiple_choice`, `open_ended` ou `unknown`.
- `objective`: o que a questão pede, em linguagem direta.
- `given_data`: dados explícitos, com valor, unidade e referência à origem.
- `unknowns`: grandezas/valores a determinar.
- `constraints_and_assumptions`: condições, domínio, aproximações e hipóteses.
- `visual_inputs`: descrição de imagens, gráficos ou tabelas e o que foi possível extrair.
- `key_concepts`: conceitos necessários.
- `irrelevant_or_contextual_information`: informação contextual que não entra diretamente no cálculo, sem descartá-la se puder mudar a interpretação.
- `ambiguities`: pontos que impedem ou fragilizam uma interpretação.
- `confidence`: confiança calibrada e justificada.

## Procedimento

1. Ler o enunciado integralmente antes de resolver.
2. Identificar o comando principal: calcular, determinar, comparar, justificar, estimar, explicar, interpretar etc.
3. Separar dados explícitos de inferências.
4. Registrar unidades e conversões necessárias.
5. Identificar incógnitas e relações entre elas.
6. Interpretar imagens e gráficos sem presumir detalhes ilegíveis.
7. Identificar condições e restrições.
8. Classificar disciplina, assunto e conceitos.
9. Registrar ambiguidades e informação ausente.
10. Só então encaminhar para resolução.

## Regras

- Não inventar dados, unidades, alternativas ou conteúdo de figuras.
- Não tratar uma hipótese implícita como fato sem registrá-la.
- Se duas interpretações plausíveis levarem a soluções diferentes, sinalizar ambiguidade.
- Se faltar informação essencial, não fabricar uma resposta: retornar `needs_review`.
- Distinguir o que o enunciado diz do conhecimento externo usado para interpretar.
- A classificação temática pode ser hierárquica e admitir mais de um conceito.

## Pontos-chave

A análise pode sugerir pontos-chave, mas a lista didática final é consolidada depois da resolução. Isso evita escolher como central um detalhe que não é necessário para chegar à resposta.
