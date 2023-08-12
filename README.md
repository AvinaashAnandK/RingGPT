# RingGPT

RingGPT enables users to iterate on a corpus to perform single-shot completion tasks using GPT-3.5, Bard, and Bing Chat. Whether you're looking to summarize text, classify data, or perform named entity recognition, RingGPT has got you covered.

## Key Features:

- **Multiple Language Model Support**: Seamlessly interact with models like OpenAIChat, BardChat, and EdgeChat.
- **Dynamic Prompt Generation**: Craft structured prompts tailored to specific tasks.
- **Efficient Data Processing**: Load, chunk, and process data for optimal language model interactions.
- **Error Handling & Retries**: Resilient request handling with built-in retries.
- **Logging**: Trace RingGPT's actions with detailed logs.

## Supported Zero-Shot Completion Tasks:

1. **Unstructured to Structured**: Extract specific attributes from unstructured text.
2. **Summarise**: Generate concise summaries of provided text.
3. **Classification**: Classify text into predefined categories.
4. **Named Entity Recognition**: Identify and categorize entities within the text.

## Ring's Settings:

- **llm_list**: A list of dictionaries specifying the language models to be used. Each dictionary should contain the service name, access token, and an identifier.
- **max_attempts**: Maximum number of retries for each request.
- **retry_delay**: Time (in seconds) to wait between retries.
- **throttle_delay**: Time (in seconds) to wait between requests.
- **log_enabled**: Enable or disable logging.
- **wip_save**: Save the work-in-progress data.

## Installation:
To get started with RingGPT, ensure you have Python 3.9 or above. Install the package using pip:
```bash
pip install ringgpt'''

## Sample Implementation: Named Entity Recognition

