# LinkQuote-RFP-
[README.md](https://github.com/user-attachments/files/31708421/README.md)
# LinkQuote RFP

Sistema web para gestão de RFPs (pedidos de cotação) e cotações de links de internet, desenvolvido como Projeto Integrador em Computação II (PJI240) — UNIVESP.

## 📋 Sobre o projeto

**Problema:** pedidos e propostas de links de internet são hoje tratados em canais dispersos (e-mail, WhatsApp, mensagens), sem controle centralizado de prazo, critérios técnicos, SLA, histórico ou justificativa do resultado.

**Objetivo:** desenvolver e validar uma aplicação web acessível que centralize RFPs de conectividade, convide provedores para cotar, receba propostas e as classifique automaticamente por:

| Critério | Peso |
|---|---|
| Valor | 40% |
| Atendimento técnico | 35% |
| SLA | 25% |

**Comunidade externa parceira:** Ultra Brasil Telecomunicações

## ✨ Funcionalidades principais

- Painel do solicitante e portal protegido do provedor
- Prazo de 3 dias úteis para resposta às cotações, com bloqueio de alterações após o envio
- Consulta de CEP/endereço (integração ViaCEP) e registro de velocidades de download/upload
- Histórico completo e logs de auditoria por provedor, sem exposição de propostas concorrentes
- Ranking automático com justificativa do resultado
- Acessibilidade orientada a WCAG 2.2 AA / eMAG

## 🛠️ Tecnologias

> Stack a ser confirmada pelo grupo — sugestão inicial abaixo, editem conforme a decisão do time.

- **Frontend:** JavaScript (React ou Vue)
- **Backend:** Node.js (Express) ou similar
- **Banco de dados:** relacional (PostgreSQL ou MySQL)
- **API externa:** ViaCEP (consulta de endereço)
- **Testes:** unitários e de integração
- **Versionamento:** Git + GitHub, com Pull Requests revisados pelo grupo
- **Hospedagem/Deploy:** ver seção abaixo

## ☁️ Onde publicar (deploy)

Comparação rápida de opções populares para projetos acadêmicos full-stack com banco de dados:

## 📁 Estrutura do repositório

```
linkquote-rfp/
├── docs/           # Plano de ação, relatórios parcial/final, atas
├── backend/        # API e regras de negócio
├── frontend/       # Interface web (painel solicitante e portal provedor)
├── database/       # Modelagem, scripts e migrações
└── README.md
```

## 👥 Integrantes

- Clara Gouvea Neves Cruz
- Douglas da Silva Almeida
- Eriel Machado Almeida
- Isabella Benevides Sampaio
- Larissa Nayara Farias Santos
- Sheila Barbosa dos Santos

**Orientadora:** Julianne Santana Cavalcanti

## 🚀 Como rodar localmente

```bash
# clonar o repositório
git clone https://github.com/<seu-usuario>/linkquote-rfp.git
cd linkquote-rfp

# instruções de instalação do backend/frontend serão adicionadas
# conforme a stack for definida pelo grupo
```

## 📄 Contexto acadêmico

Projeto Integrador em Computação II (PJI240) — UNIVESP
Polos: São Rafael, Céu Paz, Formosa e Rosa da China
