import unittest
from teams import Team

class ScoreTest(unittest.TestCase):
    def test_add_team(self):
        team = Team(team_name, score)
        teamA = Team('Team A', 0)
        teamB = Team('Team B', 0)
        team.add_team(teamA)
        team.add_team(teamB)
        self.assertEqual(len(lab.teams), 2)

    def test_get_team_score(self):
        team = Team(team_name, score)
        teamA = Team('Team A', 0)
        scores.add_team(teamA)
        self.assertEqual(scores.get_team_score)

    def test_add_team_score(self):
    	team = Team(team_name, score)
    	teamA = Team('Team A', 0)
    	scores.add_team_score('Team A', 2, 0)
    	self.assertEqual(scores.get_team_score, 2)

if __name__ == '__main__':
    unittest.main()
