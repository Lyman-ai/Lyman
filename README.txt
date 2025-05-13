
# 📬 联系方式提取工具（Streamlit 版本）

## 功能
输入任意公司官网地址，自动提取页面中出现的邮箱地址和电话号码。

## 使用方法（本地）
1. 安装依赖：
```
pip install streamlit beautifulsoup4 requests
```

2. 运行工具：
```
streamlit run contact_tool.py
```

3. 浏览器中打开 `http://localhost:8501` 即可使用。

## 云部署（可选）
如需部署为网页工具，请将 `contact_tool.py` 上传至 GitHub 并连接至 [streamlit.io/cloud](https://streamlit.io/cloud)。支持免费部署。
