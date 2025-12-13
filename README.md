# WhatsApp Chat Analyzer

## 📌 Overview

The **WhatsApp Chat Analyzer** is a Python-based data analysis application that helps you gain insights from exported WhatsApp chat files. It processes chat data to extract meaningful statistics, trends, and visualizations, making it easier to understand communication patterns in personal or group chats.

This project is useful for analyzing message activity, user engagement, media sharing behavior, and temporal trends.

---

## 🚀 Features

* Total messages, words, and media shared count
* User-wise message distribution (group chats)
* Most active users analysis
* Timeline analysis (daily, monthly, yearly activity)
* Activity heatmap (most active days and hours)
* Most common words used (after preprocessing)
* Emoji analysis
* Media and link sharing analysis

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries Used:**

  * pandas
  * numpy
  * matplotlib
  * seaborn
  * nltk
  * emoji
  * wordcloud
  * streamlit
* **Tools:** VS Code, Git, GitHub

---

## 📂 Project Structure

```
whatsapp-chat-analyser/
│
├── app.py                 # Main Streamlit application
├── helper.py              # Helper functions for analysis
├── preprocessor.py        # Chat preprocessing logic
├── requirements.txt       # Project dependencies
├── Procfile               # Deployment configuration
├── setup.sh               # Setup script for deployment
├── stop_hinglish.txt      # Custom stopwords file
├── .gitignore             # Ignored files
├── README.md              # Project documentation
```

---

## 📥 Input Format

* Export WhatsApp chat in **.txt** format
* Supported export format: **Without media**
* Example:

  ```
  12/05/2025, 10:45 PM - User Name: Message text
  ```

---

## ▶️ How to Run the Project Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/aryanfarswan77/whatsapp-chat-analyser.git
   cd whatsapp-chat-analyser
   ```

2. **Create and activate a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

5. Upload your WhatsApp chat `.txt` file in the app interface

---

## 📊 Output

* Interactive dashboards and charts
* Visual insights into chat behavior
* User and time-based analytics

---

## ⚠️ Notes

* Do not upload personal or sensitive chat data to public repositories
* Use sample or anonymized chat files for testing

---

## 📈 Future Enhancements

* Support for multiple chat formats
* Sentiment analysis of messages
* Advanced NLP-based topic modeling
* Export analysis reports as PDF

---

## 👤 Author

**Aryan Farswan**
GitHub: [aryanfarswan77](https://github.com/aryanfarswan77)

---

## ⭐ Acknowledgements

This project was developed as part of hands-on learning in Python, Data Analysis, and NLP. Feedback and contributions are welcome.

---

If you find this project useful, please consider giving it a ⭐ on GitHub.
