aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

phones = ['apple', 'samsumg', 'oneplus']
phones_iter = iter(phones)
print(next(phones_iter))
