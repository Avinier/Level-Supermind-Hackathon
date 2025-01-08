# Social Media Engagement Analysis

A RAG Chatbot made with Langflow and AstraDB, deployed with Docker, for the Level Supermind Hackathon Assignment.
### Made By: Team Byters

### Main Files
* [`engagement-dataset-1.json`](./engagement-dataset-1.json)
  * JSON dataset with all our engagement metrics
  * Contains likes, shares, comments data
  * Used as the main input for analysis

* [`generate_dataset.py`](./generate_dataset.py)
  * Main Python script for data generation
  * Handles all the data processing
  * Run this to collect new data

* [`social-media-engagement_bot.json`](./social-media-engagement_bot.json)
  * Bot configuration file
  * Contains all the settings for automated data collection
  * Edit this to customize what data gets collected

## Todo:
- [ ] Add Langflow integration
  - [ ] Custom components for data processing
  - [ ] Visual workflow builder
  - [ ] Real-time data analysis

- [ ] Expand Bot Features
  - [ ] Multi-platform support
  - [ ] Advanced scheduling
  - [ ] Custom filters

- [ ] Add Visualization Tools
  - [ ] Interactive dashboard to see social media post type,priority etc.
  - [ ] Location-based Trend analysis
