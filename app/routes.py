from app import app

from flask import render_template

@app.route('/')
def homePage():
    fav_pokemon = 'Ditto'
    return render_template('base.html', f = fav_pokemon)

@app.route('/index')
def indexPage():
    return render_template('login.html')



@app.route('/favorite_5')
def favorite_5():
    pokemon = [
        {
        'name': 'Mewtwo',
        'ability': 'pressure'
        },
        {
        'name': 'Charmander',
        'ability': 'blaze'
        },
        {
        'name': 'Eevee',
        'ability': 'adaptability'
        },
        {
        'name': 'Lucario',
        'ability': 'steadfast'
        },
        {
        'name': 'Piplup',
        'ability': 'torrent'
        }
    ]
    
    return render_template('index.html', pokemon=pokemon)