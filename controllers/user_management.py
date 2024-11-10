from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.user import db, User
from flask_login import login_required

# Tạo blueprint cho quản lý người dùng
user_management = Blueprint('user_management', __name__)

# Trang quản lý người dùng
@user_management.route('/manage')
@login_required
def manage_users():
    # Lấy tất cả người dùng từ cơ sở dữ liệu
    users = User.query.order_by(User.username).all()  # Thay đổi User.username bằng trường muốn sắp xếp
    return render_template('user_management.html', users=users)

# Trang sửa thông tin người dùng
@user_management.route('/edit/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    
    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        
        db.session.commit()
        flash('Thông tin người dùng đã được cập nhật', 'success')
        return redirect(url_for('user_management.manage_users'))
    
    return render_template('edit_user.html', user=user)

# Xóa người dùng
@user_management.route('/delete/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('Người dùng đã được xóa', 'danger')
    return redirect(url_for('user_management.manage_users'))
