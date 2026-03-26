"""
# Task (Docx Q3) — Cleaning Robot

## Problem

There is a cleaning robot in a room. The room is described by an array of strings, where:
- `"."` represents an empty floor area
- `"#"` represents an area the robot cannot enter (obstacles such as walls or furniture)
- `"*"` is the initial position of the robot

It is possible to reach all empty floor areas from the robot's initial position. Rows are numbered from 0 to R-1 (top to bottom), and columns from 0 to C-1 (left to right), so field (0, 0) is the upper-left corner. The room is always surrounded by walls (`"#"`), which means there are always walls in columns 0 and C-1 and in rows 0 and R-1.

Your task is to generate a sequence of commands consisting of moves: up (`"^"`), down (`"v"`), left (`"<"`) and right (`">"`), such that the robot will clean all the required fields (depending on the subtask: full room or just the borders). The robot cleans all the fields it visits, including the field it starts on. The robot should never step into any obstacles, but it can enter the same field multiple times. The robot may finish at any field (it does not have to return to the starting point).

Write a function:

```python
def solution(room, subtask)
```

that, given an array `room` consisting of R strings each of length C, and an integer `subtask` representing the type of subtask the function should solve, returns the string representing the required sequence of commands.

## Constraints

- Each string in array `room` consists only of the characters: `"."`, `"#"`, and `"*"`
- There is exactly one starting point, marked by `"*"`
- All empty fields can be reached from the starting point
- R and C are integers within the range [3..50]
- The generated sequence cannot contain more than 100,000 commands

## Subtasks

Your solution's score depends on how many subtasks it is able to solve. Each subtask is worth **20%** of the points. Each subtask may differ in three categories: expected area to be cleaned, room shape, and starting point of the robot.

### Subtask 1
- **Room shape:** a simple rectangle
- **Starting position:** the top-left corner
- **Area to be cleaned:** the border of the room (fields adjacent to the walls)

For example, for `room = ["#######", "#....#", "#....#", "#....#", "#######"]`, one possible sequence is `">>>>vv<<<<^"`.

### Subtask 2
- **Room shape:** a simple rectangle
- **Starting position:** no constraints (can be any field)
- **Area to be cleaned:** the whole floor

For example, for `room = ["#######", "#.....#", "#..*..#", "#.....#", "#.....#", "#######"]`, one possible sequence is `">>vv<<<<^^>>>>>vv<<<"`.

### Subtasks 3–5
Further subtasks introduce more complex room shapes (non-rectangular, with internal obstacles) and require cleaning the entire reachable floor area. The robot's starting position has no constraints.

"""

import pytest


def is_valid_answer(room, subtask, commands):
    """Simulate the robot and verify all required cells are cleaned without hitting walls."""
    R = len(room)
    C = len(room[0])

    # Find start and required cells based on subtask
    start_x = start_y = 0
    required = set()
    for i in range(R):
        for j in range(C):
            if room[i][j] == '*':
                start_x, start_y = i, j
            if room[i][j] in ('.', '*'):
                if subtask == 1:
                    # Only border cells (adjacent to a wall '#')
                    neighbors = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
                    if any(0 <= ni < R and 0 <= nj < C and room[ni][nj] == '#' for ni, nj in neighbors):
                        required.add((i, j))
                else:
                    required.add((i, j))

    move = {'>': (0, 1), '<': (0, -1), 'v': (1, 0), '^': (-1, 0)}
    x, y = start_x, start_y
    cleaned = {(x, y)}
    for cmd in commands:
        dx, dy = move[cmd]
        nx, ny = x + dx, y + dy
        if room[nx][ny] == '#':
            return False  # hit a wall
        x, y = nx, ny
        cleaned.add((x, y))

    return required.issubset(cleaned)


def solution(room, subtask):
    R = len(room)
    C = len(room[0])

    # Find the starting position
    start_x = start_y = 0
    for i in range(R):
        for j in range(C):
            if room[i][j] == '*':
                start_x, start_y = i, j

    directions = [(0, 1, '>'), (0, -1, '<'), (1, 0, 'v'), (-1, 0, '^')]
    reverse_cmd = {'>': '<', '<': '>', 'v': '^', '^': 'v'}

    visited = [[False] * C for _ in range(R)]
    visited[start_x][start_y] = True
    commands = []

    def dfs(x, y):
        for dx, dy, cmd in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and room[nx][ny] != '#':
                visited[nx][ny] = True
                commands.append(cmd)
                dfs(nx, ny)
                commands.append(reverse_cmd[cmd])  # physically move back

    dfs(start_x, start_y)
    return ''.join(commands)


pytest_cases = [
    # Subtask 1: rectangular room, start at top-left interior corner, clean border
    (["#######", "#*....#", "#.....#", "#.....#", "#######"], 1),
    # Subtask 2: rectangular room, arbitrary start, clean whole floor
    (["#######", "#.....#", "#..*..#", "#.....#", "#.....#", "#######"], 2),
    # Subtask 3–5: complex room with internal obstacles, clean whole floor
    (["#######", "#.#...#", "#.#.*.#", "#.....#", "#######"], 3),
]

@pytest.mark.parametrize("room, subtask", pytest_cases)
def test_solution(room, subtask):
    result = solution(room, subtask)
    assert is_valid_answer(room, subtask, result), (
        f"Result '{result}' does not clean the required area for subtask {subtask}"
    )