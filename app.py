from bottle import route, run, template
from bottle import debug
debug(True)


@route('/')
def index():
    return template('templates/index.tpl')


@route('/abalone', method='POST')
def result():
    return template('templates/result.tpl',
                    sex='不明',
                    length=0,
                    diameter=0,
                    height=0,
                    weight=0,
                    age=0)


# reloaderにTrueをセットするとファイル更新で再起動する
run(host='localhost', port=8080, reloader=True)
