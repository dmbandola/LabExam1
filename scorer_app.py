"""This is a docstring"""
from flask import Flask, render_template, request
from lab.scores import Score
from lab.teams import Team

APP = Flask(__name__)
SCORES = Score()

@APP.route('/')
def index():
    return render_template('lab.html')

@APP.route('/')
def display_teamA_score():
    """This is another function"""
    teamA = request.args.get('Team A')
    scoreA = BANK.get_team_score(teamA)
    return render_template('success.html', scoreA=scoreA)

@APP.route('/')
def display_teamB_score():
    """This is another function"""
    teamB = request.args.get('Team B')
    scoreB = BANK.get_team_score(teamB)
    return render_template('success.html', scoreB=scoreB)


if __name__ == '__main__':
    import cProfile

    SCORES.add_team_score(Team('Team A', 0))
    cProfile.run('APP.run(debug=True)', sort='time')