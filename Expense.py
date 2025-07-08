class Expense:
    def __init__(self, id, description, amount, category, date):
        self.id = id
        self.description = description
        self.amount = amount
        self.category = category
        self.date = date

    def __repr__(self):
        return (f"Expense(id={self.id}, description={self.description}, amount={self.amount}, category={self.category}"
                f", date={self.date})")

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'amount': self.amount,
            'category': self.category,
            'date': self.date
        }
