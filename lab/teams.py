class Team(object):
    def __init__(self, team_name, score):
        self.team_name = team_name
        self.score = score


    def check_if_int(self, score):
    	if type(score) == int:
    		return self.score
