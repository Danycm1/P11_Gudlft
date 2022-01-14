import json
from datetime import datetime

from flask import Flask, render_template, request, redirect, flash, url_for


def load_clubs():
    with open('clubs.json') as c:
        list_of_clubs = json.load(c)['clubs']
        return list_of_clubs


def load_competitions():
    with open('competitions.json') as comps:
        list_of_competitions = json.load(comps)['competitions']
        return list_of_competitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = load_competitions()
clubs = load_clubs()

current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def show_summary():
    """
    Allow use to login to the site if the email is in the database
    :return: OK only if the email is in the database, else throw an error
    """
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html', club=club, competitions=competitions, date=current_date)
    except IndexError:
        flash('Email is invalid. Please try again.')
        return render_template('index.html')


@app.route('/book/<competition>/<club>')
def book(competition, club):
    found_club = [c for c in clubs if c['name'] == club][0]
    found_competition = [c for c in competitions if c['name'] == competition][0]

    if found_club and found_competition:
        return render_template('booking.html', club=found_club, competition=found_competition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions, date=current_date)


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    places_required = int(request.form['places'])

    if datetime.now() > datetime.strptime(competition["date"], "%Y-%m-%d %H:%M:%S"):
        flash('You cannot purchase places from past competition')
    elif places_required > 12:
        flash('You cannot purchase more than 12 places.')
    elif int(club['points']) < places_required:
        flash('Not enough points to purchase.')
    elif places_required <= 0:
        flash('You must at least buy one place')
    elif places_required > int(competition['numberOfPlaces']):
        flash('You cannot purchase more places than available.')
    else:
        competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
        club['points'] = int(club['points']) - places_required
        flash(f'Great-booking complete! you bought {places_required} places')
    return render_template('welcome.html', club=club, competitions=competitions, date=current_date)


@app.route('/displayPoints')
def display_points():
    return render_template('points.html', club=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
