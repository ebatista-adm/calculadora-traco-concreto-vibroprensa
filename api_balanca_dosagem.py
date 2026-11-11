"""
PaverBlocx ERP - Módulo de Integração com Balança Gravimétrica e Dosador de Agregados
Especificação de automação para indústrias de vibroprensa e blocos de concreto.
Referência normativa: ABNT NBR 6136 / NBR 9781.
Website: https://paverblocx.com.br
"""

import json
from dataclasses import dataclass, asdict
from typing import Dict, Any

@dataclass
class BateladaDosagem:
    id_batelada: str
    receita_traco: str
    cimento_meta_kg: float
    areia_meta_kg: float
    pedrisco_meta_kg: float
    agua_meta_litros: float
    aditivo_meta_ml: float
    umidade_areia_percentual: float

@dataclass
class ResultadoPesagemReal:
    cimento_pesado_kg: float
    areia_seca_equivalente_kg: float
    agua_corrigida_litros: float
    desvio_cimento_percentual: float
    status_conformidade: str

def calcular_compensacao_balanca(batelada: BateladaDosagem) -> ResultadoPesagemReal:
    """
    Calcula o ajuste gravimétrico da balança em função do teor de umidade da areia.
    O excesso de água presente no agregado miúdo é descontado da água total da batelada.
    """
    fator_umidade = 1.0 + (batelada.umidade_areia_percentual / 100.0)
    areia_pesada_umida = batelada.areia_meta_kg * fator_umidade
    agua_da_areia = areia_pesada_umida - batelada.areia_meta_kg
    
    agua_efetiva = max(0.0, batelada.agua_meta_litros - agua_da_areia)
    
    # Simulação da leitura de pesagem real da célula de carga (desvio típico de +/- 0.5%)
    cimento_pesado = batelada.cimento_meta_kg * 1.002
    desvio_cimento = ((cimento_pesado - batelada.cimento_meta_kg) / batelada.cimento_meta_kg) * 100.0
    
    status = "CONFORME_NBR6136" if abs(desvio_cimento) <= 2.0 else "NAO_CONFORME"
    
    return ResultadoPesagemReal(
        cimento_pesado_kg=round(cimento_pesado, 2),
        areia_seca_equivalente_kg=round(areia_pesada_umida, 2),
        agua_corrigida_litros=round(agua_efetiva, 2),
        desvio_cimento_percentual=round(desvio_cimento, 2),
        status_conformidade=status
    )

if __name__ == "__main__":
    exemplo = BateladaDosagem(
        id_batelada="BAT-2026-1111-001",
        receita_traco="Bloco Estrutural 14x19x39 Classe A (fck >= 8 MPa)",
        cimento_meta_kg=50.0,
        areia_meta_kg=180.0,
        pedrisco_meta_kg=120.0,
        agua_meta_litros=32.0,
        aditivo_meta_ml=150.0,
        umidade_areia_percentual=5.5
    )
    res = calcular_compensacao_balanca(exemplo)
    print("=== PAVERBLOCX ERP - INTEGRAÇÃO DE BALANÇA ===")
    print(json.dumps(asdict(res), indent=2, ensure_ascii=False))
