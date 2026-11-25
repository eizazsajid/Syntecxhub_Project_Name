# Syntecxhub AI Internship — Week 1 Task

Domain: Artificial Intelligence (AI)

## Project 1 — Maze Solver using A* Search
File: `maze_solver.py`
- Maze/grid ko nodes ki tarah model kiya hai
- A* search, Manhattan distance heuristic
- Shortest path nikalta hai (is maze mein 11 steps)
- Agar rasta na ho to "No path found" batata hai
- Console par path (`*`) aur explored cells (`o`) dikhata hai

Chalane ke liye:
```
python3 maze_solver.py
```

## Project 2 — Rule-Based Expert System
File: `expert_system.py`
- Chhota rule engine: if-then rules + facts base
- User symptoms likhta hai, system forward chaining se conclusion nikalta hai
- Multi-step inference: ek rule ka conclusion doosre rule ki condition banta hai
  (masalan: fever + cough → flu → needs_rest)
- Inference steps ka log dikhata hai

Chalane ke liye:
```
python3 expert_system.py
```
Phir symptoms likho, masalan: `fever, cough`
