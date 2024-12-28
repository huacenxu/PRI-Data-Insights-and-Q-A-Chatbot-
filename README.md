### PRI Data Insights and Q&A Chatbot
#### Overview
This project combines data analysis, AI-powered insights, and a chatbot interface to enhance operational efficiency in handling PRI data and summary notes. The pipeline integrates modern AI techniques, visualization tools, and chatbot functionality.

#### Key Features
Data Preprocessing:
Cleans, merges, and processes PRI and summary notes data.
Maps data by semantic topics and categories.

Similarity Scoring:
Computes similarity scores between PRI descriptions and summary notes to identify alignment or gaps.

Dynamic Visualizations:
Provides insights through interactive visualizations, highlighting performance across categories and sites.

AI-Powered Q&A:
A chatbot powered by large language models for answering key business questions.

##### Getting Started
##### Clone the Repository:
git clone https://github.com/yourusername/pri-insights-chatbot.git

##### Install Dependencies:
pip install -r requirements.txt

##### Run the Scripts:
Preprocess data:
python src/data_processing.py

Compute similarity:
python src/similarity_processor.py

Visualize insights:
python src/visualization.py

Interact with the chatbot:
python src/chatbot.py

#### Sample Data
Column	Description
site	Site name or identifier
category	Semantic topic (e.g., risk, content)
PRI description	Description from PRI data
Notes description	Description from summary notes
similarity_score	Alignment score (0 to 1)

#### Future Enhancements
Integration with cloud platforms for real-time processing.
Advanced machine learning models for predictive analytics.
Streamlit-based app deployment for visualization and chatbot.
