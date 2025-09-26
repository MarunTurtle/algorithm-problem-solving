from collections import defaultdict, deque

def solution(nodes, edges):
    
    if not nodes:
        return [0, 0]
    
    adj = defaultdict(list)
    
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    for x in nodes:
        adj.setdefault(x, [])
        
    visited = set()
    white_count = 0
    reverse_count = 0
    
    for start in nodes:
        if start in visited:
            continue
        q = deque([start])
        visited.add(start)
        comp = [start]
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
                    comp.append(v)
        cnt_same = 0
        
        for u in comp:
            deg_parity = (len(adj[u]) % 2)
            label_parity = (u%2)
            if deg_parity == label_parity:
                cnt_same += 1
        size = len(comp)
        
        if cnt_same == 1:
            white_count += 1
        if cnt_same == size - 1:
            reverse_count += 1
    
    return [white_count, reverse_count]