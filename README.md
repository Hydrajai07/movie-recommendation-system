🎬 AI-Based Movie Recommendation System
This is a simple content-based movie recommendation system built using Python. It suggests similar movies based on genres and keywords. This project works even if pip installations are unavailable — it only uses Python's built-in libraries.

📁 Project Structure

* Movie_recomadation.ipynb     # Jupyter notebook implementation
*  movies.csv                   # Dataset with movie info
*  recommend.py                 # Pure Python version (no external libraries)
*  README.md                    # Project overview
📚 Dataset
The dataset used is a small custom movies.csv file with the following structure:


title,genre,keywords
Inception,Action|Sci-Fi,dream|subconscious|heist
Interstellar,Adventure|Drama|Sci-Fi,space|time|blackhole
The Dark Knight,Action|Crime|Drama,batman|joker|vigilante
...
title: Movie name

genre: Pipe-separated list of genres

keywords: Pipe-separated movie tags

🧠 How It Works
Load movie data from movies.csv

Calculate similarity based on overlapping genres and keywords

Recommend top 5 most similar movies to the selected one

▶️ How to Run
Option 1: Jupyter Notebook
Open Movie_recomadation.ipynb and run all cells.

Option 2: Python Script (No pip required)
bash

python recommend.py
Then input a movie name (e.g., Inception) to get recommendations.

📌 Example Output
diff

Enter a movie title: Star Wars (1977)

Recommended movies:
1:Empire Strikes Back, The (1980) 
2:Return of the Jedi (1983) 
3:Raiders of the Lost Ark (1981) 
4:Austin Powers: International Man of Mystery (1997)
This script uses only built-in Python libraries:

csv

math (if used for scoring)

So, no installation needed if you use the .py version.

🚀 Future Improvements
Use cosine similarity with TF-IDF for better text-based similarity

Add collaborative filtering using surprise library

Create a web app using Flask or Streamlit

Load larger datasets like MovieLens or IMDb

👨‍💻 Author
Jai Aadhavan

GitHub: Hydrajai07

Email: jaiaadhav07@gmail.com
