# **Mathematical-modeling-of-motifs**

## **PROJECT 1: Aspargine Pathway**

This project models the regulatory network involving transcription factors, substrates, and enzymes in E. coli. The focus is on simulating a negative feedback loop where the transcription factor AsnC regulates the synthesis of L-asparagine. The model is implemented using Python with kinetic equations represented as ordinary differential equations (ODEs).

## **Features**
- Biological Context: Models the AsnC regulatory network, a key component in asparagine metabolism.
- Kinetic Simulations: Solves ODEs to simulate enzyme and metabolite concentrations over time.
- Dynamic Visualization: Generates time-evolution plots for various network components.
- Parameter Justification: Includes references for the choice of biological constants and initial conditions.

---

## **System Components**
The modeled network includes the following:

- Tf: Free transcription factor (asnC)
- TfM: Transcription factor bound to the metabolite (asnC-asparagine complex)
- E: Enzyme (asparaginase)
- M: Metabolite (L-asparagine)
- S: Substrate (Aspartate)

---

## **Parameter Details**
Parameter	Description	Value	Unit

---

## **Simulation Details**
The model simulates the following processes:

- Transcription factor binding to the metabolite.
- Metabolite production and consumption.
- Enzyme synthesis and decay.
- Substrate conversion to metabolite.

The system reaches equilibrium states over time, with insights into metabolite accumulation and transcription factor dynamics.

---

## **Output**
The script generates plots showing the concentration of system components over time, such as:

- Free transcription factor
- Transcription factor-metabolite complex
- Enzyme
- Metabolite
- Substrate

---

## **References**
- Petibon, Cyrielle, et al. "AsnC: an autogenously regulated activator of asparagine synthetase A transcription in Escherichia coli."
- Relevant articles from PubMed and RegulonDB (see documentation for detailed links).

---
