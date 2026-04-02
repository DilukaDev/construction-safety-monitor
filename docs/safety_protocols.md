# Safety Protocol Specification

This document defines the logic used by the Construction Safety Monitor to determine PPE compliance. The system moves beyond simple detection by implementing a hierarchical relationship between workers and their equipment.

## 1. The Anchor-Based Inference Logic

The system uses the Person class (Class ID 6) as the Spatial Anchor.

**Rule:** An equipment detection (PPE) is only attributed to a worker if its Geometric Center Point falls within the bounding box coordinates of a detected Person.

This prevents "ghost detections" (e.g., a helmet sitting on a fence) from being marked as a compliant worker.

## 2. The 11-Class Violation Hierarchy

The system evaluates safety using a two-tier check: Explicit Negatives and Implicit Absences.

### Tier 1: Explicit Violation Detection (Classes 7-10)

The model is trained to specifically recognize "Negative" states. If any of these classes are anchored to a person, a Critical Violation is raised immediately.

| Detection | Alert Message  |
| --------- | -------------- |
| no_helmet | REQ: NO HELMET |
| no_goggle | REQ: NO GOGGLE |
| no_gloves | REQ: NO GLOVES |
| no_boots  | REQ: NO BOOTS  |

### Tier 2: Implicit Absence Detection (Classes 0-4)

If an explicit negative is not found, the system checks for the presence of "Positive" PPE. If neither the positive gear nor the explicit negative is found, the system flags it as Missing.

- **Primary PPE (Helmet & Vest):** These are mandatory. If the positive class is absent, a MISSING alert is generated.
- **Secondary PPE (Gloves, Boots, Goggles):** Currently tracked for presence to assist in site-wide safety audits.

## 3. Compliance States

| State      | Logic                               | UI Output              |
| ---------- | ----------------------------------- | ---------------------- |
| Compliant  | Person + Helmet + Vest              | Green Box              |
| Violation  | Person + (no_helmet OR no_vest)     | Red Box + Label        |
