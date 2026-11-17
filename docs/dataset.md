# Dataset e preparação de dados

## Objetivo

Construir um conjunto curado que ensine e avalie as etapas separadas:
1. interpretar questões;
2. resolver Matemática e Física;
3. identificar pontos-chave pedagógicos;
4. planejar animações;
5. produzir especificações compatíveis com o renderer.

## Fontes candidatas

Fontes sugeridas para investigação, sujeitas a conferência de licença, qualidade e disponibilidade:
- provas e gabaritos publicados por organizadoras e instituições;
- datasets de questões do ENEM e vestibulares;
- conjuntos de raciocínio matemático em português;
- exemplos de instrução/código Manim;
- exemplos próprios revisados por especialistas.

Não assumir que a licença de um dataset permite redistribuição ou uso comercial. Registrar licença, URL, data de acesso e condições de uso de cada fonte.

## Separar os tipos de dado

### A. Questão e metadados
Enunciado, alternativas, imagens, banca, ano, prova, disciplina, assunto e fonte.

### B. Interpretação
Dados, incógnitas, objetivo, restrições, conceitos, ambiguidades e evidências.

### C. Solução
Etapas, justificativas, fórmulas, unidades, resultado, gabarito e método de verificação.

### D. Planejamento pedagógico
Pontos-chave, sequência didática, erros comuns e oportunidades visuais.

### E. Animação
Especificação JSON, versão do renderer, render resultante e revisão.

## Curadoria

- Deduplicar questões e variantes de prova.
- Preservar enunciado original e metadados de origem.
- Marcar OCR incerto e imagem ilegível.
- Distinguir gabarito oficial de resposta calculada.
- Verificar soluções com ferramenta determinística ou revisor independente.
- Revisar explicações geradas por outras LLMs; não tratá-las como verdade de referência.
- Não armazenar cadeia de pensamento privada. Armazenar explicações didáticas concisas, passos verificáveis e justificativas observáveis.
- Remover ou anonimizar dados pessoais que apareçam incidentalmente.

## Divisão treino/validação/teste

Separar por questão e, sempre que possível, por prova/edição para reduzir vazamento entre variantes quase idênticas. Manter conjunto de teste intocado durante desenvolvimento de prompts e fine-tuning.

Uma divisão inicial pode ser 80/10/10, mas a separação por origem e dificuldade é mais importante que a proporção exata.

## Formato

Usar JSONL com um registro por questão, mantendo artefatos estruturados separados ou aninhados. Validar cada registro contra os schemas. Guardar imagens como arquivos referenciados por caminho/ID, não como blobs enormes no JSONL.

## Estratégia de aprendizagem

- Começar com prompting e few-shot.
- Criar exemplos aprovados para cada etapa.
- Medir erros por componente.
- Fazer SFT somente quando houver exemplos suficientes, consistentes e licenciados.
- Considerar treinamento separado ou adaptadores para análise, solução e planejamento de animação apenas se os experimentos justificarem.
- Não treinar diretamente com código Manim sem teste de execução e revisão.

## Métricas de dataset

- cobertura por disciplina, tópico e banca;
- percentual com gabarito oficial;
- percentual com solução independente validada;
- percentual com imagens/OCR revisados;
- percentual com pontos-chave aprovados;
- percentual de especificações que renderizam;
- percentual de vídeos aprovados pedagogicamente.
