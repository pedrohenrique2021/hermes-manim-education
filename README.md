# hermes-manim-education

Resolução visual de questões de vestibular com Hermes Agent e Manim.

## Visão da v1

A v1 recebe uma questão de vestibular de **Matemática ou Física**, interpreta o enunciado, identifica os pontos-chave, resolve e planeja uma explicação visual que será renderizada pelo Manim.

- **Vestibulares:** escopo amplo (`all`), sem restringir a uma banca específica.
- **Disciplinas:** Matemática e Física.
- **Estilo visual:** misto — desenvolvimento matemático passo a passo combinado com gráficos, diagramas e representações conceituais.
- **Áudio:** não haverá narração na v1.
- **Unidade de renderização:** uma cena Manim por questão, com várias etapas dentro da cena.

## Princípio arquitetural

O modelo não deve converter diretamente o enunciado em código Python/Manim. O fluxo usa artefatos intermediários estruturados:

```text
Questão
  -> Análise da questão
  -> Plano de solução
  -> Plano pedagógico / pontos-chave
  -> Especificação de animação (JSON)
  -> Renderer Manim
  -> Validação técnica, matemática e pedagógica
```

A especificação intermediária separa o raciocínio do modelo da implementação gráfica. Assim, o renderer pode evoluir sem exigir que o modelo reaprenda toda a estrutura de saída.

## Documentação

- [`docs/conceitos.md`](docs/conceitos.md): princípios pedagógicos e decisões de escopo existentes, consolidados para a v1.
- [`docs/arquitetura.md`](docs/arquitetura.md): componentes, responsabilidades e fluxo.
- [`docs/question-analysis.md`](docs/question-analysis.md): contrato de interpretação do enunciado.
- [`docs/solution-planning.md`](docs/solution-planning.md): resolução e validação.
- [`docs/pontos-chave.md`](docs/pontos-chave.md): seleção e organização dos pontos didáticos.
- [`docs/animation-specification.md`](docs/animation-specification.md): contrato entre o agente e o renderer Manim.
- [`docs/dataset.md`](docs/dataset.md): estratégia de coleta, curadoria e preparação de dados.
- [`docs/evaluation.md`](docs/evaluation.md): critérios de avaliação e aceite.
- [`schemas/`](schemas/): schemas JSON para os artefatos intermediários.
- [`examples/`](examples/): exemplo ilustrativo de ponta a ponta.

## Status

Esta entrega define a especificação documental da v1. Ela **não** implementa ainda o pipeline de ingestão, integração com Hermes Agent, renderer, treinamento ou execução Manim.

## Próximos marcos

1. Validar os schemas com 5–10 questões reais de Matemática e Física.
2. Implementar a análise e o plano de solução com saída estruturada.
3. Implementar o renderer para um conjunto pequeno de componentes Manim.
4. Criar testes automáticos e revisão humana dos vídeos.
5. Montar o dataset curado e só então decidir se fine-tuning é necessário.
