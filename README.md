# 🔋 Renewable Energy Prediction App

This is a simple web app built with **Streamlit** that predicts renewable energy output based on user inputs. It uses a trained machine learning model and a preprocessor to make accurate predictions.

---

## 🚀 How to Run

1. **Clone this repo**  
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install required packages**  
   Make sure you have Python installed, then run:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the app**  
   ```bash
   streamlit run app.py
   ```

---

## 🌐 Deploying to Streamlit Cloud

1. Push your project to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Click "New App" and choose your repo.
4. Make sure the main file is `app.py`.

**Note**: If your `model.pkl` file is bigger than 25MB, you can't upload it directly to GitHub.  
Instead:
- Use [Git LFS](https://git-lfs.com/), or  
- Upload the file to Google Drive / Dropbox and load it from the URL in your code.

---

## 🧠 What It Does

- Takes in renewable energy system features
- Uses a trained ML model to predict energy output
- Easy to use with a clean interface

---

## 🧰 Requirements

Sample `requirements.txt`:

```txt
streamlit
pandas
numpy
scikit-learn
xgboost
lightgbm
plotly
joblib
requests
```
