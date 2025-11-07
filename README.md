# 🎯 Valorant Masters 2025 - System Monitoring with Prometheus & Grafana

**Assignment #4** - Real-time monitoring system for Valorant Masters 2025 tournament database and infrastructure.

## 📊 Project Overview

This project implements a comprehensive monitoring system using:
- **Prometheus** - metrics collection and storage
- **Grafana** - visualization and dashboards
- **Custom Exporters** - Valorant game statistics and database metrics

## 🏗️ System Architecture
┌─────────────────┐ ┌──────────────┐ ┌─────────────┐
│ Exporters │ │ Prometheus │ │ Grafana │
│ │ │ │ │ │
│ • Node │◄───│ 9091/tcp │◄───│ 3001/tcp │
│ • MySQL │ │ │ │ │
│ • Valorant │ │ Metrics │ │ Dashboards │
│ • Custom │ │ Storage │ │ Alerts │
└─────────────────┘ └──────────────┘ └─────────────┘

## 📁 Project Structure
final/
├── docker-compose.yml # Docker services configuration
├── prometheus.yml # Prometheus configuration
├── custom_exporter.py # Custom metrics exporter (Valorant stats)
├── mysql_exporter.py # MySQL database metrics exporter
├── valorant_exporter.py # Valorant game statistics exporter
├── node_exporter_dashboard.json # System metrics dashboard
├── mysql_dashboard.json # Database monitoring dashboard
├── valorant_dashboard.json # Valorant statistics dashboard
└── README.md # This file


## 🚀 Quick Start

### 1. Start Infrastructure
```bash``
docker-compose up -d
## 2. Start Exporters
# Terminal 1 - Custom Exporter (Valorant stats)
python custom_exporter.py

# Terminal 2 - MySQL Exporter  
python mysql_exporter.py

# Terminal 3 - Valorant Exporter
python valorant_exporter.py

3. Access Services
Grafana: http://localhost:3001 (admin/admin123)

Prometheus: http://localhost:9091

Node Exporter: http://localhost:9100/metrics
3. Access Services
Grafana: http://localhost:3001 (admin/admin123)

Prometheus: http://localhost:9091

Node Exporter: http://localhost:9100/metrics
mysql_global_status_threads_connected
rate(mysql_global_status_questions_total[5m])
mysql_database_size_bytes / 1024 / 1024
💻 2. Node Exporter - System Metrics (25 points)
Purpose: Monitor server infrastructure resources

Metrics: CPU, memory, disk, network, load average

Features: Multi-type visualizations, alerts, real-time data

Key PromQL Examples:
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
node_memory_MemAvailable_bytes / 1024 / 1024 / 1024
rate(node_network_receive_bytes_total[5m]) / 1024 / 1024

🎮 3. Custom Exporter - Valorant Statistics (45 points)
Purpose: Monitor Valorant tournament statistics and player performance

Metrics: Player ratings, ACS, K/D ratios, agent pick rates, match data

Features: Player selection, real-time updates, game-specific alerts
Key PromQL Examples:
valorant_player_rating{player_name="TenZ"}
rate(valorant_player_kills_total[5m])
valorant_agent_pick_rate


⚙️ Configuration
Prometheus Targets
All exporters are configured in prometheus.yml:

node_exporter:9100 - System metrics

host.docker.internal:8000 - Custom exporter

host.docker.internal:8001 - MySQL exporter

host.docker.internal:8002 - Valorant exporter

Alert Rules
MySQL: High connection count (>20 for 2+ minutes)

Node: High CPU usage (>80% for 2+ minutes)

Valorant: Low player rating (<1.0 for 2+ minutes)

🎯 Features Implemented
✅ General Requirements
Prometheus + Grafana connected and running

All exporters available on localhost ports

10+ PromQL queries per dashboard

60%+ queries use functions (rate, avg, etc.)

4+ visualization types per dashboard

Dashboard variables for filtering

Alert rules with visible status

Real-time data updates

JSON dashboards exported

All configuration files included

✅ Database Exporter Specific
Active connections monitoring

Database size tracking

Uptime monitoring

Query performance (QPS)

Slow query tracking

Network traffic metrics

✅ Node Exporter Specific
CPU usage per core

Memory utilization

Disk I/O monitoring

Network traffic

Load average

System uptime

✅ Custom Exporter Specific
10+ custom metrics (player stats, agent usage, match data)

Python exporter with prometheus_client

20-second update frequency

Mathematical functions in PromQL

Real-time Valorant tournament data

🛠️ Technical Details
Exporters
Update Frequency: 15-20 seconds

Metrics Count: 10+ metrics per exporter

Data Source: Simulated Valorant Masters 2025 tournament data

Data Simulation
The exporters generate realistic data simulating:

Player performance statistics

Agent pick/win rates

Match durations and results

Database query patterns

System resource utilization
