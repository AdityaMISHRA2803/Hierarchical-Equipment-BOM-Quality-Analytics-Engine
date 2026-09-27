# Hierarchical Equipment BOM & Quality Analytics Engine

A production-oriented analytics engine for modeling, traversing, validating, and analyzing complex **Bill of Materials (BOM)** hierarchies. The system combines **Python, SQL recursive CTEs, automated data-quality validation, and Power BI** to transform multi-level equipment structures into analysis-ready datasets.

The project is designed around a common engineering challenge: complex equipment is rarely represented as a flat dataset. Assemblies contain sub-assemblies, which contain components, and each level can carry important engineering, cost, supplier, and quality attributes.

This engine provides a structured workflow for transforming that hierarchical information into actionable engineering and quality analytics.

---

## Key Capabilities

* **Hierarchical BOM Traversal** — Navigate multi-level parent-child equipment structures.
* **Bottom-Up Rollups** — Calculate cumulative properties such as mass and unit cost across assemblies.
* **Recursive SQL Processing** — Use recursive CTEs to explode nested BOM structures into analysis-ready tables.
* **Data Quality Validation** — Validate schemas, relationships, missing values, and structural consistency.
* **Cost Analysis** — Track component-level and assembly-level cost contributions.
* **Pareto Analysis** — Identify the components and suppliers responsible for the largest share of total cost.
* **Supplier Risk Analysis** — Identify single-source components and supplier concentration risks.
* **Change Tracking** — Analyze component and supplier changes across BOM structures.
* **Automated Testing** — Validate core analytics and transformation logic using PyTest.
* **Containerized Execution** — Run the analytics environment consistently using Docker.
* **Interactive BI** — Explore engineering and quality metrics through Power BI dashboards.

---

## System Architecture

```text
                    ┌─────────────────────────┐
                    │     Raw BOM Sources     │
                    │                         │
                    │ Parts / Assemblies /    │
                    │ Suppliers / Attributes  │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   Data Validation Layer │
                    │                         │
                    │ Schema Checks            │
                    │ Relationship Checks      │
                    │ Null / Quality Checks    │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   BOM Processing Engine │
                    │                         │
                    │ Hierarchy Traversal      │
                    │ Recursive Expansion      │
                    │ Bottom-Up Rollups        │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   Analytics Data Layer  │
                    │                         │
                    │ Cost / Mass / Supplier   │
                    │ Quality / Change Data    │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      Power BI Layer     │
                    │                         │
                    │ Pareto Analysis          │
                    │ Decomposition Tree       │
                    │ Supplier Risk             │
                    │ KPI Monitoring            │
                    └─────────────────────────┘
```

---

## BOM Hierarchy

The engine represents equipment as a hierarchical parent-child structure.

For example:

```text
Equipment
├── Assembly A
│   ├── Sub-Assembly A1
│   │   ├── Component A1.1
│   │   └── Component A1.2
│   └── Component A2
│
├── Assembly B
│   ├── Component B1
│   └── Component B2
│
└── Assembly C
    ├── Sub-Assembly C1
    │   ├── Component C1.1
    │   └── Component C1.2
    └── Component C2
```

This structure allows the system to retain the relationship between individual components and the assemblies that consume them.

---

## Engineering Analytics

### Bottom-Up Rollups

A major component of the project is the ability to calculate assembly-level properties from lower-level components.

For example:

```text
Assembly
│
├── Component A → 25 kg
├── Component B → 40 kg
└── Component C → 15 kg
              ↓
        Total Mass = 80 kg
```

The same approach can be applied to cumulative unit costs and other quantitative attributes.

This allows analysis to move from individual components to complete assemblies without losing the underlying hierarchy.

---

## Recursive SQL BOM Explosion

Complex BOM structures cannot always be analyzed effectively in their original nested representation.

The project uses **SQL Recursive CTEs** to traverse parent-child relationships and transform nested structures into denormalized analytical tables.

Conceptually:

```sql
WITH RECURSIVE bom_tree AS (
    SELECT
        parent_id,
        child_id,
        1 AS level
    FROM bom
    WHERE parent_id = :root_id

    UNION ALL

    SELECT
        b.parent_id,
        b.child_id,
        bt.level + 1
    FROM bom b
    JOIN bom_tree bt
        ON b.parent_id = bt.child_id
)
SELECT *
FROM bom_tree;
```

The resulting hierarchy can then be used for:

* Component-level analysis
* Assembly-level aggregation
* Cost rollups
* Mass calculations
* Supplier analysis
* Quality validation
* Downstream warehouse ingestion

---

## Data Quality & Validation

Engineering BOM data can contain structural and quality issues that can propagate into downstream analytics.

The project therefore includes validation checks for areas such as:

* Missing component attributes
* Invalid parent-child relationships
* Duplicate component records
* Schema inconsistencies
* Invalid hierarchy structures
* Missing supplier information
* Unexpected null values
* Inconsistent component metadata

These checks help ensure that analytical outputs are generated from structurally valid BOM data.

---

## Power BI Analytics

The processed BOM data can be consumed by Power BI for interactive engineering and quality analysis.

### Decomposition Tree

