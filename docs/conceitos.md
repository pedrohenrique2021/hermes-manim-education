# Conceitos do projeto

## Escopo da v1

- **Matérias:** Matemática e Física.
- **Vestibulares:** todos os principais vestibulares brasileiros, sem restringir a uma banca. A fonte e a edição devem ser registradas em cada questão.
- **Tipo de questão:** questões objetivas e discursivas de exatas, com enunciado textual e, quando disponível, figuras, gráficos, tabelas ou diagramas.
- **Estilo visual:** misto — desenvolvimento matemático passo a passo junto de representações conceituais, gráficos, diagramas e construções geométricas quando contribuírem para a compreensão.
- **Unidade de renderização:** uma cena Manim por questão, organizada em etapas/seções.
- **Áudio:** sem narração em áudio na v1. Textos, fórmulas, rótulos e destaques visuais podem aparecer na tela.

## Princípios pedagógicos

- Um passo por vez, com o enunciado sempre visível.
- Mostrar o porquê de cada passo, não só a conta.
- Cor com significado fixo (dado, mudança, erro comum, resposta).
- Destacar apenas o que mudou entre um passo e outro.
- Tempo mínimo de leitura antes do próximo passo.

### Interpretação prática dos princípios

1. **Enunciado sempre visível:** manter o enunciado completo ou uma versão resumida fiel em uma área persistente. Se o texto for longo, permitir uma área de contexto com rolagem/alternância planejada, sem perder as informações necessárias.
2. **Um passo por vez:** cada transformação matemática ou conceitual deve ter uma intenção didática identificável.
3. **Justificativa explícita:** quando uma expressão muda, indicar a propriedade, lei física, definição ou hipótese utilizada.
4. **Cores semânticas estáveis:** usar sempre o mesmo significado cromático ao longo do vídeo. A cor nunca deve ser o único meio de transmitir informação.
5. **Mudança localizada:** preservar elementos estáveis e animar somente os objetos que mudam, evitando reconstruir a tela sem necessidade.
6. **Tempo de leitura:** não avançar imediatamente após inserir uma fórmula ou conclusão. O renderer deve permitir pausas configuráveis.
7. **Correção antes de estética:** não renderizar como resposta final uma solução que não passou pelas verificações matemáticas e de consistência.

## Tipos de questão e padrões de resolução

A v1 não deve assumir que toda questão tem o mesmo método. O agente deve classificar o problema e selecionar uma estratégia apropriada.

### Matemática
- Aritmética, razão, proporção e porcentagem.
- Álgebra, equações, inequações e sistemas.
- Funções, gráficos e análise de comportamento.
- Geometria plana, espacial e analítica.
- Trigonometria.
- Sequências, progressões e combinatória.
- Probabilidade e estatística.
- Matemática financeira, quando aplicável.

### Física
- Cinemática.
- Dinâmica e leis de Newton.
- Trabalho, energia e quantidade de movimento.
- Hidrostática e gravitação.
- Termologia e termodinâmica.
- Ondulatória e óptica.
- Eletricidade e magnetismo.
- Circuitos e análise de fenômenos físicos.

A lista é uma taxonomia inicial, não uma promessa de cobertura perfeita. Questões fora das categorias devem ser sinalizadas para revisão, não forçadas a uma classificação incorreta.

## Vocabulário visual (cores, posições, tempos)

### Semântica de cores

A paleta concreta deve ser centralizada em configuração do renderer. Os significados são fixos:

- **Dado:** informação fornecida no enunciado.
- **Mudança:** termo, objeto ou relação que está sendo transformado no passo atual.
- **Erro comum:** alerta de uma interpretação ou procedimento incorreto relevante.
- **Resposta:** resultado final ou alternativa correta.

A implementação deve escolher tons com contraste suficiente no tema de fundo. Não depender exclusivamente de cor: combinar cor com rótulo, forma, contorno ou posição.

### Organização espacial

- Reservar uma região persistente para o enunciado/contexto.
- Reservar uma região principal para fórmulas, gráficos e diagramas.
- Manter a resposta final em posição visual consistente.
- Evitar sobreposição, corte e mudanças de escala que prejudiquem a leitura.
- Priorizar layout horizontal 16:9 como padrão inicial, sem impedir configuração posterior.

### Tempo

- O tempo mínimo de leitura deve ser configurável por tipo de elemento.
- Fórmulas longas, gráficos e conclusões podem exigir pausas maiores.
- Não codificar tempos fixos em cada prompt; o plano pode sugerir duração e o renderer aplica limites seguros.

## Verbos de animação

Vocabulário inicial de ações pedagógicas:

- apresentar dado;
- destacar;
- substituir expressão;
- cancelar termo;
- mover termo;
- transformar expressão;
- escrever equação;
- plotar função;
- marcar ponto;
- construir figura;
- decompor vetor;
- indicar força;
- representar trajetória;
- comparar estados;
- mostrar resposta.

O agente deve selecionar ações de uma lista conhecida pelo renderer. Não deve inventar nomes de classes ou métodos Manim arbitrários.

## Formato do pontos-chave.md

Cada questão deve produzir uma lista ordenada de pontos-chave. Cada item deve conter:
- identificador;
- ideia que o aluno precisa compreender;
- evidência no enunciado ou na resolução;
- por que é importante;
- representação visual sugerida;
- equívoco comum relacionado, se houver;
- etapa da solução em que aparece.

Ver [`pontos-chave.md`](pontos-chave.md).

## Critérios de aceite

- A cena roda sem erro.
- A resposta final confere com o gabarito, quando houver, checada fora do modelo.
- Quando não houver gabarito, a solução é verificada por método independente ou revisão especializada.
- Nada sai da tela ou fica ilegível.
- O passo a passo é revisado por uma pessoa antes de ser considerado material didático aprovado.
- O enunciado/contexto permanece disponível durante a explicação.
- Cada transformação relevante possui justificativa.
- Não há narração em áudio na v1.

## Fora de escopo (por enquanto)

- Narração, dublagem e sincronização de voz.
- Cobertura garantida de todas as bancas, disciplinas ou níveis de dificuldade.
- Resolver qualquer questão sem revisão ou sinalização de incerteza.
- Fine-tuning obrigatório desde o início.
- Geração livre de código Manim sem schema intermediário.
- Aplicativo web, gestão de usuários ou plataforma de cursos.
- Correção automática de respostas manuscritas.
