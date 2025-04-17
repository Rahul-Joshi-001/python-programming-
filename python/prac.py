def even():
    with open("practice.txt","r") as f:
        data = f.read()
        count = 0
        lis = list(data)
        for i in  lis:
            if i.isdigit() and int(i) %2 ==0:
                count += 1
        print(count)

even()