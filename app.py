from flask import Flask,render_template, url_for



app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/OregaAi')
def OregaAi():
    return render_template('OregaAi.html')

@app.route('/robotics')
def robotics():
    return render_template('robotics.html')

@app.route('/cars')
def cars():
    return render_template('cars.html')

@app.route('/plans')
def plans():
    return render_template('plans.html')



@app.route('/game')
def oregagamestudios():
    return render_template('game.html')

@app.route('/plansgame')
def plansgame():
    return render_template('plansgame.html')

@app.route('/ourprojects')
def ourprojects():
    return render_template('ourprojects.html')

@app.route('/ourprojectsgame')
def ourprojectsgame():
    return render_template('ourprojectsgame.html')

@app.route('/fps')
def fps():
    return render_template('fps.html')


@app.route('/footballsimulator')
def footballsimulator():
    return render_template('footballsimulator.html')

@app.route('/oregapass')
def oregpass():
    return render_template('oregapass.html')

@app.route('/orega_media_holding')
def orega_media_holding():
    return render_template('orega_media_holding.html')

@app.route('/orega_media_holding_plans')
def orega_media_holding_plans():
    return render_template('orega_media_holding_plans.html')

if __name__ == '__main__':
    app.run(debug=True)