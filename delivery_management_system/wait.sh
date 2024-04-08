#!/bin/sh
set -e

# Ожидание доступности сервиса (хост:порт)
wait_for_service() {
    host=$1
    port=$2

    until nc -z $host $port; do
        echo "Waiting for $host:$port to be available..."
        sleep 1
    done

    echo "$host:$port is available!"
}

# Ожидание всех необходимых сервисов
wait_for_service authentication_database 5432
wait_for_service orders_database 5432
wait_for_service warehouses_database 5432
wait_for_service delivery_database 5432

# Здесь можно добавить запуск вашего приложения
echo "All required services are available. Starting your application..."
# Команда для запуска вашего приложения
