import streamlit as st
from ingest import run_ingestion
from src.rag_chain import generate_answer

st.set_page_config(page_title="Aurora Insights", page_icon="📊", layout="wide")
st.title("📊 Aurora Insights")
st.caption("Ask questions about the Aurora Dynamics reports and requirements document.")

with st.sidebar:
    st.header("Knowledge Base")
    if st.button("Build / Refresh Knowledge Base"):
        try:
            with st.spinner("Indexing PDFs..."):
                run_ingestion()
            st.success("Knowledge base ready.")
        except Exception as exc:
            st.error(f"Ingestion failed: {exc}")

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("**Try these questions**")
    st.markdown(
        "- Compare FY2024 and FY2025 revenue.\n"
        "- What was net profit in FY2025?\n"
        "- Which segment grew fastest in FY2025?\n"
        "- How did net debt change?\n"
        "- What does the BRD require?"
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message.get("sources"):
            with st.expander("View sources"):
                for source in message["sources"]:
                    meta = source["metadata"]
                    st.markdown(f"- {meta['source']}, page {meta['page']}")

question = st.chat_input("Ask a question about your PDFs...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        try:
            with st.spinner("Searching documents..."):
                answer, sources = generate_answer(question)
            st.markdown(answer)

            if sources:
                with st.expander("View sources"):
                    for source in sources:
                        meta = source["metadata"]
                        st.markdown(f"- {meta['source']}, page {meta['page']}")

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer,
                "sources": sources,
            })
        except Exception as exc:
            st.error(f"Error: {exc}")
