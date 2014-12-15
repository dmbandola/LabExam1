import unittest

class ScoreTest(unittest.TestCase):
    def test_add_team:
        team = Team(team_name, score)
        teamA = Team('Team A', 0)
        teamB = Team('Team B', 0)
        team.add_team(teamA)
        team.add_team(teamB)
        self.assertEqual(len(lab.teams), 2)
