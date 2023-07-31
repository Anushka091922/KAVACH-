txn = open(r'C:\Users\Ahmed\Desktop\indisafehackathon_part2\verify_transactions.csv', 'r')
txns = txn.readlines()[-1].split(',')
txn.close()
print(txns)