---
title: "AlgorithmVisualizer"
description: "Interactive visualizations of sorting and pathfinding algorithms, implemented in Python."
year: 2020
stack: [Python, JavaScript, Flask, Pyodide]
repo_url: "https://github.com/DimPap99/AlgorithmVisualizer"
demo_url: "https://dimpap99.github.io/AlgorithmVisualizer/"
published: true
---

I originally built this in 2020 for an algorithms course, with a Flask backend and a vanilla JavaScript frontend. Python ran the algorithms on the server, and JavaScript animated the results.

## Sorting

Generate an array and watch the swaps made by insertion, quick, bubble, selection, merge, heap, shell, cocktail shaker, and comb sort. The animation speed can be adjusted while it runs.

## Pathfinding

Set start and end points, draw walls, and assign cell weights. The available algorithms are Dijkstra, A*, greedy best-first search, bidirectional Dijkstra, Yen’s K shortest paths, Bellman–Ford, breadth-first search, and depth-first search.

Weights can be painted manually or generated from uniform, Gaussian, exponential, and Bernoulli distributions. Bellman–Ford supports negative weights and reports negative cycles.

## WebAssembly update

We recently vibecoded a WebAssembly version using Pyodide so the demo could run on GitHub Pages. The existing Python algorithms now run in a browser worker, and JavaScript handles the animations. The Flask version still works locally.
