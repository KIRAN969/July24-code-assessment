import re,logging,json,smtplib
studentlist=[]
try:
    class Students:
        def studentDatails(self,name,rollno,admno,college,parentname,mobnum,emailid):
            pass


    class Sem1Resul(Students):
        def semMarks(self,name,rollno,admno,college,parentname,mobnum,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
            totalmarks=sub1mark+sub2mark+sub3mark+sub4mark+sub5mark
            percentage=(totalmarks/250)*100
            dict1={"percent":percentage,"total":totalmarks,"name":name,"rollno":rollno,"admno":admno,"college":college,"parentname":parentname,"mobnum":mobnum,"emailid":emailid,"sub1mark":sub1mark,"sub2mark":sub2mark,"sub3mark":sub3mark,"sub4mark":sub4mark,"sub5mark":sub5mark}
            studentlist.append(dict1)
    obj=Sem1Resul()

    def validation(name,mobnum,emailid,marks):
        val1=re.search("^[A-Z]{1}[a-z]{2,25}$",name)
        val2=re.search("^[6-9]\d{9}$",mobnum)
        val3=re.search("[a-z0-9]{5,25}@[a-z]+\.[a-z]{2,5}",email)
        val4=re.search("^{50|[0-4][0-9]$",marks)
        if val1 and val2 and val3 and val4:
            return True
        else:
            return false

    while(1):
        print("1.add student details with marks:")
        print("2.generate json file api and display the api to view  student details with marks:")
        print("3.generate json file api and display the api to view  student details based on ranking:")
        print("4.send an email to all parents if total percentage of marks less than 50%:")
        print("5.exit:")
        choice=int(input("Enter your choice:"))

        if choice==1:
            name=input("Enter your name:")
            rollno=input("Enter your rollno:")
            admno=input("Enter your admno:")
            college=input("Enter your college:")
            parentname=input("Enter your parentname:")
            mobnum=input("Enter your mobnum:")
            emailid=input("Enter your emailid:")
            sub1mark=int(input("Enter your sub1marks:"))
            sub2mark=int(input("Enter your sub2marks:"))
            sub3mark=int(input("Enter your sub3marks:"))
            sub4mark=int(input("Enter your sub4marks:"))
            sub5mark=int(input("Enter your sub5marks:"))
            obj.semMarks(name,rollno,admno,college,parentname,mobnum,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark)

        if choice==2:
            print(json.dumps(studentlist))
            myjsondata=json.dumps(studentlist)
            with open('test.json','w+',encoding='utf-8') as f:
                f.write(myjsondata)

        if choice==3:
            f=open('test.json')
            print(sorted(studentlist,key=lambda i:i["total"],reverse=True))
            f.close()
        if choice==4:
            for i in studentlist:
                if i['totalmarks']<100:
                    connection=smtp.SMTP("smtp.gmail.com",587)
                    connection.starttls()
                    connection.logging("969kiran9692@gmail.com","Kiran@969")
                    message="hello,your child got below 50% marks in sem1result "+str(i)
                    connection.sendmail("969kiran9692@gmail.com","rachapallikirankumar969@gmail.com",message)
                    print("email sent successfully")
                    connection.quit()
        
        if choice==5:
            break
except Exception:
    logging.error("something went wrong")
finally:
    print("completed the task")




