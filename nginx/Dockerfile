# Используем официальный образ Nginx
FROM nginx:latest

# Копируем конфиг Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Копируем SSL-сертификаты (если есть)
COPY ssl/ /etc/nginx/ssl/

# Копируем статику и медиа из Django
# COPY ./library/staticfiles /var/www/static/
# COPY ./library/media /var/www/media/

# Открываем порты
EXPOSE 80 443