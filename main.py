import sys

from model_manager import ModelManager
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
    sections = ["hero", "benefits", "call-to-action", "faq", "features", "testimonials"]
    model = ModelManager()
    res_json = {}

    init_prompt = "With the incoming prompt, we are going to be generating data relevant to the prompt, do not generate anything for now just keep this in mind/n ####"
    user_prompt = "Create a landing page for a fitness application"

    model.generate(init_prompt + user_prompt)
    file_manager = FileManager()
    section_prompt = ""
    section_json = ""

    for section in sections:
        if section == "hero":
            section_prompt = "Okay new we will be creating data relevant to the hero section of the landing page. Create data for the heading, and subheading of the hero section,  and represent it in json format. You must not include any code block formating"
            section_json = model.generate(section_prompt)
        elif section == "benefits":
            section_prompt = ""
            section_json = model.generate(section_prompt)
        elif section == "call-to-action":
            section_prompt = ""
            section_json = model.generate(section_prompt)
        elif section == "faq":
            section_prompt = ""
            section_json = model.generate(section_prompt)
        elif section == "features":
            section_prompt = ""
            section_json = model.generate(section_prompt)

        if section_json:
            res_json[section] = file_manager.string_to_json(section_json)
        else:
            continue

    json_str = file_manager.dict_to_json(res_json)
    json_str = file_manager.clean_json(json_str)
    model.write_res(json_str)
    # file_manager.update_page_content(json_str)



if __name__ == "__main__":
    main()