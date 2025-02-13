from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# 配置文件路径
EXCEL_FILE_PATH = os.environ.get('EXCEL_FILE_PATH', '/mnt/数据表1.xlsx')

@app.route('/')
def index():
    """
    渲染首页模板
    :return: 渲染 index.html 模板
    """
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    """
    处理搜索请求，根据用户输入的关键词在 Excel 文件中查找匹配的姓名信息
    :return: 渲染 search.html 模板并传递搜索结果
    """
    keyword = request.form.get('keyword')
    try:
        df = pd.read_excel(EXCEL_FILE_PATH)
        # 打印读取到的数据基本信息
        print('读取到的数据基本信息：')
        df.info()
        # 打印读取到的数据内容信息
        print('读取到的数据内容信息：')
        print(df.to_csv(sep='\t', na_rep='nan'))
        # 筛选包含关键词的姓名数据
        results = df[df['姓名'].str.contains(keyword, na=False)]
        # 打印匹配结果
        print('匹配结果：')
        print(results.to_csv(sep='\t', na_rep='nan'))
    except FileNotFoundError:
        results = pd.DataFrame(columns=['姓名', '出发日期', '出发时间', '班次'])
        print(f"未找到 {EXCEL_FILE_PATH} 文件，请检查文件路径。")
    return render_template('search.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)