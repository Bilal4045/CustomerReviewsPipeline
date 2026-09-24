# Customer Reviews Data Engineering Pipeline

An end-to-end Data Engineering project for processing, storing, transforming, and analyzing **584K+ customer reviews** using PostgreSQL, FastAPI, and a React-based analytics dashboard.

## 🚀 Project Overview

This project demonstrates a complete data workflow starting from customer review data and transforming it into structured analytical datasets that can be consumed through REST APIs and visualized through an interactive dashboard.

The project focuses on:

* Data storage and management using PostgreSQL
* SQL-based analytical transformations
* Materialized views for analytical workloads
* REST API development with FastAPI
* Interactive data visualization with React and Recharts
* Continuous Integration using GitHub Actions

## 🏗️ Architecture

```text
                    Customer Reviews Dataset
                              │
                              ▼
                       PostgreSQL Database
                              │
                              ▼
                    SQL Analytical Layer
                              │
              ┌───────────────┴───────────────┐
              │                               │
              ▼                               ▼
       Materialized Views                Analytical SQL
              │
              ▼
          FastAPI REST API
              │
              ▼
       React Analytics Dashboard
              │
              ▼
          Data Visualization
```

## 📊 Dataset

The project processes **584K+ customer reviews** stored in PostgreSQL.

The review data contains information used for customer, product, rating, and review analysis.

The database includes a `reviews` table along with an analytical `marts` schema.

## 🗄️ Analytical Data Mart

The project uses PostgreSQL materialized views to create reusable analytical datasets.

### Available Marts

| Mart                     | Purpose                                     |
| ------------------------ | ------------------------------------------- |
| `summary_stats`          | Overall review statistics                   |
| `score_distribution`     | Distribution of review scores               |
| `daily_review_volume`    | Reviews by day                              |
| `monthly_review_volume`  | Monthly review trends and average scores    |
| `most_reviewed_products` | Products with the highest number of reviews |
| `top_products`           | Products with strong review performance     |
| `worst_products`         | Products with lower review performance      |
| `top_reviewers`          | Reviewers with high review activity         |
| `most_helpful_reviews`   | Most helpful customer reviews               |

## ⚡ FastAPI Backend

The backend provides REST APIs for accessing the analytical datasets.

### API Endpoints

```text
/api/summary/
/api/score_distribution/
/api/daily_review_volume/
/api/monthly_review_volume/
/api/top_products/
/api/worst_products/
/api/most_reviewed_products/
/api/top_reviewers/
/api/most_helpful_reviews/
```

FastAPI automatically provides interactive API documentation through Swagger UI.

When running locally:

```text
http://127.0.0.1:8000/docs
```

## 📈 Frontend Dashboard

The React frontend consumes the FastAPI endpoints and presents the analytical results through an interactive dashboard.

The dashboard includes:

* Summary statistics
* Review score distribution
* Daily review volume
* Monthly review trends
* Top products
* Worst products
* Most reviewed products
* Top reviewers
* Most helpful reviews
* Interactive charts

## 🛠️ Tech Stack

### Data Engineering & Database

* PostgreSQL
* SQL
* Materialized Views

### Backend

* Python
* FastAPI
* SQLAlchemy
* psycopg2
* python-dotenv

### Frontend

* React.js
* JavaScript
* Axios
* Recharts

### DevOps / CI

* Git
* GitHub
* GitHub Actions

## 📁 Project Structure

```text
CustomerReviewsPipeline/
│
├── backend/
│   ├── app/
│   │   ├── db/
│   │   ├── routers/
│   │   ├── main.py
│   │   └── ...
│   │
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── api.js
│   │   └── ...
│   │
│   ├── package.json
│   └── ...
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── marts.sql
├── .env.example
├── .gitignore
└── README.md
```

## 🔧 Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Bilal4045/CustomerReviewsPipeline.git
cd CustomerReviewsPipeline
```

### 2. Backend Setup

Navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file inside the `backend` directory:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/Reviews
```

Replace `YOUR_PASSWORD` with your PostgreSQL password.

**Never commit your `.env` file to GitHub.**

### 4. Run the Backend

From the `backend` directory:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

### 5. Run the Frontend

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:5173
```

## 🔐 Environment Variables

The backend uses environment variables for database configuration.

Example:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/Reviews
```

An `.env.example` file is included so that required environment variables can be configured without exposing credentials.

## 🔄 GitHub Actions

The project includes a GitHub Actions workflow that performs automated CI checks.

The workflow:

* Sets up Python
* Installs backend dependencies
* Sets up Node.js
* Installs frontend dependencies
* Builds the React frontend

Workflow location:

```text
.github/workflows/ci.yml
```

This helps ensure that changes pushed to the repository do not introduce basic dependency or frontend build issues.

## 🔍 Key Data Engineering Concepts Demonstrated

This project demonstrates practical use of:

* Relational database design
* PostgreSQL
* SQL transformations
* Aggregations
* Analytical data marts
* Materialized views
* API-based data serving
* Backend/frontend separation
* Environment-based configuration
* CI automation
* Data visualization

## 🎯 Project Goals

The main goal of this project is to demonstrate how raw customer review data can be transformed into an analytical system that supports:

```text
Raw Data
   ↓
Database Storage
   ↓
SQL Transformations
   ↓
Analytical Data Mart
   ↓
REST APIs
   ↓
Analytics Dashboard
```

## 🚀 Future Improvements

Potential future improvements include:

* Automated data ingestion pipeline
* Scheduled data transformations
* Incremental data processing
* Data quality validation
* Database indexing optimization
* Pipeline monitoring and logging
* Cloud-based data warehouse integration
* Workflow orchestration

## 👨‍💻 Author

**Bilal**

BS Data Science | Data Engineering Enthusiast

GitHub: [Bilal4045](https://github.com/Bilal4045)

---

⭐ If you find this project useful, consider giving the repository a star.
