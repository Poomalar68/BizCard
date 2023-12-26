import streamlit as st
import shapely
import mysql.connector
from sqlalchemy import create_engine 
from tabulate import tabulate
import streamlit as st
from PIL import Image
import pandas as pd
import re
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Malar'
)
print(mydb)
mycursor = mydb.cursor(buffered=True)
Engine=create_engine("mysql+pymysql://root:Malar@localhost/Bizcard")
try:
    mycursor.execute("Create  database Bizcard")
except:
    mycursor.execute("use Bizcard")

st.set_page_config(page_title="Bizcard",layout="wide")

add_selectbox = st.sidebar.selectbox(
    "",
    ("Home/About", "Biz_Card Extraction", "View\Delete",)
)
def bizcard(image_path):
    reader=shapely.Reader(['en'],gpu=False)
    result=reader.readtext(image_path,detail=0)
    return result
filepath = "C:/Users/poomalar/Downloads/download (1).jpeg"
if(add_selectbox=="Home/About"):
    st.header(":voilet[BizCardX: Extracting Business Card Data with OCR]")
    st.subheader(":green[An application that allows users to upload an image of a business card and extract relevant information from it. This image processing interface also comes with an editable option which enable user to add or edit information]")
    col1,col2,col3=st.columns(3)
    col1.markdown(":violet[Name]")
    col1.success("Porselvan")
    col2.markdown(":violet[Designation]")
    col2.success("Student at Guvi")
    col3.markdown(":violet[Email]")
    col3.success("s***.n***@gmail.com")
    col1.markdown(":violet[Phone]")
    col1.success("9********6")
    col2.markdown(":violet[Address]")
    col2.success("Chennai")
    col3.markdown(":violet[Pincode]")
    col3.success("6000053")
    col2.markdown(":violet[Website]")
    col2.success("Porselvan")

