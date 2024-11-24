import sys
import os
import gradio as gr

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import ArgumentParser, ConfigLoader, LOG
from model import GLMModel, OpenAIModel
from translator import PDFTranslator


def initialize_translator():
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

    global Translator
    Translator = PDFTranslator(model_name)

def translation(input_file):
    # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
    print(input_file.name)
    output_file_path = input_file.name
    #output_file_path = Translator.translate_pdf(input_file.name)
    return output_file_path

def launch_gradio():
    demo = gr.Interface(
        fn=translation, 
        inputs=gr.File(label="上传文件"),
        outputs=gr.File(label="下载翻译文件"),
        allow_flagging="never"
    )
        
    demo.launch(share=True, server_name="0.0.0.0")

initialize_translator()
launch_gradio()