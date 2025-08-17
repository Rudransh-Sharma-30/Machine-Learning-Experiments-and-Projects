# import pandas as pd
# import streamlit as st
# st.write(1234)
# st.write(
#     pd.DataFrame(
#        { 
#         "first column" :[1,2,3,4],
#         "second column" : [10,20,30,40]
#        }
#     )
# )
# data_frame = pd.DataFrame(
#     {"first column" :[1,2,3,4],
#        "second column" : [10,20,30,40]}
# )
# st.write("1 + 1 = " , 2)
# st.write("Below is a DataFrame: ", data_frame, "Abve is a dataframe.")

import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
df = pd.DataFrame(np.random.randn(200,3), columns = ['a','b','c'])
c = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.write(c)