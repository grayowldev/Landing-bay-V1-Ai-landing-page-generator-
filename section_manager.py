from model_manager import ModelManager
from promptManager import PromptManager


class SectionManager:

    def __init__(self):
        self.section = ""

    def hero_section_generator(self, raw_data):
        res  = {}
        res["heading"] = raw_data[0].strip()
        res["subheading"] = raw_data[1].strip()
        return res

    def benefits_section_generator(self, raw_data):
        print("!!!!!!!!!!!!!")
        print(raw_data)
        res = {}
        res["title"] = raw_data[0].strip()
        res["benefits"] = [item.strip() for item in raw_data[1:]]
        return res

    def action_call_section_generator(self, raw_data):
        pass

    def faq_section_generator(self, raw_data):
        pass

    def feature_section_generator(self, raw_data):
        res = {}
        res["title"] = raw_data[0].strip()
        res["features"] = [item.strip() for item in raw_data[1:]]
        return res

    def footer_section_generator(self, raw_data):

        pass

    def pricing_section_generator(self, raw_data):
        print("^^^^^^^^^^^^")
        print(raw_data)
        res = {}
        print(raw_data[0])
        try:
            res["title"] = raw_data[0].split(":")[1].strip()
        except:
            res["title"] = raw_data[0].strip()
        r_categories = raw_data[1].split("{")
        categories = []

        for cat in r_categories[1:]:
            category = {}
            slice = cat.split("[")
            info = slice[0]
            features = slice[1]
            category["name"] = info.split(":")[1].split("**")[0].strip()
            category["price"] = info.split(":")[2].split("**")[0].strip()
            category["features"] = [item.strip() for item in features.strip().split("]")[0].split("**")]
            categories.append(category)

        res["categories"] = categories
        return res

    def testimonials_section_generator(self, raw_data):
        pass

    def get_section_data(self, sections_array):
        model = ModelManager()
        promptManager = PromptManager()
        res = {}

        # section prompts path
        hero_path = "prompts/hero-section.md"
        benefits_path = "prompts/benefits-section.md"
        pricing_path = "prompts/pricing-section.md"
        features_path = "prompts/feature-section.md"

        for section in sections_array:
            print(section)
            if section == "hero":
                prompt = promptManager.read(hero_path)
                pass
            elif section == "benefits":
                prompt = promptManager.read(benefits_path)
                pass
            elif section == "pricing":
                prompt = promptManager.read(pricing_path)
                pass
            elif section == "features":
                prompt = promptManager.read(features_path)
                pass
            else:
                return None

            tokens = model.generate(prompt)
            if section == "benefits":
                print(">>>>>>>>>")
                print(tokens)
            data = promptManager.token_to_dict(tokens, section)
            res[section] = data

        return res

    def set_section(self, section):
        self.section = section

