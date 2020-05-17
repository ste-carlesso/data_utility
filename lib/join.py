import pandas as pd

df1 = pd.DataFrame(
    data = {"A": [2.1, 5.1]},
    index = [0,1]
)

df2 = pd.DataFrame(
    data = {"B": [9.7,8.1]},
    index = [2,3],
)

df3 = pd.DataFrame(
    data = {"C": [4.4,3.0]},
    index = [2,4],
)

cat = pd.concat(
    objs = [df1,df2,df3], 
    axis = 1,
    #join = "outer",
    # join_axes = None,
    # ignore_index = False,
    # keys = None,
    # levels = None,
    # names = None,
    # verify_integrity = False,
    #sort = None,
    #copy = True,
    )
