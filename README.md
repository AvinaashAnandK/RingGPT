# RingGPT

RingGPT enables users to iterate on a corpus to perform single-shot completion tasks using GPT-3.5, Bard, and Bing Chat. Whether you're looking to summarize text, classify data, or perform named entity recognition, RingGPT has got you covered.

## Table of Contents
- [Key Features](#key-features)
- [Supported Zero-Shot Completion Tasks](#supported-zero-shot-completion-tasks)
- [Ring's Settings](#rings-settings)
- [Installation](#installation)
- [Sample Implementation: Named Entity Recognition](#sample-implementation-named-entity-recognition)
- [Prompt Objects for Other Tasks](#prompt-objects-for-other-tasks)
- [Copyright](#copyright)
- [Legal Notice](#legal-notice)

## Key Features

- **Multiple Language Model Support**: Seamlessly interact with models like OpenAIChat, BardChat, and EdgeChat.
- **Dynamic Prompt Generation**: Craft structured prompts tailored to specific tasks.
- **Efficient Data Processing**: Load, chunk, and process data for optimal language model interactions.
- **Error Handling & Retries**: Resilient request handling with built-in retries.
- **Logging**: Trace RingGPT's actions with detailed logs.

## Supported Zero-Shot Completion Tasks

1. **Unstructured to Structured**: Extract specific attributes from unstructured text.
2. **Summarise**: Generate concise summaries of provided text.
3. **Classification**: Classify text into predefined categories.
4. **Named Entity Recognition**: Identify and categorize entities within the text.

## Ring's Settings

- **llm_list**: A list of dictionaries specifying the language models to be used. Each dictionary should contain the service name, access token, and an identifier.
- **max_attempts**: Maximum number of retries for each request.
- **retry_delay**: Time (in seconds) to wait between retries.
- **throttle_delay**: Time (in seconds) to wait between requests.
- **log_enabled**: Enable or disable logging.
- **wip_save**: Save the work-in-progress data.

**_Obtaining Access Tokens_**
_BardGPT_
  Authentication
  Go to https://bard.google.com/
  F12 for console
  Copy the values
  Session: Go to Application → Cookies → __Secure-1PSID and __Secure-1PSIDTS. Copy the value of those cookie.

_GPT 3.5_
  Access token
  https://chat.openai.com/api/auth/session
  ```
  {
    "access_token": "<access_token>"
  }
  ```

## Installation:
To get started with RingGPT, ensure you have Python 3.9 or above. Install the package using pip:

```
pip install ringgpt
```

## Sample Implementation: Named Entity Recognition
**Import Classes:**
```
from ringgpt import DataLoader, Prompt, Ring
```

**Define Data:**
```
file = [
    "...",  # Your data here
]
```

**Initialize DataLoader:**
```
data = DataLoader(file=file)
```

**Define Task & Categories:**
```
task = "Named Entity Recognition"
categories = ["Location"]
prompt = Prompt(instruction=task, instruction_categories=categories)
```

**Define Language Models & Access Tokens:**
```
list_test = [
    {"service": "OpenAIChat", "access_token": "<ACCESS_TOKEN>", "identifier": "TEST_USER"},
    {"service": "BardChat", "access_token": "<ACCESS_TOKEN>", "identifier": "TEST_USER"},
    {"service": "EdgeChat"}
]
attempts = 10
delay = 5
throttle = 4
```

**Initialize Ring & Run:**
```
ner_model = Ring(
    llm_list=list_test,
    max_attempts=attempts,
    retry_delay=delay,
    throttle_delay=throttle,
    log_enabled=True,
    wip_save=True,
    prompt=prom,
    data_loader=data
)
await ner_model.run()
```

## Prompt Objects for Other Tasks
**Unstructured to Structured:**
```
task = "Unstructured to Structured"
categories = ["Addressee", "Key Points of Regulatory Notification", "Subject Matter"]
prom = Prompt(instruction=task, instruction_categories=categories)
```

**Summarize:**
```
task = "Summarise"
prom = Prompt(instruction=task)
```

**Classification:**
```
task = "Classification"
categories = ["Positive", "Negative", "Neutral"]
prom = Prompt(instruction=task, instruction_categories=categories)
```

## Copyright
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

## Legal Notice

This repository is _not_ associated with or endorsed by providers of the APIs contained in this GitHub repository. This project is intended **for educational purposes only**. This is just a little personal project. Sites may contact me to improve their security or request the removal of their site from this repository.

Please note the following:

1. **Disclaimer**: The APIs, services, and trademarks mentioned in this repository belong to their respective owners. This project is _not_ claiming any right over them nor is it affiliated with or endorsed by any of the providers mentioned.

2. **Responsibility**: The author of this repository is _not_ responsible for any consequences, damages, or losses arising from the use or misuse of this repository or the content provided by the third-party APIs. Users are solely responsible for their actions and any repercussions that may follow. We strongly recommend the users to follow the TOS of the each Website.

3. **Educational Purposes Only**: This repository and its content are provided strictly for educational purposes. By using the information and code provided, users acknowledge that they are using the APIs and models at their own risk and agree to comply with any applicable laws and regulations.

4. **Indemnification**: Users agree to indemnify, defend, and hold harmless the author of this repository from and against any and all claims, liabilities, damages, losses, or expenses, including legal fees and costs, arising out of or in any way connected with their use or misuse of this repository, its content, or related third-party APIs.

5. **Updates and Changes**: The author reserves the right to modify, update, or remove any content, information, or features in this repository at any time without prior notice. Users are responsible for regularly reviewing the content and any changes made to this repository.
