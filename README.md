# 🎬 Movie Recommendation System (Content-Based)

A simple and fast **Movie Recommender System** that suggests the top 5 similar movies based on a selected movie title.  
Built using the **TMDB 5000 Movies Dataset**, processed and deployed using **Streamlit**.

---

## 🚀 Features
- Content-based recommendation  
- Uses cosine similarity  
- Clean Streamlit UI  
- Fast response using precomputed matrices  
- Easy to extend or integrate into another app

---

## 🧠 How It Works
1. TMDB movies & credits datasets are loaded  
2. Important features are extracted and combined  
3. Text is vectorized  
4. Cosine similarity matrix is generated  
5. App returns the top 5 most similar movies to the selected title

---

## 📂 Project Structure
├── app.py # Streamlit UI + recommendation logic

├── model.ipynb # Preprocessing + similarity matrix creation


## 🛠 Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Streamlit  
- Pickle  
