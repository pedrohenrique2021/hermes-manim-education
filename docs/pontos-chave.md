# Pontos-chave

## Objetivo

Registrar o que o estudante precisa perceber para compreender a solução. Pontos-chave não são uma cópia dos cálculos: são as ideias, relações e decisões que tornam a resolução compreensível.

## Formato de cada ponto

Cada item deve conter:

- **ID:** identificador estável, por exemplo `K1`.
- **Ideia central:** conceito ou relação que o estudante precisa compreender.
- **Evidência:** trecho, dado, figura ou etapa da solução que sustenta o ponto.
- **Importância:** por que esse ponto é necessário.
- **Representação visual:** fórmula, gráfico, diagrama, vetor, construção ou destaque.
- **Erro comum:** equívoco que pode ser prevenido, se pertinente.
- **Etapa relacionada:** referência ao `step_id` do plano de solução.
- **Prioridade:** `essential`, `helpful` ou `optional`.

## Regras de seleção

1. Incluir somente pontos que contribuam para interpretar, resolver ou compreender a questão.
2. Ordenar na sequência em que o aluno precisa deles.
3. Separar pré-requisito de resultado.
4. Evitar excesso de conceitos em uma mesma etapa.
5. Preferir uma representação visual quando ela tornar uma relação abstrata mais clara.
6. Não animar algo apenas porque é possível animar.
7. Não incluir um erro comum se ele desviar a atenção ou não for relevante para a questão.

## Modelo para preenchimento

```yaml
question_id: "exam_year_subject_question"
key_points:
  - id: K1
    idea: "Identificar a grandeza que a questão solicita"
    evidence: "Comando final do enunciado"
    importance: "Define a incógnita e orienta o método"
    visual_representation: "Destacar a incógnita no enunciado"
    common_misconception: null
    solution_step_id: S1
    priority: essential
```

## Exemplo ilustrativo — função quadrática

Questão fictícia: determinar as raízes de `f(x) = x² - 5x + 6`.

| ID | Ideia central | Representação visual | Prioridade |
|---|---|---|---|
| K1 | Raiz é o valor de x para o qual f(x) = 0 | Destacar `f(x)=0` | Essential |
| K2 | A fatoração transforma a equação em produto nulo | Mostrar a passagem para `(x-2)(x-3)=0` | Essential |
| K3 | Cada fator pode ser igual a zero | Resolver os dois casos em paralelo ou em sequência | Essential |
| K4 | As raízes correspondem às interseções com o eixo x | Gráfico da parábola e marcação de x=2 e x=3 | Helpful |

O exemplo é ilustrativo e não representa um item oficial de vestibular.
