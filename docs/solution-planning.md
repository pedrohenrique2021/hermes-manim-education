# Solution Planning — resolução verificável

## Objetivo

Produzir uma solução correta, explicável e dividida em passos que possam ser ensinados visualmente.

## Saída esperada

A saída deve seguir `schemas/solution-plan.schema.json`.

Cada etapa deve registrar:
- `step_id` e `order`;
- `goal`: objetivo local do passo;
- `reasoning`: explicação curta do que está sendo feito e por quê;
- `expression_before` e `expression_after`, quando aplicável;
- `formula_or_law`: fórmula, definição ou lei utilizada;
- `substitution`: substituição de valores;
- `units`: unidades relevantes;
- `result`: resultado intermediário;
- `visual_value`: se a etapa merece visualização e por quê.

## Procedimento geral

1. Reformular o objetivo sem alterar o significado.
2. Selecionar método compatível com os dados e o conteúdo.
3. Declarar hipóteses e convenções necessárias.
4. Resolver em passos pequenos e ordenados.
5. Justificar cada transformação.
6. Preservar unidades e conversões.
7. Conferir sinais, domínio, ordem de grandeza e casos-limite quando aplicável.
8. Verificar consistência dimensional em problemas físicos.
9. Resolver por método independente ou ferramenta determinística quando possível.
10. Comparar com o gabarito oficial, sem ajustar artificialmente o desenvolvimento para coincidir.
11. Registrar divergência e bloquear aprovação se o resultado não for explicado.

## Matemática

- Usar cálculo simbólico ou numérico determinístico quando aplicável (por exemplo, SymPy).
- Não confundir aproximação decimal com valor exato.
- Registrar restrições de domínio e soluções extranhas introduzidas por operações.
- Para gráficos, verificar domínio, escala, interceptos e comportamento.
- Para geometria, explicitar relações e propriedades utilizadas.

## Física

- Listar grandezas, símbolos e unidades.
- Declarar referencial, orientação e convenção de sinais quando relevantes.
- Identificar modelo físico e hipóteses de idealização.
- Verificar consistência dimensional.
- Não omitir conversões de unidade relevantes.
- Conferir se o resultado é fisicamente plausível.

## Gabarito

O gabarito é uma referência externa de validação, não a fonte do raciocínio. Registrar separadamente:
- `computed_answer`;
- `official_answer`, se disponível;
- `answer_match`;
- `verification_method`.

Para questões discursivas, usar critérios de correção/rubrica quando disponíveis. Não reduzir uma resposta aberta a uma alternativa inexistente.

## Falhas e encaminhamento

Marcar `needs_review` quando:
- o enunciado está incompleto ou ilegível;
- existem interpretações concorrentes;
- a solução depende de hipótese não confirmada;
- ferramentas independentes discordam;
- o gabarito diverge sem explicação;
- o modelo não consegue justificar uma etapa.
