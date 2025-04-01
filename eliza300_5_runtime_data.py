key_words = []
complaint_types = []

def read_complaint_data():
        data_source = "ElizaData1.txt"
        file = open(data_source,'r')
        line_read =file.readline().rstrip()
        while line_read != '':
                index_of_key = line_read.index("for")
                complaint_types_set = line_read[index_of_key+4:]
                complaint_types.append(complaint_types_set)
                line_read =file.readline().rstrip()
                key_words_set = line_read.split(" ")
                key_words.append(key_words_set)
                line_read =file.readline().rstrip()
        file.close()

