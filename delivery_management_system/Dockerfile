# Dockerfile

FROM alpine:latest

# Копируем wait.sh внутрь образа
COPY wait.sh /wait.sh
RUN chmod +x /wait.sh

# Команда по умолчанию для запуска вашего приложения
CMD ["./wait.sh"]
