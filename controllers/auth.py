from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import db, User
from flask_login import login_user, login_required, logout_user

# Tạo blueprint cho phần đăng ký, đăng nhập
auth = Blueprint('auth', __name__)

# Route đăng ký
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash("Mật khẩu không khớp!", 'danger')
            return redirect(url_for('auth.register'))  # Đảm bảo sử dụng 'auth.register'

        user = User.query.filter_by(username=username).first()
        if user:
            flash("Tên người dùng đã tồn tại!", 'danger')
            return redirect(url_for('auth.register'))  # Đảm bảo sử dụng 'auth.register'

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Đăng ký thành công! Bạn có thể đăng nhập ngay.", 'success')
        return redirect(url_for('auth.login'))  # Đảm bảo redirect đúng

    return render_template('register.html')

# Route đăng nhập
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)  # Đăng nhập người dùng
            flash("Đăng nhập thành công!", 'success')
            return redirect(url_for('home'))
        else:
            flash("Tên người dùng hoặc mật khẩu sai", 'danger')

    return render_template('login.html')

# Route đăng xuất
@auth.route('/logout')
@login_required
def logout():
    logout_user()  # Đăng xuất người dùng
    flash('Đăng xuất thành công!', 'success')
    return redirect(url_for('auth.login'))  # Đảm bảo redirect đúng
