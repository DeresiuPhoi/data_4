from prometheus_client import start_http_server, Gauge, Counter, Histogram
import time
import random
import requests
from datetime import datetime

class ValorantMetrics:
    def __init__(self):
        # Метрики для Valorant статистики
        self.player_count = Gauge('valorant_players_online', 'Number of online players')
        self.match_activity = Counter('valorant_matches_played_total', 'Total matches played', ['map', 'mode'])
        self.kill_death_ratio = Gauge('valorant_kill_death_ratio', 'Average K/D ratio')
        self.headshot_percentage = Gauge('valorant_headshot_percentage', 'Headshot percentage')
        self.damage_per_round = Gauge('valorant_damage_per_round', 'Average damage per round')
        self.ability_usage = Counter('valorant_ability_used_total', 'Abilities used', ['ability_type'])
        self.rank_distribution = Gauge('valorant_players_by_rank', 'Players by rank', ['rank'])
        self.server_latency = Gauge('valorant_server_latency_ms', 'Server latency in milliseconds')
        self.weapon_usage = Gauge('valorant_weapon_usage', 'Weapon usage statistics', ['weapon_type'])
        self.game_duration = Histogram('valorant_match_duration_seconds', 'Match duration in seconds',
                                      buckets=[300, 600, 900, 1200, 1800, 2400, 3000, 3600])
        
        # Метрики для внешних API
        self.weather_temperature = Gauge('external_weather_temperature', 'Current temperature')
        self.currency_rate = Gauge('external_currency_rate', 'Currency exchange rate', ['currency'])
        self.air_quality = Gauge('external_air_quality', 'Air quality index')
        self.github_stars = Gauge('external_github_stars', 'GitHub repository stars')
        self.crypto_price = Gauge('external_crypto_price', 'Cryptocurrency price', ['crypto'])

    def update_valorant_metrics(self):
        """Обновление метрик Valorant"""
        try:
            # Онлайн игроки
            self.player_count.set(random.randint(5000, 15000))
            
            # Активность матчей
            maps = ['Bind', 'Haven', 'Split', 'Ascent', 'Icebox']
            modes = ['Competitive', 'Unrated', 'Spike Rush']
            
            for map_name in maps:
                for mode in modes:
                    self.match_activity.labels(map=map_name, mode=mode).inc(random.randint(1, 5))
            
            # Игровая статистика
            self.kill_death_ratio.set(round(random.uniform(0.8, 1.8), 2))
            self.headshot_percentage.set(round(random.uniform(18, 42), 1))
            self.damage_per_round.set(random.randint(130, 220))
            
            # Использование способностей
            abilities = ['Smoke', 'Flash', 'Heal', 'Ultimate', 'Wall']
            for ability in abilities:
                self.ability_usage.labels(ability_type=ability).inc(random.randint(2, 8))
            
            # Распределение по рангам
            ranks = ['Iron', 'Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Immortal', 'Radiant']
            for rank in ranks:
                self.rank_distribution.labels(rank=rank).set(random.randint(500, 3500))
            
            # Задержка сервера
            self.server_latency.set(random.randint(15, 65))
            
            # Использование оружия
            weapons = ['Vandal', 'Phantom', 'Operator', 'Spectre', 'Classic']
            for weapon in weapons:
                self.weapon_usage.labels(weapon_type=weapon).set(random.randint(800, 2500))
            
            # Длительность матча
            self.game_duration.observe(random.randint(1200, 3600))
            
        except Exception as e:
            print(f"Error updating Valorant metrics: {e}")

    def update_external_apis(self):
        """Обновление данных из внешних API"""
        try:
            # Погода (симуляция)
            self.weather_temperature.set(round(random.uniform(-5, 30), 1))
            
            # Курсы валют
            currencies = ['USD', 'EUR', 'GBP', 'JPY']
            base_rates = {'USD': 1.0, 'EUR': 0.85, 'GBP': 0.75, 'JPY': 110.0}
            for currency in currencies:
                variation = random.uniform(0.95, 1.05)
                rate = round(base_rates[currency] * variation, 4)
                self.currency_rate.labels(currency=currency).set(rate)
            
            # Качество воздуха
            self.air_quality.set(random.randint(25, 175))
            
            # GitHub stars (симуляция)
            self.github_stars.set(random.randint(1000, 5000))
            
            # Цены криптовалют
            cryptos = ['bitcoin', 'ethereum', 'solana']
            base_prices = {'bitcoin': 45000, 'ethereum': 3000, 'solana': 120}
            for crypto in cryptos:
                variation = random.uniform(0.98, 1.02)
                price = round(base_prices[crypto] * variation, 2)
                self.crypto_price.labels(crypto=crypto).set(price)
                
        except Exception as e:
            print(f"Error updating external APIs: {e}")

def main():
    metrics = ValorantMetrics()
    start_http_server(8000)
    print("🚀 Custom exporter started on http://localhost:8000")
    
    while True:
        print(f"📊 Updating metrics at {datetime.now().strftime('%H:%M:%S')}")
        metrics.update_valorant_metrics()
        metrics.update_external_apis()
        time.sleep(20)

if __name__ == '__main__':
    main()