import streamlit as st
import pandas as pd
import numpy as np

# 1. 设置网页基本信息
st.set_page_config(
    page_title="我的第一个Streamlit网页", 
    page_icon="🌍",
    layout="wide"  # 宽屏模式
)

# 2. 添加标题和文字
st.title("🎉 欢迎来到我的Streamlit网页！")
st.write("这是一个用Python快速构建的交互式网页。")

# 3. 侧边栏（可选）
with st.sidebar:
    st.header("设置选项")
    user_name = st.text_input("你的名字")
    theme_color = st.color_picker("选择主题颜色", "#00f900")

# 4. 主页面内容
st.divider()  # 分割线
st.header(f"你好, {user_name if user_name else '游客'}！")

# 5. 交互式组件示例
tab1, tab2, tab3 = st.tabs(["数据输入", "图表展示", "其他功能"])

with tab1:
    # 输入数字
    num = st.number_input("输入一个数字", min_value=0, max_value=100)
    # 按钮
    if st.button("点击生成随机数据"):
        data = np.random.randn(10, 2)
        df = pd.DataFrame(data, columns=["A列", "B列"])
        st.session_state.my_data = df  # 保存到会话状态

with tab2:
    # 显示图表（如果数据存在）
    if "my_data" in st.session_state:
        st.line_chart(st.session_state.my_data)
        st.dataframe(st.session_state.my_data)
    else:
        st.warning("请先在【数据输入】标签页生成数据！")

with tab3:
    # 文件上传示例
    uploaded_file = st.file_uploader("上传一个CSV文件", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("文件前5行：")
        st.table(df.head())

# 6. 页脚
st.divider()
st.markdown("> 由 [Streamlit](https://streamlit.io/) 强力驱动")
