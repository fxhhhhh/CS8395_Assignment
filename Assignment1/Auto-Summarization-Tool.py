import streamlit as st
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)
from langchain.document_loaders import *
from langchain.chains.summarize import load_summarize_chain
import tempfile
from langchain.docstore.document import Document
from langchain.document_loaders import TextLoader

st.title('Auto Summarization Tool')

def load_document(file_path):
    loader = TextLoader(file_path)
    docs = loader.load()
    return docs

def summarize_document(docs):
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k")
    chain = load_summarize_chain(llm, chain_type="stuff")
    return chain.run(docs)

def display_summary(summary):
    if summary:
        st.markdown(f"**Summary of the Document:** {summary}")
    else:
        st.markdown("No summary available. Please upload a valid document.")

uploaded_file = st.file_uploader("Upload your research paper or article", type=["txt", "pdf", "docx"])

if 'file_path' not in st.session_state:
    st.session_state['file_path'] = None

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        st.session_state['file_path'] = temp_file.name

if st.button('Generate Summary'):
    if st.session_state['file_path']:
        document = load_document(st.session_state['file_path'])
        if document:
            summary = summarize_document(document)
            display_summary(summary)
        else:
            st.markdown("No document available. Please upload a valid document.")
    else:
        st.markdown("No file uploaded. Please upload a valid document.")