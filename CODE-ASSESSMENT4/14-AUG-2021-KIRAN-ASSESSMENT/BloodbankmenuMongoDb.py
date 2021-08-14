import pymongo,re,smtplib,logging
try:
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    mydatabase=client['BloodbankDetailsDb']
    collection_name=mydatabase['donors']
    donor_list=[]
    class BloodBank:
        def addDonors(self,name,address,bloodgroup,pincode,mobilenumber,last_donated_date,place,email):
            dict={"name":name,"address":address,"bloodgroup":bloodgroup,"pincode":pincode,"mobilenumber":mobilenumber,"last_donated_date":last_donated_date,"place":place,"email":email,"flag":0}
            donor_list.append(dict)
    def validation(name,pincode,mobilenumber,email):
        val1=re.search("^[a-z]{2,20}$",name)
        val2=re.match("^[1-9]{1}[0-9]{2,7}$",pincode)
        val3=re.match("^[6-9]{1}\d{9}$",mobilenumber)
        val4=re.search("^[a-z0-9]{3,20}@[a-z]+\.[a-z]{2,3}$")
        if val1 and val2 and val3 and val4:
            return True
        else:
            return False

    obj=BloodBank()


    while(1):
        print("1.add Donor:")
        print("2.search donor based on blood group:")
        print("3.search donor based on blood group and place:")
        print("4.update all donors with their mobile number:")
        print("5.delete donor using their mobile number:")
        print("6.Display the total number of donors on blood group:")
        print("7.read msg fro user and send maill to all donors:")

        choice=int(input("Enter your choice:"))
        if choice==1:
            name=input("enter your name:")
            address=input("enter your address:")
            bloodgroup=input("enter your blood group:")
            pincode=input("enter your pincode:")
            mobilenumber=input("enter your mobile number:")
            last_donated_date=input("enter your last donated date:")
            place=input("enter your place:")
            email=input("enter your mailid:")
            if validation(name,pincode,mobilenumber,email):
                obj.addDonors(name,address,bloodgroup,pincode,mobilenumber,last_donated_date,place,email)
                result=collection_name.insert_many(donor_list)
                print(result.inserted_ids)
                donor_list.clear()
                    
            else:
                print("invalid details")

        if choice==2:
            result=collection_name.find()
            for i in result:
                print(i)
            # bloodgroup=input("Enter your blood group:")
            # result=collection_name.find({"bloodgroup":bloodgroup,"flag":0})
            # for i in result:
            #     print(i)

        if choice==3:
            bloodgroup=input("Enter your blood group:")
            place=input("Enter your place:")
            result=collection_name.find({"bloodgroup":bloodgroup,"place":place,"flag":0})
            for i in result:
                print(i)

        if choice==4:
            mobilenumber=input("Enter your phone number:")
            name=input("Enter your name:")
            address=input("enter the address")
            bloodgroup=input("enter your blood group:")
            pincode=input("enter your pincode:")
            result=collection_name.update_one({"mobilenumber":mobilenumber},{"$set":{"name":name,"address":address,"bloodgroup":bloodgroup,"pincode":pincode}})
            print(result)

        if choice==5:
            mobilenumber=input("Enter the phone number:")
            result=collection_name.update_many({"$and":[{"mobilenumber":mobilenumber}]},{"$set":{"delflag":1}})
            print(result)

        if choice==6:
            result=collection_name.aggregate([{"$group":{"_id":"$bloodgroup","type_of_blood":{"$sum":1}}}])
            for i in result:
                print(i)

        if choice==7:
            bloodgroup=input("Enter your bloodgroup:")
            result=collection_name.find({"flag":0})
            for i in result:
                message="Hello,immediately wants blood at KIMS hospital and blood group is  "+str(bloodgroup)+"if you are willing to donate contact 6300902344"
                connection=smtplib.SMTP("smtp.gmail.com",587)
                connection.starttls()
                connection.login("969kiran969@gmail.com","Kiran@969")
                connection.sendmail("969kiran969@gmail.com",i["email"],message)
                print("email sent successfully")
                connection.quit()

        if choice==8:
            break

except Exception:
    logging.error("something went wrong")

finally:
    print("completed!!")






