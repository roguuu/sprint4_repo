# Vehicle Analysis Dashboard

## Project Overview

This project is a web application dashboard built using **Streamlit**, **Pandas**, **Plotly Express**, and **Altair**. The application provides an interactive interface for analyzing a car advertisement dataset (`vehicles_us.csv`). Users can explore various visualizations and insights derived from the dataset.

## Features

- **Interactive Data Visualizations**: Generate histograms and scatter plots to analyze the distribution and relationships between different variables in the dataset.
- **Data Exploration**: Perform exploratory data analysis (EDA) in Jupyter notebooks and integrate these findings into the web app.

## Technology Stack

- **Python**: Core programming language for data processing and visualization.
- **Streamlit**: Framework for building the web application dashboard.
- **Pandas**: Library for data manipulation and analysis.
- **Plotly Express**: Library for creating interactive plots and charts.
- **Altair**: Library for declarative statistical visualization.

## Project Setup Instructions

### Prerequisites

1. **Python**: Ensure that you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).
2. **Git**: Make sure Git is installed. Download it from [git-scm.com](https://git-scm.com/).

### Step-by-Step Guide

1. **Clone the Repository**
    ```bash
    git clone https://github.com/roguuu/sprint4_repo.git
    cd your-repository
    ```

2. **Set Up a Virtual Environment**
    ```bash
    python -m venv envname
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install Required Packages**
    ```bash
    pip install pandas streamlit plotly.express altair
    ```

4. **Download the Dataset**
    - Place the `vehicles_us.csv` file in the root directory of the project.

5. **Launch the Web Application**
    ```bash
    streamlit run app.py
    ```

    The application will be available at `https://sprint4-repo.onrender.com`.

### Using the Web Application

- Navigate through different sections of the dashboard to explore various data visualizations.


Hello, thank you for the feedback! I updated my cylinders column using the transform method. I tried applying the same logic to odometer and model year but I just don't have the vision to see how I can apply a more relevant way of handling the missing values so if you can help me with that to, it would be great (assuming transform can be applied opposed to what I did). Thank you! And the render website should be working now.
