from bokeh.plotting import figure
from bokeh.embed import components
from collections import namedtuple
from abalone_predictor import AbalonePredictor
from bottle import(
    default_app, route, template,
    request, HTTPError)
# debug(True)

READABLE_SEX = ['メス', '不明', 'オス']

INPUT_DATA = ('sex', 'length', 'diameter', 'height', 'weight')

BaseAbalone = namedtuple('BaseAbalone', INPUT_DATA + ('age',))


class Abalone(BaseAbalone):
    @property
    def sex_str(self):
        return READABLE_SEX[int(self.sex)]


@route('/')
def index():
    return template('templates/index.tpl')


@route('/abalone', method='POST')
def result():
    try:
        age = calc_age(**request.params)
        abalone = Abalone(age=age, **request.params)
    except (TypeError, ValueError) as e:
        raise HTTPError(status=400, body=e)
    else:
        script, div = get_graph(abalone)
        return template('templates/result.tpl', abalone=abalone, script=script, graph=div)


_predictor = AbalonePredictor()


def calc_age(sex, length, diameter, height, weight):
    age = _predictor.predict(
        int(sex),
        int(length),
        int(diameter),
        int(height),
        int(weight))
    return float(age)


def get_graph(abalone):
    p = figure(plot_width=400, plot_height=400, title='実年齢と推定値の分布')
    p.xaxis.axis_label = '実年齢'
    p.ｙaxis.axis_label = '推定値'

    p.line([0, 30], [0, 30], line_dash='dotted', legend='実年齢と推定値が一致するライン')

    p.circle(_predictor.y_train, _predictor.prediction, legend='訓練データにおける分布')

    p.line([0, 30], [abalone.age, abalone.age],
           legend='捕まえたアワビの推定年齢', color="green")
    p.legend.location = 'top_left'
    p.legend.click_policy = 'mute'

    # JavaScriptコード生成
    script, div = components(p)
    return script, div

application = default_app()

