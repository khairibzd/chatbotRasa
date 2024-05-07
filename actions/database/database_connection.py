import mysql.connector

def DataUpdate(firstName, lastName, email, gender, age, zone, numeroTlp, salaire, etatSociale):
    mydb = mysql.connector.connect(
        host="localhost",
        user="khairi",
        passwd="root",
        database="rasachat"
    )

    mycursor = mydb.cursor()

    # first we create the table
    #sql = 'CREATE TABLE User_informations (firstName VARCHAR(255),lastName VARCHAR(255),email VARCHAR(255),gender VARCHAR(20),age INT,zone VARCHAR(255), numeroTlp VARCHAR(20),salaire VARCHAR(20), etatSociale VARCHAR(20))';
    # here we insert the data 
    sql = 'INSERT INTO User_informations (firstName, lastName, email, gender, age, zone, numeroTlp, salaire, etatSociale) VALUES ("{0}", "{1}", "{2}", "{3}", {4}, "{5}", "{6}", "{7}", "{8}")'.format(firstName, lastName, email, gender, age, zone, numeroTlp, salaire, etatSociale)
    
    print(f"Executing SQL: {sql}")

    mycursor.execute(sql)
    mydb.commit()

    print("Data inserted successfully.")

    mycursor.close()
    mydb.close()

# Example usage
#DataUpdate("John", "Doe", "john.doe@example.com", "Male", 25, "Zone1", "123456789", "30000dt", "Married")
