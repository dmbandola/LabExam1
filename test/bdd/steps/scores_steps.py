import lettuce
from scores import Scores
from teams import Team

@step(u'Given there are two teams')
def given_there_are_two_teams(step):
    team = Team()
    teamA = Team('Team A', 0)
    teamB = Team('Team B', 0)
    team.add_team(teamA)
    team.add_team(teamB)
    self.assertEqual(len(lab.teams), 2)