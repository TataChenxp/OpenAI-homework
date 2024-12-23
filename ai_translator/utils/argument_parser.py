import argparse

class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Translate English PDF book to Chinese.')
        self.parser.add_argument('--book', type=str, required=False, help='PDF file to translate.')
        self.parser.add_argument('--config', type=str, default='config.yaml', required=False, help='Configuration file with model and API settings.')
        self.parser.add_argument('--model_type', type=str, default="OpenAIModel", required=False, choices=['GLMModel', 'OpenAIModel'], help='The type of translation model to use. Choose between "GLMModel" and "OpenAIModel".')        
        #self.parser.add_argument('--glm_model_url', type=str,required=False, help='The URL of the ChatGLM model URL.')
        #self.parser.add_argument('--timeout', type=int, default=300, required=False, help='Timeout for the API request in seconds.')
        #self.parser.add_argument('--openai_model', type=str, default="gpt-3.5-turbo", required=False, help='The model name of OpenAI Model. Required if model_type is "OpenAIModel".')
        #self.parser.add_argument('--openai_api_key', type=str, required=False, help='The API key for OpenAIModel. Required if model_type is "OpenAIModel".')
        #self.parser.add_argument('--file_format', type=str, default="markdown", required=False, help='The file format of translated book. Now supporting PDF and Markdown')

    def parse_arguments(self):
        args = self.parser.parse_args()
        return args
