import xml.etree.ElementTree as ET
import logging as lg
import pprint as pp
#step 1: get all the tags out of each xml using findall()
#step 2: make sure both have the same tags
#step 3: make sure all the tags have data



#parse xml files
gold_tree = ET.parse('GOLD_file.xml')
test_tree = ET.parse('test.xml')
gold_root = gold_tree.getroot()
test_root = test_tree.getroot()

print(gold_root.tag)
#step 1
# for i in gold_root.iter(): 
#     print(i)
# for j in test_root.iter():
#     print(j)

#step 3
empty_tags = []
for test_ch in test_root.iter():
    if test_ch.text == None:
        empty_tags.append(test_ch.tag)
        
for tags in empty_tags:
    print("ERROR REPORT: TAGS WITH NO DATA: " + tags)






def recursion_xml(file):
    text = ""
    current_file_length = len(file)
    print(file, current_file_length)
    for i in range(current_file_length):
        if file[i].tag == "Client":
            print("Client checked")
            parent = file[i]
            text += recursion_xml(parent)
        elif file[i].tag == "Job":
            print("Job checked")
            parent = file[i]
            text += recursion_xml(parent)
            #not sure how to check double nested elements.
        # elif file[i].tag == "Comepensation":
        #     print("Comp checked")
        #     parent = file[i]
        #     print(parent)
        #     text += recursion_xml(parent)
        elif file[i] == "Type":
            print("Type checked")
            text += "{} ".format(file[i].text)
    return text

recursion_xml(gold_root)
