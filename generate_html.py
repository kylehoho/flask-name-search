import pandas as pd

# 读取 Excel 文件
excel_file = pd.ExcelFile('数据表1.xlsx')
df = excel_file.parse('Sheet1')

# 创建包含搜索框和 JavaScript 代码的 HTML 文件
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search Results</title>
    <style>
        input[type=text] {{
            width: 200px;
            padding: 12px 20px;
            margin: 8px 0;
            box-sizing: border-box;
        }}
        button {{
            padding: 12px 20px;
            margin: 8px 0;
            box-sizing: border-box;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
        }}
    </style>
</head>
<body>
    <h1>Search by Name</h1>
    <input type="text" id="searchInput" placeholder="Search for names..">
    <button onclick="searchTable()">Search</button>
    <div id="searchResults"></div>

    <script>
        const data = {df.to_json(orient='records')};
        function searchTable() {{
            const input = document.getElementById("searchInput");
            const filter = input.value.toUpperCase();
            const results = [];
            for (let i = 0; i < data.length; i++) {{
                const row = data[i];
                const name = Object.values(row)[0].toString().toUpperCase();
                if (name.indexOf(filter) > -1) {{
                    results.push(row);
                }}
            }}
            const resultsDiv = document.getElementById("searchResults");
            if (results.length === 0) {{
                resultsDiv.innerHTML = '<p>No results found.</p>';
            }} else {{
                let tableHtml = '<table>';
                const headers = Object.keys(results[0]);
                tableHtml += '<tr>';
                for (let header of headers) {{
                    tableHtml += `<th>${{header}}</th>`;
                }}
                tableHtml += '</tr>';
                for (let result of results) {{
                    tableHtml += '<tr>';
                    for (let value of Object.values(result)) {{
                        tableHtml += `<td>${{value}}</td>`;
                    }}
                    tableHtml += '</tr>';
                }}
                tableHtml += '</table>';
                resultsDiv.innerHTML = tableHtml;
            }}
        }}
    </script>
</body>
</html>
"""

# 保存 HTML 文件
with open('search_results.html', 'w', encoding='utf-8') as f:
    f.write(html_content)