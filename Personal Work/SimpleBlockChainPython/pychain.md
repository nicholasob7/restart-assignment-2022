# Simple Blockchain Hash sha-256

A simple blockchain pseudocode
``` python
testCoin (TC)

t1: Anna sends Bob 2 TC
t2: Bob sends Dani 4.3 TC
t3: Marc sends Charlie 3.2 TC

Block 1 B1 ("AAA", t1, t2, t3) -> 
hash = 76fd89, 
B2("76fd89", t4, t5, t6) -> 
hash = 8923ff, 
B3 ("8923ff", t7, t8) -> 
hashgonnacome

FulvCoinHash()
```

Here we have a 

```
testCoin (TC)
```
in which three transactions have occurred in the initial block B1.
```
t1: Anna sends Bob 2 TC
t2: Bob sends Dani 4.3 TC
t3: Marc sends Charlie 3.2 TC 
```
A salt or placeholder in our first block B1, "AAA" occupies the position our proceeding blockhashes will be in as each block hashes from the prior block into the immediate block hash. Note that in Block 1 our purely imaginary hash becomes 76fd89.
```
Block 1 B1 ("AAA", t1, t2, t3) -> 
hash = 76fd89
```
In Block 2 - B2, the hash of the previous B1 block, 76fd89 is now included in B2 block where the string of AAA wrote into the hash of B1.
```
B2("76fd89", t4, t5, t6) -> 
hash = 8923ff
```
In B3 the hash of B2, "8923ff" is now included as the basis of B3 in preparation of the blockchains hash of B3.
```
B3 ("8923ff", t7, t8) ->
hashgonnacome
```
In light of all these requirements we will need to code a program to control our blockchain blockhash function.
```
FulvCoinHash()
```
# A Simple Python Blockchain

Our first step is to create a main.py file and on line 1 of main.py import hash library, "hashlib" into it.
```python
1  import hashlib
```
Next on Line 3 of main.py we generate our blockchain as a class named here for our token, "FulVCoin".
```python
3  class FulvCoinBlock:
```
Now we have a class for our blockchain, into which any number of functions can be constructed for our FulVCoin blocks. Here we will write a function which performs the task of hashing our blocks in sequence creating the hash immutability of our blockchain.
On line  5 of main.py we initialize our block hash function.
```python
5  def __init__(self, previous_block_hash, transaction_list):
```
def means 'function', '__init__' initializes the contents of a block prepared for the hash function. Inside the ( ), the own being or 'self' of a block is a combination of the previous blocks hash and the transactions listed within the current block.
```python
import hashlib

class FulvCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):

```
Expanding on our block 'self' we now define the parts of our block with a 'self' of their very own.
```python
self.previous_block_hash = previous_block_hash
```
Next the 'self' of the list of transactions included in our current block.
```python
self.transaction_list = transaction_list
```
In the first part of our code in main.py we have described what the self of a FulVCoinBlock is:
```python
import hashlib

class FulvCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
```
Now we need to tell our program how and with what tools we want to hash our blockchain blocks with.
```python
import hashlib

class FulvCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
```
First we have tell our function how to produce the raw data we will hash. With the combination of a transaction_list and the previous_block_hash
Next we tell the function what tool we want to use to perform the task of hashing our raw data.
```python
import hashlib

class FulvCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
```
Now our function knows exactly how to organise itself. So we need to give our function a list of transactions it can call a block.
```python
t1 = "Anna sends 2 FC to Mike"
t2 = "Bob sends 4.1 FC to Mike"
```
Let's pretend our first two transactions occurred in real time. Lets call our first block our Initial Block and in place of a hash write "Initial String". 
```python
initial_block = FulvCoinBlock("Initial String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)
```
In our second block we call the initial block hash where we located our "Inital String" in block 1.
```python
second_block = FulvCoinBlock(initial_block.block_hash, [t3,t4])

print(second_block.block_data)
print(second_block.block_hash)
```
As in Block2 so too Block3
```python
third_block = FulvCoinBlock(second_block.block_hash, [t5,t6])

print(third_block.block_data)
print(third_block.block_hash)
```

The entire code for this very rudimentary form of the simple blockchain in python is as follows.
```python
import hashlib

class FulvCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Anna sends 2 FC to Mike"
t2 = "Bob sends 4.1 FC to Mike"
t3 = "Mike sends 3.2 FC to Bob"
t4 = "Daniel sends 0.3 FC to Anna"
t5 = "Mike sends 1 FC to Charles"
t6 = "Mike sends 5.4 FC to Dani"

initial_block = FulvCoinBlock("Initial String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = FulvCoinBlock(initial_block.block_hash, [t3,t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = FulvCoinBlock(second_block.block_hash, [t5,t6])

print(third_block.block_data)
print(third_block.block_hash)
```

This file and its content were originally produced by the talented NeuralNine team in a
youtube video. Here is the link.
[![](https://img.youtube.com/vi/pYasYyjByKI/0.jpg)](https://www.youtube.com/watch?v=pYasYyjByKI)