# Arquitetura da v1

## Objetivo

Converter uma questão de vestibular de Matemática ou Física em uma explicação visual verificável, renderizada em uma única cena Manim por questão, sem áudio.

## Componentes e responsabilidades

### 1. Entrada e normalização (`Question Input`)

Responsável por receber a questão e padronizar:
- texto do enunciado;
- alternativas, se existirem;
- imagens/figuras e referências aos arquivos;
- disciplina e banca, se conhecidas;
- ano, fase, prova, número da questão e fonte;
- gabarito oficial, se disponível.

Não inferir metadados ausentes. Usar `null` ou `unknown` e preservar a origem.

### 2. Análise da questão (`Question Analyzer`)

Produz `QuestionAnalysis`:
- classifica disciplina e assunto;
- identifica objetivo;
- extrai dados, incógnitas, unidades, restrições e hipóteses;
- interpreta gráficos/figuras quando disponíveis;
- identifica ambiguidades e informação insuficiente;
- propõe pontos-chave e oportunidades visuais preliminares.

A análise não deve inventar valores que não estejam no enunciado ou que não sejam consequência explícita de uma hipótese.

### 3. Resolução (`Solution Planner`)

Produz `SolutionPlan`:
- formula o problema;
- seleciona método;
- apresenta etapas ordenadas;
- registra fórmulas, substituições e unidades;
- justifica cada etapa;
- calcula resultado;
- verifica dimensionalidade e consistência quando aplicável;
- compara com gabarito oficial, se disponível.

O agente deve distinguir resultado calculado, resposta oficial e resposta inferida. Divergências bloqueiam a aprovação automática.

### 4. Planejamento pedagógico (`Pedagogical Planner`)

Produz os pontos-chave e uma sequência didática:
- o que o estudante precisa perceber;
- por que cada ponto é importante;
- o que merece representação visual;
- o que pode permanecer como texto;
- que erro comum vale a pena prevenir;
- quando apresentar a resposta final.

Nem toda etapa precisa de animação complexa. A visualização deve reduzir carga cognitiva, não decorar a tela.

### 5. Especificação de animação (`Animation Planner`)

Produz `AnimationSpec`, JSON independente do Manim:
- cena única;
- etapas ordenadas;
- elementos visuais de tipos permitidos;
- ações do vocabulário controlado;
- textos e fórmulas;
- referências a pontos-chave e etapas da solução;
- duração sugerida e pausa de leitura;
- layout e identidade visual.

O modelo não escreve código Python nesta etapa.

### 6. Renderer Manim

Converte `AnimationSpec` em código/cenas Manim usando componentes e templates conhecidos:
- fórmulas e textos;
- eixos e gráficos;
- pontos, segmentos, vetores e formas;
- tabelas e diagramas simples;
- ações de entrada, destaque, transformação e saída.

O renderer valida os tipos e parâmetros antes de executar. Não executar código arbitrário recebido diretamente do modelo.

### 7. Validação

Três trilhas independentes:

- **Técnica:** schema válido, componentes permitidos, renderização concluída, arquivos gerados, sem objetos fora da tela.
- **Matemática/física:** cálculos, unidades, equações, hipóteses e resultado verificados por ferramentas ou revisão independente.
- **Pedagógica:** enunciado/contexto legível, sequência coerente, justificativas, tempo de leitura e clareza visual revisados por pessoa.

### 8. Artefatos e rastreabilidade

Salvar junto do vídeo:
- questão normalizada;
- análise;
- plano de solução;
- pontos-chave;
- especificação de animação;
- versão do prompt/modelo;
- versão do renderer;
- logs e resultado dos validadores;
- status da revisão humana.

## Fluxo principal

```text
INPUT
  |
  v
NORMALIZE QUESTION
  |
  v
QUESTION ANALYSIS ---- ambiguity / insufficient data ---> HUMAN REVIEW
  |
  v
SOLUTION PLAN
  |
  v
INDEPENDENT SOLUTION CHECK ---- mismatch ---> BLOCK / HUMAN REVIEW
  |
  v
KEY POINTS + PEDAGOGICAL SEQUENCE
  |
  v
ANIMATION SPEC (JSON)
  |
  v
SCHEMA + ALLOWLIST VALIDATION
  |
  v
MANIM RENDERER
  |
  v
TECHNICAL + VISUAL CHECKS
  |
  v
HUMAN PEDAGOGICAL REVIEW
  |
  v
APPROVED VIDEO + TRACEABLE ARTIFACTS
```

## Contratos entre componentes

Os componentes comunicam-se por JSON versionado. Schemas iniciais:
- `schemas/question-analysis.schema.json`
- `schemas/solution-plan.schema.json`
- `schemas/animation-spec.schema.json`

Cada artefato deve incluir `schema_version`. Alterações incompatíveis exigem nova versão do schema.

## Estratégia de implementação

### Primeiro protótipo
- Uma LLM existente via Hermes Agent.
- Prompting e exemplos few-shot, sem fine-tuning.
- Um conjunto pequeno de questões curadas.
- Renderer com allowlist de componentes.
- Validação manual e scripts de verificação.

### Evolução
- Coletar erros por etapa.
- Corrigir prompts, schemas e templates.
- Construir dataset supervisionado com exemplos aprovados.
- Avaliar fine-tuning somente se houver evidência de falhas recorrentes que prompting e ferramentas não resolvam.

## Decisões e limites

- Uma cena por questão não significa uma única animação: a cena contém várias etapas.
- O modelo é responsável por raciocínio e planejamento; o renderer é responsável por executar instruções gráficas seguras.
- O gabarito não deve ser usado como substituto da resolução.
- Questões com imagens ilegíveis, enunciado incompleto ou ambiguidade relevante devem ser encaminhadas para revisão.
