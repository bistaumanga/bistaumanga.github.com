---
layout: post
title: Union Find
meta: Union Find Data Structure Implementation in Scala
comments: true
category: data-structures
tags: union find, scala, disjoint set
published: true

---
**Disjoint Set** or **Union Find** is a data structures that tracks a set of keys/elements which are partitioned into number of disjoint sets. It is useful in number of applications such as speeding up **Kruskal's Minimum Spanning Tree**, **maximal k space clustering** etc. It basically supports two operations:

1. **Find(x)**: finds the subset in which element **x** belongs.
2. **Union(x, y)**: Merges the subsets in which **x** and **y** belongs to a single subset.

## Data Structure
The data structure accomplishes the operations by representing as tree and thus maintaining the two invariants.

1. **Parent pointers** : The pointer to the parent of each element **x**
2. **Rank**: The rank of **x** is the maximum distance among all paths from x to the leaves

For the detail [see here](http://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/UnionFind.pdf).

A quick aimplementation of Union Find, optimized with lazy unions, path compression and Union By Rank is given here. 
<script src="https://gist.github.com/bistaumanga/f4ec43701fc5b5552ebd.js"></script>

## Runtime
The runtime of Union Find is very hard to analyze. There is a theorem for this by Ullman-HopCroft:

> Starting from an empty data structure, Union By Rank with path compression performs any intermixed sequence of $m \geq n$ FIND and $n – 1$ UNION operations in $\mathcal{O}(m \log^*{n} )$ time. 
 
 where $\log^*{n}$ is number of times we need to apply $\log$ before the final result reaches 1.