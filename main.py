import streamlit as st

# 设置页面配置
st.set_page_config(
    page_title="实用网址导航",
    page_icon="🔗",
    layout="wide"
)

# 页面标题
st.title("🔗 实用网址导航")
st.write("---")

# 定义网址数据（分类 -> 网站列表）
website_data = {
    "搜索引擎": [
        {"name": "百度", "url": "https://www.baidu.com", "desc": "国内常用搜索引擎"},
        {"name": "谷歌", "url": "https://www.google.com", "desc": "国际知名搜索引擎"},
        {"name": "必应", "url": "https://www.bing.com", "desc": "微软旗下搜索引擎"}
    ],
    "社交平台": [
        {"name": "微信", "url": "https://weixin.qq.com", "desc": "国内主流社交工具"},
        {"name": "微博", "url": "https://weibo.com", "desc": "社交媒体平台"},
        {"name": "抖音", "url": "https://www.douyin.com", "desc": "短视频社交平台"}
    ],
    "视频平台": [
        {"name": "腾讯视频", "url": "https://v.qq.com", "desc": "综合视频平台"},
        {"name": "爱奇艺", "url": "https://www.iqiyi.com", "desc": "高清视频在线观看"},
        {"name": "B站", "url": "https://www.bilibili.com", "desc": "年轻人喜爱的视频平台"}
    ],
    "学习资源": [
        {"name": "MOOC", "url": "https://www.icourse163.org", "desc": "中国大学MOOC"},
        {"name": "GitHub", "url": "https://github.com", "desc": "代码托管平台"},
        {"name": "Stack Overflow", "url": "https://stackoverflow.com", "desc": "程序员问答社区"}
    ],
    "工具网站": [
        {"name": "在线翻译", "url": "https://fanyi.baidu.com", "desc": "百度翻译"},
        {"name": "思维导图", "url": "https://www.processon.com", "desc": "在线绘图工具"},
        {"name": "草料二维码", "url": "https://cli.im", "desc": "二维码生成工具"}
    ]
}

# 显示各个分类的网站（使用markdown链接，支持云端打开）
for category, websites in website_data.items():
    st.subheader(f"📌 {category}")
    
    # 每行显示3个网站
    cols = st.columns(3)
    for i, site in enumerate(websites):
        with cols[i % 3]:
            # 关键修改：用markdown生成可点击链接，target="_blank"确保在新标签页打开
            st.markdown(f"[🔍 **{site['name']}**]({site['url']})", unsafe_allow_html=True)
            st.caption(site['desc'])
    
    st.write("---")

# 底部信息
st.caption("提示：点击网站名称即可在新标签页打开对应链接")
