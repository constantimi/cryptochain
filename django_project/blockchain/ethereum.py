import datetime

import psycopg2
from web3.auto.infura import w3


# https://ethereum.stackexchange.com/questions/19665/how-to-calculate-transaction-fee


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


def main():
    """Is connected with Database"""
    print(w3.isConnected())
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    """Adds blocks and transaction into Database"""
    inc = 0
    for index in range(30):
        block = w3.eth.getBlock(w3.eth.blockNumber - index)
        insert_into_db_block(block, index)
        li = block.transactions
        for i in range(len(li)):
            transaction = w3.eth.getTransaction(li[i])
            insert_into_db_transaction(transaction, inc)
            inc += 1


if __name__ == '__main__':
    main()
