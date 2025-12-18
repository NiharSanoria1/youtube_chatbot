import streamlit as st
import atexit

from src.backend.yt_chatbot import generating_embedding, get_ans
from src.backend.langchain_pinecone import deleting_all_vectors

INDEX_NAME = "yt-embeddings2"

# -------------------------------
# Automatic cleanup on app exit
# -------------------------------
def cleanup_vectors():
    try:
        deleting_all_vectors(INDEX_NAME)
        print("✅ Pinecone vectors cleaned up on exit")
    except Exception as e:
        print("⚠️ Cleanup failed:", e)

atexit.register(cleanup_vectors)

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(
    page_title="YouTube Chatbot",
    page_icon="🎥",
    layout="centered"
)

st.title("🎥 YouTube Video Q&A Chatbot")
st.write("Ask questions directly from a YouTube video's transcript.")

# -------------------------------
# Session state
# -------------------------------
if "embedded" not in st.session_state:
    st.session_state.embedded = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -------------------------------
# Inputs
# -------------------------------
video_url = st.text_input(
    "📎 Enter YouTube Video URL",
    placeholder="https://www.youtube.com/watch?v=xxxx"
)

user_question = st.text_input(
    "❓ Ask a question about the video",
    placeholder="What is the video mainly about?"
)

# -------------------------------
# Ask Question
# -------------------------------
if st.button("Ask Question"):
    if not video_url or not user_question:
        st.warning("Please enter both video URL and a question.")
    else:
        with st.spinner("Processing..."):
            # Generate embeddings only once
            if not st.session_state.embedded:
                generating_embedding(video_url)
                st.session_state.embedded = True

            answer = get_ans(video_url, user_question)

            st.session_state.chat_history.append(
                {"question": user_question, "answer": answer.content}
            )

# -------------------------------
# Display Chat History
# -------------------------------
if st.session_state.chat_history:
    st.subheader("💬 Conversation")
    for chat in st.session_state.chat_history:
        st.markdown(f"**You:** {chat['question']}")
        st.markdown(f"**Bot:** {chat['answer']}")
        st.divider()

# -------------------------------
# Clear embeddings manually
# -------------------------------
st.subheader("🧹 Cleanup")

if st.button("Clear Embeddings & Reset"):
    with st.spinner("Deleting embeddings..."):
        deleting_all_vectors(INDEX_NAME)
        st.session_state.embedded = False
        st.session_state.chat_history = []
        st.success("All embeddings deleted successfully!")
