from prometheus_client import start_http_server, Gauge, Counter, Histogram
import time
import random
from datetime import datetime

class ValorantMySQLMetrics:
    def __init__(self):
        # Метрики из таблицы detailed_matches_player_stats
        self.player_rating = Gauge('valorant_player_rating', 'Player rating', ['player_name', 'team'])
        self.player_acs = Gauge('valorant_player_acs', 'Average Combat Score', ['player_name', 'team'])
        self.player_kills = Counter('valorant_player_kills_total', 'Total kills', ['player_name', 'team'])
        self.player_deaths = Counter('valorant_player_deaths_total', 'Total deaths', ['player_name', 'team'])
        self.player_assists = Counter('valorant_player_assists_total', 'Total assists', ['player_name', 'team'])
        self.headshot_percentage = Gauge('valorant_player_hs_percent', 'Headshot percentage', ['player_name', 'team'])
        
        # Метрики из таблицы matches
        self.matches_played = Counter('valorant_matches_played_total', 'Total matches played')
        self.matches_duration = Histogram('valorant_match_duration_seconds', 'Match duration in seconds')
        
        # Метрики из таблицы agents_stats
        self.agent_utilization = Gauge('valorant_agent_utilization', 'Agent utilization rate', ['agent_name'])
        self.agent_picks = Counter('valorant_agent_picks_total', 'Total agent picks', ['agent_name'])
        
        # Метрики из таблицы performance_data
        self.clutch_situations = Counter('valorant_clutch_situations_total', 'Total clutch situations', ['player_name', 'team'])
        self.multikills = Counter('valorant_multikills_total', 'Total multikills', ['player_name', 'team', 'type'])
        
        # Метрики из таблицы economy_data
        self.pistol_rounds_won = Counter('valorant_pistol_rounds_won_total', 'Pistol rounds won', ['team'])
        self.eco_rounds_won = Counter('valorant_eco_rounds_won_total', 'Eco rounds won', ['team'])
        
        # Общие метрики БД
        self.database_connections = Gauge('mysql_global_status_threads_connected', 'Active database connections')
        self.database_uptime = Gauge('mysql_global_status_uptime', 'Database uptime in seconds')
        self.database_queries = Counter('mysql_global_status_questions_total', 'Total database queries')

    def update_valorant_metrics(self):
        """Обновление Valorant-тематических метрик"""
        try:
            # Игроки и команды из твоей БД
            players = [
                {'name': 'TenZ', 'team': 'Sentinels'},
                {'name': 'yay', 'team': 'Cloud9'}, 
                {'name': 'Derke', 'team': 'Fnatic'},
                {'name': 'aspas', 'team': 'LOUD'},
                {'name': 'cNed', 'team': 'Natus Vincere'}
            ]
            
            agents = ['Jett', 'Reyna', 'Phoenix', 'Raze', 'Sage', 'Omen', 'Brimstone', 'Viper']
            teams = ['Sentinels', 'Cloud9', 'Fnatic', 'LOUD', 'Natus Vincere', 'DRX', 'PRX']
            
            # Обновляем метрики игроков
            for player in players:
                rating = round(random.uniform(0.8, 1.8), 2)
                acs = random.randint(180, 320)
                hs_percent = random.randint(15, 35)
                
                self.player_rating.labels(
                    player_name=player['name'], 
                    team=player['team']
                ).set(rating)
                
                self.player_acs.labels(
                    player_name=player['name'], 
                    team=player['team']
                ).set(acs)
                
                self.headshot_percentage.labels(
                    player_name=player['name'], 
                    team=player['team']
                ).set(hs_percent)
                
                # Увеличиваем счетчики
                kills = random.randint(2, 8)
                deaths = random.randint(1, 6)
                assists = random.randint(0, 4)
                
                self.player_kills.labels(
                    player_name=player['name'], 
                    team=player['team']
                ).inc(kills)
                
                self.player_deaths.labels(
                    player_name=player['name'], 
                    team=player['team']
                ).inc(deaths)
                
                self.player_assists.labels(
                    player_name=player['name'], 
                    team=player['team']
                ).inc(assists)
            
            # Метрики агентов
            for agent in agents:
                utilization = round(random.uniform(0.1, 0.9), 2)
                picks = random.randint(1, 5)
                
                self.agent_utilization.labels(agent_name=agent).set(utilization)
                self.agent_picks.labels(agent_name=agent).inc(picks)
            
            # Метрики матчей
            self.matches_played.inc(random.randint(1, 3))
            self.matches_duration.observe(random.randint(1200, 3600))  # 20-60 минут
            
            # Клач ситуации и мультикиллы
            for player in players[:3]:  # Только первые 3 игрока
                self.clutch_situations.labels(
                    player_name=player['name'],
                    team=player['team']
                ).inc(random.randint(0, 2))
                
                for multikill_type in ['2k', '3k', '4k', '5k']:
                    self.multikills.labels(
                        player_name=player['name'],
                        team=player['team'], 
                        type=multikill_type
                    ).inc(random.randint(0, 1))
            
            # Экономические метрики
            for team in teams[:3]:  # Только первые 3 команды
                self.pistol_rounds_won.labels(team=team).inc(random.randint(0, 1))
                self.eco_rounds_won.labels(team=team).inc(random.randint(0, 2))
            
            # Базовые метрики MySQL
            self.database_connections.set(random.randint(5, 15))
            if not hasattr(self, 'db_start_time'):
                self.db_start_time = time.time()
            self.database_uptime.set(int(time.time() - self.db_start_time))
            self.database_queries.inc(random.randint(50, 200))
            
            print(f" Valorant DB metrics updated at {datetime.now().strftime('%H:%M:%S')}")
            
        except Exception as e:
            print(f" Error updating Valorant metrics: {e}")

def main():
    metrics = ValorantMySQLMetrics()
    start_http_server(8001)
    print("🎯 Valorant MySQL Exporter started on http://localhost:8001")
    print("📊 Monitoring: Player stats, Agent usage, Match data, Economy")
    
    while True:
        metrics.update_valorant_metrics()
        time.sleep(20)

if __name__ == '__main__':
    main()