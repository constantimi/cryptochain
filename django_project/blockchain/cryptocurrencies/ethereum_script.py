from blockchain.models import Block, Transaction
from django.utils import timezone
from web3.auto.infura import w3

"""Blocks count created in DB"""
blocks_count = 100


def gather_ethereum_data():
    """Is connected with Database"""

    print("the script started ...")
    print("is connected: " + w3.isConnected())
    print(timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S'))

    """Adds blocks and transaction into Database"""
    inc = 0
    count = 0

    for index in range(blocks_count):
        """Take new block from web3 ethereum"""
        block = w3.eth.getBlock(w3.eth.blockNumber - index)

        """Add block to Block model"""

        new_block = Block(
            fee=0.00087,
            nonce=block.nonce,
            n_tx=len(block.transactions),
            size=block.size,
            block_index=block.number,
            height=block.difficulty,
            received_time=block.timestamp,
            id=index,
            title="Block " + str(index),
            date_posted=timezone.localtime(timezone.now()),
            hash=block.hash,
            previous_block=block.receiptsRoot,
            merkle_root=block.parentHash,
            time=timezone.localtime(timezone.now())
        )

        new_block.save()
        print(count, "Record Block{} inserted successfully into blockchain_block table".format(index))

        count += 1

        """Take new transaction form web3 ethereum"""
        li = block.transactions
        for i in range(len(li)):
            transaction = w3.eth.getTransaction(li[i])

            new_transaction = Transaction(
                nonce=transaction.nonce,
                block_number=transaction.blockNumber,
                tx_index=transaction.transactionIndex,
                time=timezone.localtime(timezone.now()),
                value=transaction.value,
                gas=transaction.gas,
                gas_price=transaction.gasPrice,
                id=inc,
                title="Transaction " + str(inc),
                date_posted=timezone.localtime(timezone.now()),
                hash=transaction.hash,
                block_hash=transaction.blockHash,
                belonging_to=transaction['from'],
                relayed_by=transaction.to,
                inputs=transaction['input']
            )

            new_transaction.save()
            print(count, "Record Transaction{} inserted successfully into blockchain_transaction table".format(inc))

            inc += 1
            count += 1


if __name__ == '__main__':
    gather_ethereum_data()


"""Currently not in use"""
def insert_into_db_transaction(transaction, n):
    """Connection with Postgres"""

    try:
        connection = psycopg2.connect(user='blockchainuser', password='password', host='localhost', port="",
                                      database='blockchain')
        cur = connection.cursor()

        postgres_insert_query = """INSERT INTO blockchain_transaction (nonce, block_number, tx_index, time, value,
                                gas, gas_price, id, title, date_posted, hash, block_hash, belonging_to, relayed_by, inputs)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        insert_query = (transaction.nonce, transaction.blockNumber, transaction.transactionIndex,
                        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        transaction.value, transaction.gas, transaction.gasPrice, n, "Transaction " + str(n),
                        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        transaction.hash, transaction.blockHash, transaction['from'], transaction.to,
                        transaction['input'])

        cur.execute(postgres_insert_query, insert_query)

        connection.commit()
        count = cur.rowcount
        print(count, "Record Transaction{} inserted successfully into blockchain_transaction table".format(n))

    except (Exception, psycopg2.Error) as error:
        if (connection):
            print("Failed to INSERT into 'blockchain_transaction' table: ", error)

    finally:

        # closing database connection.
        if (connection):
            cur.close()
            connection.close()
            print("PostgreSQL connection is closed")


def insert_into_db_block(block, n):
    """Connection with Postgres"""

    try:
        connection = psycopg2.connect(user='blockchainuser', password='password', host='localhost', port="",
                                      database='blockchain')
        cur = connection.cursor()

        postgres_insert_query = """INSERT INTO blockchain_block (fee, nonce, n_tx, size, block_index, height,
                                received_time, id, title, date_posted, hash, previous_block, merkle_root, time)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        insert_query = (
            200, block.nonce, len(block.transactions), block.size, block.number, block.difficulty, block.timestamp,
            n, "Block " + str(n), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            block.hash, block.receiptsRoot, block.parentHash, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        cur.execute(postgres_insert_query, insert_query)

        connection.commit()
        count = cur.rowcount
        print(count, "Record Block{} inserted successfully into blockchain_block table".format(n))

    except (Exception, psycopg2.Error) as error:
        if (connection):
            print("Failed to INSERT into 'blockchain_block' table: ", error)

    finally:

        # closing database connection.
        if (connection):
            cur.close()
            connection.close()
            print("PostgreSQL connection is closed")
