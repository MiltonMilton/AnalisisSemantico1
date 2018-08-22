from simpleGraphGenerator import get_graph

def distancia_key_entity(key,entity,levels = 5):
    g = get_graph(key,levels)
    dic = {}
    for l, v in enumerate(g):
        dic.update(v)
    print "llego"
    print len(g)
    #print dic
    paths = find_all_paths(dic,key,entity)
    #print paths
    print min(paths, key= len)
    print max(paths, key= len)
    
    return min(paths, key= len)



def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node  not in path:
            newpath = find_path(graph, node , end, path)
            if newpath: return newpath
    return None

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node  not in path:
            newpaths = find_all_paths(graph, node , end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node  not in path:
            newpath = find_shortest_path(graph, node , end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest