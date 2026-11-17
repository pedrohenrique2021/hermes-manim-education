# Avaliação e critérios de aceite

## Objetivo

Avaliar cada estágio separadamente. Uma boa resposta final não deve esconder uma interpretação ruim ou uma animação incorreta.

## Métricas por etapa

### 1. Interpretação
- disciplina/tópico classificados corretamente;
- dados e unidades extraídos corretamente;
- incógnita e objetivo identificados;
- hipóteses e ambiguidades sinalizadas;
- interpretação de figura consistente com a fonte.

### 2. Resolução
- resultado correto;
- etapas matematicamente/fisicamente válidas;
- justificativas adequadas;
- unidades e dimensões consistentes;
- concordância com gabarito, quando disponível;
- divergências explicadas e bloqueadas.

### 3. Pontos-chave e didática
- pontos essenciais cobertos;
- ausência de pontos irrelevantes;
- sequência pedagógica coerente;
- justificativas compreensíveis;
- erros comuns tratados sem desviar do objetivo.

### 4. Especificação e renderização
- JSON válido contra schema;
- somente elementos e ações permitidos;
- renderização sem exceção;
- nenhuma sobreposição/corte;
- enunciado/contexto legível;
- tempos de leitura suficientes;
- ausência de áudio.

### 5. Revisão humana
Um revisor deve avaliar:
- correção;
- clareza;
- ritmo;
- valor pedagógico das visualizações;
- fidelidade ao enunciado;
- adequação ao nível da questão.

## Conjunto de avaliação inicial

Montar um conjunto pequeno, porém diverso:
- Matemática e Física;
- questões objetivas e discursivas;
- álgebra, funções, geometria, estatística/probabilidade;
- mecânica, termologia, ondas, óptica e eletricidade;
- questões com e sem gráficos/figuras;
- diferentes bancas e níveis de dificuldade.

Não usar as mesmas questões no prompt de desenvolvimento e no teste final.

## Critérios de bloqueio

Bloquear aprovação automática se:
- análise sinalizar ambiguidade essencial;
- verificação independente divergir da solução;
- gabarito oficial divergir sem explicação;
- schema for inválido;
- renderer falhar;
- objeto importante sair da tela ou ficar ilegível;
- não houver evidência de revisão humana pedagógica.

## Baseline

Antes de fine-tuning, medir o modelo base com:
- instrução simples;
- instrução com schema;
- instrução com exemplos few-shot;
- ferramentas de cálculo/verificação habilitadas.

Comparar resultados por etapa. Fine-tuning só é justificável se produzir melhoria mensurável no conjunto de teste e não degradar outras competências.
