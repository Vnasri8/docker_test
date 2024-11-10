from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):  # Kế thừa từ UserMixin để Flask-Login có thể quản lý
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

    # Flask-Login cần các thuộc tính này, nhưng bạn có thể sử dụng các mặc định từ UserMixin
    # Các thuộc tính này đều có sẵn trong UserMixin, vì vậy bạn không cần phải thêm trực tiếp

    # def get_id(self):
    #     return str(self.id)  # Trả về ID người dùng dưới dạng chuỗi (có thể bị ghi đè nếu cần)

    # Phương thức is_active, is_authenticated, is_anonymous đều có sẵn trong UserMixin
