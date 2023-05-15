- [ChatGPT plugins](https://openai.com/blog/chatgpt-plugins)
- [ChatGPT plugins Doc](https://platform.openai.com/docs/plugins/introduction)
- [OpenAPI Specification](https://swagger.io/specification)


## Plugin development

```bash
[plugin-repo]
|- main.py
|- manifest.json
|- openapi.yaml
|- logo.png
`- ... # other
```

### manifest.json

[plugin-manifest](https://platform.openai.com/docs/plugins/getting-started/plugin-manifest): Every plugin requires a ai-plugin.json file, which needs to be hosted on the API’s domain.

### openapi.yaml

[openapi-definition](https://platform.openai.com/docs/plugins/getting-started/openapi-definition): OpenAPI specification to document the API. The model in ChatGPT does not know anything about your API other than what is defined in the OpenAPI specification and manifest file. This means that if you have an extensive API, you need not expose all functionality to the model and can choose specific endpoints.

## Plugin Deploy (Replit)

- Open [Replit](https://replit.com) and click the `Create Repl` button.
- When the pop-up window appears, click the `Import from GitHub` button in the top right corner.
- In the GitHub URL field, enter `https://github.com/mirage-studio-io/chat-currency-converter-plugin` and select `Python` as the language.
- Then click the `Import from GitHub` button in the bottom right corner and wait for the initialization to complete.
- Click the `Run` button and wait for the execution to finish.

<!-- ## Local Development

```bash
# install dependencies
poetry install

# run the service
poetry run python main.py
``` -->

## CURRENCY CONVERTER API

### Convert Currency
```bash
curl -X GET http://0.0.0.0:5002/convert \
 -H 'Content-Type: application/json' \
 -d '{"from_currency": "USD", "to_currency": "EUR", "amount": 100}'
```


MIT License - Mirage Studio
