import streamlit as st
import time
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import requests
from threading import Thread

def update_access_time():
    """ 访问 Streamlit 页面时调用后端 API 记录最后访问时间 """
    appid = "Calculator"  # 你的 Streamlit 应用 ID
    flask_server_url = "http://11.2.171.248:5000"  # 你的 Flask 服务器地址
    url = f"{flask_server_url}/api/apps/{appid}/update_access_time"

    try:
        response = requests.post(url)
        if response.status_code == 200:
            st.success("访问时间已更新")
        else:
            st.warning("无法更新访问时间")
    except Exception as e:
        st.error(f"更新访问时间失败: {e}")

# **只在用户首次进入页面（当前会话）时调用**
if "access_logged" not in st.session_state:
    update_access_time()
    st.session_state.access_logged = True  # 标记当前会话已记录访问时间

# 设置页面配置
st.set_page_config(
    page_title="大时钟",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 隐藏Streamlit默认样式
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 设置时钟样式
clock_css = """
    <style>
    .clock {
        font-size: 120px;
        font-family: 'Courier New', monospace;
        text-align: center;
        color: #FF4500;
        margin-top: 20%;
    }
    </style>
"""

st.markdown(clock_css, unsafe_allow_html=True)

# 创建时钟显示
placeholder = st.empty()

# 动态更新时钟
def update_clock():
    while True:
        # 获取当前时间
        current_time = datetime.now().strftime("%H:%M:%S")
        # 更新时钟显示
        placeholder.markdown(f'<div class="clock">{current_time}</div>', unsafe_allow_html=True)
        # 每秒更新一次
        time.sleep(1)

# 使用 Streamlit 提供的线程安全方法启动时钟
update_clock()
