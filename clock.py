import streamlit as st
import time
from datetime import datetime
import requests

# **确保 set_page_config() 是第一个 Streamlit 相关命令**
st.set_page_config(
    page_title="大时钟",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# **隐藏 Streamlit 默认样式**
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# **时钟样式**
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

# **更新访问时间**
def update_access_time():
    """ 访问 Streamlit 页面时调用后端 API 记录最后访问时间 """
    appid = "Clock"  # 你的 Streamlit 应用 ID
    flask_server_url = "http://11.2.171.248:5000"  # 你的 Flask 服务器地址
    url = f"{flask_server_url}/api/apps/{appid}/update_access_time"

    try:
        requests.post(url)  # **删除 st.success() 避免影响 set_page_config**
    except Exception:
        pass  # 避免显示错误信息

# **只在用户首次进入页面（当前会话）时调用**
if "access_logged" not in st.session_state:
    update_access_time()
    st.session_state.access_logged = True  # 标记当前会话已记录访问时间

# **创建时钟显示**
placeholder = st.empty()

# **动态更新时钟**
while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    placeholder.markdown(f'<div class="clock">{current_time}</div>', unsafe_allow_html=True)
    time.sleep(1)  # 每秒更新一次
