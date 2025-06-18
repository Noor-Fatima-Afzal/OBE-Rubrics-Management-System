# 📊 OBE Rubrics Management System

A Streamlit-powered web app to manage Outcome-Based Education (OBE) data: students, CLOs, rubrics, assessments, rubric levels and reports — all backed by a MySQL database.

---

## Table of Contents

- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Prerequisites](#prerequisites)  
- [Installation & Setup](#installation--setup)  
  - [1. Clone the repo](#1-clone-the-repo)  
  - [2. Python dependencies](#2-python-dependencies)  
  - [3. MySQL database & schema](#3-mysql-database--schema)  
  - [4. Configure connection](#4-configure-connection)  
- [Running the App](#running-the-app)  
- [Usage](#usage)  
- [Database Schema](#database-schema)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Features

- **Manage Students**: Add / view / validate unique student records  
- **Manage CLOs**: Create / list Course Learning Outcomes  
- **Manage Rubrics**: Define rubrics tied to specific CLOs  
- **Manage Assessments**: Create assessments with total marks  
- **Manage Rubric Levels**: Specify performance levels (1–5) per rubric  
- **Reports**:  
  - Evaluation Summary  
  - CLO-wise Class Results  
  - Assessment-wise Class Results  

---

## Tech Stack

- **Frontend & Server**: [Streamlit](https://streamlit.io/)  
- **Database**: MySQL (via `mysql-connector-python`)  
- **Data handling**: pandas  

---

## Prerequisites

- **Python 3.7+**  
- **MySQL 5.7+** (or compatible)  
- `pip` (or `conda`)  
- Access to create databases & tables  

---

## Installation & Setup

### 1. Clone the repo

```bash
git clone https://github.com/Noor-Fatima-Afzal/obe-rubrics-management.git
cd obe-rubrics-management
