#ensure data is present in the tag
#*if there is data, compare it to the other file
#*no match = False
#length of the x.text needs to be the same?
#!find a way to return false and move on to the next conditional to check that xml property
#!RECURSION!
#if n == len(xml_file) return <-- terminate the recrusion with this
#!ensure TEMPLATE_ID and MARKET_ID are the same before comparing

import xml.etree.ElementTree as ET
import logging as lg

#elem1 and elem2 are paramaters that we are filling in when we call the function
def elements_equal(elem1, elem2):
    # for child in elem1.iter():
    #     ch_tag = child.tag
    #     ch_text = child.text
    # for child2 in elem2.iter():
    #     ch2_tag = child2.tag
    #     ch2_text = child2.text
    if elem1.tag != elem2.tag:
        print(elem1.tag + " and " + elem2.tag + " do not match")
        return False
    if elem1.text != elem2.text:
        print(elem1.text + " and " + elem2.text + " do not match")
        if  elem1.text != None and elem2.text != None:
            lg.warning("Both elem1 and elem2 text are None")
#             #this is where the two files differ for the first time
            return False
#     #not 100% sure what tail is but I went ahead and made conditionals to check  everything in the ET documentation
    if elem1.tail != elem2.tail:
        print(elem1.tail + " and " + elem2.tail + " do not match")
        if elem1.tail != None and elem2.tail != None:
            lg.warning("Both elem1 and elem2 tail are None")
            return False
    if elem1.attrib != elem2.attrib:
        print(elem1.attrib + " and " + elem2.attrib + " do not match")  
        return False
    # checks to make sure the length is the same
    # if len(elem1) != len(elem2):
    #     print("Lengths are not the same") 
    #     return False
#     #all() returns true if ALL items in the iteration are true, otherwise it returns false. if the iteration object is empty, all() also returns true
    return all(elements_equal(c1, c2) for c1, c2 in zip(elem1, elem2))

def parse_xml(f1, f2):
    tree_elem1 = ET.parse(f1)
    root1 = tree_elem1.getroot()
    tree_elem2 = ET.parse(f2)
    root2 = tree_elem2.getroot()
    #find all returns a list that has to be iterated over even though there's only 1 item in the list
    for ch in root2.findall("./MARKET_ID"):
        #set the text from the market_id tag to a variable
        market_id_2 = ch.text
    for ch in root1.findall("./MARKET_ID"):
        market_id_1 = ch.text
    #compare the two variables
    if market_id_2 == market_id_1:
        print("TRUE")
    else:
        print("FALSE")
    

    #function call
    return elements_equal(root1,root2)

# #declaring the two sample xmls as f1 and f2 variables
f1 = 'sample_2.xml'
f2 = 'sample_1.xml'
# #fucntion call
print(parse_xml(f1, f2))