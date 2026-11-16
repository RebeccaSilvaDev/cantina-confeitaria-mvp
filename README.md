# 🧁 Cantina & Confeitaria Artesanal — MVP

Sistema web responsivo para controle de estoque de insumos perecíveis, registro de vendas no balcão e emissão de alertas preventivos de validade e estoque mínimo.

## 🎯 Objetivo e Alinhamento aos ODS
Desenvolvido como parte da disciplina de **Projeto de Software (Análise e Desenvolvimento de Sistemas)**, o sistema busca reduzir o desperdício de alimentos e otimizar a gestão financeira de microempreendimentos alimentícios, alinhando-se aos **ODS 8** (Trabalho Decente e Crescimento Econômico) e **ODS 12** (Consumo e Produção Responsáveis).

## 🛠️ Stack Tecnológica Planejada
* **Backend:** Python / Flask + SQLAlchemy
* **Banco de Dados:** SQLite (Ambiente de Desenvolvimento/MVP)
* **Segurança:** Autenticação com Hash Argon2
* **Frontend:** HTML5, CSS3 (Mobile-First, áreas de toque ≥ 44x44px, conformidade WCAG)
* **Qualidade & CI/CD:** Pytest e GitHub Actions

## 📂 Estrutura do Projeto (Escopo do MVP)
* **RF01 — Autenticação:** Acesso restrito à gestora operacional.
* **RF02 — Gestão de Estoque e Vendas:** Cadastro de insumos com data de validade e baixa atômica via registro de venda.
* **RF03 — Painel de Alertas e Faturamento:** Monitoramento visual de estoque crítico e resumo financeiro diário.
