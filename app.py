""""
Equipe: 50 códigos de preto
Participantes: 
Davi Armando Lira Sales
Bianca Vilas Boas
Bruna Vilas Boas
Geovanna Calixto
Letícia Ribeiro dos Santos
Mateus Furtado Rodrigues
"""

from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "e4539baed2629244f84ac7bba842782f"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definindo as tabelas
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

class LocalReciclagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    endereco = db.Column(db.String(200), nullable=False)
    material = db.Column(db.String(50), nullable=False)

# Inicializando o banco de dados
with app.app_context():
    db.create_all()

    if not Usuario.query.filter_by(username='davi').first():
        admin_user = Usuario(username='davi', password='1234', is_admin=True)
        db.session.add(admin_user)
        db.session.commit()

# Rota Home
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/tutorial_vidro')
def tutorial_vidro():
    return render_template('tutorial_vidro.html')

# Rota de Cadastro de Usuários
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = Usuario(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

# Rota de Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Usuario.query.filter_by(username=username, password=password).first()
        if user:
            session['username'] = username
            session['is_admin'] = user.is_admin
            return redirect(url_for('dashboard'))
    return render_template('login.html')

# Rota Principal
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    empresas = Empresa.query.all()
    locais = LocalReciclagem.query.all()
    return render_template('dashboard.html', username=session['username'], empresas=empresas, locais=locais)

# Rota para gerenciar empresas
@app.route('/gerenciar_empresas', methods=['GET', 'POST'])
def gerenciar_empresas():
    if 'username' not in session:
        return redirect(url_for('login'))

    # Cadastrar nova empresa
    if request.method == 'POST':
        if 'add_empresa' in request.form:
            nome = request.form['nome']
            endereco = request.form['endereco']
            nova_empresa = Empresa(nome=nome, endereco=endereco)
            db.session.add(nova_empresa)
            db.session.commit()
        # Editar uma empresa
        elif 'edit_empresa' in request.form:
            empresa_id = request.form['empresa_id']
            empresa = Empresa.query.get(empresa_id)
            empresa.nome = request.form['nome']
            empresa.endereco = request.form['endereco']
            db.session.commit()
        # Excluir uma empresa
        elif 'delete_empresa' in request.form:
            empresa_id = request.form['empresa_id']
            empresa = Empresa.query.get(empresa_id)
            db.session.delete(empresa)
            db.session.commit()
    
    empresas = Empresa.query.all()
    return render_template('gerenciar_empresas.html', empresas=empresas)

# Rota para gerenciar locais de reciclagem
@app.route('/gerenciar_locais', methods=['GET', 'POST'])
def gerenciar_locais():
    if 'username' not in session or not session.get('is_admin'):
        return redirect(url_for('login'))

    # Cadastrar novo local
    if request.method == 'POST':
        if 'add_local' in request.form:
            endereco = request.form['endereco']
            material = request.form['material']
            novo_local = LocalReciclagem(endereco=endereco, material=material)
            db.session.add(novo_local)
            db.session.commit()
        # Editar um local
        elif 'edit_local' in request.form:
            local_id = request.form['local_id']
            local = LocalReciclagem.query.get(local_id)
            local.endereco = request.form['endereco']
            local.material = request.form['material']
            db.session.commit()
        # Excluir um local
        elif 'delete_local' in request.form:
            local_id = request.form['local_id']
            local = LocalReciclagem.query.get(local_id)
            db.session.delete(local)
            db.session.commit()
    
    locais = LocalReciclagem.query.all()
    return render_template('gerenciar_locais.html', locais=locais)


if __name__ == "__main__":
    app.run(debug=True)
