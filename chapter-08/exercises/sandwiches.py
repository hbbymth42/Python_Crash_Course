def make_sandwich(*items):
    print("\nThe following items were ordered for your sandwich:")
    for item in items:
        print(f"- {item.title()}")

make_sandwich('cheese')
make_sandwich('tuna', 'pickles')
make_sandwich('bacon', 'lettuce', 'tomato')