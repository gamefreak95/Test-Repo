from typing import List, Dict
class Solution:
    def get_count(self, messages: List[str]) -> Dict[str, int]:
        my_dict = {}

        for line in messages:
            key = line.split(":")[0].strip().lower()
            if key in my_dict:
                my_dict[key] += 1
            else:
                my_dict[key] = 1
        return my_dict

error_list = ["ERROR : this line has an error",
              "error : this line has an error",
              "FATAL : the app has crashed please check",
              "fatal : we have a new message for why the app isnt working",
              "severe : we do not have a good message here for this error",
              "ERROR : this line has an issue listed",
              "SEVERE : this line has a message indicating why we crashed",
              "log : this line has a log that is not useful",
              "ERROR : this line has an issue listed",
              "log : this line has a log message",
              "FATAL : this line has an issue listed",
              "log : this line has a log message",
              "error : this line has an issue listed",
              "log : this line has a log message",
              "error : this line has an issue listed",
              "log : this line has a log message"]

s = Solution()
result = s.get_count(error_list)
print(result)






