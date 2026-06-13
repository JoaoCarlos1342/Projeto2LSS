# Projeto 02 - Sistema de Monitorização Ambiental IoT

Este projeto implementa uma arquitetura IoT com sensores simulados, um broker MQTT (Mosquitto), uma base de dados relacional (PostgreSQL) para persistência e o Grafana para visualização.

## Como correr o projeto

1. Certifique-se que tem o Docker e o Docker Compose instalados.
2. Na raiz do repositório, execute:
   `docker-compose up --build`
3. Aceda ao Grafana em `http://localhost:3000` (User: `admin` | Pass: `admin`).

## Configurar o Grafana
1. Vá a Connections -> Data Sources -> Add data source.
2. Escolha "PostgreSQL".
3. Configure os detalhes:
   - Host: `db:5432`
   - Database: `iot_data`
   - User: `iot_user`
   - Password: `iot_password`
   - Desative o SSL Mode (coloque em `disable`).
4. Clique em "Save & Test".
5. Crie uma Dashboard utilizando a tabela `sensor_data` para visualizar `temperature`, `humidity` e `air_quality` usando o `timestamp`.