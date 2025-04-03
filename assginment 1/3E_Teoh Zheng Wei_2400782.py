import csv

def read_transactions(file_path):
    transactions = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row)
    return transactions

#remove duplicate, empty and negative values
def clean_transactions(transactions):
    cleaned = {}
    for data in transactions:
        if not all(data[key] for key in ['date', 'client_id', 'card_id', 'amount', 'merchant_id', 'merchant_city', 'use_chip']):
            continue
        
        try:
            data['amount'] = float(data['amount'].replace('$', ''))
            if data['amount'] < 0:
                continue
        except ValueError:
            continue
        
        key = (data['date'], data['client_id'], data['card_id'], data['amount'])
        if key not in cleaned or data['date'] > cleaned[key]['date']:
            cleaned[key] = data
    
    return list(cleaned.values())

#validate use_chip
def validate_transactions(transactions):
    valid_transactions = []
    for use_chip in transactions:
        if use_chip['use_chip'] not in ('Swipe Transaction', 'Online Transaction'):
            continue
        if (use_chip['use_chip'] == 'Online Transaction' and use_chip['merchant_city'] != 'ONLINE' and use_chip['merchant_city'] != 'Online' and use_chip['merchant_city'] != 'online') or\
           (use_chip['use_chip'] == 'Swipe Transaction' and use_chip['merchant_city'] == 'ONLINE' and use_chip['merchant_city'] == 'Online' and use_chip['merchant_city'] == 'online'):
            continue
        valid_transactions.append(use_chip)
    return valid_transactions

#reformat date
def reformat_date(transactions):
    for date in transactions:
        date_parts = date['date'].split(' ')
        y, m, d = date_parts[0].split('-')
        date['date'] = f"{d}-{m}-{y} {date_parts[1]}"

#sort the data
def sort_transactions(transactions):
    return sorted(transactions, key=lambda x: (x['merchant_id'], x['date'], x['client_id']))

#export final result
def save_transactions(file_path, transactions):
    if not transactions:
        return
    with open(file_path, 'w', newline = '') as file:
        writer = csv.DictWriter(file, fieldnames=transactions[0].keys())
        writer.writeheader()
        for money in transactions:
            money['amount'] = f"${money['amount']:.2f}" 
            writer.writerow(money)

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
