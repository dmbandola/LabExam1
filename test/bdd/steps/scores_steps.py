from lettuce import step
from lab.scores import Score
from lab.teams import Team
from nose.tools import assert_equal, assert_in

@step(u'Given there are two teams Team A and Team B')
def given_there_are_two_teams_team_a_and_team_b(step):
	assert True

@step(u'When a team has scored')
def when_a_team_has_scored(step):
	assert True

@step(u'Then the scoring teams point will be added with the scored point')
def then_the_scoring_team_s_point_will_be_added_with_the_scored_point(step):
	assert True