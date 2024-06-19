from collections import deque

# 프로젝트 문제 3번
input = [[4, 3, 2, 1],
         [0, 0, 0, 0],
         [0, 0, 9, 0],
         [1, 2, 3, 4]]
N = 4

forest = []

def problem3(input):
    bear_size = 2
    honeycomb_count = 0
    result = 0
    bear_x, bear_y = 0, 0
    # 입력 힌트

    # forest 리스트를 input 리스트로 초기화
    forest = [row[:] for row in input]
    
    # 곰의 초기 위치 찾기
    for i in range(N):
        for j in range(N):
            if forest[i][j] == 9:
                bear_x, bear_y = i, j
                forest[i][j] = 0
    print("곰의 초기 위치 x : {0}, y : {1}".format(bear_x, bear_y))
    
    # BFS 탐색
    def bfs():
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * N for _ in range(N)]
        queue = deque([(bear_x, bear_y, 0)])
        visited[bear_x][bear_y] = True
        eatable_honeycombs = []

        while queue:
            x, y, dist = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if forest[nx][ny] <= bear_size:
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist + 1))
                        
                        if 0 < forest[nx][ny] < bear_size:
                            eatable_honeycombs.append((dist + 1, nx, ny))

        if eatable_honeycombs:
            eatable_honeycombs.sort()
            return eatable_honeycombs[0]
        return None

    while True:
        next_target = bfs()
        if not next_target:
            break

        dist, target_x, target_y = next_target
        bear_x, bear_y = target_x, target_y
        result += dist
        honeycomb_count += 1
        forest[target_x][target_y] = 0

        if honeycomb_count == bear_size:
            bear_size += 1
            honeycomb_count = 0

    return result


result = problem3(input)

assert result == 14
print("정답입니다.")
