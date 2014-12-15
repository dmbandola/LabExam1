Feature: An app that tallies the score of two teams in a game

		As a scorer, I want to tally the points of the two teams so I can keep track of the winner of the game.

		Scenario: Tally points of the team that scored
		Given there are two teams Team A and Team B
		When a team has scored
		Then the scoring teams updated scores will be displayed
			|team   |score|
			|Team A | 0 |
			|Team B | 0 |