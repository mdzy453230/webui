import os
import time

import pandas as pd
import streamlit as st

os.system("python database.py")
# 设置网页名称
st.set_page_config(page_title='JCTRANS-TEST')
# 设置网页标题

# 设置网页子标题
st.subheader('JC-AUTO_TEST')


st.success("自动化测试报告")


df = pd.read_excel("result.xlsx")
df_reset = df.set_index('序号')

# 侧边栏

job_filter = st.selectbox("请选择项目", pd.unique(df_reset["项目"]))  # 下拉选择框(非空单选)
#job_time = st.sidebar.selectbox("请选择日期", pd.unique(df_reset["执行时间"]))


placeholder = st.empty()

# dataframe filter
df1 = df_reset[df_reset["项目"] == job_filter]
sum = df1.shape[0]
#df2 = df_reset[df_reset["执行时间"] == job_time]
st.markdown("### Detailed Data View")

word=st.empty()
bar=st.progress(0)
#进度条
for i in range(100):
    word.text('Iteration: '+str(i+1))
    bar.progress(i+1)
    time.sleep(0.1)

st.write("当前页面数据总数:\n",sum)
st.dataframe(df1)
time.sleep(1)








