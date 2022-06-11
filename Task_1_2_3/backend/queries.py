import sqlite3
import hashlib

"""Task 1 e. Create a file named queries.py and add [20] Python functions
                which use Python's sqlite3 [10 marks]

Task 1 f. 
'demonstrate use of ORDER in at least 1 table' [2 marks]
        

Task 1 g.
'demonstrate use of WHERE and LIMIT in at least 3 tables' [1 mark]

Task 1 e.
q1      [1 of 20 Python Queries]  
Task 1 f.         
q1      [ 1 of 3 ORDER queries q1, q2, q3]
Task 1 g.
q1      [1 of 3 WHERE and LIMIT queries q1- table film, q2, q3]

Query 1: status 'print' vscode passing | 
                'return' uvicorn passing | """

def get_film_title_by_first_letter_order_by_length(letter):
        connie = sqlite3.connect('sakila.db')
        cursor = connie.cursor()
        q1 = f"""SELECT title, description, rental_rate, 
                rental_duration, length,
                rating, special_features FROM film
                WHERE film.title LIKE '{letter}%'
                ORDER BY length LIMIT 3;"""
        cursor.execute(q1)
        results = cursor.fetchall()
        connie.close()
        for result in results:
                title = result[0]
                description = result[1]
                rental_rate = result[2]
                rental_duration = result[3] 
                length = result[4]
                rating = result[5]
                special_features = result [6]
                (f""" {title} {description} {rental_rate} 
                        {rental_duration} {length}
                        {rating} {special_features}""")
        return results

"""
Task 1 f. COMPLETE AT q1
'demonstrate use of ORDER in at least 1 table' [2 marks]
"""
        
"""
Task 1 e.
q2      [2 of 20 Python Queries]
Task 1 g.
q2      [2 of 3 WHERE and LIMIT queries q1, q2 - table actor, q3]

Query 2: status 'print' vscode passing |
                'return' uvicorn passing | 
"""

def get_actor_first_letter_desc_order(letter):
        connie = sqlite3.connect('sakila.db')
        cursor = connie.cursor()
        q2 = f"""SELECT actor_id, first_name,
                last_name FROM actor WHERE 
                actor.first_name like '{letter}%'
                ORDER BY actor_id DESC LIMIT 3;"""
        cursor.execute(q2)
        results = cursor.fetchall()
        connie.close()
        for result in results:
                actor_id = result[0]
                first_name = result[1]
                last_name = result[2]
                (f"""{actor_id} {first_name} 
                        {last_name}""")  
        return results
                

"""
Task 1 e.
q3      [3 of 20 Python Queries]
Task 1 g.
q3      [3 of 3 WHERE and LIMIT queries q1 film, q2 actor, q3 city]

Query 3: status 'print' vscode passing |
                'return' uvicorn passing | 
"""

def get_city_by_first_letter(letter):
        conn = sqlite3.connect('sakila.db')
        cursor = conn.cursor()
        q3 = f"""SELECT city_id, city, country_id 
                FROM city WHERE city like '{letter}%'
                LIMIT 3;"""
        cursor.execute(q3)
        results = cursor.fetchall()
        conn.close()
        for result in results:
                city_id = result[0]
                city = result[1]
                country_id = result[2]
                (f"{city_id} {city} {country_id}")
        return results

""" 
Task 1 g. Complete at q1 film, q2 actor, q3 city
'demonstrate use of WHERE and LIMIT in at least 3 tables' [1 mark]
"""

"""
Task 1 e.
q4      [4 of 20 Python Queries]

Query 4: status 'print' vscode passing |
                'return' uvicorn passing | """

def get_discount_customer_by_letter(letter):
        conn = sqlite3.connect("sakila.db")
        cursor = conn.cursor()
        q4 = f"""SELECT first_name, last_name 
                FROM customer WHERE first_name 
                LIKE '%{letter}%'
                LIMIT 6;"""
        cursor.execute(q4)
        results = cursor.fetchall()
        conn.close()
        for result in results:
                first_name = result[0]
                last_name = result[1]
                (f"{first_name} {last_name}")
        return results

""" 
Task 1 e.
q5      [5 of 20 Python Queries]

Task 1 j: 
'Demonstrate the use of INSERT INTO in at least five tables[5 marks]'

q5      [1 of 5 INSERT queries q5 category,q7,q9,q11,q13]

Query 5 : status 'print' vscode passing |
                'return' uvicorn passing |"""

