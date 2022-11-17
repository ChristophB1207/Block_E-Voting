import hashlib


class Block:
    def __init__(self, nr, transactions, hash_before):
        self.nr = nr
        self.transactions = transactions
        self.hash_before = hash_before
        self.hash = self.generate_hash()

    def generate_hash(self):
        block_data = str(self.nr) + ''.join(self.transactions) + self.hash_before
        return hashlib.sha256(block_data.encode()).hexdigest()

    def __str__(self):
        erg = ''
        erg += f'Block Nr.     : {self.nr}\n'
        erg += f'vorh. Hash    : {self.hash_before}\n'
        erg += f'Transaktionen : {self.transactions}\n'
        erg += f'Hash          : {self.hash}\n'
        erg += f'tats. Hash    : {self.generate_hash()}\n'
        return erg


class BlockChain:
    def __init__(self, app):
        self.app = app
        self.blocks = [Block(0, ['Genesis', 'Genesis'], '00' * 32)]

    def append(self, transactions):
        nr = len(self.blocks)
        hash_before = self.blocks[-1].hash
        self.blocks.append(Block(nr, transactions, hash_before))

    def get_blocks(self):
        return self.blocks

    def __str__(self):
        return '\n'.join([str(block) for block in self.blocks])

