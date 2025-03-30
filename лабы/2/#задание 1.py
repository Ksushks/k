#задание 1.1
with open("/Users/ksenia/Desktop/Новая папка/лабы/2/data.txt") as file:
    for line in file:
        num=list(map(int,file.read().split()))
        print(num)
        suma=sum(num)
        cn=len(num)
        srz=sum(num)//cn
        maxi=max(num)
        mini=min(num)
        print(suma)
        print(srz)
        print(maxi)
        print(mini)
with open("/Users/ksenia/Desktop/Новая папка/лабы/2/result.txt","w") as file:
    file.writelines([f"Сумма:{suma}\n"])
    file.writelines([f"Максимальное значение:{maxi}\n"])
    file.writelines([f"Минимальное значение:{mini}\n"])
    file.writelines([f"Среднее значение:{srz}\n"])
file.close()
file.close()
    






    

        


        
        

    
