from datetime import date, timedelta
from models import Insumo

def test_alerta_estoque_minimo():
    item = Insumo(nome="Leite Condensado", quantidade=2.0, quantidade_minima=3.0, validade=date.today() + timedelta(days=10))
    assert item.alerta_critico is True

def test_insumo_normal():
    item = Insumo(nome="Morango Fresco", quantidade=5.5, quantidade_minima=2.0, validade=date.today() + timedelta(days=5))
    assert item.alerta_critico is False
