# Auto Summarization Tool

This repository contains an Auto Summarization Tool built using Python and Streamlit. The tool allows users to upload research papers, articles, or documents in various formats (e.g., txt, pdf, docx) and generates a summary of the document using the GPT-3.5 Turbo language model from OpenAI.

## Getting Started

To use the Auto Summarization Tool, you'll need to set up a Python environment and install the required dependencies. Here are the steps to get started:

### Prerequisites

- Python 3.7 or higher
- [Streamlit](https://streamlit.io/) (for the user interface)
- [LangChain](https://github.com/JustAnotherArchivist/langchain) (a Python library for managing text generation tasks with AI models)
- [OpenAI GPT-3.5 Turbo](https://beta.openai.com/signup/) (for generating document summaries)

### Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/auto-summarization-tool.git
   ```
2. Navigate to the project directory:
    ```bash
   cd auto-summarization-tool
   ```
2. Install the required Python packages using pip
    ```bash
   pip install streamlit langchain
   ```

### Usage

1. Run the Streamlit app by executing the following command:
    ```bash
   streamlit run app.py
   ```
2. The Auto Summarization Tool's user interface will open in your default web browser.

3. Click the "Upload your research paper or article" button to select and upload a document in one of the supported formats (txt, pdf, docx).

4. After uploading the document, click the "Generate Summary" button.

5. The tool will use the GPT-3.5 Turbo model to generate a summary of the document and display it on the screen.

### Customization
You can customize the behavior of the Auto Summarization Tool by modifying the code in the app.py file. For example, you can adjust the model's temperature or choose a different model from OpenAI for summarization.

### Acknowledgments
- This tool was created using Streamlit, LangChain, and the OpenAI GPT-4.0  model.
- Streamlit: https://streamlit.io/
- LangChain: https://github.com/JustAnotherArchivist/langchain
- OpenAI GPT-4.0 : https://beta.openai.com/signup/

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Authors
Cecilia Fu
