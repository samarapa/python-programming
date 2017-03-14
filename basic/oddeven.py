def evenodd(v):
    if (v%2==0):
        return "It's EVEN"
    else:
        return "It's ODD"


v=int(raw_input("Enter the number : "))

print(evenodd(v))
