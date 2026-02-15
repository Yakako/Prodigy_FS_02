from flask import Flask, render_template, redirect, request, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
from models import db, User, Employee

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ems.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create tables
with app.app_context():
    db.create_all()

# ---------------- Routes ----------------

@app.route('/')
def home():
    return redirect(url_for('login'))

# -------- Authentication --------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and bcrypt.check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash("Invalid username or password.")
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.")
    return redirect(url_for('login'))

# -------- Dashboard --------
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# -------- Employee CRUD --------
@app.route('/employees')
@login_required
def employees():
    all_employees = Employee.query.all()
    return render_template('employees.html', employees=all_employees)

@app.route('/employees/add', methods=['GET', 'POST'])
@login_required
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        department = request.form['department']
        position = request.form['position']
        salary = float(request.form['salary'])

        # Validation: email uniqueness
        if Employee.query.filter_by(email=email).first():
            flash("Employee email already exists!")
            return redirect(url_for('add_employee'))

        new_employee = Employee(
            name=name, email=email, department=department, position=position, salary=salary
        )
        db.session.add(new_employee)
        db.session.commit()
        flash("Employee added successfully!")
        return redirect(url_for('employees'))

    return render_template('add_employee.html')

@app.route('/employees/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_employee(id):
    emp = Employee.query.get_or_404(id)
    if request.method == 'POST':
        emp.name = request.form['name']
        emp.email = request.form['email']
        emp.department = request.form['department']
        emp.position = request.form['position']
        emp.salary = float(request.form['salary'])
        db.session.commit()
        flash("Employee updated successfully!")
        return redirect(url_for('employees'))
    return render_template('edit_employee.html', employee=emp)

@app.route('/employees/delete/<int:id>')
@login_required
def delete_employee(id):
    emp = Employee.query.get_or_404(id)
    db.session.delete(emp)
    db.session.commit()
    flash("Employee deleted successfully!")
    return redirect(url_for('employees'))

if __name__ == "__main__":
    app.run(debug=True)
