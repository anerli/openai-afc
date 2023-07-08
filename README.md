# openai-afc
OpenAI auto-function-calling. A simple interface to auto-magically having GPT call your Python functions.

## Install
```sh
git clone https://github.com/anerli/openai-afc.git
cd openai-afc
pip install .
```
> You need openai as a dependency

## Example
```python
# examples/addition.py
from openai_afc import AutoFnChatCompletion, AutoFnDefinition, AutoFnParam

def add(x, y):
    print(f'Adding {x} and {y}')
    return x + y

completion = AutoFnChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "What is 42 + 99?"}
        ],
        functions=[
            AutoFnDefinition(
                add,
                description='Add two numbers',
                params=[
                    AutoFnParam('x', {'type': 'number'}),
                    AutoFnParam('y', {'type': 'number'})
                ]
            )
        ],
        temperature=0.0
    )
# This completion response is of the same form you would get from openai.ChatCompletion
print(completion['choices'][0]['message']['content'])
```

In this example, GPT will use the `add` function in order to compute `42 + 99`, and then will return a textual interpretation of that response to the user:

```
> python3 addition.py
Adding 42 and 99
42 + 99 equals 141.
```

## Overview

Basically, this is a wrapper for the openai-python ChatCompletion. Instead of providing function schemas and handling the logic for triggering those functions, you give AutoFnChatCompletion the usual parameters that you would pass to ChatCompletion, but you pass actual function implementations that GPT will be able to trigger. The completion result you get will always be an "assistant" response, not a function call. The function calls happen automatically based on the passed function references, via a back-and-forth with GPT resolving each call.

> Since multiple (potentially very many or 'infinite') function calls may be made by GPT, keep in mind when you use AutoFnChatCompletion it could use an arbitrary number of calls to OpenAI, so be careful of your usage.
