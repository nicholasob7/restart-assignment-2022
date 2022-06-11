from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import queries as queries
import hashlib

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

""" q1
Query 1: status 'print' vscode passing | 
                'return' uvicorn passing |
"""


@app.get('/film_title_by_first_letter_order_by_length')
def film_title_by_first_letter_order_by_length(letter):
    q1 = queries.get_film_title_by_first_letter_order_by_length(letter)
    return q1


""" q2 
Query 2: status 'print' vscode passing | 
                'return' uvicorn passing |"""


@app.get('/actor_first_letter_desc_order')
def actor_first_letter_desc_order(letter):
    q2 = queries.get_actor_first_letter_desc_order(letter)
    return q2


""" q3 
Query 3: status 'print' vscode passing | 
                'return' uvicorn passing |"""


@app.get('/city_by_first_letter')
def city_by_first_letter(letter):
    q3 = queries.get_city_by_first_letter(letter)
    return q3


""" q4
Query 4: status 'print' vscode passing | 
                'return' uvicorn passing | """


@app.get('/discount_customer_by_letter')
def discount_customer_by_letter(letter):
    q4 = queries.get_discount_customer_by_letter(letter)
    return q4


""" q5 
Query 5: status 'print' vscode passing | 
                'return' uvicorn passing | """


@app.post('/new_category')
async def new_category(name, last_update):
    q5 = queries.insert_new_category(name, last_update)
    return q5

""" q6
Query 6: status 'print' vscode passing | 
                'return' uvicorn passing |"""


@app.delete('/by_category_id')
def by_category_id(category_id):
    q6 = queries.delete_by_category_id(category_id)
    return q6


""" q7
Query 7: status 'print' vscode passing | 
                'return' uvicorn passing |"""


@app.post('/variables_into_new_language_row')
async def variables_into_new_language_row(name, last_update):
    q7 = queries.insert_variables_into_new_language_row(name, last_update)
    return q7


""" q8
Query 8: status 'print' vscode passing | 
                'return' uvicorn passing |"""


@app.delete('/language_by_name')
async def language_by_name(name):
    q8 = queries.delete_language_by_name(name)
    return q8

""" q9
Query 9: status 'print' vscode passing | 
                'return' uvicorn passing |"""


@app.post('/new_city_row')
async def all_city(city, country_id, last_update):
    q9 = queries.insert_new_city_row(city, country_id, last_update)
    return q9

""" q10 
Query 10: status 'print' vscode passing | 
                'return' uvicorn passing |"""


@app.delete('/by_city_name')
async def by_city_name(city):
    q10 = queries.delete_by_city_name(city)
    return q10

""" q11
Query 11: status 'print' vscode passing | 
                'return' uvicorn passing |"""


@app.post('/new_customer_row')
async def new_customer_row(store_id, first_name, last_name, email, address_id,
                           active, create_date, last_update):
    q11 = queries.insert_new_customer_row(store_id, first_name, last_name,
                                          email, address_id, active, create_date, last_update)
    return q11

""" q12
Query 12: status 'print' vscode passing | 
                    'return' uvicorn passing |"""


@app.delete('/customer_by_customer_id')
async def customer_by_customer_id(customer_id):
    q12 = queries.delete_customer_by_customer_id(customer_id)
    return q12

""" q13
Query 13: status 'print' vscode passing | 
                    'return' uvicorn passing |"""


@app.post('/new_country_row')
async def new_country_row(country, last_update):
    q12 = queries.insert_new_country_row(country, last_update)
    return q12

""" q14
Query 14: status 'print' vscode passing | 
                    'return' uvicorn passing |"""


@app.delete('/by_country')
async def by_country(country):
    q12 = queries.delete_by_country(country)
    return q12

""" q15
Query 15: status 'print' vscode passing | 
                    'return' uvicorn passing |"""


@app.put('/format_staff_email')
async def format_staff_email(manual_key_stroke):
    q15 = queries.put_format_staff_email(manual_key_stroke)
    return q15

""" q16
Query 16: status 'print' vscode passing | 
                    'return' uvicorn passing | """


@app.put('/format_customer_email')
async def format_customer_email(manual_key_stroke):
    q16 = queries.put_format_customer_email(manual_key_stroke)
    return q16

""" q17
Query 17: status 'print' vscode passing | 
                    'return' uvicorn passing |"""


@app.get('/customer_by_total_dollars_paid')
def customer_by_total_dollars_paid(any_key_displays_top_3_customers):
    q17 = queries.get_customer_by_total_dollars_paid(
        any_key_displays_top_3_customers)
    (any_key_displays_top_3_customers)
    return q17


""" q18
Query 18: status 'print' vscode passing | 
                    'return' uvicorn passing |"""


@app.get('/district_postal_code_city')
def district_postal_code_city(first_letter_in_district_name):
    q18 = queries.get_district_postal_code_city(first_letter_in_district_name)
    return q18


"""q19
Query 19 status : status 'print' vscode passing | 
                    'return' uvicorn passing |"""


@app.get('/actor_by_film')
def actor_by_film(first_letter):
    q19 = queries.get_actor_by_film(first_letter)
    return q19


""" q20
Query 20: status 'print' vscode passing | 
                    'return' uvicorn passing |"""


@app.get('/film_by_first_letter')
def film_by_first_letter(letter):
    q20 = queries.get_film_by_first_letter(letter)
    return q20


""" 
q21 
1 f. Create a /hash_password route which accepts a password via HTTP POST and returns a 
hexdigest using an algorithm from Python’s hashlib library. [4 marks]

Query 21 : status 'print' vscode passing | 
                    'return' uvicorn passing |"""


@app.post("/hash_password")
def hash_password(input_str):
    pw = ("SHA-256:", hashlib.sha256(input_str.encode()).hexdigest())
    return pw


"""
Task 1 f. COMPLETE at q21"""


"""
TASK ONE COMPLETE
"""

"""
Query 22 is a former failing attempt resolved,
apparently order of items SELECTED affected whether it worked.
I had all the film SELECTIONS in the first part of the SELECT,
and couldnt get the result I wanted. 
EG attributing every category to selected film title."""


@app.get('/film_by_category')
def film_by_category(first_letter):
    q22 = queries.get_film_by_category(first_letter)
    return q22
