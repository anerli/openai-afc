class AutoFnParam():
    def __init__(self, name: str, schema: dict, required: bool = True):
        '''
        name: Name of the parameter. This should be the same as the name of the parameter
            in the corresponding Python function.
        schema: JSON Schema which GPT will try to follow when providing this parameter's value
        required: Whether GPT will see this parameter as required or not.
        '''
        self.name = name
        self.schema = schema
        self.required = required
