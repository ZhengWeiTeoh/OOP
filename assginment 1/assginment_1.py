import csv

def read_transactions(file_path):
    transactions = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row)
    return transactions

#remove empty and duplicates from the transactions list
def clean_transactions(transactions):
    cleaned = {}
    for txn in transactions:
        if not all(txn[key] for key in ['date', 'client_id', 'card_id', 'amount', 'merchant_id', 'merchant_city', 'use_chip']):
            continue
        
        try:
            txn['amount'] = float(txn['amount'].replace('$', ''))
            if txn['amount'] < 0:
                continue
        except ValueError:
            continue
        
        key = (txn['date'], txn['client_id'], txn['card_id'], txn['amount'])
        if key not in cleaned or txn['date'] > cleaned[key]['date']:
            cleaned[key] = txn
    
    return list(cleaned.values())

#remove error in merchant_city and use_chip columns
def validate_transactions(transactions):
    valid_transactions = []
    for txn in transactions:
        if txn['use_chip'] not in ('Swipe Transaction', 'Online Transaction'):
            continue
        if (txn['use_chip'] == 'Online Transaction' and txn['merchant_city'] != 'ONLINE' or 'Online' or 'online') or\
           (txn['use_chip'] == 'Swipe Transaction' and txn['merchant_city'] == 'ONLINE' or 'Online' or 'online'):
            continue
        valid_transactions.append(txn)
    return valid_transactions

#reformat date from YYYY MM DD to DD MM YYYY
def reformat_date(transactions):
    for txn in transactions:
        date_parts = txn['date'].split(' ')
        y, m, d = date_parts[0].split('-')
        txn['date'] = f"{d}-{m}-{y} {date_parts[1]}"

#sort the data
def sort_transactions(transactions):
    return sorted(transactions, key=lambda x: (x['merchant_id'], x['date'], x['client_id']))

#save result to csv file
def save_transactions(file_path, transactions):
    if not transactions:
        return
    with open(file_path, 'w', newline = '') as file:
        writer = csv.DictWriter(file, fieldnames=transactions[0].keys())
        writer.writeheader()
        for txn in transactions:
            txn['amount'] = f"${txn['amount']:.2f}" 
            writer.writerow(txn)

def main():
    input_file = 'transactions.csv'
    output_file = 'processed_transactions.csv'
    
    transactions = read_transactions(input_file)
    transactions = clean_transactions(transactions)
    transactions = validate_transactions(transactions)
    reformat_date(transactions)
    transactions = sort_transactions(transactions)
    save_transactions(output_file, transactions)
    
    print("Output saved to", output_file, end='')

main()