elif(add_selectbox=="Biz_Card Extraction"):
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        col1,col2=st.columns(2)
        a=uploaded_file.name
        col2.image(uploaded_file)
        b=filepath+a
        c=bizcard(b)
        #col1.write(c)
        for i in range(len(c)):
            c[i] = c[i].rstrip(' ')
            c[i] = c[i].rstrip(',')
        extract = ' '.join(c)
        
        #Regex Pull
        
        Phone_No=re.findall(r"\d+-\d+-\d+",extract)
        phoneno=" ".join(Phone_No)
        for i in Phone_No:
            extract=extract.replace(i,"")    
        Pincode=re.findall(r"\b\d{6}|\d{7}\b",extract)
        extract=extract.replace(Pincode[0],"")
        Pincode=" ".join(Pincode)
        email=re.findall(r"[\w\.]+@+[\w\.]+",extract)
        extract=extract.replace(email[0],"")
        email=" ".join(email)
        try:
            web=re.findall(r'[www|WWW|wwW]+[\.\s]+[a-zA-Z0-9]+[\.][a-zA-Z]+',extract)
            extract=extract.replace(web[0],"")
            web=" ".join(web)
        except:
            web=re.findall(r'[www|WWW|wwW]+[\.\s]+[a-zA-Z0-9]+[a-zA-Z]+',extract)
        extract=extract.replace(web[0],"")
        web=" ".join(web)
        name=re.match(r"\b[A-Za-z]+",extract)
        name_=name.group()
        extract=extract.replace(name_,"")
        designation=re.findall(r"\b[A-Za-z\s]+\b",extract)
        extract=extract.replace(designation[0],"")
        designation=designation[0]
        address=re.findall(r'\d+\s[A-Za-z\s,]+',extract)
        extract=extract.replace(address[0],"")
        address=" ".join(address)
        bname=extract
        
        if(add_selectbox=="Home/About"):
            st.header(":voilet[BizCardX: Extracting Business Card Data with OCR]")
            st.subheader(":green[An application that allows users to upload an image of a business card and extract relevant information from it. This image processing interface also comes with an editable option which enable user to add or edit information]")
            col1,col2,col3=st.columns(3)
            col1.markdown(":violet[Name]")
            col1.success("Malar")
            col2.markdown(":violet[Designation]")
            col2.success("Student at Guvi")
            col3.markdown(":violet[Email]")
            col3.success("s***.n***@gmail.com")
            col1.markdown(":violet[Phone]")
            col1.success("8********6")
            col2.markdown(":violet[Address]")
            col2.success("Coimbatore")
            col3.markdown(":violet[Pincode]")
            col3.success("631027")
            col2.markdown(":violet[Website]")
            col2.success("Malar")

        elif(add_selectbox=="Biz_Card Extraction"):
            uploaded_file = st.file_uploader("Choose a file")
            if uploaded_file is not None:
                col1,col2=st.columns(2)
                a=uploaded_file.name
                col2.image(uploaded_file)
                b=filepath+a
                c=bizcard(b)
                #col1.write(c)
                for i in range(len(c)):
                    c[i] = c[i].rstrip(' ')
                    c[i] = c[i].rstrip(',')
                extract = ' '.join(c)
                
                #Regex Pull
                
                Phone_No=re.findall(r"\d+-\d+-\d+",extract)
                phoneno=" ".join(Phone_No)
                for i in Phone_No:
                    extract=extract.replace(i,"")    
                Pincode=re.findall(r"\b\d{6}|\d{7}\b",extract)
                extract=extract.replace(Pincode[0],"")
                Pincode=" ".join(Pincode)
                email=re.findall(r"[\w\.]+@+[\w\.]+",extract)
                extract=extract.replace(email[0],"")
                email=" ".join(email)
                try:
                    web=re.findall(r'[www|WWW|wwW]+[\.\s]+[a-zA-Z0-9]+[\.][a-zA-Z]+',extract)
                    extract=extract.replace(web[0],"")
                    web=" ".join(web)
                except:
                    web=re.findall(r'[www|WWW|wwW]+[\.\s]+[a-zA-Z0-9]+[a-zA-Z]+',extract)
                extract=extract.replace(web[0],"")
                web=" ".join(web)
                name=re.match(r"\b[A-Za-z]+",extract)
                name_=name.group()
                extract=extract.replace(name_,"")
                designation=re.findall(r"\b[A-Za-z\s]+\b",extract)
                extract=extract.replace(designation[0],"")
                designation=designation[0]
                address=re.findall(r'\d+\s[A-Za-z\s,]+',extract)
                extract=extract.replace(address[0],"")
                address=" ".join(address)
                bname=extract
                
                with col1:
                    st.success("Check & edit for any data mismatch and then Click on Submit")
                    ls_name = st.text_input('Name:',name_)
                    ls_designation = st.text_input('Designation:',designation)
                    ls_email = st.text_input('email:',email)
                    ls_ph = st.text_input('Phone or Mobile No:',phoneno)
                    ls_add = st.text_input('Address:',address)
                    ls_pin = st.text_input('Pincode:',Pincode)
                    ls_bs = st.text_input('Business Name:',bname)
                    ls_web = st.text_input('Website:',web)
                    if(st.button('Submit')):
                        df=pd.DataFrame([{"Name":ls_name,
                                "Designation":ls_designation,
                                "email":ls_email,
                                "Phone or Mobile No":ls_ph,
                                "Address":ls_add,
                                "Pincode":ls_pin,
                                "Business Name":ls_bs,
                                "Website":ls_web}])
                        df.to_sql("Biz",Engine,if_exists="append",index=False)
                        st.info("Thanks! Keep Extracting")
        elif(add_selectbox=="View\Delete"):
            st.subheader(":red[Choose any contact to edit or delete from Database]")
            mycursor.execute("select Name from biz")
            out=mycursor.fetchall()
            ls=[]
            for i in out:
                ls.append('{}'.format(i[0]))
            a=st.selectbox("Select any Contact",ls)
            st.text(a)
            mycursor.execute(f"select * from biz where name = '{a}'")
            out=mycursor.fetchall()
            col1,col2,col3=st.columns(3)
            l_name=col1.text_input("Name:",out[0][0])
            l_desig=col2.text_input("Designation:",out[0][1])
            l_email=col3.text_input("Email:",out[0][2])
            l_Ph=col1.text_input("Phone No:",out[0][3])
            l_add=col2.text_input("Address:",out[0][4])
            l_Pin=col3.text_input("Pincode:",out[0][5])
            l_web=col2.text_input("Website:",out[0][7])
            l_bz=col1.text_input("Business Name:",out[0][6])
            st.text("Once edited, Click Submit")
            
            if(col2.button("Submit")):
                mycursor.execute(f"delete from biz where name='{a}'")
                mydb.commit()
                df=pd.DataFrame([{"Name":l_name,
                                    "Designation":l_desig,
                                    "email":l_email,
                                    "Phone or Mobile No":l_Ph,
                                    "Address":l_add,
                                    "Pincode":l_Pin,
                                    "Business Name":l_bz,
                                    "Website":l_web}])
                df.to_sql("Biz",Engine,if_exists="append",index=False)
                st.info("Thanks! Keep Extracting")
            
                
            