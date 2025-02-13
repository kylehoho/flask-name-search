from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)
print(os.path.abspath(app.template_folder))

# 验证 search.html 文件是否存在
template_path = os.path.join(app.template_folder, 'search.html')
if os.path.exists(template_path):
    print("search.html 文件存在")
else:
    print("search.html 文件不存在")

# 读取 Excel 文件
file_path = '数据表1.xlsx'
df = pd.read_excel(file_path)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        result = df[df['姓名'].str.contains(keyword, na=False)]
        if not result.empty:
            # 将结果转换为列表的列表，方便在 HTML 中使用
            result = [result.columns.tolist()] + result.values.tolist()
        else:
            result = "未找到相关结果。"
    else:
        result = "请输入搜索关键词。"
    return render_template('search.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)