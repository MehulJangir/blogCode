
class League:

	def __init__(self,table):
		self.table = dict()
		self.table = table
		
	def does_team_exist(self, name):
		if self.table.get(name) == None:
			return False
		return True

	def add_team(self, team):
		self.table[team] = Team(team)

	def match_won(self, winner_name, loser_name, gd):
		self.table[winner_name].win(gd)
		self.table[loser_name].lose(gd)

	def match_drawn(self, name1, name2):
		self.table[name1].draw()
		self.table[name2].draw()

	def return_top_two(self):
		k = list(self.table.values())
		k = sorted(k, key = lambda x: (x.get_points(), x.get_gd()))
		return k[-1].get_name(), k[-2].get_name()

class Team:
	
	def __init__(self, name):
		self.name = name
		self.points = 0
		self.diff = 0

	def win(self, gd):
		self.points += 3
		self.diff += gd

	def lose(self, gd):
		self.diff -= gd

	def draw(self):
		self.points += 1

	def get_name(self):
		return self.name

	def get_points(self):
		return self.points

	def get_gd(self):
		return self.diff

def main():

	T = int(input())
	for _ in range(T):
		table = dict()
		league = League(table)
		for _ in range(12):
			result = str(input())
			result = result.split(' ')
			home_team_name, home_team_goals = result[0], int(result[1])
			away_team_goals, away_team_name = int(result[3]), result[4]
			if not league.does_team_exist(home_team_name):
				league.add_team(home_team_name)
			if not league.does_team_exist(away_team_name):
				league.add_team(away_team_name)
			if home_team_goals > away_team_goals:
				league.match_won(home_team_name, away_team_name, home_team_goals - away_team_goals)
			elif home_team_goals == away_team_goals:
				league.match_drawn(home_team_name, away_team_name)
			else:
				league.match_won(away_team_name, home_team_name, away_team_goals - home_team_goals)
		out = league.return_top_two()
		print(out[0] + " " + out[1])


main()