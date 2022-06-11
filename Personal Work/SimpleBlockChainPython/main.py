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