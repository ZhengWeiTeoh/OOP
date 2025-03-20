import csv

def read_transactions(file_path):
    transactions = []
    with open(file_path, mode='r',) as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row)
    return transactions

def clean_transactions(transactions):
    """Cleans the transactions list based on the given criteria."""
    cleaned = {}
    for txn in transactions:
        # Ensure required fields are present
        if not all(txn[key] for key in ['date', 'client_id', 'card_id', 'amount', 'merchant_id', 'merchant_city', 'use_chip']):
            continue
        
        # Remove $ sign and convert amount to float, check validity
        try:
            txn['amount'] = float(txn['amount'].replace('$', ''))
            if txn['amount'] < 0:
                continue
        except ValueError:
            continue
        
        # Create a unique key for duplicate detection
        key = (txn['date'], txn['client_id'], txn['card_id'], txn['amount'])
        if key not in cleaned or txn['date'] > cleaned[key]['date']:
            cleaned[key] = txn
    
    return list(cleaned.values())

def validate_transactions(transactions):
    """Validates the transactions based on use_chip and merchant_city rules."""
    valid_transactions = []
    for txn in transactions:
        if txn['use_chip'] not in ('Swipe Transaction', 'Online Transaction'):
            continue
        if (txn['use_chip'] == 'Online Transaction' and txn['merchant_city'] != 'ONLINE') or \
           (txn['use_chip'] == 'Swipe Transaction' and txn['merchant_city'] == 'ONLINE'):
            continue
        valid_transactions.append(txn)
    return valid_transactions

def reformat_date(transactions):
    """Reformats the transaction date from YYYY-MM-DD to DD-MM-YYYY manually."""
    for txn in transactions:
        date_parts = txn['date'].split(' ')
        y, m, d = date_parts[0].split('-')
        txn['date'] = f"{d}-{m}-{y} {date_parts[1]}"

def sort_transactions(transactions):
    """Sorts transactions by merchant_id, date, and client_id."""
    return sorted(transactions, key=lambda x: (x['merchant_id'], x['date'], x['client_id']))

def save_transactions(file_path, transactions):
    """Saves the processed transactions to a CSV file."""
    if not transactions:
        return
    with open(file_path, mode='w') as file:
        writer = csv.DictWriter(file, fieldnames=transactions[0].keys())
        writer.writeheader()
        writer.writerows(transactions)

def main():
    input_file = 'transactions.csv'
    output_file = 'processed_transactions.csv'
    
    transactions = read_transactions(input_file)
    transactions = clean_transactions(transactions)
    transactions = validate_transactions(transactions)
    reformat_date(transactions)
    transactions = sort_transactions(transactions)
    save_transactions(output_file, transactions)
    
    print("Output saved to", output_file)

main()



