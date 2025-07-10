import streamlit as st
import webbrowser
from datetime import datetime

# 设置网页配置
st.set_page_config(
    page_title="我的全能导航站",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS样式
st.markdown("""
<style>
    .big-font {
        font-size:24px !important;
        font-weight: bold;
    }
    .category-box {
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
        background-color: #f0f2f6;
    }
    .website-button {
        margin: 5px;
        width: 100%;
    }
    .search-box {
        padding: 20px;
        background-color: #e6f7ff;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .quick-access {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-bottom: 20px;
    }
    .quick-access-item {
        padding: 10px 15px;
        background-color: #f0f2f6;
        border-radius: 20px;
        cursor: pointer;
        transition: all 0.3s;
    }
    .quick-access-item:hover {
        background-color: #d0d2d6;
    }
</style>
""", unsafe_allow_html=True)

# 网站分类数据
website_categories = {
    "搜索引擎": {
        "Google": "https://www.google.com",
        "百度": "https://www.baidu.com",
        "Bing": "https://www.bing.com",
        "DuckDuckGo": "https://duckduckgo.com"
    },
    "社交媒体": {
        "微博": "https://weibo.com",
        "Twitter": "https://twitter.com",
        "Facebook": "https://facebook.com",
        "知乎": "https://www.zhihu.com"
    },
    "学习资源": {
        "Coursera": "https://www.coursera.org",
        "edX": "https://www.edx.org",
        "慕课网": "https://www.imooc.com",
        "B站学习区": "https://www.bilibili.com"
    },
    "编程开发": {
        "GitHub": "https://github.com",
        "Stack Overflow": "https://stackoverflow.com",
        "Gitee": "https://gitee.com",
        "LeetCode": "https://leetcode-cn.com"
    },
    "实用工具": {
        "Canva设计": "https://www.canva.com",
        "ProcessOn流程图": "https://www.processon.com",
        "TinyPNG图片压缩": "https://tinypng.com",
        "PDF转换器": "https://smallpdf.com/cn"
    }
}

# 快速访问网站
quick_access = {
    "邮件": {
        "Gmail": "https://mail.google.com",
        "Outlook": "https://outlook.live.com",
        "QQ邮箱": "https://mail.qq.com"
    },
    "云存储": {
        "Google Drive": "https://drive.google.com",
        "OneDrive": "https://onedrive.live.com",
        "百度网盘": "https://pan.baidu.com"
    }
}

# 侧边栏
with st.sidebar:
    st.title("🌐 导航设置")
    st.markdown("---")
    
    # 主题选择
    theme = st.selectbox("选择主题", ["默认", "暗色", "亮色"])
    
    # 布局选择
    layout = st.radio("布局风格", ["网格", "列表"])
    
    st.markdown("---")
    st.markdown("**添加快捷方式**")
    new_site_name = st.text_input("网站名称")
    new_site_url = st.text_input("网站URL")
    if st.button("添加"):
        if new_site_name and new_site_url:
            website_categories["自定义"].update({new_site_name: new_site_url})
            st.success("添加成功！")
    
    st.markdown("---")
    st.markdown(f"🕒 最后更新: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

# 主页面
st.title("🚀 我的全能导航站")
st.markdown("一个集成了所有常用网站的多功能导航页面")

# 搜索框
with st.container():
    st.markdown('<div class="search-box">', unsafe_allow_html=True)
    col1, col2 = st.columns([4, 1])
    with col1:
        search_query = st.text_input("全网搜索", "")
    with col2:
        search_engine = st.selectbox("搜索引擎", ["Google", "百度", "Bing"], label_visibility="collapsed")
    if search_query:
        if search_engine == "Google":
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        elif search_engine == "百度":
            webbrowser.open(f"https://www.baidu.com/s?wd={search_query}")
        else:
            webbrowser.open(f"https://www.bing.com/search?q={search_query}")
    st.markdown('</div>', unsafe_allow_html=True)

# 快速访问区域
st.subheader("⚡ 快速访问")
with st.container():
    st.markdown('<div class="quick-access">', unsafe_allow_html=True)
    for category, sites in quick_access.items():
        st.markdown(f'<div class="quick-access-item" onclick="window.open(\'{list(sites.values())[0]}\', \'_blank\')">{category}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 网站分类展示
for category, sites in website_categories.items():
    with st.container():
        st.markdown(f'<div class="category-box">', unsafe_allow_html=True)
        st.subheader(f"📁 {category}")
        
        if layout == "网格":
            cols = st.columns(4)
            for i, (name, url) in enumerate(sites.items()):
                with cols[i % 4]:
                    if st.button(name, key=f"{category}_{name}"):
                        webbrowser.open(url)
        else:
            for name, url in sites.items():
                if st.button(name, key=f"{category}_{name}"):
                    webbrowser.open(url)
        
        st.markdown('</div>', unsafe_allow_html=True)

# 天气预报组件
st.markdown("---")
st.subheader("🌤️ 天气预报")
city = st.text_input("输入城市名称", "北京")
if st.button("查询天气"):
    # 这里可以接入天气API，简化版只显示文本
    st.write(f"即将显示 {city} 的天气信息...")
    # 实际应用中可替换为:
    # weather_data = get_weather(city)
    # st.write(f"温度: {weather_data['temp']}°C")
    # st.write(f"天气: {weather_data['condition']}")

# 便签功能
st.markdown("---")
st.subheader("📝 快速便签")
note = st.text_area("记录临时笔记", height=100)
if st.button("保存便签"):
    with open("quick_note.txt", "w", encoding="utf-8") as f:
        f.write(note)
    st.success("便签已保存！")