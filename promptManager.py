# from section_manager import SectionManager
from utils.file_manager import FileManager


class PromptManager:
    def __init__(self):
        self.prompts = []


    def read(self, file_name):
        content = FileManager.read(self, file_name)
        print(content)
        return content

    def write(self, file_name, content):
        FileManager.append_file(self, file_name, content)


    def token_to_dict(self, tokens, section_name):
        from section_manager import SectionManager

        section_manager = SectionManager()
        token_array = tokens.split("--")
        section_data = ""
        if section_name == "pricing":
            section_data = section_manager.pricing_section_generator(token_array)
        elif section_name == "hero":
            section_data = section_manager.hero_section_generator(token_array)
        elif section_name == "benefits":
            section_data = section_manager.benefits_section_generator(token_array)
        elif section_name == "features":
            section_data = section_manager.feature_section_generator(token_array)
        elif section_name == "faq":
            print("generating faqs ... ")
            section_data = section_manager.faq_section_generator(tokens)
        return section_data





if __name__ == "__main__":
    from section_manager import SectionManager
    promptManager = PromptManager()
    section_manager = SectionManager()
    # c = promptManager.read('prompts/init.md')
    # promptManager.write('res.md', c)
    sample = promptManager.read("res.md")
    d = promptManager.token_to_dict(sample, "pricing")
    # s = pricing_section_generator(d)
    print(d)
