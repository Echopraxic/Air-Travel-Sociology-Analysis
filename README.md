# US Air Transportation Network Analysis

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![NetworkX](https://img.shields.io/badge/NetworkX-2.6+-orange.svg)](https://networkx.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Course](https://img.shields.io/badge/Course-CMPLXSYS%20270-purple.svg)](https://lsa.umich.edu/cscs)

&gt; **Analyzing air travel in a network through the lens of sociology** — A complex systems approach to understanding the interplay between air traffic, geography, and cultural influences using force-directed graphs and agent-based modeling.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Research Findings](#-research-findings)
- [Project Structure](#-project-structure)
- [Methodology](#-methodology)
- [Limitations](#-limitations)
- [Future Work](#-future-work)
- [Citations](#-citations)
- [Acknowledgments](#-acknowledgments)

---

## 🌐 Overview

This project explores the United States domestic air transportation network as a complex system, analyzing the six largest hub airports and their connections to over 100 destinations across all 50 states. Using a **Kamada-Kawai force-directed graph** combined with an **agent-based model (ABM)**, the study investigates:

- **Network topology** and centrality metrics of major US airports
- **Geographic patterns** in air travel (Appalachian regions, Rockies, Southwest)
- **Cultural influences** on travel patterns (demographics, historical ties)
- **Transportation efficiency** and infrastructure implications

The research demonstrates that Dallas (DFW) emerges as the most well-connected hub, while regional patterns reveal how geographic barriers (mountain ranges) and cultural affinities shape air travel networks.

---

## ✨ Features

- ✈️ **Kamada-Kawai Force-Directed Graph** — Visualizes 100+ airports with geographically-informed positioning
- 🕸️ **Network Centrality Analysis** — Computes degree, closeness, and betweenness centrality for hub comparison
- 🤖 **Agent-Based Model** — Simulates passenger/plane movement patterns across the network
- 📊 **Real Route Data** — Based on actual flight distances from six major hubs (JFK, ATL, ORD, DFW, DEN, LAX)
- 🗺️ **Geographic Coordinate Mapping** — Uses latitude/longitude for spatially accurate node positioning
- 📈 **Interactive Visualization** — Animated agent movement showing regional travel patterns

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Dependencies

```bash
pip install networkx matplotlib numpy pandas
```
---
## 💡 Usage

Basic Network Visualization
Run the main script to generate the Kamada-Kawai graph:
```bash
python "CMPLXSYS 270 Final Project.py"
```
**This will:**
Load flight routes from the CSV data
Construct a directed weighted graph (100+ nodes, 200+ edges)
Apply Kamada-Kawai layout using geographic distances
Display the network with edge labels showing route distances

### Example Output
The visualization produces a force-directed graph showing:
Hub nodes (JFK, ATL, ORD, DFW, DEN, LAX) as major connection points.
Edge weights representing flight distances in miles.
Spatial clustering reflecting geographic regions (Northeast, Southeast, Midwest, Southwest, West Coast).
Centrality Analysis
To analyze hub importance programmatically:
```Python
import networkx as nx

# Load graph
G = nx.DiGraph()
# ... add edges ...

# Calculate centrality metrics
degree_cent = nx.degree_centrality(G)
closeness_cent = nx.closeness_centrality(G)
betweenness_cent = nx.betweenness_centrality(G)

# Dallas (DFW) typically shows highest values across all metrics
print(f"Dallas Degree Centrality: {degree_cent['DFW']:.4f}")
```
## 📊 Research Findings
### Centrality Metrics Results
| City                | Degree | Closeness | Betweenness |
| ------------------- | ------ | --------- | ----------- |
| **Dallas, TX**      | 0.84   | 0.8621    | 0.3800      |
| **Denver, CO**      | 0.72   | 0.7813    | 0.2238      |
| **Los Angeles, CA** | 0.72   | 0.7813    | 0.1901      |
| **Chicago, IL**     | 0.47   | 0.6536    | 0.0722      |
| **New York, NY**    | 0.42   | 0.6329    | 0.0867      |
| **Atlanta, GA**     | 0.39   | 0.6211    | 0.0812      |

### Key Insights
Geographic Patterns:
Atlanta serves the Appalachian/Piedmont region — mountain barriers make air travel essential despite short distances.
Denver connects Rocky Mountain communities with limited ground infrastructure.
Chicago acts as the primary East-West connector despite lower raw connectivity.

Cultural Patterns:
Los Angeles dominates Southwest travel due to Hispanic cultural ties and historical Spanish/Mexican frontier legacy.
New York maintains strong Northeast Corridor connections plus Florida routes (snowbird migration).

Efficiency Implications:
100-500 mile corridors (Northeast, Florida, California) show potential for high-speed rail alternatives.
Airport consolidation opportunities exist in overlapping metro areas (Austin/San Antonio, Miami/Fort Lauderdale).

