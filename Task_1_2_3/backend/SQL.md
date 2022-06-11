#  Task 1 - Database
# a. 
Name all the tables in this database. 
# Query


```sql
SELECT name FROM sqlite_schema 
WHERE type IN ('table') 
AND name NOT LIKE 'sqlite_%'
ORDER BY 1;
```
# Response

```
1. actor
2. address
3. category
4. city
5. country
6. customer
7. film
8. film_actor
9. film_category
10. film_text
11. inventory
12. language
13. payment
14. rental
15. staff
16. store

```
# b. 
Select data types of entities from table 'actor'

```
Integer
Varchar
DATE
DATETIME
```
# c.  
What is the purpose of the 'autoincrement' keyword in each of the table DDL (Data Definition Language)?

```
Each new row appears with a unique id under auto-increment. Assigned as a +1 of the previous data row.
```
# d. 
What is the purpose of the 'references' keyword in the tables with external relationship 'film_actor', column 'actor_id references actor'?

```
Refers to actors who have played in films and other data entries for those actors. Unique actor-id can be used by categories film_actor and other categories via a unique actor_id which is an instance of 'references'.
```