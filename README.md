 🖥️ Retail Data Cleaning Engine (NumPy)

A high-performance NumPy-based data cleaning system that transforms raw retail datasets into clean, analysis-ready output.

It fixes invalid values, imputes missing data, smooths noisy spikes, and exports a polished CSV — reflecting real data engineering and ML preprocessing workflows.

🚀 Overview

The Retail Data Cleaning Engine performs an automated preprocessing pipeline:

🚫 Replaces negative values with valid zeros

📊 Fills missing values using column-wise means

🔧 Corrects isolated zero spikes using neighbor-based smoothing

💾 Saves the cleaned dataset as result.csv

Built using fully vectorized NumPy operations for speed and scalability.

🧩 Features

| Feature                        | Description                                  |
| ------------------------------ | -------------------------------------------- |
| 🧮 Vectorized NumPy Processing | Fast, scalable array operations              |
| 🚫 Negative Value Handling     | Invalid entries converted to zero            |
| 📉 Spike Correction            | Repairs isolated zero spikes using neighbors |
| 📊 NaN Imputation              | Missing values replaced using column means   |
| 📝 Clean CSV Output            | Exports ready-to-use `result.csv`            |
| 🧱 Modular Pipeline            | `load → clean → save` class-based design     |


📁 Project Structure

retail-data-cleaning-engine/
│

├── main.py              # Core cleaning logic

├── retail_sales.csv     # Raw dataset

├── result.csv           # Cleaned output file

└── README.md            # Documentation

⚙️ Installation & Usage

1️⃣ Clone the Repository

git clone https://github.com/sreeranga-chippala/retail-data-cleaning-engine.git

cd retail-data-cleaning-engine

2️⃣ Run the Script

python3 main.py

A cleaned dataset named result.csv will be generated.

🧠 Concepts Demonstrated

| Concept               | Description                               |
| --------------------- | ----------------------------------------- |
| 📥 NumPy File Loading | Efficient parsing of CSV data             |
| 🧩 Masking & Indexing | Applying conditions across arrays         |
| 📊 NaN Handling       | Column-wise imputation logic              |
| 🔗 Broadcasting       | Smoothing spikes using vector math        |
| 🧱 Array Stacking     | Reconstructing full cleaned datasets      |
| 🧭 OOP Workflow       | Class-based structure for clarity & reuse |

🌟 Future Enhancements

Outlier detection and removal

JSON / Excel export support

Min-max or standard scaling

Log transformation options

Basic visualization of trends

CLI arguments for flexible file input

API version using FastAPI

👨‍💻 Author

Chippala Sree Ranganath
B.E. Artificial Intelligence and Machine Learning — MSRIT
Trained under NxtWave CCBP 4.0 Technologies
Focused on data engineering, automation, NumPy pipelines, and scalable system design.

🔗 GitHub: https://github.com/sreeranga-chippala









