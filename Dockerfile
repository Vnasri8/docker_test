# Chọn image Python chính thức từ Docker hub
FROM python:3.9-slim

# Đặt thư mục làm việc cho ứng dụng Flask
WORKDIR /app

# Sao chép file yêu cầu Python (requirements.txt) vào container
COPY requirements.txt /app/

# Cài đặt tất cả các thư viện Python từ requirments.txt
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn ứng dụng Flask vào trong container
COPY . /app/

# Mở cổng 5000 để ứng dụng Flask có thể truy cập từ ngoài
EXPOSE 5000

# Lệnh chạy ứng dụng Flask khi container khởi động
CMD ["python", "app.py"]
