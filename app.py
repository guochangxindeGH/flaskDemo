from flask import Flask, abort, request, jsonify

# from flask import request

# 创建一个应用
app = Flask(__name__)

tasks = []


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>hello world!<h1>'


@app.route('/add_task/', methods=['POST'])
def add_task():
    if not request.json or 'id' not in request.json or 'info' not in request.json:
        abort(400)
    task = {
        'id': request.json['id'],
        'info': request.json['info']
    }
    tasks.append(task)
    return jsonify({'result': 'success'})


@app.route('/get_task/', methods=['GET'])
def get_task():
    if not request.args or 'id' not in request.args:
        # 没有指定id则返回全部
        return jsonify(tasks)
    else:
        task_id = request.args['id']
        task = filter(lambda t: t['id'] == int(task_id), tasks)
        return jsonify(task) if task else jsonify({'result': 'not found'})


if __name__ == '__main__':
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(host="0.0.0.0", port=5000, debug=True)
