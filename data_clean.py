import csv
import pandas as pd
from collections import Counter




df = pd.read_csv("newer_music.csv")
genre = df['terms']
#
# for i,v in genre.items():
#     if "rock" in str(v):
#         genre[i] = "rock"
#     if "metal" in str(v):
#         genre[i] = "metal"
#     if "blues" in str(v):
#         genre[i] = "blues"
#     if "pop" in str(v):
#         genre[i] = "pop"
#     if "jazz" in str(v):
#         genre[i] = "jazz"
#     if "alternative" in str(v):
#         genre[i] = "alternative"
#     if "soul" in str(v):
#         genre[i] = "soul"
#     if "gospel" in str(v):
#         genre[i] = "gospel"
#     if "indie" in str(v):
#         genre[i] = "indie"
#     if "country" in str(v):
#         genre[i] = "country"
#     if "core" in str(v):
#         genre[i] = "metal"
#     if "garage" in str(v):
#         genre[i] = "garage"
#     if "filk" in str(v):
#         genre[i] = "folk"
#     if "folk" in str(v):
#         genre[i] = "folk"
#     if "grunge" in str(v):
#         genre[i] = "grunge"
#     if "swing" in str(v):
#         genre[i] = "swing"
#     if ("reggae" in str(v)) and (str(v) != "reggaeton"):
#         genre[i] = "reggae"
#     if "rap" in str(v):
#         genre[i] = "rap"
#     if "hop" in str(v):
#         genre[i] = "hip-hop"
#     if "punk" in str(v):
#         genre[i] = "punk"
#     if "house" in str(v):
#         genre[i] = "house"
#     if "vocalist" in str(v):
#         genre[i] = "vocalist"
#     if "zydeco" in str(v):
#         genre[i] = "blues"
#     if "trance" in str(v):
#         genre[i] = "trance"
#     if "dance" in str(v):
#         genre[i] = "dance"
#     if "dub" in str(v):
#         genre[i] = "dance"
#
# print(genre)

sum = 0
count = Counter(df['terms'])
bad_genres = []

for i in range(len(count.values())):
    sum = sum + 1
    if count.values()[i] < 40:
        bad_genres.append(count.keys()[i])

print(sum)
print(bad_genres)

for b in bad_genres:
    df = df[df.terms != b]

df.reset_index(drop=True)
print(df)
# for i in df.rows():
#     print(i)
#     print(i['terms'])
    # if i['terms'] in bad_genres:
    #     df.drop(i)
#
# df.to_csv("newest_music.csv")
