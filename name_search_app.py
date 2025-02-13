from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form.get('keyword')
    try:
        df = pd.read_excel('/mnt/数据表1.xlsx')
        print('读取到的数据基本信息：')
        df.info()
        print('读取到的数据内容信息：')
        print(df.to_csv(sep='\t', na_rep='nan'))
        results = df[df['姓名'].str.contains(keyword, na=False)]
        print('匹配结果：')
        print(results.to_csv(sep='\t', na_rep='nan'))
    except FileNotFoundError:
        results = pd.DataFrame(columns=['姓名', '出发日期', '出发时间', '班次'])
        print("未找到数据表1.xlsx文件，请检查文件路径。")
    return render_template('search.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)