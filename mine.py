from time import sleep, time
from hashlib import sha256


def sha256_str(text):
    '''Changes the hash to a hex digest so it can be read. 

    It hashes the given text using utf-8 encoding'''
    return sha256(str(text).encode('utf-8')).hexdigest()


def mine_naive(transaction, last_hash, n=4, t=5):
    '''
    Parameters:
    hash : string
        previous transaction hash
    transaction : string
        content of the transaction. (e.g.: json format)
    n : int
        how many zeros the hash must start with.
        Default is 4. With 7 zeros takes many hours in a normal computer
    t : int
        minimum number of seconds the mining must take
    '''
    # MAX nonce just in case it starts to take too long
    MAX_NONCE = 10**100

    prefix_zeros = '0'*n
    start = time()
    now = time()
    current = ''
    nonce = -1
    while not current.startswith(prefix_zeros) and nonce < MAX_NONCE:
        nonce += 1
        current = sha256_str(transaction + last_hash + str(nonce))
        now = time()
    try:
        # This waits in case the mining is done before the minimum seconds set
        sleep(t - (now - start))
    except ValueError:
        # This means the given time has already passed
        pass
    print('\nMining time: {:.2f} s'.format(time() - start))
    print('Real mining time: {:.2f} s'.format(now - start))
    print('Nonce: {}'.format(nonce))
    print('Hash: {}'.format(current))
    return current


if __name__ == '__main__':
    end = False
    while not end:
        if input('\n\nType 0 to exit. Anything else to continue: ') == '0':
            end = True
            break
        in_hash = input('Previous transaction hash: ')
        transaction = input('Transaction content: ')
        n = int(input('Zeros: '))
        t = int(input('Time (s): '))
        mine_naive(transaction, in_hash, n, t)
