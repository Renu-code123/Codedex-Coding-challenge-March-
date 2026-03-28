###

from collections import deque
def days_to_infect(city):
    rows, cols = len(city), len(city[0])
    queue = deque()
    healthy = 0
    for r in range(rows):
        for c in range(cols):
            if city[r][c] == '🧟':
                queue.append((r, c))
            elif city[r][c] == '👤':
                healthy += 1
    if healthy == 0:
        return 0
    days = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and city[nr][nc] == '👤':
                    city[nr][nc] = '🧟'
                    healthy -= 1
                    queue.append((nr, nc))
        days += 1
    return days - 1 if healthy == 0 else -1
  