The Decomposition Tree enables users to drill from overall equipment cost into increasingly granular dimensions such as:

```text
Total Cost
    ↓
Assembly
    ↓
Sub-Assembly
    ↓
Component
    ↓
Supplier
```

### Pareto Analysis

The dashboard uses dynamic Pareto analysis to identify the components contributing the largest share of total cost.

Example analytical flow:

```text
Total Equipment Cost
        │
        ▼
Component Cost Ranking
        │
        ▼
Cumulative Cost %
        │
        ▼
80/20 Identification
```

This helps highlight cost concentration within large BOM structures.

### Supplier Vulnerability

Supplier-level analysis can be used to identify:

* Single-source components
* Supplier concentration
* High-cost supplier dependencies
* Components exposed to supplier changes

---

## Scale

The analytics workflow is designed to operate across large engineering BOM structures containing **15,000+ assembly components**.

The hierarchical processing approach allows the same analytical model to be applied across different equipment configurations while maintaining component-to-assembly relationships.

---

## Technology Stack

| Category         | Technologies                                 |
| ---------------- | -------------------------------------------- |
| Programming      | Python                                       |
| Data Processing  | Pandas, NumPy                                |
| Database / SQL   | SQL, Recursive CTEs                          |
| Analytics        | Power BI                                     |
| Testing          | PyTest                                       |
| Containerization | Docker                                       |
| Data Modeling    | Hierarchical BOM / Parent-Child Structures   |
| Visualization    | Power BI Decomposition Tree, Pareto Analysis |
| Version Control  | Git / GitHub                                 |

---

## Project Structure

```text
hierarchical-bom-analytics/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
│
├── src/
│   ├── bom/
│   │   ├── hierarchy.py
│   │   ├── traversal.py
│   │   └── rollups.py
│   │
│   ├── analytics/
│   │   ├── cost_analysis.py
│   │   ├── supplier_analysis.py
│   │   └── pareto_analysis.py
│   │
│   └── validation/
│       ├── schema_checks.py
│       └── quality_checks.py
│
├── sql/
│   ├── recursive_bom.sql
│   └── analytical_views.sql
│
├── tests/
│   ├── test_bom.py
│   ├── test_rollups.py
│   └── test_validation.py
│
├── powerbi/
│   └── bom_quality_analytics.pbix
│
├── Dockerfile
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd hierarchical-bom-analytics
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

On Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run the BOM processing workflow:

```bash
python -m src.bom.traversal
```

Run analytical processing:

```bash
python -m src.analytics.cost_analysis
```

Run data-quality validation:

```bash
python -m src.validation.quality_checks
```

> Update these commands if the final repository uses different entry points.

---

## Docker

Build the container:

```bash
docker build -t hierarchical-bom-analytics .
```

Run the application:

```bash
docker run --rm hierarchical-bom-analytics
```

For a multi-container workflow:

```bash
docker compose up --build
```

---

## Testing

The project uses **PyTest** for automated validation of the core processing and analytics logic.

Run the complete test suite:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

Run a specific test module:

```bash
pytest tests/test_bom.py
```

The test suite is intended to validate:

* BOM hierarchy traversal
* Recursive processing
* Bottom-up aggregation
* Cost calculations
* Data-quality validation
* Edge cases in hierarchical structures

---

## Example Analytical Workflow

A typical execution flow is:

```text
Raw BOM Data
     │
     ▼
Schema & Quality Validation
     │
     ▼
Build Parent → Child Relationships
     │
     ▼
Traverse BOM Hierarchy
     │
     ▼
Recursive SQL Expansion
     │
     ▼
Calculate Bottom-Up Metrics
     │
     ├── Mass Rollups
     ├── Cost Rollups
     └── Supplier Metrics
     │
     ▼
Create Analytical Tables
     │
     ▼
Power BI
     │
     ├── KPI Scorecards
     ├── Pareto Analysis
     ├── Decomposition Tree
     └── Supplier Vulnerability
```

---

## Key Engineering Outcomes

The project demonstrates practical experience with:

* Designing analytics around hierarchical engineering data
* Processing **15,000+ component BOM structures**
* Writing recursive SQL transformations
* Building bottom-up aggregation logic
* Implementing automated data-quality checks
* Creating analysis-ready dimensional datasets
* Developing interactive Power BI analytics
* Applying Pareto analysis to engineering cost structures
* Identifying supplier concentration and single-source risks
* Building automated tests for data-processing workflows
* Containerizing analytical applications with Docker

---

## Use Cases

This architecture can be adapted to engineering and manufacturing scenarios such as:

* Equipment configuration analysis
* Manufacturing BOM analytics
* Product cost analysis
* Supplier dependency analysis
* Engineering change analysis
* Component quality monitoring
* Assembly-level KPI reporting
* Cost optimization
* Configuration comparison

---

## Future Improvements

Potential extensions include:

* Incremental BOM processing
* Automated BOM version comparison
* Historical component change tracking
* Graph-based hierarchy visualization
* Advanced anomaly detection
* Automated data-quality reporting
* REST API for querying BOM structures
* CI/CD integration for automated testing and deployment

---

## License

This project is licensed under the terms specified in the repository's `LICENSE` file.
