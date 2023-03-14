import xml.etree.ElementTree as ET
import logging as lg
import pprint as pp

#parse xml files
gold_tree = ET.parse('GOLD_file.xml')
test_tree = ET.parse('test.xml')
sample_tree = ET.parse('sample_1.xml')
gold_root = gold_tree.getroot()
test_root = test_tree.getroot()
sample_root = sample_tree.getroot()

#step 3
empty_tags = []
for test_ch in test_root.iter():
    if test_ch.text == None:
        empty_tags.append(test_ch.tag)       
for tags in empty_tags:
    print("ERROR REPORT: TAGS WITH NO DATA: " + tags)


'''
This recursion function takes one parameter, it gets the length of the xml file and does a loop within that range. if the tag is found, it will append the .text from that tag to a list called "text". If it finds a tag that has children (this is static for the moment) then it will run the recrsion on with that section of the xml as the new parameter, it will run through the whole function again. 

The plan is to append all the values that come out of this function to a list, then do the same by plugging in the other xml file as the parameter, then comparing the lists to see if they all have the same values. 
'''
        
        
def recursion_xml(current_node):
    text = []
    current_file_length = len(current_node)
    for n in range(current_file_length):
        #trying to find any nodes that have nested elements
        if len(current_node[n]) > 0:
            #only returns Client and Job, skips over Compensation for some reason
            parent = current_node[n]
            text.append(recursion_xml(parent))
        if len(current_node[n]) == 0:
            text.append(current_node[n].tag)
    
    return text

# print(recursion_xml(gold_root))
print(recursion_xml(test_root))

#its putting nested nodes in a nested list