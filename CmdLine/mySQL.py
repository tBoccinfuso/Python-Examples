# Start using the MySQL connector
import mysql.connector

# Set out connection string
conn = mysql.connector.connect(user='username', password='password',
                              host='127.0.0.1',
                              database='Users')
query = conn.cursor()

# Inserting a new user into database
# Setting up out insert template
newUser = ("INSERT INTO Users "
               "(FirstName, LastName) "
               "VALUES (%s, %s)")

# Create a new user
user = ('John', 'Doe')

# Insert the user using our query command by passing in our template and data
query.execute(newUser, user)  

# Close database connection
conn.close()



# Selecting a record

template = ("SELECT FirstName, LastName FROM Users "
         "WHERE FirstName = %s")

userFirst = 'John'

# Select the user using our query command by passing in our template and data
query.execute(template, userFirst)

# Thomas Boccinfuso - www.tboccinfuso.com / www.twitter.com/BoccinfusoT
