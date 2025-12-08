

betsy_info = {
    'Name': 'Betsy Foobar',
    'Phone': 'x8012',
    'Street': '1600 Grand Avenue',
    'City': 'Saint Paul',
    'State': 'MN',
    'Email': 'bfoobar@macalester.edu'
}

tom_info = {
    'Name': 'Tom Riddle',
    'Phone': 'x8512',
    'Street': '1600 Grand Avenue',
    'City': 'Saint Paul',
    'State': 'MN',
    'Email': 'triddle@macalester.edu'
}

address_book = [
    betsy_info,
    tom_info,
    {
        'Name': 'Susan Fox',
        'Phone': 'x6553',
        'Street': '1600 Grand Avenue',
        'City': 'Saint Paul',
        'State': 'MN',
        'Email': 'fox@macalester.edu'
    }
]


print("Original address book:")
print(address_book)


address_book.append({
    'Name': 'John Carter',
    'Phone': '555-1111',
    'Street': '123 Lake St',
    'City': 'Minneapolis',
    'State': 'MN',
    'Email': 'john@example.com'
})

address_book.append({
    'Name': 'Lisa Gomez',
    'Phone': '555-2222',
    'Street': '500 Summit Ave',
    'City': 'Chicago',
    'State': 'IL',
    'Email': 'lisa@example.com'
})


def filter_by_city(city, book):
    return [entry for entry in book if entry['City'] == city]


print("\nFiltered for Saint Paul:")
print(filter_by_city("Saint Paul", address_book))
