# Biological Pathways and Signaling Systems in *E. coli*

## Project Overview

This repository contains documentation and simulation code for two major biological systems in *Escherichia coli*:

1. **Asparagine Biosynthetic Pathway**
2. **PhoQ/PhoP Two-Component Signaling System**

# Biological Pathways and Signaling Systems in *E. coli*

## 1. Asparagine Biosynthetic Pathway

📄 **File:** `Documentation_Asparagine_Pathway.pdf`

### Description
 
<img src="https://github.com/user-attachments/assets/71342d17-488e-495c-9729-c965378913ad" alt="SCC2" width="10%">

This document explains the asparagine biosynthetic pathway in *E. coli*, focusing on the regulatory role of AsnC and the enzyme asparaginase.

### Key Concepts

- **AsnC (Transcription Factor):** Activates the expression of the `asnA` gene, which encodes asparaginase.
- **Asparginase:** Converts the aspartate (substrate) to L-aspargine (product).
- **L-Asparagine:** Binds AsnC to form the AsnC-asparagine complex (TfM), inhibiting further asparaginase production via a negative feedback loop.

### Model Details

- **Regulatory Mechanism:** Negative feedback regulation of asparaginase synthesis.
- **Mathematical Model:** Ordinary Differential Equations (ODEs) describing interactions between transcription factors, metabolites, and enzymes.
- **Python Simulation Code:** Simulates the dynamics of the asparagine biosynthetic pathway over time.

---

## 2. PhoQ/PhoP Two-Component System

📄 **File:** `Simulations_of_a_two-component_system_(E_coli).pdf`

### Description

<img src="https://github.com/user-attachments/assets/a5df7905-af0b-459b-b75e-ba433eed7235" alt="PhoPQ network" width="40%">

This document contains Python code for simulating the PhoQ/PhoP two-component system in *E. coli*. This system is crucial for bacterial adaptation to changes in environmental Mg²⁺ levels.

### Key Components

- **PhoQ:** Sensor kinase that phosphorylates itself in response to environmental signals.
- **PhoP:** Response regulator that gets phosphorylated by PhoQ.
- **MgrB:** Negative feedback regulator that inhibits PhoQ.

### Simulation Details

- **Initial Conditions:** Concentrations of PhoQ, PhoP, PhoQ-P, PhoP-P, and MgrB.
- **Parameters:** Rates of phosphorylation, dephosphorylation, and feedback inhibition.
- **Output:** Time-evolution plots of system components (PhoQ, PhoP, PhoQ-P, PhoP-P, and MgrB).

---

📄 **File:** `Mathematical_modeling_of_a_two-component_system_(PhoQ_PhoP_Signaling_System)_in_Escherichia_coli.pdf`

### Description

This document provides an in-depth explanation of the mathematical model for the PhoQ/PhoP signaling pathway.

### Highlights

- **Mechanism Overview:** How PhoQ detects environmental signals and activates PhoP.
- **ODEs:** Equations describing the dynamics of phosphorylation and feedback regulation.
- **Biological Relevance:** The role of this system in modulating gene expression under varying environmental conditions.

---

## Requirements

### Software Dependencies

- **Python 3.x**

### Libraries

- `numpy`
- `matplotlib`
- `scipy`

### Installation

To install the required libraries, run:

```bash
pip install numpy matplotlib scipy
```

## How to Run the Simulations

### Asparagine Pathway Simulation
1. Open the Python code provided in `Documentation_Asparagine_Pathway.pdf`.
2. Run the script to simulate the asparagine biosynthetic pathway.
3. The output will be a plot showing the concentrations of transcription factors, enzymes, and metabolites over time.

### PhoQ/PhoP System Simulation
1. Open the Python code provided in `Simulations_of_a_two-component_system_(E_coli).pdf`.
2. Execute the script to simulate the PhoQ/PhoP signaling dynamics.
3. Adjust the parameters as needed to explore different scenarios.
4. The script generates time-evolution plots for PhoQ, PhoP, PhoQ-P, PhoP-P, and MgrB.

---

## References

### Asparagine Pathway
- [RegulonDB AsnC Regulatory Network](https://regulondb.ccg.unam.mx/)
- [PlosOne Article on Regulatory Networks](https://journals.plos.org/plosone/)

### PhoQ/PhoP System
- [ResearchGate Figure on PhoQ-PhoP System](https://www.researchgate.net/)
- [Wiley Article on PhoQ-PhoP Dynamics](https://www.wiley.com/)
