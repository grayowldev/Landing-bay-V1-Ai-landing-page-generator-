import json
import os.path


class FileManager:

    def clean_json(self, json_file):
        content = json_file.strip("```json").strip("```").strip()
        # with open('res.txt', 'r+') as file:
        #     # Read the current content
        #     content = file.read()
        #
        #     print("----------------------")
        #     print("Current content:", content)
        #     content = content.strip("```json").strip("```").strip()
        #     print("Current content:", content)
        #     print("----------------------")
        #     file.write(content)
        #
        #     file.close()
        return content
        # print("----------------------")
        # print(json_file)
        # print("----------------------")
    def dict_to_json(self,data):
        json_string = json.dumps(data, indent=4)
        return json_string

    def string_to_json(self,string):
        string = self.clean_json(string)
        return json.loads(string)

    def update_page_content(self,content):
        path = os.path.abspath(os.path.join("landing-page/src/app/pageContent.json"))
        print(path)
        with open(path, 'w') as file:
            # Write a string to the file
            file.write(content)
            file.close()

    if __name__ == "__main__":
        clean_json("a", "a")