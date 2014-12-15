"""This is a docstring"""
from flask import Flask, render_template, request
from lab.scores import Score
from lab.teams import Team

APP = Flask(__name__)
SCORES = Score()

@APP.route('/')
def hello_world():
    """This is another function"""
    team_name = request.args.get('team_name')
    score = BANK.get_team_score(team_name)
    return render_template('lab.html', score=score)

if __name__ == '__main__':
    import cProfile

    SCORES.add_team_score(Team('Team A', 0))
    cProfile.run('APP.run(debug=True)', sort='time')