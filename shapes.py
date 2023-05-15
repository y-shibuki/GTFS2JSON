import pandas as pd

df = pd.read_csv("./kanto_GTFS/shapes.txt")
df["coord"] = df[["shape_pt_lon", "shape_pt_lat"]].values.tolist()

df.groupby(by="shape_id", as_index=False)["coord"].apply(list).to_json("shapes.json", orient="records")