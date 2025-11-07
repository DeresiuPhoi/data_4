from prometheus_client import start_http_server, Gauge, Counter, Histogram
import time
import random
from datetime import datetime

class ValorantExporter:
    def __init__(self):
        # Player Statistics
        self.player_rating = Gauge('valorant_player_rating', 'Player rating', ['player_name', 'team'])
        self.player_acs = Gauge('valorant_player_acs', 'Average Combat Score', ['player_name', 'team'])
        self.player_kills = Counter('valorant_player_kills', 'Player kills', ['player_name', 'team'])
        self.player_deaths = Counter('valorant_player_deaths', 'Player deaths', ['player_name', 'team'])
        self.player_kd_ratio = Gauge('valorant_player_kd_ratio', 'K/D Ratio', ['player_name', 'team'])
        self.headshot_percent = Gauge('valorant_headshot_percent', 'Headshot %', ['player_name', 'team'])
        
        # Match Statistics
        self.matches_played = Counter('valorant_matches_played', 'Matches played')
        self.match_duration = Histogram('valorant_match_duration', 'Match duration', buckets=[600, 1200, 1800, 2400, 3000])
        
        # Agent Statistics
        self.agent_pick_rate = Gauge('valorant_agent_pick_rate', 'Agent pick rate', ['agent_name'])
        self.agent_win_rate = Gauge('valorant_agent_win_rate', 'Agent win rate', ['agent_name'])
        
        # Team Statistics
        self.team_rating = Gauge('valorant_team_rating', 'Team rating', ['team_name'])
        self.team_maps_won = Counter('valorant_team_maps_won', 'Maps won', ['team_name'])
        
        # Economy
        self.pistol_rounds = Counter('valorant_pistol_rounds', 'Pistol rounds', ['team_name', 'result'])
        self.eco_rounds = Counter('valorant_eco_rounds', 'Eco rounds', ['team_name', 'result'])

    def update_metrics(self):
        """Update Valorant metrics"""
        try:
            players = [
                {'name': 'TenZ', 'team': 'Sentinels'},
                {'name': 'yay', 'team': 'Cloud9'},
                {'name': 'Derke', 'team': 'Fnatic'},
                {'name': 'aspas', 'team': 'LOUD'},
                {'name': 'cNed', 'team': 'Navi'}
            ]
            
            agents = ['Jett', 'Reyna', 'Phoenix', 'Sage', 'Omen', 'Viper', 'Brimstone', 'Raze']
            teams = ['Sentinels', 'Cloud9', 'Fnatic', 'LOUD', 'Navi', 'DRX', 'PRX']
            
            # Update player metrics
            for player in players:
                rating = round(random.uniform(0.8, 1.8), 2)
                acs = random.randint(180, 320)
                kd = round(random.uniform(0.7, 1.5), 2)
                hs = random.randint(15, 35)
                
                self.player_rating.labels(
                    player_name=player['name'],
                    team=player['team']
                ).set(rating)
                
                self.player_acs.labels(
                    player_name=player['name'],
                    team=player['team']
                ).set(acs)
                
                self.player_kd_ratio.labels(
                    player_name=player['name'],
                    team=player['team']
                ).set(kd)
                
                self.headshot_percent.labels(
                    player_name=player['name'],
                    team=player['team']
                ).set(hs)
                
                # Increment counters
                kills = random.randint(1, 5)
                deaths = random.randint(1, 4)
                
                self.player_kills.labels(
                    player_name=player['name'],
                    team=player['team']
                ).inc(kills)
                
                self.player_deaths.labels(
                    player_name=player['name'],
                    team=player['team']
                ).inc(deaths)
            
            # Update agent metrics
            for agent in agents:
                pick_rate = round(random.uniform(0.1, 0.9), 2)
                win_rate = round(random.uniform(0.4, 0.8), 2)
                
                self.agent_pick_rate.labels(agent_name=agent).set(pick_rate)
                self.agent_win_rate.labels(agent_name=agent).set(win_rate)
            
            # Update team metrics
            for team in teams:
                team_rating = round(random.uniform(0.9, 1.6), 2)
                self.team_rating.labels(team_name=team).set(team_rating)
                
                maps_won = random.randint(0, 2)
                self.team_maps_won.labels(team_name=team).inc(maps_won)
            
            # Update match metrics
            self.matches_played.inc(1)
            self.match_duration.observe(random.randint(1200, 3600))
            
            # Update economy metrics
            for team in teams[:3]:
                self.pistol_rounds.labels(team_name=team, result='won').inc(random.randint(0, 1))
                self.pistol_rounds.labels(team_name=team, result='lost').inc(random.randint(0, 1))
                self.eco_rounds.labels(team_name=team, result='won').inc(random.randint(0, 2))
                self.eco_rounds.labels(team_name=team, result='lost').inc(random.randint(0, 2))
            
            print(f"Valorant metrics updated: {len(players)} players, {len(agents)} agents")
            
        except Exception as e:
            print(f"Error: {e}")

def main():
    exporter = ValorantExporter()
    start_http_server(8002)
    print("Valorant Exporter started on http://localhost:8002")
    print("Tracking: Players, Agents, Matches, Economy")
    
    while True:
        exporter.update_metrics()
        time.sleep(15)

if __name__ == '__main__':
    main()