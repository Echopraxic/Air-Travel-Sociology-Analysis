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
---
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

---
## 📁 Project Structure
```text
air-transport-network/
├── CMPLXSYS 270 Final Project.py          # Main visualization script
├── CMPLXSYS 270 Final Project data.csv     # Flight route data (100+ routes)
├── node_coordinates.csv                     # Airport coordinates
├── Complex Systems 270 Final.docx           # Full research paper
├── Complexsys 270 Final Slides.pptx         # Presentation slides
├── Complexsys 270 Research Poster.pdf       # Academic poster
└── README.md                                # This file
```
---
## 🔬 Methodology
### Two-Layer Model Architecture
```text
┌─────────────────────────────────────────────────────────┐
│  LAYER 1: Kamada-Kawai Graph (Static Network)          │
│  • Nodes: 100+ US airports                             │
│  • Edges: Flight routes with distance weights            │
│  • Layout: Force-directed using geographic distances    │
├─────────────────────────────────────────────────────────┤
│  LAYER 2: Agent-Based Model (Dynamic Simulation)       │
│  • Agents: Simulated aircraft/passengers                 │
│  • Behavior: Random walk between connected nodes       │
│  • Visualization: Animated movement patterns             │
└─────────────────────────────────────────────────────────┘
```
### Technical Implementation
Graph Construction: Directed weighted graph using NetworkX

Layout Algorithm: Kamada-Kawai with distance matrix derived from route lengths

Agent Simulation: Randomized agent placement on hub nodes, random neighbor selection for movement

Centrality Analysis: Standard NetworkX algorithms for topological analysis

---
## ⚠️ Limitations
**Data Scope:** Limited to 6 major hubs; excludes smaller regional airports and international routes

**Spatial Distortion:** 2D force-directed graphs cannot perfectly preserve spherical Earth distances

**Agent Realism:** Movement simulation does not account for temporal scaling or flight scheduling constraints

**Outlier Handling:** Alaska and Hawaii positioning requires geographic compromises in the 2D layout

**Static Network:** Does not incorporate real-time factors (delays, weather, seasonal variations)

---
## 🔮 Future Work
[ ] Expand to include all domestic airports (~500 nodes)

[ ] Integrate real-time delay data for dynamic congestion modeling

[ ] Implement multi-layer network (airlines as different edge types)

[ ] Add temporal dimension for seasonal pattern analysis

[ ] Develop predictive models for hub congestion using entropy metrics

[ ] Create interactive web visualization (D3.js/Plotly)

---
## 📚 Citations
If you use this work in your research, please cite:

```Bibtex
@misc{mckenna2024airtransport,
  title={Analyzing Air Travel in a Network Through the Lens of Sociology},
  author={McKenna, Michael},
  year={2024},
  institution={University of Michigan},
  course={CMPLXSYS 270: Agent-based Modeling}
}
```
### References

Guimerà, R., Mossa, S., Turtschi, A., & Amaral, L. A. N. (2005). The worldwide air transportation network: Anomalous centrality, community structure, and cities' global roles. Proceedings of the National Academy of Sciences, 102(22), 7794–7799. https://doi.org/10.1073/pnas.0407994102 

Wang, Z., Wen, X., & Wu, M. (2019). Identification of Key Nodes in Aircraft State Network Based on Complex Network Theory. IEEE Access, 7, 60957–60967. https://doi.org/10.1109/ACCESS.2019.2915508 

Kaziyeva, D., Stutz, P., Wallentin, G., & Loidl, M. (2023). Large-scale agent-based simulation model of pedestrian traffic flows. Computers, Environment and Urban Systems, 105, 102021. https://doi.org/10.1016/j.compenvurbsys.2023.102021

Rocha, L. E. C. (2017). Dynamics of air transport networks: A review from a complex systems perspective. Chinese Journal of Aeronautics, 30(2), 469–478. https://doi.org/10.1016/j.cja.2016.12.029

---
## 🙏 Acknowledgments
This project was developed as the final project for Complex Systems 270: Agent-based Modeling at the University of Michigan.

Special thanks to:

The course instructors and TAs for guidance on complex network analysis

NetworkX developers for the excellent graph analysis library

The Federal Aviation Administration (FAA) and OpenFlights for public flight data
