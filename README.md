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
