import sys

from model_manager import ModelManager
from promptManager import PromptManager
from section_manager import SectionManager
from utils.file_manager import FileManager


def main():
    print("Welcome!!!")
    input_listener("flash")

def input_listener(model_type=None):
    model = ModelManager()
    prev_prompt = ""

    if model_type is not None:
        # TODO: set explicit types like flash and pro
        model.set_model(model_type)

    print("What kind of landing page would you like to create today?")
    print("\nexample: Create a landing page for a fitness center")
    print("\nYou can also always enter exit to exit the program")


    while True:
        user_input = input("> ")

        if user_input.lower() == "exit":
            print("Exiting...")
            sys.exit()
        elif user_input == "retry":
            print("Retrying...")
            generate_sections(prev_prompt)
        elif user_input != "":
            print("Valid")
            user_prompt = user_input
            prev_prompt = user_prompt
            generate_sections(user_prompt)
        else:
            print("Invalid")
            user_prompt = " Create a landing page for a saas application"
            prev_prompt = user_prompt
            generate_sections(user_prompt)

def generate_sections(user_input):
    promptManager = PromptManager()
    file_manager = FileManager()
    section_manager = SectionManager()
    model = ModelManager()

    sections = ["hero", "benefits", "pricing", "features", "faq", "testimonials"]


    init_prompt = promptManager.read('prompts/init.md')
    user_prompt = user_input

    model.generate(init_prompt + user_prompt)

    data = section_manager.get_section_data(sections)


    json_str = file_manager.dict_to_json(data)
    # json_str = file_manager.clean_json(json_str)

    # print(json_str)
    # model.write_res(json_str)
    file_manager.update_page_content(json_str)



if __name__ == "__main__":
    main()