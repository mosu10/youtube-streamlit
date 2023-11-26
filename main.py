import streamlit as st
import time

st.title('Streamlit 超入門')


#プログレスバー
st.write("プログレスバーの表示")
'Start!!'

bar = st.progress(0)
latest_iteration = st.empty()

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!'

#エクスパンダー
expander1 = st.expander('問い合わせ１')
expander1.write('問い合わせ1の解答')
expander2 = st.expander('問い合わせ２')
expander2.write('問い合わせ２の解答')
expander3 = st.expander('問い合わせ３')
expander3.write('問い合わせ３の解答')

# text = st.text_input('あなたの趣味を教えてください。') 
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味：', text
# 'コンディション：', condition