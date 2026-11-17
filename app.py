from flask import Flask, render_template, request, jsonify
from models import db, Insumo

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cantina.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    insumos = Insumo.query.all()
    alertas = [i for i in insumos if i.alerta_critico]
    return render_template("index.html", insumos=insumos, alertas=alertas)

@app.route("/vender/<int:insumo_id>", methods=["POST"])
def registrar_venda(insumo_id):
    try:
        qtd = float(request.form.get("quantidade", 1))
        if qtd <= 0:
            return jsonify({"erro": "Quantidade inválida"}), 400
    except ValueError:
        return jsonify({"erro": "Formato numérico inválido"}), 400

    insumo = db.session.get(Insumo, insumo_id)
    if not insumo or insumo.quantidade < qtd:
        return jsonify({"erro": "Estoque insuficiente"}), 400

    insumo.quantidade -= qtd
    db.session.commit()
    return jsonify({"status": "Venda registrada", "restante": insumo.quantidade}), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=False)
