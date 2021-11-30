import wikipedia as wiki

while True:
    i = input("Press Any Key To Continue (or Enter to quit): ")
    if not i:
        break
    print("Let Search something for you ......\n")
    print("What Do You Want to search...??? \n1-Title and URL of your topic\n2-Search about your topic\n3-Suggested words\n4-Summary about a Topic\n5-Summary in another language")
    print("6-image sourse on your topic\n7-content of your topic ")l
    c=input("enter your choice:")
    if c=='1':
         a=input("enter the topic to be searched : ")
         p = wiki.page(a)
         print(p.title)
         print(p.url)
    elif c=='2':
         a=input("enter the topic to be searched :")
         print(wiki.search(a))
    elif c=='3':
         a=input("enter the topic to be searched :")
         print(wiki.suggest(a))
    elif c=='4':
          a=input("enter the topic to be searched :")
          print(wiki.summary(a))
    elif c=='5':
          b=input("enter the language to be searched in :")
          wiki.set_lang(b)
          #en, ja , ur ,sa , ru, pa , ko-KR , it,
          a=input("enter the topic to be searched :")
          print(wiki.summary(a))
    elif c=='6':
         a=input("enter the topic to be searched :")
         p = wiki.page(a)
         print(p.images)    
    elif c=='7':
         a=input("enter the topic to be searched :")
         p = wiki.page(a)
         print(p.content)       
    else:
        print("wrong search  ....!!!!")
print("Thank You For Searching :) ")               
