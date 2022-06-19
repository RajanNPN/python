import psycopg2
mydb = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="1234",
    host="localhost",
    port=5432,
)
cursor=mydb.cursor()
query='Select * from "student"'
cursor.execute(query)
array=list(cursor.fetchall())
print(array)
print("Given data is:")
for x in array:
    print(x)


def merge(array,age):
    if len(array)>1:
        mid=len(array)//2
        L=array[:mid]
        R=array[mid:]
        merge(L,age)
        merge(R,age)
        i=j=k=0
    
        while i<len(L) and j<len(R):
            if L[i][3] <= R[j][3]:
                array[k]=L[i]
                i+=1

            else:
                array[k]=R[j]
                j+=1
            k+=1

        while i<len(L):
            array[k]=L[i]
            i+=1
            k+=1

        while j<len(R):
            array[k]=R[j]
            j+=1
            k+=1

merge(array,2)
print("The sorted age is :")
for x in array:
    print(x)
