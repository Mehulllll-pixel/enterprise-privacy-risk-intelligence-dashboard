#  Enterprise Privacy Risk Intelligence Platform

> Enterprise-grade full-stack platform for privacy risk assessment, governance automation, and compliance reporting.

---

## Overview

The Enterprise Privacy Risk Intelligence Platform is a full-stack application designed to help organizations identify, assess, and manage privacy risks across enterprise data assets.

The platform centralizes data inventory management, automates risk scoring, enforces role-based access control, and provides interactive dashboards for governance teams to monitor compliance and prioritize remediation efforts.

Built with scalability in mind, the system supports **1,000+ enterprise data assets**, real-time risk analytics, and a dual-database architecture optimized for high-performance workloads.

---

## Features

- Enterprise Data Inventory Management
- Real-time Privacy Risk Assessment
- Automated Risk Classification (Low, Medium, High, Critical)
- Executive Analytics Dashboard
- Interactive Risk Heatmaps
- Downloadable Risk Register
- Role-Based Access Control (5 User Roles)
- Automated ETL Pipeline
- Audit-ready Governance Reports
- Responsive Web Interface

---

## Dashboard Preview

### Executive Dashboard

![Dashboard Overview](assets/dashboard_overview.png)

---

### Privacy Risk Register

![Risk Register](assets/risk_register.png)

---

### Enterprise Data Inventory

![Data Inventory](assets/data_inventory.png)

---

## Key Highlights

- Manages **1,000+ enterprise data assets**
- Supports **5-role Role-Based Access Control (RBAC)**
- Real-time enterprise privacy risk scoring
- Automated ETL pipeline for continuous data ingestion
- Dual-database architecture using **PostgreSQL** and **SQL Server**
- Reduced database query contention by approximately **40%**
- Dockerized deployment reducing environment setup from **hours to under 5 minutes**

---

## Risk Assessment Model

Each asset is evaluated using a quantitative scoring framework based on:

- Data Sensitivity
- Business Impact
- Likelihood of Exposure
- Regulatory Compliance Requirements

Final risk levels are automatically categorized into:

- Low
- Medium
- High
- Critical

---

## System Architecture

```text
Enterprise Data Sources
          │
          ▼
 Automated ETL Pipeline
          │
          ▼
 PostgreSQL + SQL Server
          │
          ▼
 Risk Assessment Engine
          │
          ▼
 Governance Dashboard
          │
          ▼
 Reports & Analytics
```

---

## Technology Stack

### Frontend

- React
- Tailwind CSS

### Backend

- ASP.NET Core Web API
- Entity Framework Core

### Database

- PostgreSQL
- SQL Server

### Authentication

- JWT Authentication
- Role-Based Authorization (RBAC)

### DevOps

- Docker
- Docker Compose

### Data Processing

- Python
- Pandas

---

## Performance

| Metric | Value |
|---------|------:|
| Enterprise Assets | 1,000+ |
| User Roles | 5 |
| Query Contention Reduction | ~40% |
| Environment Setup | <5 Minutes |
| Risk Categories | 4 |
| Database Architecture | PostgreSQL + SQL Server |

---

## Future Improvements

- Live compliance monitoring
- GDPR & DPDP compliance modules
- Email notifications
- Risk trend forecasting
- Audit log visualization
- SSO (Azure AD / OAuth)
- Multi-tenant architecture

---

## License

This project is intended for educational and portfolio purposes.
