from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient(
'mongodb+srv://test:sparta@cluster0.8d7bfaw.mongodb.net/?retryWrites=true&w=majority',
tlsCAFile = ca
)
db = client.dbsparta

@app.route('/')
def index_1():
  return render_template('index.html')

@app.route('/red')
def red():
  return render_template('red.html')

@app.route('/blue')
def blue():
  return render_template('blue.html')

@app.route('/black')
def black():
  return render_template('black.html')

@app.route('/yellow')
def yellow():
  return render_template('yellow.html')

@app.route('/pink')
def pink():
  return render_template('pink.html')

@app.route('/about_jn')
def about_jn():
  return render_template('about_jn.html')

@app.route("/api/save_comment", methods=["POST"])
def homework_post():
  name_receive = request.form['name_give']
  comment_receive = request.form['comment_give']
  time_receive = request.form['time_give']
  doc = {
    'name': name_receive,
    'comment': comment_receive,
    'time': time_receive
  }
  db.guest.insert_one(doc)
  return jsonify({'msg':'댓글 입력 완료!'})

@app.route("/api/load_comment", methods=["GET"])
def homework_get():
  comments_list = list(db.guest.find({},{'_id':False}))
  return jsonify({'comments_list': comments_list})


if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)