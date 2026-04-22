# AI Programming with Python: From Scratch to Transformers

## Welcome!
Welcome to my AI Programming portfolio! This repository tracks my journey from foundational Python coding all the way to building deep learning models and natural language processing (NLP) pipelines. 

Instead of relying on heavy, pre-packaged solutions like Anaconda, this entire workspace is built from the ground up using standard Python, native virtual environments (`venv`), and Visual Studio Code. This approach ensures a lightweight, fast, and completely reproducible environment.

---

## The Tech Stack (The "Why")
Here is a quick breakdown of the tools used in this project and why they were chosen:

* **`venv` (Virtual Environment):** Think of this as an isolated "workshop" for this specific project. It prevents the libraries we install here from clashing with other Python projects on the computer.
* **Jupyter Notebooks:** An interactive coding environment where you can write code in blocks (cells) and instantly see the data outputs or charts right below them. Perfect for data science!
* **NumPy & Pandas:** The backbone of AI data prep. NumPy provides ultra-fast math arrays, while Pandas acts like a programmatic version of Excel for cleaning and filtering tabular data.
* **Matplotlib & Seaborn:** Visualization libraries used to turn raw numbers into beautiful, understandable graphs to spot trends.
* **PyTorch:** The industry-standard deep learning framework. It allows us to build artificial neural networks that can run on GPUs and automatically calculate the complex calculus (gradients) needed for AI to "learn."
* **Hugging Face (`transformers`):** The premier library for modern NLP. It allows us to easily download and use massive, pre-trained Large Language Models (LLMs) instead of spending millions of dollars to train our own from scratch.

---

## Environment Setup & Installation

To run the code in this repository, you will need Python and Visual Studio Code installed. Follow these steps to replicate the environment.

### 1. Create and Activate the Virtual Environment
Open your terminal in the root folder of this project and run:

**Create the environment:**
```bash
python -m venv venv
```

**Mac/Linux users: If the above fails, try:**
```bash
python3 -m venv venv
```

**Activate the environment:**
You must run this command every time you open this project to "turn on" the workspace.

Windows:

```bash
.\venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

(You will know it worked when you see **(venv)** at the beginning of your terminal line).

### 2. Install Required Libraries
Once the environment is active, install all the necessary dependencies in one go:

```bash
pip install ipykernel numpy pandas matplotlib seaborn torch torchvision transformers
```

(Note for VS Code users: Make sure you also install the official **"Jupyter"** and **"Python"** extensions from the VS Code extensions marketplace).

## Project Structure & Modules
This repository is broken down into four progressive modules:

### Module 1: Python Fundamentals
**Focus:** Variables, Data Types, Logic (if/else, loops), Data Structures (Lists, Dictionaries), and Functions.

**Highlight:** project1.py - A script that acts as an automated review analyzer, looping through raw dictionary data to calculate average scores and filter out negative reviews.

### Module 2: Data Tools in VS Code
**Focus:** Transitioning to Jupyter Notebooks for Exploratory Data Analysis (EDA).

**Highlight:** project2.ipynb - Generates mock health data, cleans missing values using modern Pandas techniques (avoiding inplace=True errors), and plots the relationship between Age and Cholesterol using Seaborn.

### Module 3: Neural Networks & PyTorch
**Focus:** The math behind AI (Gradient Descent, Backpropagation) and building custom neural networks from scratch.

**Highlight:** project3_mnist.ipynb - A complete deep learning training loop that teaches a PyTorch model to look at pixel data and correctly identify handwritten digits.

### Module 4: Programming Transformers (Capstone)
**Focus:** Natural Language Processing, Tokenization, and leveraging pre-trained Transformer models (the same architecture behind ChatGPT).

**Highlight:** portfolio_project.py - The Capstone Project. An end-to-end sentiment analysis pipeline. It takes raw text (movie reviews), converts them to tokens, and passes them through a fine-tuned DistilBERT model to predict if the text is POSITIVE or NEGATIVE with a confidence percentage.

Note: The capstone script includes use_safetensors=False to ensure smooth, crash-free execution on macOS systems.

## How to Run the Code
Ensure your virtual environment is active.

For Python scripts (.py), run them in the terminal: python file_name.py

For Jupyter Notebooks (.ipynb), open them in VS Code, ensure your venv is selected as the kernel in the top right corner, and click "Run All" or press Shift + Enter on individual cells.