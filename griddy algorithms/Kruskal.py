from tkinter import *

class Disjoint:

    def __init__(self):
        self.sets = []

    def make_set(self, repr):
        self.sets.append([repr])

    def union(self, repr1, repr2):
        set1 = self.find_set(repr1)
        set2 = self.find_set(repr2)
        if set1 != set2:
            set1.extend(set2)
            self.sets.remove(set2)

    def find_set(self, repr1):
        for oneSet in self.sets:
            if repr1 in oneSet:
                return oneSet


    def getSets(self):
        return self.sets
class Edge:

    def __init__(self,u,v,w):
        self.u=u
        self.v=v
        self.weight = w

    def __lt__(self, other):
        return  self.weight < other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __ge__(self, other):
        return self.weight >=other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __ne__(self, other):
        return self.weight != other.weight
    def __repr__(self):
        return str(self.u) + "-->" + str(self.v)
    def __hash__(self):
        return hash((self.u,self.v))

class Graph:
    def __init__(self):
        self.vert_lst = {}
        self.edges = []
        self.weights={}

    def add_vertex(self,label):
        self.vert_lst[label] = []

    def add_edge(self,start,end,weight):
        self.weights[(start,end)] = weight
        self.vert_lst[start].append(end)
        self.edges.append(Edge(start,end,weight))

    def add_double_edge(self,start,end,weight):
        self.add_edge(start,end,weight)
        self.add_edge(end,start,weight)

    def get_edges(self):
        return weight.keys()

    def get_vertices(self):
        return self.vert_lst.keys()

    def get_weight(self,start,end):
        return self.weights[(start,end)]

    def mst_kruskal(self):
        A = set()
        ds = Disjoint()

        for v in self.get_vertices():
            ds.make_set(v)
        self.edges.sort()
        for e in self.edges:
            if ds.find_set(e.u) != ds.find_set(e.v):
                A.add(e)
                ds.union(e.u,e.v)
        return A


class GUI:

    def __init__(self):
        self.master = Tk()
        self.canvas = Canvas(self.master, width=700, height=700)
        self.start = None
        self.canvas.bind("<Button-1>", self.onclick_handler)
        self.canvas.bind("<ButtonRelease-1>", self.onrelease_handler)
        self.canvas.pack()
        self.count=0
        self.G = Graph()
        self.k_button = Button(self.master, text="Kruskal", width=10, command = self.find_mst)
        self.k_button.pack()
        self.lines = {}
        self.master.mainloop()  


    
    def find_mst(self):
        A = self.G.mst_kruskal()
        total_weight = 0
        for e in A:
            self.canvas.itemconfig(self.lines[(e.u,e.v)], fill="red")
            self.canvas.itemconfig(self.lines[(e.u,e.v)], width=5)   
            total_weight += self.G.get_weight(e.u,e.v)

        self.canvas.create_text(75, 25,fill="black",font="Times 15 bold",text="Weight = " + str(total_weight))

    def des(self,t,s,c,e):
        w = int(e.get())
        self.G.add_double_edge(s,c,w)
        t.destroy()

    def onclick_handler(self,event):
        cur = self.canvas.find_withtag(CURRENT)
        if cur:
            self.start = (event.x, event.y,cur[0])
        else:
            self.start = (event.x, event.y,None)


    def onrelease_handler(self,event):

        if self.start ==(event.x,event.y,None):
            v = self.canvas.create_oval(event.x-25,event.y-25, event.x+25, event.y+25, fill="black")
            self.G.add_vertex(v)
            self.canvas.create_text(event.x ,event.y,fill="white",font="Times 15 bold",text=str(self.count))
            self.count+=1
            return
        if self.start is not None:
            cur = self.canvas.find_withtag(CURRENT)

            x = self.start[0]
            y = self.start[1]
            if cur:
                l = event.widget.create_line(x, y, event.x, event.y)
                self.lines[(self.start[2],cur[0])] = l
                temp = Tk()
                e=Entry(temp, width=3)
                e.pack()
                w_button = Button(temp, text="Weight", width=10, command = lambda t=temp,s=self.start[2],c=cur[0] : self.des(t,s,c,e))
                w_button.pack()

            self.start = None
   
if __name__ == '__main__':
    g = GUI()
    g.master.mainloop()
