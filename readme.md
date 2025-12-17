📩 Spam Detection Web App

Machine Learning + Web Application

This project is part of my #12WeeksOfDomains challenge (Week 5), where I combine concepts from Data Science, Machine Learning, Deep Learning basics, and Web Development into a single practical application.

The Spam Detection Web App allows users to enter a text message and instantly check whether it is Spam or Not Spam using a trained Machine Learning model, wrapped inside a clean and user-friendly web interface.

🚀 Project Overview

Spam messages are a common real-world problem. This project demonstrates how a Machine Learning classification model can be trained and integrated into a web application so users can interact with predictions in real time.

The focus of this project is not only prediction accuracy, but also end-to-end integration, including model training, backend logic, and frontend user experience.

🧠 Features

Predicts whether a message is Spam or Not Spam

Clean and modern UI with responsive design

Character counter for user input

Loading animation during prediction

Prediction history (session-based)

Dark mode toggle

Simple and intuitive user experience

🛠️ Tech Stack

Machine Learning & Backend

Python

Pandas

Scikit-learn

Multinomial Naive Bayes

Flask

Frontend

HTML

CSS

JavaScript

📂 Project Structure
spam-detection-web-app/
│
├── app.py
├── train_model.py
├── model.pkl
├── vectorizer.pkl
├── sms.tsv
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

⚙️ How It Works

User enters a text message in the web interface

The message is sent to the Flask backend

Text is transformed using the trained vectorizer

Machine Learning model predicts Spam / Not Spam

Result is displayed on the UI with visual feedback

▶️ How to Run the Project Locally
1️⃣ Clone the repository
git clone https://github.com/your-username/spam-detection-web-app.git
cd spam-detection-web-app

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Train the model
python3 train_model.py


This will generate:

model.pkl

vectorizer.pkl

4️⃣ Run the web application
python3 app.py

5️⃣ Open in browser
http://127.0.0.1:5000/

📊 Machine Learning Details

Problem Type: Binary Classification

Input: SMS text message

Output: Spam (1) or Not Spam (0)

Algorithm Used: Multinomial Naive Bayes

Text Vectorization: CountVectorizer

The model was selected for its simplicity, speed, and effectiveness in text classification tasks.

🔮 Future Enhancements

This project can be extended further to make it more robust and production-ready:

Replace CountVectorizer with TF-IDF

Experiment with models like Logistic Regression and SVM

Integrate Deep Learning models (LSTM / Bi-LSTM)

Add database support for storing user predictions

Expose the model as a REST API

Deploy the app using Docker and cloud platforms

Improve UI with real-time predictions and analytics

Add authentication and security features

💼 What This Project Demonstrates

End-to-end Machine Learning workflow

Integration of ML models with web applications

Practical use of Flask for backend development

Clean UI/UX design for better user interaction

Ability to combine multiple domains into one project

📌 Learning Outcome

This project helped me understand how Machine Learning models are deployed and used in real-world applications, beyond notebooks and offline predictions. It strengthened my skills in ML, backend integration, and frontend design, while reinforcing the importance of user experience.

🔗 Challenge Context

This project is part of my 12 Weeks of Domains Challenge, where I explore one tech domain per week and build a mini project to reinforce learning.

👤 Author

K. Narsimhulu
GitHub: https://github.com/Narsimhakurvaa

⭐ If you like this project, feel free to star the repository and share feedback.