import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import ArgumentParser, ConfigLoader, LOG
from model import GLMModel, OpenAIModel
from translator import PDFTranslator

if __name__ == "__main__":
    argument_parser = ArgumentParser()
    args = argument_parser.parse_arguments()
    config_loader = ConfigLoader(args.config)

    config = config_loader.load_config()
    LOG.info(f"Config: {config}")

    model_name = config['OpenAIModel']['model']
    api_key = config['OpenAIModel']['api_key']
    base_url = config['OpenAIModel']['base_url']
    if args.model_type == 'OpenAIModel' and (not model_name or not api_key):
        LOG.error("--openai_model and --openai_api_key is required when using OpenAIModel")
    
    os.environ["OPENAI_API_KEY"] = api_key
    os.environ["OPENAI_BASE_URL"] = base_url
    
    model = OpenAIModel(model=model_name, api_key=api_key)

    pdf_file_path = config['common']['book']
    file_format = config['common']['file_format']

    # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
    translator = PDFTranslator(model)
    translator.translate_pdf(pdf_file_path, file_format)
