# Task 9
Database Cloud Deployment – 8 Marks
# a. 
A paragraph about your chosen database software 
(e.g. PostgreSQL, MariaDB, MySQL) and why you 
chose it over the alternatives. [2 marks]

```
I chose MariaDB because it is growing in popularity. Although all three of these databases support basic SQL operations, PostgreSQL and MariaDB return zero division errors, MySQL does not. MariaDB may also be popular with users already familiar with MySQL. This is beacuse MariaDB uses MySQL workbench and mysql command line applications.
```
# b. 
A link to the resource(s) you used when learning how to do this. [2 marks]

```
https://stackoverflow.com/questions/38962507/how-to-export-a-data-base-from-datagrip-at-one-sql-file/40827315
```
```
[](https://labs.vocareum.com/main/main.php?m=editor&asnid=767578&stepid=767583&hideNavBar=1)
```
```
[MariaDB vs MySQL vs PostgreSQL | What are the differences? (stackshare.io)](https://stackshare.io/stackups/mariadb-vs-mysql-vs-postgresql)
```
```
[](https://www.rebasedata.com/)
```
# c.
The SQL client command used to connect a CLI client to the database. [2 marks]

Replace <RDS Instance Database Endpoint Address> with an actual sakila_db address, example address, "cafedbinstance.ctfiwhpsvvaj.us-west-2.rds.amazonaws.com"
```
mysql --user=root --password='Re:Start!9' \
--host=<RDS Instance Database Endpoint Address> \
sakila_db
```
# d.
Export the sakila schema & data from this database (not-SQLite) to a .sql file and add it to 
GitHub. [2 marks]

I didn't manage to complete this task. Mainly because I had trouble trying to convert the sakila to a single .sql file.