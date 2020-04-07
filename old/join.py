import pandas as pd
# wrong use concat
A = pd.DataFrame(
    data = {
        "id": [0,1],
        "var_a": [2.1, 5.1]
        },
)
B = pd.DataFrame(
    data = {
        "id": [2,3],
        "var_b": [9.7,8.1]
        },
)

C = pd.DataFrame(
    data = {
        "id": [0,1],
        "var_c": [4.4,3.0]
        },
)

m2 = pd.merge(A,C,how="outer", on="id")
m3 = pd.merge(m2,B,how="outer", on="id")
#print(left)
#print(right)

# df_para_list = [left, right, middle]
# merge = pd.merge(
#     left, 
#     right, 
#     how="outer",
#     )

# cat = pd.concat(
#     objs = df_para_list, 
#     axis = 0,
#     join = "outer",
#     # join_axes = None,
#     # ignore_index = False,
#     # keys = None,
#     # levels = None,
#     # names = None,
#     # verify_integrity = False,
#     #sort = None,
#     #copy = True,
#     )
