from langflow.load import run_flow_from_json

TWEAKS = {
  "ChatInput-OL5eo": {
    "background_color": "",
    "chat_icon": "",
    "files": "",
    "input_value": "hi what is the data all about",
    "sender": "User",
    "sender_name": "User",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  },
  "ParseData-QCohJ": {
    "sep": "\n",
    "template": "{text}"
  },
  "Prompt-nP9vv": {
    "context": "",
    "question": "",
    "template": "Given the following context and question:\n\nContext: {context}\nQuestion: {question}\n\nBased on the above, analyze the social media engagement data and generate insights in the following format:\n\nMETRICS OVERVIEW\n- Total posts analyzed: [number]\n- Content types: [list types]\n- Timeframe: [period]\n\nPERFORMANCE BY TYPE\n[For each content type (carousel, reels, static)]\n- Engagement rate: [%]\n- Likes avg: [number]\n- Comments avg: [number]\n- Shares avg: [number]\n- Comparison to baseline: [±%]\n\nKEY INSIGHTS\n- List 3 main findings comparing content types\n- Express differences in % or multipliers\n- Example: \"Reels drive 2x more comments than static posts\"\n\nRECOMMENDATIONS\n- Best performing content type: [type]\n- Primary recommendation: [1-2 sentences]\n\nConsider the specific details provided in {context} and answer the {question} while following these requirements:\n- Round all numbers to 2 decimals\n- Compare performance between types\n- Focus on most significant patterns\n- Provide actionable conclusions based on the given context"
  },
  "SplitText-3BxkL": {
    "chunk_overlap": 100,
    "chunk_size": 500,
    "separator": "\n"
  },
  "ChatOutput-qYWi4": {
    "background_color": "",
    "chat_icon": "",
    "data_template": "{text}",
    "input_value": "",
    "sender": "Machine",
    "sender_name": "AI",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  },
  "AstraDB-IExwM": {
    "advanced_search_filter": "{}",
    "api_endpoint": "https://26321830-4a3c-44f5-91f9-feeacba121c2-us-east1.apps.astra.datastax.com",
    "batch_size": None,
    "bulk_delete_concurrency": None,
    "bulk_insert_batch_concurrency": None,
    "bulk_insert_overwrite_concurrency": None,
    "collection_indexing_policy": "",
    "collection_name": "engagementvectordb3",
    "embedding_choice": "Embedding Model",
    "keyspace": "",
    "metadata_indexing_exclude": "",
    "metadata_indexing_include": "",
    "metric": "cosine",
    "number_of_results": 4,
    "pre_delete_collection": False,
    "search_filter": {},
    "search_input": "",
    "search_score_threshold": 0,
    "search_type": "Similarity",
    "setup_mode": "Sync",
    "token": "ASTRA_DB_APPLICATION_TOKEN"
  },
  "AstraDB-vKclI": {
    "advanced_search_filter": "{}",
    "api_endpoint": "https://26321830-4a3c-44f5-91f9-feeacba121c2-us-east1.apps.astra.datastax.com",
    "batch_size": None,
    "bulk_delete_concurrency": None,
    "bulk_insert_batch_concurrency": None,
    "bulk_insert_overwrite_concurrency": None,
    "collection_indexing_policy": "",
    "collection_name": "engagementvectordb3",
    "embedding_choice": "Embedding Model",
    "keyspace": "",
    "metadata_indexing_exclude": "",
    "metadata_indexing_include": "",
    "metric": "cosine",
    "number_of_results": 4,
    "pre_delete_collection": False,
    "search_filter": {},
    "search_input": "",
    "search_score_threshold": 0,
    "search_type": "Similarity",
    "setup_mode": "Sync",
    "token": "ASTRA_DB_APPLICATION_TOKEN"
  },
  "File-7ORDQ": {
    "concurrency_multithreading": 4,
    "path": "engagement-dataset-1-cropped.json",
    "silent_errors": False,
    "use_multithreading": False
  },
  "GoogleGenerativeAIModel-ImQaw": {
    "google_api_key": "",
    "input_value": "",
    "max_output_tokens": None,
    "model": "gemini-1.5-pro",
    "n": None,
    "stream": False,
    "system_message": "",
    "temperature": 0.1,
    "top_k": None,
    "top_p": None
  },
  "AIMLEmbeddings-Be3Vo": {
    "aiml_api_key": "84677b294ad84ccb9fba0d86b247ef11",
    "model_name": "text-embedding-ada-002"
  },
  "AIMLEmbeddings-WfKFT": {
    "aiml_api_key": "84677b294ad84ccb9fba0d86b247ef11",
    "model_name": "text-embedding-ada-002"
  },
  "GoogleGenerativeAIModel-UMM0F": {
    "google_api_key": "AIzaSyANHKAf8lcA_vV39TxQAdjZRGacJza-T3A",
    "input_value": "",
    "max_output_tokens": None,
    "model": "gemini-1.5-pro",
    "n": None,
    "stream": False,
    "system_message": "",
    "temperature": 0.1,
    "top_k": None,
    "top_p": None
  }
}

result = run_flow_from_json(flow="social-media-engagement_bot.json",
                            session_id="", # provide a session id if you want to use session state
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)