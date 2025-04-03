import heapq

def is_closed(closures, start_time, travel_time):
    
    end_time = start_time + travel_time
    for s, e in closures:
        if start_time < e and end_time > s:  
            return max(e, start_time)  
    return start_time 

def min_time(N, M, T, roads):
    graph = {i: [] for i in range(1, N+1)}
    
    for u, v, t, k, closures in roads:
        graph[u].append((v, t, closures))
        graph[v].append((u, t, closures))
    
    pq = [(T, 1)]
    min_time = {i: float('inf') for i in range(1, N+1)}
    min_time[1] = T
    
    while pq:
        curr_time, station = heapq.heappop(pq)
        
        if station == N:
            return curr_time
        
        for neighbor, travel_time, closures in graph[station]:
            new_time = is_closed(closures, curr_time, travel_time) + travel_time
            if new_time < min_time[neighbor]:
                min_time[neighbor] = new_time
                heapq.heappush(pq, (new_time, neighbor))
    
    return -1


N, M, T = map(int, input().split())
roads = []
for _ in range(M):
    data = list(map(int, input().split()))
    u, v, t, k = data[:4]
    closures = [(data[i], data[i+1]) for i in range(4, len(data), 2)]
    roads.append((u, v, t, k, closures))

print(min_time(N, M, T, roads))
