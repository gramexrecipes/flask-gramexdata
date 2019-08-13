import gramex.data
import gramex.cache
from pathlib import Path
from flask import Flask, make_response, render_template, request

app = Flask(__name__)
config = gramex.cache.open(Path().absolute() / 'config.yaml', 'config')


@app.route('/flags')
def gramexdata():
    args = request.args.to_dict(flat=False)
    data = gramex.data.filter(url=config.data.flags, args=args)
    fmt = args.get('_format', ['json'])[0]
    result = gramex.data.download(data, format=fmt)
    return make_response((result, config.formats.get(fmt)))


@app.route('/')
def docs():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
