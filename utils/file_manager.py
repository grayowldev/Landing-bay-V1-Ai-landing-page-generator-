import json
import os.path


class FileManager:

    # Read a file
    def read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read()

    #   Write to a file
    def write_file(self, file_name):
        with open(file_name, 'w') as f:
            return f.write()


    #   Update/ append to a file
    def append_file(self, file_name):
        with open(file_name, 'a') as f:
            return f.write()

    # Read a file then append to it
    def read_write_file(self, file_name):
        with open(file_name, 'r+') as f:
            return f.read()



    def clean_json(self, json_file):
        content = json_file.strip("```json").strip("```").strip()
        return content

    def dict_to_json(self,data):
        json_string = json.dumps(data, indent=4)
        return json_string

    def string_to_json(self,string):
        string = self.clean_json(string)
        print("String to convert to json", string)
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