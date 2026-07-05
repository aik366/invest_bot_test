def quotation_to_float(q):
    """Преобразует Quotation в float."""
    return q.units + q.nano / 1_000_000_000