
class OpenAIClientWrapper:
    def __init__(self, client):
        self.client = client

    def get_structured_response(self, system: str, user: str, model: str, schema_model):
        print("Using wrapped client to get structured response")
        response = self.client.responses.parse(
            model=model,
            input=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            text_format=schema_model,
        )
        return response.output[0].content[0].parsed
