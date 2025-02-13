import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)


def load_data():
    try:
        df = pd.read_excel('C:\\Users\\DELL\\Desktop\\2025年会\\数据表1.xlsx')
        print('数据全部内容信息：')
        print(df.to_csv(sep='\t', na_rep='nan'))
        data = df.values.flatten().tolist()
        return data
    except FileNotFoundError:
        print('C:\\Users\\DELL\\Desktop\\2025年会\\数据表1.xlsx 文件未找到')
        return []


table_data = load_data()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    query = request.args.get('name')
    global table_data
    print('当前使用的 table_data:', table_data)
    results = [name for name in table_data if query.lower() in name.lower()]
    print('搜索结果 results:', results)
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)