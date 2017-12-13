from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def route_home():

    return render_template('home.html')


@app.route('/request-counter', methods=['GET', 'POST'])
def route_request_counter():
    counts = {GET:0, POST:0}
    global counts
    if methods == 'GET':
        counts[GET] += 1
    else:
        methods == 'POST':
        counts[POST] += 1
    return render_template('request_counter.html')

@app.route('/statistics')
def route_statistics():
    pass

if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True
    )
