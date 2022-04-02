from random import randint as rnd
from random import choice as ch
nodes = "nodes.csv"
edges = "edges.csv"
id  = 0
nodes = open(nodes, 'w')
nodes.write("id;Name \n")

actions =["love each other", "hate each other", "enemies", "siblings", "friends", "served in army together", "party together",
          "used to go to the same school", "used to go to the same university", "like to play tennis together", "have their own favourite song",
          "cheated on each other multiple times", "want to avenge the death of a relative", "make tiktok clips together"]
edges = open(edges, 'w')
edges.write("Source;Target;Type;Label;Weight \n")

with open("characters.txt") as fp:
    for lines in fp:
        if lines!="\n":
            id += 1
            strochka  = str(id)+";"+str(lines)+"\n"
            nodes.write(strochka)





for i in range(100):
    one = rnd(1,id)
    two = rnd(1,id)

    relation = ch(["undirected", "directed"])
    weight = rnd(1,11)
    action = ch(actions)
    strochka = str(one)+";"+str(two)+";"+str(relation)+";"+str(action)+";"+str(weight)+"\n"
    edges.write(strochka)