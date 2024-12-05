import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title  ('Stremlit 超入門')

#st.write('DataFrame')

#st.write('Interactive Widgets')
st.write('プログレスバー')

'Start!!'

latest_ineration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_ineration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容')

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
text = st.text_input('あなたの趣味を教えてください')

'コンディション:', condition
'あなたの趣味:', text

#st.sidebar.write('Interactive Widgets')

#condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
#text = st.sidebar.text_input('あなたの趣味を教えてください')

#'コンディション:', condition
#'あなたの趣味:', text

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)

'あなたの好きな数字は', option, 'です'


st.write('Display Image')

if st.checkbox('Show Image'):
    img = Image.open('IMG_2534.JPG')

    st.image(img, caption='Jubilo', use_column_width=True)

#df = pd.DataFrame({
#    '１列目': [1,2,3,4],
#    '２列目': [10,20,30,40]
#})

#st.table(df.style.highlight_max(axis=0))

#df = pd.DataFrame(
#    np.random.rand(20, 3),
#    columns=['a', 'b', 'c']
#)

#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)

#df = pd.DataFrame(
#    np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
#    columns=['lat', 'lon']
#)

#st.map(df)

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""
