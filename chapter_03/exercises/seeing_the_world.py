places = ['Japan', 'Portugal', 'New Zealand', 'Singapore', 'Germany']
print(places) # Original Order
print(sorted(places)) # Sorted
print(places) # Original Order
print(sorted(places, reverse=True)) # Reverse Sorted
print(places) # Original Order
places.reverse()
print(places) # Reverse Sorted (Alter Original)
places.reverse()
print(places) # Reverse Sorted (Return to Original)
places.sort()
print(places) # Sorted (Alter Original)
places.sort(reverse=True)
print(places) # Reverse Sorted (Alter Original using sort())