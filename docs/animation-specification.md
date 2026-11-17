# Animation Specification — contrato com o renderer Manim

## Objetivo

Descrever a animação em JSON estruturado, sem exigir que a LLM gere código Python/Manim diretamente.

## Princípios

- Uma classe/cena Manim por questão.
- A cena pode conter várias etapas/seções.
- Estilo misto: fórmulas e transformações passo a passo combinadas com visualizações conceituais.
- Sem narração em áudio na v1.
- Enunciado ou contexto fiel permanece visível.
- Cada etapa deve estar ligada a um ponto-chave ou etapa da solução.
- Usar somente elementos e ações suportados pelo renderer.
- O renderer controla cores, posicionamento padrão, tempos mínimos e segurança.

## Elementos visuais permitidos — conjunto inicial

O primeiro renderer deve implementar uma lista pequena e explícita:
- `text`: título, rótulo ou trecho do enunciado;
- `math`: expressão LaTeX;
- `axes`: plano cartesiano ou eixos;
- `function_graph`: gráfico de função com expressão/domínio;
- `point`: ponto com coordenadas e rótulo opcional;
- `line` / `segment`: reta ou segmento;
- `vector`: vetor com origem, componentes e rótulo;
- `circle`: circunferência;
- `polygon`: polígono com vértices;
- `brace`: chave de agrupamento;
- `table`: tabela simples;
- `diagram`: diagrama declarado por um template permitido.

Elementos não suportados devem resultar em validação negativa e pedido de revisão, não em código improvisado.

## Ações permitidas — vocabulário inicial

- `write`
- `fade_in`
- `fade_out`
- `create`
- `transform`
- `indicate`
- `circumscribe`
- `move_to`
- `plot`
- `mark`
- `build`
- `wait`

A implementação mapeia esses identificadores para chamadas Manim conhecidas. O modelo não escolhe nomes arbitrários de classes ou métodos.

## Estrutura da cena

1. Contexto: enunciado integral ou resumo fiel e dados relevantes.
2. Interpretação: objetivo e incógnita.
3. Desenvolvimento: passos matemáticos/físicos, com justificativas.
4. Visualização conceitual: gráfico, diagrama ou construção quando útil.
5. Resposta: resultado final e alternativa, se houver.
6. Conferência: validação ou interpretação do resultado.

Nem toda questão exige todas as seções. O plano pode combinar ou omitir seções, desde que não omita conteúdo essencial.

## Layout e legibilidade

- Padrão inicial: proporção 16:9.
- Margem de segurança configurável.
- Enunciado/contexto em área persistente.
- Área principal para fórmulas e visualizações.
- Não permitir sobreposição de objetos importantes.
- Respeitar tamanho mínimo de fonte e limites de tela.
- Cor não pode ser o único canal de significado.
- Tempos de leitura definidos por configuração do renderer, com sugestão do agente.

## Segurança

- Não executar `exec`, imports ou código arbitrário vindo do JSON.
- Validar `element.type`, `action` e parâmetros por allowlist.
- Restringir expressões LaTeX e parâmetros de gráficos conforme necessário.
- Renderizar em ambiente isolado e com limites de tempo/recursos.
- Salvar logs de falha e a especificação que os originou.

## Relação com o schema

O contrato inicial está em `schemas/animation-spec.schema.json`. Ele é deliberadamente restrito: ampliar os recursos do renderer deve ser acompanhado por atualização versionada do schema e testes.
