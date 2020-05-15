import re

def default_callback(match_tuple, **kwargs):
    print('creator function not defined!')
    quit()

class Regulation():
    def __init__(self, topic_name):
        self.topic_name = topic_name
        self.patterns = []
        self.stamp_msg_callback = default_callback

    def apply(self, text_file):
        match_list = self.__create_match_list__(text_file)
        return self.__create_stamp_msg_list__(match_list)

    def __create_match_list__(self, text_file):
        match_list = []
        for pattern in self.patterns:
            match_list = re.findall(pattern, text_file, flags=re.MULTILINE)
            if(len(match_list) > 0):
                break
        if(0 == len(match_list)):
            print("topic: " + self.topic_name + ' matches nothing!')
        return match_list

    def __create_stamp_msg_list__(self, match_list):
        msg_list = []
        for match in match_list:
            msg_list += [self.stamp_msg_callback(match)]
        return msg_list
        

