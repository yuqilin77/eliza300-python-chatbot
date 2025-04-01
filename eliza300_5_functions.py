
from eliza300_5_runtime_data import key_words

def get_complaint_type(user_complaint):
        observed_complaint_type = set()
        for words in key_words:
                index = key_words.index(words)
                for word in words:
                        if word in user_complaint.lower():
                                observed_complaint_type.add(index)
                                break;
        return observed_complaint_type
                                
