from node import * 

def main():

    #Question 1 
    head = node('2',None)
    head = node('=',head)
    head = node('1',head)
    head = node('+',head)
    head = node('1',head)

    #Question 2 
    operator = head 

    #Question 3
    operator = operator.getLink()

    #Question 4 
    result = head 

    #Question 5 
    result = result.getLink()
    result = result.getLink()
    result = result.getLink()
    result = result.getLink()

    #Question 6 
    result.set_data('0')
    operator.set_data('-')

    #Question 7 
    operator.set_data('*')
    result.set_data('1')

    #Question 8
    operator.set_data('/')

    #Question 9 
    head.set_data('7')
    result.set_data('7')

    #Question 10 
    operator = operator.getLink()

    #Question 11
    head.removeNodeAfter()
    operator.removeNodeAfter()


    #Question 12
    print(f"Head contains {node.listLength(head)} nodes")
    print(f"Operator contains {node.listLength(operator)} nodes")
    print(f"Result contains {node.listLength(result)} nodes")

    #Question 13 
    if (node.listSearch(head,'1') != None):
        print("Head contains character 1")
    else: 
        print("Head doesn't contain charater 1")

    if (node.listSearch(operator,'1') != None):
        print("Operator contains character 1")
    else: 
        print("Operator doesn't contain charater 1")

    if (node.listSearch(result,'1') != None):
        print("Result contains character 1")
    else: 
        print("Result doesn't contain charater 1")
   
    #Question 14 
    copy = node.listCopywithTail(head)
    
    #Question 15 
    print(f"Copy[0] contains {node.listLength(copy[0])} nodes")
    print(f"Copy[1] contains {node.listLength(copy[1])} nodes")

    #Question 16
    if (node.listSearch(copy[0],'1') != None):
        print("Copy[0] contains character 1")
    else: 
        print("Copy[0] doesn't contain charater 1")
    
    if (node.listSearch(copy[1],'1') != None):
        print("Copy[1] contains character 1")
    else: 
        print("Copy[1] doesn't contain charater 1")

if __name__ == "__main__":
    main()