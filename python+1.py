class A:
    def a(self, change):
        print(id(change))
        change = change.upper().lower()
        print(id(change))