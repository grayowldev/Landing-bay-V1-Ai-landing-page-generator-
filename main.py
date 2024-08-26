import sys

from model_manager import ModelManager
from promptManager import PromptManager
from section_manager import SectionManager
from utils.file_manager import FileManager


def main():
    print("Welcome!!!")
    generate_sections()
    # input_listener("flash")

def input_listener(model_type=None):
    model = ModelManager()

    if model_type is not None:
        # TODO: set explicit types like flash and pro
        model.set_model(model_type)

    while True:
        user_input = input("> ")

        if user_input.lower() == "exit":
            print("Exiting...")
            sys.exit()

        model.generate(user_input)

def generate_sections():
    promptManager = PromptManager()
    file_manager = FileManager()
    section_manager = SectionManager()

    sections = ["hero", "benefits", "pricing", "features", "faq", "testimonials"]

    # , "call-to-action", "features", "testimonials"
    model = ModelManager()
    res_json = {}

    init_prompt = promptManager.read('prompts/init.md')
    user_prompt = " Create a landing page for a saas application"

    model.generate(init_prompt + user_prompt)

    data = section_manager.get_section_data(sections)
    # print(data)


    json_str = file_manager.dict_to_json(data)
    # json_str = file_manager.clean_json(json_str)
    print("vvvvvvvvvvvvv")
    # print(json_str)
    # model.write_res(json_str)
    file_manager.update_page_content(json_str)



if __name__ == "__main__":
    main()