def insert_new_category(name, last_update):
        conn = sqlite3.connect("sakila.db")
        cursor = conn.cursor()
        q5 = f"""INSERT INTO category (name, last_update)
                VALUES ('{name}','{last_update}');"""
        cursor.execute(q5)
        conn.commit()
        cursor.close()
        return("Total", cursor.rowcount, name, "category added")

"""
Task 1 e.
q6      [6 0f 20 Python Queries] 

Task 1 h: Demonstrate the use of DELETE in at least one table[1 mark]
q6      [1 of 1 (required) DELETE queries q6 - table category]

Query 6: status 'print' vscode passing |
                'return' uvicorn passing |"""

def delete_by_category_id(category_id):
        conn = sqlite3.connect("sakila.db")
        cursor = conn.cursor()
        q6 = f"""DELETE FROM category
                        Where category_id = {category_id};""" 
        cursor.execute(q6)
        conn.commit()
        cursor.close()
        return("Total", cursor.rowcount, "Category deleted")

"""
Task 1 h. 
"""    
"""
Task 1 e.
q7      [7 of 20 Python Queries]

Task 1 j. 

q7     [2 of 5 INSERT queries q5 category,q7 language,q9,q11,q13]

Query 7 : status 'print' vscode pass | 
                'return' uvicorn pass |"""

def insert_variables_into_new_language_row(name, last_update):
        conn = sqlite3.connect("sakila.db")
        cursor = conn.cursor()
        q7 = f"""INSERT INTO language 
                (name, last_update)
                VALUES ('{name}','{last_update}');"""
        cursor.execute(q7)
        conn.commit()
        cursor.close()
        return("Total", cursor.rowcount, name, "inserted into languages")

"""
Task 1 e.
q8      [8 of 20 Python Queries]

Query 8:  status 'print' vscode pass | 
                'return' uvicorn pass |"""

def delete_language_by_name(name):
        conn = sqlite3.connect("sakila.db")
        cursor = conn.cursor()
        q8 = f"DELETE FROM language WHERE name LIKE '%{name}%';"
        cursor.execute(q8)
        conn.commit()
        conn.close()
        return("Total", cursor.rowcount, name, "deleted from languages")

"""
Task 1 e.
q9      [9 of 20 Python Queries]

Task 1 j. 

q9     [3 of 5 INSERT queries q5 category,q7 language,q9 city,
        q11,q13]

Query 9: status 'print' vscode passing |
                'return' uvicorn passing |"""

def insert_new_city_row(city, country_id, last_update):
        conn = sqlite3.connect("sakila.db")
        cursor = conn.cursor()
        q9 = f"""INSERT INTO city 
                (city, country_id, last_update)
                VALUES ('{city}','{country_id}','{last_update}');"""
        cursor.execute(q9)
        conn.commit()
        cursor.close()
        return("Total", cursor.rowcount, city, "City inserted into record_list")


""" 
Task 1 e.
q10      [10 of 20 Python Queries]

Query 10 status 'print' vscode passing |
                'return' uvicorn passing | """

def delete_by_city_name(city):
        conn = sqlite3.connect("sakila.db")
        cursor = conn.cursor()
        q10 = f"DELETE FROM city WHERE city LIKE '%{city}%';"
        cursor.execute(q10)
        conn.commit()
        cursor.close()
        return("Total", cursor.rowcount, city, "deleted from city")


""" 
Task 1 e.
q11      [11 of 20 Python Queries]

Task 1 j. 

q11     [4 of 5 INSERT queries q5 category,q7 language,q9 city,
        q11 customer,q13]

Query 11 : status 'print' vscode passing |
                'return' uvicorn passing |  """

def insert_new_customer_row(store_id, first_name, last_name, email, address_id,
                active, create_date, last_update):
        conn = sqlite3.connect("sakila.db")
        cursor = conn.cursor()
        q11 = f"""INSERT INTO customer 
                (store_id, first_name, last_name, email, address_id,
                active, create_date, last_update)
                VALUES ('{store_id}','{first_name}','{last_name}','{email}',
                '{address_id}','{active}','{create_date}','{last_update}');"""
        cursor.execute(q11)
        conn.commit()
        cursor.close()
        return("Total", cursor.rowcount, "Row inserted into record_list")
        
