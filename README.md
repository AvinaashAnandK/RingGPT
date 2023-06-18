[tool.poetry]
name = "ringgpt"
version = "0.1.14"
description = "Package enables users to iterate on a corpus to perform single shot completion tasks leveraging GPT-3.5, Bard and Bing Chat"
authors = ["Avinaash Anand K <avinaash96@gmail.com>"]
license = "Apache-2.0"
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.9"
pandas = "^2.0.2"
GoogleBard = "^1.3.2"
asyncio = "^3.4.3"
EdgeGPT = "0.5.0"
revChatGPT = "^6.3.3"
requests = "^2.31.0"
rich = "^13.4.2"
langchain = "^0.0.203"
tiktoken = "^0.4.0"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
