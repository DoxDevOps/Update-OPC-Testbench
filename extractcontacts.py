import psycopg2

try:
    connection = psycopg2.connect(user="myuser",
                                  password="mypass",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="test_bench_2")
    cursor = connection.cursor()
    postgreSQL_select_Query = "COPY users_account(first_name, email) TO '/home/ubuntu/my_contacts.txt';"

    cursor.execute(postgreSQL_select_Query)
    print("Selecting first name and emails")
    mobile_records = cursor.fetchall()

    #print("Print each row and it's columns values")
    #for row in mobile_records:
     #   print("Id = ", row[0], )
     #   print("Model = ", row[1])
     #   print("Price  = ", row[2], "\n")

except (Exception, psycopg2.Error) as error:
    print("fetching data from PostgreSQL complete", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

