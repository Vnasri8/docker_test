from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, current_user
from models.user import User, db

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Cấu hình kết nối PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/app_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key_here'  # Để sử dụng flash messages

db.init_app(app)  # Liên kết db với ứng dụng Flask

# Khởi tạo đối tượng Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Đặt đường dẫn mặc định khi chưa đăng nhập
login_manager.login_view = "auth.login"  # Đảm bảo chỉ ra đúng blueprint và route

# Import các blueprint
from controllers.auth import auth
from controllers.user_management import user_management

# Đăng ký blueprint
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(user_management, url_prefix='/user_management')

# Định nghĩa hàm load_user cho Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Trang chủ
@app.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)

# Tạo bảng dữ liệu nếu chưa có
@app.before_request
def create_tables():
    db.create_all()

# Chạy ứng dụng
if __name__ == '__main__':
    app.run(debug=True)
