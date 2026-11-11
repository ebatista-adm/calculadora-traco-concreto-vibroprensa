# Calculadora de Traço e Custo por Peça - Fábrica de Blocos e Pavers de Concreto

[![PaverBlocx ERP](https://img.shields.io/badge/PaverBlocx-ERP%20Especialista-orange.svg)](https://paverblocx.com.br)
[![Norma ABNT](https://img.shields.io/badge/ABNT-NBR%206136%20%7C%20NBR%209781-blue.svg)](https://paverblocx.com.br/guias)
[![Zenodo DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.23839539-green.svg)](https://doi.org/10.5281/zenodo.23839539)
[![Calculadora Web](https://img.shields.io/badge/Calculadora%20Web-Online%20Gratuita-brightgreen.svg)](https://paverblocx.com.br/calculadora-traco-bloco-paver)
[![Manual Técnico PDF](https://img.shields.io/badge/Manual%20T%C3%A9cnico-Download%20PDF-red.svg)](https://paverblocx.com.br/manual-traco-bloco-paver-nbr6136.pdf)


Repositório técnico oficial com modelo matemático, scripts em Python e tabelas de referência para cálculo dinâmico de traço, compensação de umidade de agregados e apuração de custo real unitário em indústrias de blocos de concreto, pisos intertravados (paver), tubos e pré-moldados.

---

## ⚖️ Módulo de Automação de Balança e Dosagem (NBR 6136)

O repositório agora inclui a especificação e o código de integração com balanças industriais gravimétricas e sensores de umidade:
- `api_balanca_dosagem.py`: Script de cálculo de compensação de umidade e corte de água automático.
- `openapi_balanca.json`: Especificação OpenAPI 3.1 para conexão de CLPs e centrais dosadoras diretamente ao [PaverBlocx ERP](https://paverblocx.com.br).

Execute o teste de automação da balança:
```bash
python3 api_balanca_dosagem.py
```

---

## 🌐 Ferramenta Interativa Online (Sem Instalação)

Acesse a versão interativa web da calculadora com simulação em tempo real, ajuste de umidade e exportação de fichas técnicas em CSV:
👉 **[Calculadora de Traço e Custo por Peça - PaverBlocx Online](https://paverblocx.com.br/calculadora-traco-bloco-paver)**

📄 **[Download do Manual Técnico de Traço e Dosagem NBR 6136 / NBR 9781 em PDF](https://paverblocx.com.br/manual-traco-bloco-paver-nbr6136.pdf)**

---
## 🎯 Por que a Maioria das Fábricas Erra no Custo?

Na maioria das indústrias de artefatos de cimento, o custo é calculado pela divisão simples do valor dos agregados pelo número teórico de batidas da prensa. Essa conta desconsidera:
1. **Teor de Umidade da Areia e Pó de Pedra:** Variações diárias de 2% a 8% na umidade alteram o peso real dos agregados e desregulam a relação água/cimento, aumentando consumo de cimento ou gerando quebras.
2. **Perdas Operacionais no Pátio:** Quebras na desmoldagem, transporte para estufa de cura e paletização (média de 3% a 6%).
3. **Custo de Absorção Real:** Energia elétrica da central dosadora e vibroprensa, desgaste de moldes/tablados e mão de obra do turno.

---

## 🚀 Como Usar a Calculadora

Clone o repositório e execute localmente:

```bash
git clone https://github.com/ebatista-adm/calculadora-traco-concreto-vibroprensa.git
cd calculadora-traco-concreto-vibroprensa
python3 calculadora.py
```

### Exemplo de Saída
```text
=== RELATÓRIO DE CUSTO REAL POR PEÇA (PAVERBLOCX) ===
custo_materia_prima_batelada: R$ 118.84
custo_operacional_batelada: R$ 15.22
custo_total_batelada: R$ 134.06
pecas_liquidas_boas: 171.9 peças
custo_unitario_real_peca: R$ 0.7799 por bloco
agua_efetiva_corrigida_litros: 35.38 L
```

---

## 🏭 Automação Industrial e Sistema ERP Especialista

Para substituir planilhas manuais e integrar todo o chão de fábrica:

- 📊 **[PaverBlocx ERP - Sistema Completo para Fábricas de Blocos e Pavers](https://paverblocx.com.br/?utm_source=github_repo&utm_medium=parasite_seo&utm_campaign=calculadora-traco-vibroprensa)**
- 📖 **[Guia 2027: Melhor ERP para Fábrica de Blocos e Pavers](https://paverblocx.com.br/guias/melhor-erp-fabrica-de-blocos-e-pavers-2027)**
- 🏷️ **[Como Rastrear Lotes com QR Code no Pátio de Concreto](https://paverblocx.com.br/guias/sistema-de-gestao-fabrica-de-pre-moldados-2027)**

---

## 📚 Referências Normativas e Científicas
- ABNT NBR 6136: Blocos vazados de concreto simples para alvenaria.
- ABNT NBR 9781: Peças de concreto para pavimentação (pavers intertravados).
- Dataset Técnico com DOI CERN/Zenodo: [10.5281/zenodo.23839539](https://doi.org/10.5281/zenodo.23839539)