""" 
Task 1 e.
q12      [12 of 20 Python Queries]

Query 12 : status 'print' vscode passing |
                'return' uvicorn passing | """

def delete_customer_by_customer_id(customer_id):
        conn = sqlite3.connect("sakila.db")
        cursor = conn.cursor()
        q12 = f"DELETE FROM customer WHERE customer_id LIKE '{customer_id}%';"
        cursor.execute(q12)
        conn.commit()
        cursor.close()
        return("Total", cursor.rowcount, customer_id, "deleted from customer")

"""
Task 1 e.
q13      [13 of 20 Python Queries]

Task 1 j. 
q13      [5 of 5 INSERT queries q5 category,q7 language,q9 city,
                q11 customer,q13 country]

Query 13 : status 'print' vscode passing |
                        'return' uvicorn passing |"""

def insert_new_country_row(country, last_update):
        conn = sqlite3.connect("sakila.db")
        cursor = conn.cursor()
        q13 = f"""Insert into country (country, last_update)
                VALUES ('{country}','{last_update}');"""
        cursor.execute(q13)
        conn.commit()
        conn.close()
        return("Total", cursor.rowcount, country, "added to country")

"""
Task 1 j: COMPLETE at [q5 category,q7 language,q9 city,
                        q11 customer,q13 country]

'Demonstrate the use of INSERT INTO in at least five tables[5 marks]'
"""



""" 
Task 1 e.
q14      [14 of 20 Python Queries]

Query 14 : status 'print' vscode passing |
                'return' uvicorn passing |"""

def delete_by_country(country):
        conn = sqlite3.connect("sakila.db")
        cursor = conn.cursor()
        q14 = f"DELETE FROM country WHERE country LIKE '%{country}%';"
        cursor.execute(q14)
        conn.commit()
        cursor.close()
        return("Total", cursor.rowcount, country, "deleted from country")
        

""" 
Task 1 e.
q15      [15 of 20 Python Queries]

Task 1 i: Demonstrate the use of UPDATE in at least one table[1 mark]

q15     [1 of 1(required) Query using UPDATE q15 staff]

Query 15 : status 'print' vscode passing |
                'return' uvicorn passing |"""

def put_format_staff_email(q15):#argprovision
        conn = sqlite3.connect("sakila.db")
        cursor = conn.cursor()
        q15 = f"""UPDATE staff
                        SET email = LOWER(first_name || "." || last_name ||
                        "@sakilastaff.com")
                        WHERE staff_id = staff_id;"""
        cursor.execute(q15)
        conn.commit()
        cursor.close()
        return("Total", cursor.rowcount, "Staff emails successful format.")

"""
Task 1 i: COMPLETE at [1 of 1(required) Query using UPDATE q15 staff]
'Demonstrate the use of UPDATE in at least one table[1 mark]'
"""

""" 
Task 1 e.
q16      [16 of 20 Python Queries]

Query 16  status 'print' vscode passing |
                'return' uvicorn passing |
"""

def put_format_customer_email(q16):
        conn = sqlite3.connect("sakila.db")
        cursor = conn.cursor()
        q16 = f"""UPDATE customer
                        SET email = LOWER(first_name || "." || last_name ||
                        "@sakilacustomer.org")
                        WHERE customer_id = customer_id;"""
        cursor.execute(q16)
        conn.commit()
        cursor.close()
        return("Total", cursor.rowcount, "Customer emails successful format.")
""" 
Task 1 e.
q17      [17 of 20 Python Queries]

Task 1 k: Demonstrate the use of JOIN in at least 3 tables[5 marks]

q17     [1 of 3 JOIN queries q17 customer, q18, q19]

Query 17 : status 'print' vscode passing |
                'return' uvicorn passing |
"""

def get_customer_by_total_dollars_paid(total_dollars_paid):
        conn = sqlite3.connect("sakila.db")
        cursor = conn.cursor()
        q17 = f"""SELECT c.first_name, c.last_name, 
                printf('%.2f', SUM(p.amount)) 
                AS total_dollars_paid
                FROM customer as c
                INNER JOIN payment as p
                ON c.customer_id = p.customer_id
                GROUP by c.first_name, c.last_name
                ORDER BY total_dollars_paid desc
                LIMIT 3;"""
        cursor.execute(q17)
        results = cursor.fetchall() 
        cursor.close()
        for result in results:
                first_name = result[0]
                last_name = result[1]
                total_dollars_paid = result[2]
                print(f"{first_name} {last_name} {total_dollars_paid}")
        return results




