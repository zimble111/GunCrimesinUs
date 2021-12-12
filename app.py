from flask import Flask, render_template, url_for
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)
data = pd.read_csv('guns.csv')
s1 = data.describe()
s1.to_html('templates/1.html')
data.age.plot(kind='hist')
plt.savefig('static/2.png')
plt.clf()
plt.pie(data.race.value_counts().values, labels=data.race.value_counts().index)
plt.savefig('static/3.png')
plt.clf()
plt.bar(data.education.value_counts().index, data.education.value_counts().values)
plt.savefig('static/4.png')
plt.clf()
plt.pie(data.intent.value_counts().values, labels=data.intent.value_counts().index)
plt.savefig('static/5.png')
plt.clf()
s2 = sns.barplot(x=data.intent,y=data.age, hue='sex', data=data).get_figure()
s2.savefig('static/7.png')
s3 = sns.histplot(x='education', hue='race', data=data, weights=1.4, bins=10).get_figure()
s3.savefig('static/8.png')


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/1')
def n1():
    return render_template('1.html')


@app.route('/2')
def n2():
    return render_template('2.html')


@app.route('/3')
def n3():
    return render_template('3.html')


@app.route('/4')
def n4():
    return render_template('4.html')


@app.route('/5')
def n5():
    return render_template('5.html')


@app.route('/7')
def n7():
    return render_template('7.html')


@app.route('/8')
def n8():
    return render_template('8.html')


@app.route('/9')
def n9():
    return render_template('9.html')


if __name__ == '__main__':
    app.run(debug=True)