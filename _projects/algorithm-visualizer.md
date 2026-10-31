---
title: "AlgorithmVisualizer"
description: "Interactive visualizations of sorting and pathfinding algorithms, implemented in Python."
year: 2020
stack: [Python, JavaScript, Flask, Pyodide]
repo_url: "https://github.com/DimPap99/AlgorithmVisualizer"
demo_url: "https://dimpap99.github.io/AlgorithmVisualizer/"
published: true
---

An algorithm visualizer I originally built for an algorithms course. It includes sorting animations and grid-based pathfinding.

## Sorting

Generate an array and watch the swaps made by insertion, quick, bubble, selection, merge, heap, shell, cocktail shaker, and comb sort. The animation speed can be adjusted while it runs.

## Pathfinding

Set start and end points, draw walls, and assign cell weights. The available algorithms are Dijkstra, A*, greedy best-first search, bidirectional Dijkstra, Yen’s K shortest paths, Bellman–Ford, breadth-first search, and depth-first search.

Weights can be painted manually or generated from uniform, Gaussian, exponential, and Bernoulli distributions. Bellman–Ford supports negative weights and reports negative cycles.

## Browser version

The live demo runs the Python implementations in the browser through Pyodide. Computation runs in a Web Worker, and JavaScript animates the results. The original Flask version uses the same Python code and can still be run locally.
