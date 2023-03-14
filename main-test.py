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

# print(gold_root)
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
        
# for tags in empty_tags:
#     print("ERROR REPORT: TAGS WITH NO DATA: " + tags)


'''
This recursion function takes one parameter, it gets the length of the xml file and does a loop within that range. if the tag is found, it will append the .text from that tag to a list called "text". If it finds a tag that has children (this is static for the moment) then it will run the recrsion on with that section of the xml as the new parameter, it will run through the whole function again. 

The plan is to append all the values that come out of this function to a list, then do the same by plugging in the other xml file as the parameter, then comparing the lists to see if they all have the same values. 
'''

# def recursion_xml(file):
#     text = ""
#     current_file_length = len(file)
#     for i in range(current_file_length):
#         if file[i].tag == "Id":
#             print("Id checked")
#             text += f"{file[i].text}"
#         if file[i].tag == "Client":
#             print("Client checked")
#             parent = file[i]
#             text += recursion_xml(parent)
#         elif file[i].tag == "Job":
#             print("Job checked")
#             parent = file[i]
#             text += recursion_xml(parent)
#             #not sure how to check double nested elements.
#         # elif file[i].tag == "Comepensation":
#         #     print("Comp checked")
#         #     parent = file[i]
#         #     print(parent)
#         #     text += recursion_xml(parent)
#         elif file[i].tag == "Frequency":
#             #frequency = None
#             print("Frequency checked")
#             text += f" {file[i].text}"
#     return text

# print(recursion_xml(gold_root))

#finds out if there is nested items in the xml
# for i in gold_root.iter():
#     if len(i) > 0:
#         print(i.tag)
        
        
def recursion_xml(current_node):
    text = []
    current_file_length = len(current_node)
    for n in range(current_file_length):
        #trying to find any nodes that have nested elements
        if len(current_node[n]) > 1:
            #only returns Client and Job, skips over Compensation for some reason
            parent = current_node[n]
            text.append(recursion_xml(parent))
        if len(current_node[n]) == 0:
            text.append(current_node[n].tag)
    return text

print(recursion_xml(gold_root))