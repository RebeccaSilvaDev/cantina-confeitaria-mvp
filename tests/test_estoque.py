import pytest
from datetime import date, timedelta
from app import app, db
from models import Gestora, Insumo

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

# --- TESTES UNITÁRIOS (Modelos e Segurança Argon2) ---
def test_unitario_alerta_estoque_minimo():
    item = Insumo(nome="Leite Condensado", quantidade=2.0, quantidade_minima=3.0, validade=date.today() + timedelta(days=10))
    assert item.alerta_critico is True

def test_unitario_insumo_normal():
    item = Insumo(nome="Morango Fresco", quantidade=5.5, quantidade_minima=2.0, validade=date.today() + timedelta(days=5))
    assert item.alerta_critico is False

def test_unitario_hash_senha_argon2():
    gestora = Gestora(email="admin@cantina.com")
    gestora.definir_senha("SenhaForte@2026")
    assert gestora.senha_hash != "SenhaForte@2026"
    assert gestora.verificar_senha("SenhaForte@2026") is True
    assert gestora.verificar_senha("SenhaErrada") is False

# --- TESTES DE INTEGRAÇÃO (Rotas Flask + SQLite em Memória) ---
def test_integracao_painel_e_baixa_atomica(client):
    with app.app_context():
        insumo = Insumo(nome="Farinha de Trigo", quantidade=10.0, quantidade_minima=2.0, validade=date.today() + timedelta(days=15))
        db.session.add(insumo)
        db.session.commit()
        insumo_id = insumo.id

    # Valida carregamento do painel HTML
    resp_painel = client.get("/")
    assert resp_painel.status_code == 200

    # Valida baixa atômica de estoque via POST
    resp_venda = client.post(f"/vender/{insumo_id}", data={"quantidade": "3"})
    assert resp_venda.status_code == 200
    assert resp_venda.get_json()["restante"] == 7.0

    # Valida bloqueio de estoque insuficiente
    resp_erro = client.post(f"/vender/{insumo_id}", data={"quantidade": "50"})
    assert resp_erro.status_code == 400