""" 
Task 1 e.
q18     [18 of 20 Python Queries]

Task 1 k: Demonstrate the use of JOIN in at least 3 tables[5 marks]

q18     [2 of 3 JOIN queries q17 customer, q18 address, q19]

Query 18 : status 'print' vscode passing |
                'return' uvicorn passing |
"""

def get_district_postal_code_city(first_letter_in_district_name):
        conn = sqlite3.connect("sakila.db")
        cursor = conn.cursor()
        q18 = f"""SELECT address.District, address.Postal_code, city.City from address
                JOIN city on address.City_id = city.City_id
                WHERE district like '{first_letter_in_district_name}%'
                LIMIT 4;"""
        cursor.execute(q18)
        results = cursor.fetchall()
        conn.close()
        for result in results:
                district = result[0]
                postal_code = result[1]
                city = result[2]
                print(f"{district} {postal_code} {city}")
        return results


""" 
Task 1 e.
q19      [19 of 20 Python Queries]

Task 1 k: Demonstrate the use of JOIN in at least 3 tables[5 marks]

q19     [3 of 3 JOIN queries q17 customer, q18 address,  q19 actor]

Query 19 : status 'print' vscode passing |
                'return' uvicorn passing |
"""


def get_actor_by_film(first_letter):
        conn = sqlite3.connect("sakila.db")
        cursor = conn.cursor()
        q19 = f"""SELECT actor.first_name, actor.Last_name, film.title FROM actor
                JOIN film_actor on actor.actor_id = film_actor.actor_id
                JOIN film on film.film_id = film_actor.film_id
                WHERE actor.first_name LIKE '{first_letter}%'
                LIMIT 13;"""
        cursor.execute(q19)
        results = cursor.fetchall()
        conn.close()
        for result in results:
                first_name = result[0]
                last_name = result[1]
                title = result[2]
                print(f"{first_name} {last_name} {title}")
        return results

        

"""
Task 1 k: COMPLETE at [3 of 3 JOIN queries q17 customer, q18 address,  q19 actor]
Demonstrate the use of JOIN in at least 3 tables[5 marks]
"""
        

""" 
Task 1 e.
q20      [20 of 20 Python Queries]

Query 20: status 'print' vscode passing |
                'return' uvicorn passing |
"""

def get_film_by_first_letter(letter):
        conn = sqlite3.connect('sakila.db')
        cursor = conn.cursor()
        q20 = f"""SELECT film_id, title, description
                FROM film WHERE title like '{letter}%'
                LIMIT 3;"""
        cursor.execute(q20)
        results = cursor.fetchall()
        cursor.close()
        for result in results:
                film_id = result[0]
                title = result[1]
                description = result[2]
                (f"{film_id} {title} {description}")
        return results


"""
Task 1 e. COMPLETE at [q1-q20]
Create a file named queries.py and add [20] Python functions
which use Python's sqlite3 [10 marks]
"""

"""

Task 1 f. Create a /hash_password route which accepts a password via HTTP POST and returns a 
hexdigest using an algorithm from Python’s hashlib library. [4 marks]

q21 : See main.py
"""

"""TASK ONE COMPLETE."""

"""
Query 22 is a former failing attempt resolved,
apparently order of items SELECTED affected whether it worked.
I had all the film SELECTIONS in the first part of the SELECT,
and couldnt get the result I wanted. 
EG attributing every category to selected film title."""


def get_film_by_category(first_letter):
        conn = sqlite3.connect("sakila.db")
        cursor = conn.cursor()
        q22 = f"""SELECT title, category.name, film.description FROM film
                INNER JOIN film_category ON film.film_id = film_category.film_id
                INNER JOIN category ON film_category.category_id = category.category_id
                WHERE category.name LIKE '{first_letter}%'
                LIMIT 13;"""
        cursor.execute(q22)
        results = cursor.fetchall()
        conn.close()
        for result in results:
                title = result[0]
                name = result[1]
                description = result[2]
                print(f"{title} {name} {description}")
        return results
