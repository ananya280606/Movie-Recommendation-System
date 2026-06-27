# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using **Python**, **Machine Learning**, and **Streamlit**. The application recommends movies similar to the one entered by the user using cosine similarity.

## 🚀 Features

* Recommend movies based on user input.
* Fuzzy string matching to handle spelling mistakes.
* Interactive web interface built with Streamlit.
* Fast recommendation generation using a precomputed similarity matrix.
* Simple and responsive UI.

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle

## 📂 Project Structure

```
movie-recommendation-system/
│── app.py
│── requirements.txt
│── movies_list.pkl
│── dataset/
│   └── movies.csv
│── model/
│   └── movie_recommender.ipynb
│── .gitignore
```

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/ananya280606/Movie-Recommendation-System.git
```

2. Navigate to the project folder:

```bash
cd Movie-Recommendation-System
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit application:

```bash
streamlit run app.py
```

## 📌 Note

The file `similarity.pkl` is **not included** in this repository because it exceeds GitHub's 100 MB file size limit.

To run the project successfully, generate the similarity matrix using the notebook (`model/movie_recommender.ipynb`) or place the `similarity.pkl` file in the project root directory.
