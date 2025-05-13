
import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

st.set_page_config(page_title="联系方式提取工具", layout="centered")
st.title("📬 联系方式提取工具")

url = st.text_input("请输入公司网站 URL（包含 http 或 https）")

def extract_contacts(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()

        emails = set(re.findall(r"[\w\.-]+@[\w\.-]+", text))
        phones = set(re.findall(r"(?:\+7|\+86|\+1)?[\s\-\(\)\d]{7,}", text))

        return list(emails), list(phones)
    except Exception as e:
        return [], [f"错误：{str(e)}"]

if st.button("提取联系方式"):
    if url:
        with st.spinner("正在抓取，请稍候..."):
            emails, phones = extract_contacts(url)
            st.subheader("📧 邮箱地址")
            st.write(emails if emails else "未找到邮箱")
            st.subheader("📞 电话号码")
            st.write(phones if phones else "未找到电话号码")
    else:
        st.warning("请输入有效的网址")
