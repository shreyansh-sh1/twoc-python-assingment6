flag=0
n = int(input("Enter length: "))
arr=[]
for i in range(n):
    d=int(input("Enter element : "))
    arr.append(d)
for i in range(0,n-1):
    if arr[i]>arr[i+1]:
        flag=1
        break
if flag==1:
    print("Your arr",arr,"is not sorted.")
else:
    print("Your arr", arr, "is sorted.")

# code by shreyansh sharma