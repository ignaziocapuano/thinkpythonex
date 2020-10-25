#Formatting Lists

from listInsertion import listInsertion

def formatList(list):
    final_string=""
    final_string += list[0]
    if len(list)==1:
        return final_string
    if len(list)>2:
        for i in range(1,len(list)-1):
            final_string+=", "+list[i]
    if len(list)>1:
        final_string+=" e "+list[len(list)-1]
    return final_string

def main():
    lista=listInsertion("str","")
    print(formatList(lista))

if __name__ == '__main__':
    main()