# Implementação — Question Understanding (v0.1.0)

## O que está implementado

- Skill `question-understanding` para Hermes Agent; a inferência é feita pelo modelo ativo da sessão (configurado como Hermes 3 pelo usuário).
- Contrato de saída igual a `schemas/question-analysis.schema.json` (Draft 2020-12).
- Biblioteca Python para extrair um único objeto JSON, carregar o schema e validar a análise.
- CLI de validação e testes unitários.

## Por que uma skill Hermes

O runtime escolhido é Hermes Agent existente. A skill orienta o agente a produzir a análise com o modelo já configurado, sem abrir um segundo cliente HTTP, duplicar credenciais ou acoplar o repositório a uma API específica. A parte determinística (parse e schema validation) fica no Python.

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
./scripts/install_hermes_skill.sh
```

Reinicie/abra uma sessão Hermes Agent com o modelo Hermes 3 ativo. A skill será exposta como `/question-understanding`.

## Uso

No chat do Hermes:

```text
/question-understanding Analise esta questão: ...
```

Peça para salvar o JSON em `outputs/question-analysis/<question_id>.json`. A skill deve validar o arquivo antes de afirmar que está válido.

Validação manual:

```bash
PYTHONPATH=src python -m hermes_education.question_understanding validate \
  outputs/question-analysis/<question_id>.json
```

## Contrato e estados

- `ready_for_solution`: análise suficiente para encaminhar à etapa seguinte.
- `needs_review`: interpretação incerta, ambiguidade, hipótese ou imagem parcialmente legível.
- `insufficient_information`: informação essencial ausente.

O módulo não resolve a questão, não verifica gabarito e não escolhe os pontos-chave didáticos finais. Essas responsabilidades pertencem às etapas seguintes, conforme `docs/arquitetura.md`.

## Limites da entrega

A validação automatizada garante conformidade estrutural com o JSON Schema, não correção matemática, factual ou pedagógica. A inferência real do Hermes 3 ainda precisa ser testada no ambiente local do usuário; este ambiente de execução não tem acesso ao Hermes Agent instalado nem ao modelo local.
