import streamlit as st
import os
from dotenv import load_dotenv

from langflow import load_flow_from_json


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
    "token": os.getenv("ASTRA_DB_APPLICATION_TOKEN")
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
    "token": os.getenv("ASTRA_DB_APPLICATION_TOKEN")
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
    "aiml_api_key": os.getenv("AIML_API_KEY"),
    "model_name": "text-embedding-ada-002"
  },
  "AIMLEmbeddings-WfKFT": {
    "aiml_api_key": os.getenv("AIML_API_KEY"),
    "model_name": "text-embedding-ada-002"
  },
  "GoogleGenerativeAIModel-UMM0F": {
    "google_api_key": os.getenv("GOOGLE_API_KEY"),
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

SAMPLE_DATA = {
    "posts": [
        {
            "post_id": "P030",
            "post_type": "static",
            "created_at": "2024-01-30T17:00:00.000Z",
            "engagement": {
                "likes": 917,
                "comments": 40,
                "shares": 21,
                "saves": 64,
                "reach": 8367,
                "impressions": 10570
            }
        },
        {
            "post_id": "P031",
            "post_type": "carousel",
            "created_at": "2024-01-31T15:00:00.000Z",
            "engagement": {
                "likes": 922,
                "comments": 78,
                "shares": 35,
                "saves": 103,
                "reach": 15272,
                "impressions": 21751
            }
        },
        {
            "post_id": "P032",
            "post_type": "carousel",
            "created_at": "2024-02-01T12:00:00.000Z",
            "engagement": {
                "likes": 1081,
                "comments": 83,
                "shares": 42,
                "saves": 100,
                "reach": 13819,
                "impressions": 16903
            }
        },
        {
            "post_id": "P033",
            "post_type": "static",
            "created_at": "2024-02-02T10:00:00.000Z",
            "engagement": {
                "likes": 896,
                "comments": 43,
                "shares": 22,
                "saves": 62,
                "reach": 10636,
                "impressions": 14670
            }
        }
    ]
}

# Page config
st.set_page_config(
    page_title="Team Byters Chat",
    page_icon="💭",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    * {
        font-family: 'Poppins', sans-serif !important;
    }

    .main {
        background: #1E1E1E;
    }

    .block-container {
        max-width: 1200px;
    }

    h1 {
        color: white !important;
        font-weight: 600 !important;
        text-align: center !important;
        padding: 1rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }

    .chat-container {
        display: flex;
        margin: 10px auto;
        padding: 0 20px;
        max-width: 800px;
    }

    .message-bubble {
        max-width: 70%;
        padding: 15px;
        border-radius: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .user-message {
        margin-right: auto;
        background: linear-gradient(135deg, #FF0080 0%, #FF4D4D 100%);
        color: white;
        border-bottom-left-radius: 5px;
    }

    .assistant-message {
        margin-left: auto;
        background: linear-gradient(135deg, #7928CA 0%, #9C4DFF 100%);
        color: white;
        border-bottom-right-radius: 5px;
    }

    .stButton>button {
        background: linear-gradient(135deg, #FF0080 0%, #7928CA 100%);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 10px;
        font-weight: 500;
    }

    .chart-container {
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
    }

    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Custom input styling */
    .stTextInput>div>div>input {
        background: rgba(255,255,255,0.9);
        border-radius: 10px;
        padding: 0.5rem 1rem;
        border: 1px solid rgba(255,255,255,0.2);
    }
</style>
""", unsafe_allow_html=True)


def create_mini_chart(df, metric):
    """Create a miniaturized chart for a specific metric"""
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('date:N', title=None, axis=alt.Axis(labels=False)),
        y=alt.Y(metric + ':Q', title=None),
        color=alt.value('#FF0080' if metric in ['likes', 'shares'] else '#7928CA'),
        tooltip=['date', metric, 'type']
    ).properties(
        width=100,
        height=60,
        title=metric.capitalize()
    ).configure_view(
        strokeWidth=0
    ).configure_axis(
        grid=False
    )
    return chart


def create_full_chart(df, metric):
    """Create a full-sized chart for a specific metric"""
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('date:N', title='Date', axis=alt.Axis(labelAngle=-45)),
        y=alt.Y(metric + ':Q', title=metric.capitalize()),
        color=alt.value('#FF0080' if metric in ['likes', 'shares'] else '#7928CA'),
        tooltip=['date', metric, 'type']
    ).properties(
        width=250,
        height=150,
        title=f'{metric.capitalize()} per Post'
    ).configure_view(
        strokeWidth=0
    ).configure_axis(
        grid=False
    )
    return chart


def chat(prompt: str):
    with current_chat_message:
        # Block input
        st.session_state.disabled = True

        # Add user message to chat history
        st.session_state.messages.append(("human", prompt))

        # Display user message
        with st.chat_message("human"):
            st.markdown(prompt)

        # Display assistant response
        with st.chat_message("assistant"):
            history = "\n".join([f"{role}: {msg}" for role, msg in st.session_state.messages])
            query = f"{history}\nAI:"
            inputs = {"question": query}

            # Load and run the flow
            flow = load_flow_from_json(flow="social-media-engagement_bot.json", tweaks=TWEAKS)
            output = flow(inputs)

            try:
                output = output['chat_history'][-1].content
            except Exception as e:
                output = f"Application error: {str(e)}\nOutput: {output}"

            placeholder = st.empty()
            with placeholder:
                st.markdown(output)

        # Log AI response
        st.session_state.messages.append(("assistant", output))

        # Enable charts after first exchange
        st.session_state.show_charts = True

        # Unblock chat input
        st.session_state.disabled = False
        st.rerun()


# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "disabled" not in st.session_state:
    st.session_state.disabled = False
if "show_charts" not in st.session_state:
    st.session_state.show_charts = False

st.title("Team Byters: Social Media Engagement Analysis")

# Create layout
if st.session_state.show_charts:
    # Two-column layout
    chat_col, viz_col = st.columns([0.6, 0.4])

    # Chat column
    with chat_col:
        current_chat_message = st.container()
        for role, message in st.session_state.messages:
            with st.chat_message(role):
                st.markdown(message)

    # Visualization column
    with viz_col:
        st.markdown("### 📊 Analytics")
        metrics = ['likes', 'comments', 'shares', 'saves']

        # Create DataFrame
        df = pd.DataFrame([
            {
                'post_id': post['post_id'],
                'date': pd.to_datetime(post['created_at']).strftime('%Y-%m-%d'),
                'type': post['post_type'],
                **post['engagement']
            }
            for post in SAMPLE_DATA['posts']
        ])

        # Display mini charts with expanders
        for metric in metrics:
            with st.expander(f"{metric.capitalize()} Analysis"):
                # Show mini chart
                mini_chart = create_mini_chart(df, metric)
                st.altair_chart(mini_chart, use_container_width=True)

                # Show full chart on demand
                if st.button(f"Expand {metric} chart", key=f"expand_{metric}"):
                    full_chart = create_full_chart(df, metric)
                    st.altair_chart(full_chart, use_container_width=True)
else:
    # Centered single-column layout
    current_chat_message = st.container()
    for role, message in st.session_state.messages:
        with st.chat_message(role):
            st.markdown(message)

# Chat input
prompt = st.chat_input(
    "Ask about your social media data...",
    disabled=st.session_state.disabled
)

if prompt:
    chat(prompt)