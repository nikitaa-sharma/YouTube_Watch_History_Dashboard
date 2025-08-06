## 📊 YouTube Watch History Dashboard

An interactive Streamlit dashboard that visualizes your personal YouTube watch history. See your most watched channels, daily/hourly viewing habits, and generate a word cloud of your video titles.

---

### 🚀 Features

* 🔝 **Top Watched Channels** – Bar chart of your top 10 most-watched channels
* ⏰ **Activity by Hour** – Histogram of what time of day you watch the most
* 📅 **Activity by Day of Week** – Your weekly viewing habits
* 🔠 **Word Cloud** – Visual summary of words in the video titles you watched

---

### 📁 Folder Structure

```
youtube-dashboard/
├── app.py                    # Main Streamlit app
├── analyze.py               # Preprocess and clean the data
├── visualizations.py        # Plotting functions for dashboard
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

### 📦 Requirements

Install the dependencies using:

```bash
pip install -r requirements.txt
```

---

### 🧾 How to Get Your Watch History (JSON)

1. Go to [Google Takeout](https://takeout.google.com/)
2. Select **only** "YouTube and YouTube Music"
3. Click **Multiple formats** → make sure **History format is JSON**
4. Export your data and download the `.zip` file
5. Inside the zip, go to:
   `Takeout/YouTube and YouTube Music/history/watch-history.json`
6. Upload this file into the dashboard

---

### ▶️ Running the App

```bash
streamlit run app.py
```

Your browser will open with an interactive dashboard where you can upload your `watch-history.json`.

---

### 🧠 Built With

* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/) – for building the dashboard
* [Plotly](https://plotly.com/) – for interactive charts
* [WordCloud](https://github.com/amueller/word_cloud) – for generating the word cloud
* [Pandas](https://pandas.pydata.org/) – for data manipulation

---

### 📸 Sample Output

> Add screenshots of your dashboard here after running it!
> E.g., Top Channels, Word Cloud, Time-Based Activity

---

### 📚 Future Enhancements

* 📆 Date range filter for customized time periods
* 🎯 Channel filter and search
* 📤 Export analysis as PDF or CSV
* 📈 Trendline of videos watched over time

---

### 🙋‍♀️ Author

**Nikita Sharma**
Aspiring Data Scientist | 3rd Year IT Engineering Student

---