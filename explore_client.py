import os
from t_tech.invest import Client
from config import TOKEN
from utils import quotation_to_float

os.environ["SSL_TBANK_VERIFY"] = "true"

with Client(TOKEN) as client:

    # accounts = client.users.get_accounts()

    # for account in accounts.accounts:
    #     print(account.id, account.name)
        
    portfolio_brok = client.operations.get_portfolio(account_id="2262924871")
    portfolio_iis = client.operations.get_portfolio(account_id="2263033839")
    
    # volue_brok = quotation_to_float(portfolio_brok.total_amount_portfolio)
    # volue_iis = quotation_to_float(portfolio_iis.total_amount_portfolio)
    # volue_brok_iis = volue_brok + volue_iis
    # print(volue_brok, volue_iis, volue_brok_iis)
    
    for position in portfolio_brok.positions:
        print("=" * 40)
        print(position.instrument_uid)
        print(f"Количество: {quotation_to_float(position.quantity)}")     
        print(f"Средняя цена: {quotation_to_float(position.average_position_price)}")
        print(f"Цена: {quotation_to_float(position.current_price)}")
        print(f"Прибыль: {quotation_to_float(position.expected_yield)}")