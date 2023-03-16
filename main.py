import xml.etree.ElementTree as ET
from collections.abc import Iterable

# Parse XML files
gold_tree = ET.parse('GOLD_file.xml')
test_tree = ET.parse('test.xml')
sample_tree = ET.parse('sample_1.xml')
gold_root = gold_tree.getroot()
test_root = test_tree.getroot()

#set compare_market_id to False intitially
def recursion_xml(param, compare_market_id=False):
    #if compare_market_id is true
    if compare_market_id:
        e_gold = gold_root.findall("Market_ID")
        for i_gold in e_gold:
            term_gold = i_gold.text

        e_test = param.findall("Market_ID")
        for i_test in e_test:
            term_test = i_test.text

            if term_test != term_gold:
                #stops the function if the market_IDs don't match
                raise Exception("The Market IDs do not match")
    #initialize empty list
    node_list = []
    #declare length of file
    current_file_length = len(param)
    #iterate over the length of the file
    for n in range(current_file_length):
        #if the node has children and the text inside is not None
        if len(param[n]) > 0 and param[n].text != None:
            #parent is now the same as param[n]
            parent = param[n]
            #append whatever the return from the recustion_xml function with the new parent variable to the node_list
            node_list.append(recursion_xml(parent, compare_market_id))
            #if the node has no children, just append the tag to the node_list
        if len(param[n]) == 0 and param[n].text != None:
            node_list.append(param[n].tag)
    #inner function used to "flatten" the nested list 
    def flatten_list(items, ignore_types=(str, bytes)):
        for v in items:
            if isinstance(v, Iterable) and not isinstance(v, ignore_types):
                yield from flatten_list(v)
            else:
                yield v
    
    node_list = list(flatten_list(node_list))
    return node_list

#declare gold_node_list to whatever the return from the recursion_xml with using the gold xml file
gold_node_list = recursion_xml(gold_root)
#declare test_node_list to whatever the return from the recursion_xml with using the test xml file
test_node_list = recursion_xml(test_root, compare_market_id=True)
#just formatting the output better
print("Gold Node List:")
print(gold_node_list)
print("\nTest Node List:")
print(test_node_list)

main_list = list(set(gold_node_list) - set(test_node_list))
print("ERROR: MISSING DATA: ", main_list)


   
