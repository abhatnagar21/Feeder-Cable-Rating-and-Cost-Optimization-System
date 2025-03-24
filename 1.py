def get_cable_prices(feeder_voltage: float):
    # Dictionaries to store cable prices and ratings
    cable_prices = {}
    cable_ratings = {}
    combined_cables = {}

    if feeder_voltage == 11.0:
        # Taking price inputs for 11 kV feeder cables
        cables = ['3C-185', '1C-240', '1C-400', '1C-500', '1C-630']
        print('Enter the prices and ratings for 11 kV feeder cables:')
    elif feeder_voltage == 3.3:
        # Taking price inputs for 3.3 kV feeder cables
        cables = ['3C-150', '1C-150']
        print('Enter the prices and ratings for 3.3 kV feeder cables:')
    else:
        print('Invalid feeder voltage. Please enter 11 or 3.3.')
        return None

    # Taking price and rating inputs for the specified cables
    for cable in cables:
        while True:
            try:
                price = float(input(f'Price of {cable}: '))
                rating = int(input(f'Rating of {cable}: '))
                cable_prices[cable] = price
                cable_ratings[cable] = rating

                # Storing values for multiplied cables (2x and 3x)
                cable_prices[f'2_{cable}'] = 2 * price
                cable_ratings[f'2_{cable}'] = 2 * rating

                cable_prices[f'3_{cable}'] = 3 * price
                cable_ratings[f'3_{cable}'] = 3 * rating
                break
            except ValueError:
                print('Invalid input. Please enter valid numbers.')

    # Combine both original and multiplied cables
    combined_cables = {**cable_ratings}

    # Sorting cables by their ratings in ascending order
    sorted_cables = sorted(combined_cables.items(), key=lambda x: x[1])

    # Display all sorted cables
    print('\nAll cables sorted by rating:')
    for cable, rating in sorted_cables:
        print(f'{cable}: Price = {cable_prices[cable]} per meter, Rating = {rating}')

    # Loop for continuously asking current density
    while True:
        try:
            current_density = int(input('\nEnter the current density (or type -1 to exit): '))
            if current_density == -1:
                print('Exiting the program.')
                break

            # Displaying the cable with least price that meets or exceeds the current density
            suitable_cables = [(cable, cable_prices[cable], rating) for cable, rating in sorted_cables if rating >= current_density]
            if suitable_cables:
                best_cable = min(suitable_cables, key=lambda x: x[1])
                print(f'\nBest suitable cable for current density {current_density}:')
                print(f'{best_cable[0]}: Price = {best_cable[1]} per meter, Rating = {best_cable[2]}')
            else:
                print('No cable meets the required current density.')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

    return cable_prices, cable_ratings


if __name__ == "__main__":
    try:
        feeder_voltage = float(input('Enter the feeder voltage (11 or 3.3): '))
        get_cable_prices(feeder_voltage)
    except ValueError:
        print('Invalid input. Please enter a valid number.')
