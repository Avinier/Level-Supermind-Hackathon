# Social Media Engagement Analysis

A RAG Chatbot made with Langflow and AstraDB, deployed with Docker, for the Level Supermind Hackathon Assignment.

### Made By: Team Byters
### Demo Video: [https://youtu.be/n7o5SZzaWzo]
### Findcoder Project: [https://www.findcoder.io/projects/team-byters-social-media-engagement-analysis/677f86e18015401a9896b4c7]

### Main Files
* [`engagement-dataset-1.json`](./engagement-dataset-1.json)
  * JSON dataset with all our engagement metrics
  * Contains likes, shares, comments data
  * Used as the main input for analysis

* [`generate_dataset.py`](./generate_dataset.py)
  * Main Python script for data generation
  * Handles all the data processing
  * Generated data through this and RLHFed through the claude-model.

* [`social-media-engagement_bot.json`](./social-media-engagement_bot.json)
  * JSON file of the langflow workflow
  * Contains all the settings for automated data retrieval and insight generation

* [`langflow_code.py`](./langflow_code.py)
  * Langflow python library code
  * Created for more granular tweaking of components, and deploying on cloud.

* [`streamlit_chatbot.py`](./streamlit_chatbot.py)
  * Langflow API is integrated to a better ui and deployable chatbot
  * Contains basic data visualization.

## Outputs:
Langflow Flow:
1. Creating embeddings and storing in AstraDB
![image](https://github.com/user-attachments/assets/9589b41d-9124-4eb4-b9f5-d6c294a1be99)

2. Retrieval and Inference
![image](https://github.com/user-attachments/assets/9ac6ee4c-9312-44df-bb4c-08fe548c8442)

From the Langflow Playground:
![image](https://github.com/user-attachments/assets/fd20df4c-7705-4d6d-bf77-e04167376310)
![image](https://github.com/user-attachments/assets/e010686a-dc10-4acf-8244-3196a426ab47)

From Streamlit Chatbot:
![image](https://github.com/user-attachments/assets/7a519993-6dc4-4652-8cd4-da66ad870ff6)
![image](https://github.com/user-attachments/assets/05023133-d108-4c60-a6eb-c55ada6fcfe7)



## Todo:
- [ ] Adding More Langflow integration
  - [ ] Custom components for data processing
  - [ ] Trying different embedding techniques and models
  - [ ] Real-time data analysis (Streaming API)

- [ ] Expand Bot Features
  - [ ] Multi-platform support
  - [ ] Advanced scheduling
  - [ ] Custom filters

- [ ] Add Visualization Tools
  - [ ] Interactive dashboard to see social media post type,priority etc.
  - [ ] Location-based Trend analysis
