from t_tech.invest.schemas import AccountType


def account_type_name(account_type: AccountType) -> str:

    mapping = {

        AccountType.ACCOUNT_TYPE_TINKOFF: "Брокерский счет",

        AccountType.ACCOUNT_TYPE_TINKOFF_IIS: "ИИС",

        AccountType.ACCOUNT_TYPE_INVEST_BOX: "Инвесткопилка",

        AccountType.ACCOUNT_TYPE_DFA: "Смарт-счет",

    }

    return mapping.get(account_type, "Неизвестный тип")