import os

from t_tech.invest import Client

from config import TOKEN
from invest_sdk.money import Money

os.environ["SSL_TBANK_VERIFY"] = "true"


def main():
    with Client(TOKEN) as client:
        accounts = client.users.get_accounts()
        d = {}
        for i in range(2):
            account = accounts.accounts[i]
            account_name = account.name
            for position in client.operations.get_portfolio(account_id=account.id).positions:
                if position.instrument_type == "share":
                    temp_dict = {"Цена": Money.format(Money.to_decimal(position.current_price)),
                                 "Кол-во": position.quantity.units,
                                }
                    if account_name not in d:
                        d[account_name] = [temp_dict]
                    else:
                        d[account_name].append(temp_dict)
                # d[account_name] = {position[n].ticker: {"Цена": Money.format(Money.to_decimal(position[n].current_price)),
                #                                         "Кол-во": position[n].quantity.units,
                #                                         }}
            # print(position[0].ticker)

        print(d)
        #                                   "Кол-во": position.quantity.units,
        #                                   }}
            # for portfolio in client.operations.get_portfolio(account_id=accounts.accounts[i].id).positions:
            #     print(portfolio)


        # account_bro = accounts.accounts[0]
        # account_iis = accounts.accounts[1]
        #
        # portfolio_bro = client.operations.get_portfolio(account_id=account_bro.id)
        # portfolio_iis = client.operations.get_portfolio(account_id=account_iis.id)
        #
        # total_value_bro = Money.to_decimal(portfolio_bro.total_amount_shares)
        #
        # d_bro, d_iis, d_all = {}, {}, {}
        # for position in portfolio_bro.positions:
        #     if position.instrument_type == "share":
        #         d_bro[position.ticker] = {"Цена": Money.format(Money.to_decimal(position.current_price)),
        #                                   "Кол-во": position.quantity.units,
        #                                   }
        #
        # for position in portfolio_iis.positions:
        #     if position.instrument_type == "share":
        #         d_iis[position.ticker] = {"Цена": Money.format(Money.to_decimal(position.current_price)),
        #                                   "Кол-во": position.quantity.units,
        #                                   }
        #
        # for i in range(len(d_iis)):
        #     pass
        # print(total_value)
        # print(type(total_value))


if __name__ == "__main__":
    main()
