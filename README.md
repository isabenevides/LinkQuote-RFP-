[README (1).md](https://github.com/user-attachments/files/31708550/README.1.md)
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

- **Frontend:** JavaScript (React ou Vue)
- **Backend:** Python + Django
- **Banco de dados:** relacional (PostgreSQL)
- **API externa:** ViaCEP (consulta de endereço)
- **Testes:** unitários e de integração
- **Versionamento:** Git + GitHub, com Pull Requests revisados pelo grupo
- **Hospedagem/Deploy:** ver seção abaixo

## ☁️ Onde publicar (deploy)

Comparação rápida de opções populares para projetos acadêmicos full-stack com banco de dados:

## 📁 Estrutura do repositório

```
linkquote-rfp/
├── docs/                   # Plano de ação, relatórios parcial/final, atas
├── backend/
│   ├── manage.py
│   ├── config/             # Settings, urls e wsgi/asgi do projeto Django
│   ├── rfps/                # App: RFPs, prazos e regras de negócio
│   ├── propostas/           # App: propostas, ranking e justificativas
│   ├── provedores/          # App: cadastro e portal do provedor
│   └── requirements.txt
├── frontend/               # Interface web (painel solicitante e portal provedor)
├── database/               # Modelagem e scripts de apoio
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
cd linkquote-rfp/backend

# criar e ativar ambiente virtual
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# instalar dependências
pip install -r requirements.txt

# configurar variáveis de ambiente (copiar e preencher)
cp .env.example .env

# aplicar migrações e subir o servidor
python manage.py migrate
python manage.py runserver
```

## 📄 Contexto acadêmico

Projeto Integrador em Computação II (PJI240) — UNIVESP
Polos: São Rafael, Céu Paz, Formosa e Rosa da China
