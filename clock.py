import streamlit as st
import time
from datetime import datetime

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
