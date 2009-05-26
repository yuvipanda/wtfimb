# Dijkstra's algorithm for shortest paths
# David Eppstein, UC Irvine, 4 April 2002

# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/117228
from priodict import priorityDictionary

G = {}

def Dijkstra(G,start,end=None,weighted=True):
    """
    Find shortest paths from the start vertex to all
    vertices nearer than or equal to the end.

    The input graph G is assumed to have the following
    representation: A vertex can be any object that can
    be used as an index into a dictionary.  G is a
    dictionary, indexed by vertices.  For any vertex v,
    G[v] is itself a dictionary, indexed by the neighbors
    of v.  For any edge v->w, G[v][w] is the length of
    the edge.  This is related to the representation in
    <http://www.python.org/doc/essays/graphs.html>
    where Guido van Rossum suggests representing graphs
    as dictionaries mapping vertices to lists of neighbors,
    however dictionaries of edges have many advantages
    over lists: they can store extra information (here,
    the lengths), they support fast existence tests,
    and they allow easy modification of the graph by edge
    insertion and removal.  Such modifications are not
    needed here but are important in other graph algorithms.
    Since dictionaries obey iterator protocol, a graph
    represented as described here could be handed without
    modification to an algorithm using Guido's representation.

    Of course, G and G[v] need not be Python dict objects;
    they can be any other object that obeys dict protocol,
    for instance a wrapper in which vertices are URLs
    and a call to G[v] loads the web page and finds its links.
    
    The output is a pair (D,P) where D[v] is the distance
    from start to v and P[v] is the predecessor of v along
    the shortest path from s to v.
    
    Dijkstra's algorithm is only guaranteed to work correctly
    when all edge lengths are positive. This code does not
    verify this property for all edges (only the edges seen
    before the end vertex is reached), but will correctly
    compute shortest paths even for some graphs with negative
    edges, and will raise an exception if it discovers that
    a negative edge has caused it to make a mistake.
    """

    D = {}  # dictionary of final distances
    P = {}  # dictionary of predecessors
    Q = priorityDictionary()   # est.dist. of non-final vert.
    Q[start] = 0
    
    for v in Q:
        D[v] = Q[v]
        if v == end: break

        for w in G[v]:
            if weighted:
                vwLength = D[v] + G[v][w]
            else:
                vwLength = D[v] + 1
            if w in D:
                if vwLength < D[w]:
                    raise ValueError, \
  "Dijkstra: found better path to already-final vertex"
            elif w not in Q or vwLength < Q[w]:
                Q[w] = vwLength
                P[w] = v
    
    return (D,P)
            
def shortestPath(G,start,end,weighted=True):
    """
    Find a single shortest path from the given start vertex
    to the given end vertex.
    The input has the same conventions as Dijkstra().
    The output is a list of the vertices in order along
    the shortest path.
    """

    D,P = Dijkstra(G,start,end,weighted)
    Path = []
    while 1:
        Path.append(end)
        if end == start: break
        end = P[end]
    Path.reverse()
    return Path
    
def shortest_route(from_, to):
    import marshal

    G = marshal.load(open('cache/graph', 'rb'))
    
    route_path = []

    path = shortestPath(G, from_, to, weighted=True)

    if len(path) > 2:
        path2 = shortestPath(G, from_, to, weighted=False)

        if len(path2) < len(path):
            path = path2
    
    for i in range(0, len(path) - 1):
        route_path.append((path[i], path[i+1]))
        
    return route_path

cursor = None
routes = None

def routes_between(a, b):
    x = cursor.execute("SELECT route_id FROM route_stop " \
            "WHERE stop_id = %s AND route_id IN " \
            "(SELECT route_id FROM route_stop WHERE stop_id = %s)", (a, b))
    
    return [row[0] for row in cursor.fetchall()]

def test():
    import marshal
    
    G = marshal.load(open('cache/graph', 'rb'))

    #print shortestPath(G, 153, 358)
    for i in range(100, 200, 10):
        for j in range(300, 500, 10):
            path = shortestPath(G, i, j, weighted=True)
            path2 = shortestPath(G, i, j, weighted=False)

            print "%d, %d" % (len(path), len(path2))

    #print routes_between(153, 152), routes_between(152,  358)

if __name__ == "__main__":
    import sys
    sys.path.append('')
    import MySQLdb
    import config

    conn = MySQLdb.connect(user=config.db.user, passwd=config.db.password, \
                            db=config.db.db)
    cursor = conn.cursor()

    import cProfile
    cProfile.run("test()")
