#!/usr/bin/env python3
"""
Calculadora de Traço e Custo Unitário por Peça - Fábrica de Blocos e Pavers de Concreto
Em conformidade com ABNT NBR 6136 (Blocos vazados de concreto simples para alvenaria)
e ABNT NBR 9781 (Peças de concreto para pavimentação - Paver).

Desenvolvido para integração com PaverBlocx ERP (https://paverblocx.com.br)
"""

def calcular_batelada(
    cimento_kg: float,
    po_pedra_kg: float,
    areia_kg: float,
    pedrisco_kg: float,
    aditivo_kg: float,
    agua_litros: float,
    precos: dict,
    umidade_areia_pct: float = 4.0,
    pecas_teoricas: int = 150,
    perda_patio_pct: float = 4.0,
    custo_kwh: float = 0.85,
    kwh_consumido: float = 3.2,
    mao_obra_batelada: float = 12.50
):
    """
    Calcula o custo real por peça considerando compensação de umidade e perdas.
    """
    # Correção de umidade dos agregados (areia)
    areia_seca_kg = areia_kg / (1.0 + (umidade_areia_pct / 100.0))
    agua_efetiva = agua_litros - (areia_kg - areia_seca_kg)

    # Custos de Matéria-Prima
    custo_cimento = cimento_kg * precos['cimento_kg']
    custo_po = po_pedra_kg * precos['po_pedra_kg']
    custo_areia = areia_kg * precos['areia_kg']
    custo_pedrisco = pedrisco_kg * precos['pedrisco_kg']
    custo_aditivo = aditivo_kg * precos['aditivo_kg']

    custo_materia_prima = (
        custo_cimento + custo_po + custo_areia + custo_pedrisco + custo_aditivo
    )

    # Custos Operacionais
    custo_energia = kwh_consumido * custo_kwh
    custo_operacional = custo_energia + mao_obra_batelada

    custo_total_batelada = custo_materia_prima + custo_operacional

    # Peças efetivas após perdas de desmoldagem, transporte e cura
    pecas_liquidas = pecas_teoricas * (1.0 - (perda_patio_pct / 100.0))

    custo_unitario_real = custo_total_batelada / pecas_liquidas

    return {
        'custo_materia_prima_batelada': round(custo_materia_prima, 2),
        'custo_operacional_batelada': round(custo_operacional, 2),
        'custo_total_batelada': round(custo_total_batelada, 2),
        'pecas_liquidas_boas': round(pecas_liquidas, 1),
        'custo_unitario_real_peca': round(custo_unitario_real, 4),
        'agua_efetiva_corrigida_litros': round(agua_efetiva, 2)
    }

if __name__ == '__main__':
    precos_exemplo = {
        'cimento_kg': 0.62,     # R$ 31,00 saco 50kg CP-V ARI
        'po_pedra_kg': 0.055,   # R$ 55,00 tonelada
        'areia_kg': 0.075,      # R$ 75,00 tonelada
        'pedrisco_kg': 0.065,   # R$ 65,00 tonelada
        'aditivo_kg': 4.80      # R$ 4,80 kg plastificante
    }

    resultado = calcular_batelada(
        cimento_kg=100.0,
        po_pedra_kg=350.0,
        areia_kg=250.0,
        pedrisco_kg=200.0,
        aditivo_kg=0.4,
        agua_litros=45.0,
        precos=precos_exemplo,
        pecas_teoricas=180,
        perda_patio_pct=4.5
    )

    print("=== RELATÓRIO DE CUSTO REAL POR PEÇA (PAVERBLOCX) ===")
    for k, v in resultado.items():
        print(f"{k}: {v}")
