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
  * Generated data through this and RLHFed through the claude-model.

* [`social-media-engagement_bot.json`](./social-media-engagement_bot.json)
  * JSON file of the langflow workflow
  * Contains all the settings for automated data retrieval and insight generation

* [`langflow_code.py`](./langflow_code.py)
  * Langflow python library code
  * Created for more granular tweaking of components, and deploying on cloud.

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
