# # AI Agent in Python

A command-line AI agent built with Python and the <Gemini API / model name you used>. The agent takes a task in natural language and uses tool calls to <describe what it can do, e.g. list files, read files, write files, run Python files> inside a restricted working directory.

Built while completing the "Build an AI Agent in Python" course on boot.dev.

## How it works
```
User prompt → LLM → tool call (<functions>) → result fed back to LLM → final answer
```
- The agent runs in a loop until the model returns a final response
- Tools: `<function names from your code>`
- Safety: <e.g. file access limited to the working directory, max iterations>

## Tech stack
Python, <Gemini API / model>, <other libraries from your requirements>

## Setup
1. `git clone https://github.com/Ashwinkumarv123/Boot_dev_ai`
2. `pip install -r requirements.txt`
3. Create a `.env` file with `<API_KEY_NAME>=your_key`
4. `python main.py "<example prompt>"`

## Example
```
$ python main.py "<example prompt>"
<paste real output>
```
