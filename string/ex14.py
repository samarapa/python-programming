

items = raw_input("Enter the items")
words = [word for word in items.split(',')]
print(',' .join(sorted(list(set(words)))))
