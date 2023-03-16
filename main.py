import xml.etree.ElementTree as ET
import sys

#could check if the xpaths match?

#parse xml files
gold_tree = ET.parse('GOLD_file.xml')
test_tree = ET.parse('test.xml')
sample_tree = ET.parse('sample_1.xml')
gold_root = gold_tree.getroot()
test_root = test_tree.getroot()

'''
This recursion function takes one parameter, it gets the length of the xml file and does a loop within that range. if the tag is found, it will append the .node_list from that tag to a list called "node_list". If it finds a tag that has children (this is static for the moment) then it will run the recrsion on with that section of the xml as the new parameter, it will run through the whole function again. 

The plan is to append all the values that come out of this function to a list, then do the same by plugging in the other xml file as the parameter, then comparing the lists to see if they all have the same values. 

Make sure MARKET_ID and LETTER_TYPE match

Iterate over all files in database and plugging them into the parameters of the function
'''

'''
This first function is to recursively parse the "gold" xml file, the one that the other files will be compared to.
'''
      
def recursion_xml_1(param):
    param_list = [gold_root, test_root]
    #xpath to the market_id node
    e_gold = gold_root.findall("Market_ID")
    #iterate over the e_gold variable because it is a list
    for i_gold in e_gold:
        #set the term_gold as a global variable so it can be accessed outside of the function
        global term_gold
        term_gold = i_gold.text
        #if the Market_ID from the test.xml and gold.xml do not match, an exception will be raised and the program will stop
    if term_test != term_gold:
        raise Exception("The Market IDs do not match")
    global node_list 
    node_list = []
    current_file_length = len(param)
    for n in range(current_file_length):
        #trying to find any nodes that have nested elements 
        # print("param = ",param[n])
        if len(param[n]) > 0 and param[n].text != None:
            # print("param = ",param[n])
            #only returns Client and Job, skips over Compensation for some reason
            parent = param[n]
            node_list.append(recursion_xml_1(parent))
        if len(param[n]) == 0 and param[n].text != None:
            list_info = param[n].tag, param[n].text
            node_list.append(list_info)
    
    return node_list

'''
This function is to recursively parse the files that need to be checked against the "gold" xml file. 
'''

def recursion_xml_2(param):
    #!first make sure the market_ids match
    e_test = test_root.findall("Market_ID")
    for i in e_test:
        global term_test 
        term_test = i.text
    global node_list_2 
    node_list_2 = []
    current_file_length = len(param)
    param_list = [gold_root, test_root]
    for param in param_list:
    #!shows the path of nodes that have no data but its iterating too many times, need to only loop once
    # for m in param.iter():
    #     if m.text == None:
    #         print("ERROR: MISSING DATA: " + str(test_root.find("./[@source='DH']").tag) + "/" + str(m.tag))
    #         continue
        for n in range(current_file_length):
            #trying to find any nodes that have nested elements and those nodes are not empty
            
            if len(param[n]) > 0 and param[n].text != None:
                #only returns Client and Job, skips over Compensation for some reason
                parent = param[n]
                node_list_2.append(recursion_xml_2(parent))
                print(node_list_2)
            if len(param[n]) == 0 and param[n].text != None:
                list_info = param[n].tag, param[n].text
                node_list_2.append(list_info)
        
        return node_list_2

print(recursion_xml_2(test_root))
recursion_xml_1(gold_root)

   
