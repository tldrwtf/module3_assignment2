

# Import colorama for colorful output
from colorama import init, Fore, Back, Style
init(autoreset=True)

# The Dataset
movies = [
    {'title': 'The Matrix', 'year': 1999, 'rating': 8.7, 'genre': 'Sci-Fi'},
    {'title': 'Inception', 'year': 2010, 'rating': 8.8, 'genre': 'Thriller'},
    {'title': 'Pulp Fiction', 'year': 1994, 'rating': 8.9, 'genre': 'Crime'},
    {'title': 'The Godfather', 'year': 1972, 'rating': 9.2, 'genre': 'Crime'},
    {'title': 'Avatar', 'year': 2009, 'rating': 7.8, 'genre': 'Sci-Fi'},
    {'title': 'Titanic', 'year': 1997, 'rating': 7.8, 'genre': 'Romance'}
]

# Your Tasks
# Task 1a: Movie Sorting
# TODO: Sort movies by rating (highest first)
by_rating = sorted(movies, key=lambda movie: movie['rating'], reverse=True)

# TODO: Sort movies by year (newest first)
by_year = sorted(movies, key=lambda movie: movie['year'], reverse=True)

# Test your sorting
print(f"{Fore.CYAN}🎬 Movie Sorting Results:{Style.RESET_ALL}")
print(f"{Fore.GREEN}Highest rated: {Fore.YELLOW}{by_rating[0]['title']}{Style.RESET_ALL}")
print(f"{Fore.GREEN}Newest movie: {Fore.YELLOW}{by_year[0]['title']}{Style.RESET_ALL}")

# Expected Output:
# Highest rated: The Godfather
# Newest movie: Inception

# Task 1b: Movie Classification
# TODO: Create a lambda to classify movies by era
# - Year >= 2000: 'Modern'
# - Year >= 1990: 'Recent'
# - Otherwise: 'Classic'
classify_era = lambda year: 'Modern' if year >= 2000 else ('Recent' if year >= 1990 else 'Classic')

# TODO: Create a lambda to determine rating category
# - Rating >= 9.0: 'Masterpiece'
# - Rating >= 8.0: 'Excellent'
# - Otherwise: 'Good'
rating_category = lambda rating: 'Masterpiece' if rating >= 9.0 else ('Excellent' if rating >= 8.0 else 'Good')

# Test your lambdas
print(f"\n{Fore.MAGENTA}🎭 Movie Classifications:{Style.RESET_ALL}")
for movie in movies:
    era = classify_era(movie['year'])
    category = rating_category(movie['rating'])
    
    # Color coding for eras
    era_color = Fore.BLUE if era == 'Modern' else Fore.GREEN if era == 'Recent' else Fore.YELLOW
    
    # Color coding for categories
    category_color = Fore.RED if category == 'Masterpiece' else Fore.CYAN if category == 'Excellent' else Fore.WHITE
    
    print(f"{Fore.WHITE}{movie['title']}: {era_color}{era}{Style.RESET_ALL}, {category_color}{category}{Style.RESET_ALL}")

# Expected Output:
# Movie Classifications:
# The Matrix: Recent, Excellent
# Inception: Modern, Excellent
# Pulp Fiction: Recent, Excellent
# The Godfather: Classic, Masterpiece
# Avatar: Modern, Good
# Titanic: Recent, Good

# Task 2: Map Function with Temperature Data
# Scenario
# A weather station has recorded temperatures in Celsius and needs them converted to Fahrenheit and Kelvin for international reports.
# The Dataset
weather_data = [
    {'city': 'New York', 'temp_celsius': 22, 'humidity': 65},
    {'city': 'London', 'temp_celsius': 15, 'humidity': 80},
    {'city': 'Tokyo', 'temp_celsius': 28, 'humidity': 70},
    {'city': 'Sydney', 'temp_celsius': 18, 'humidity': 60},
    {'city': 'Dubai', 'temp_celsius': 35, 'humidity': 45}
]

# Your Task
# Temperature Conversion
# TODO: Use map() with lambda or user defined function to add Fahrenheit and Kelvin temperatures
# Formula: Fahrenheit = (Celsius × 9/5) + 32
# Formula: Kelvin = Celsius + 273.15
weather_converted = list(map(lambda data: {
    'city': data['city'],
    'temp_celsius': data['temp_celsius'],
    'humidity': data['humidity'],
    'temp_fahrenheit': (data['temp_celsius'] * 9/5) + 32,
    'temp_kelvin': data['temp_celsius'] + 273.15
}, weather_data))

# Test your result
print(f"\n{Fore.CYAN}🌡️  Temperature Conversions:{Style.RESET_ALL}")
for data in weather_converted:
    print(f"{Fore.YELLOW}{data['city']}:{Style.RESET_ALL}")
    print(f"  {Fore.BLUE}Celsius: {Fore.WHITE}{data['temp_celsius']}°C{Style.RESET_ALL}")
    print(f"  {Fore.RED}Fahrenheit: {Fore.WHITE}{data['temp_fahrenheit']:.1f}°F{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}Kelvin: {Fore.WHITE}{data['temp_kelvin']:.1f}K{Style.RESET_ALL}")

# Expected Output:
# Temperature Conversions:
# New York:
#   Celsius: 22°C
#   Fahrenheit: 71.6°F
#   Kelvin: 295.2K
# London:
#   Celsius: 15°C
#   Fahrenheit: 59.0°F
#   Kelvin: 288.2K
# Tokyo:
#   Celsius: 28°C
#   Fahrenheit: 82.4°F
#   Kelvin: 301.2K
# Sydney:
#   Celsius: 18°C
#   Fahrenheit: 64.4°F
#   Kelvin: 291.2K
# Dubai:
#   Celsius: 35°C
#   Fahrenheit: 95.0°F
#   Kelvin: 308.2K

# Task 3: Filter Function with Customer Data
# Scenario
# An e-commerce company wants to identify premium customers for a special promotion based on their purchase history and account status.
# The Dataset
customers = [
    {'name': 'Alice Johnson', 'total_spent': 1250, 'orders': 8, 'vip_member': True},
    {'name': 'Bob Smith', 'total_spent': 750, 'orders': 12, 'vip_member': False},
    {'name': 'Carol Davis', 'total_spent': 2100, 'orders': 15, 'vip_member': True},
    {'name': 'David Wilson', 'total_spent': 450, 'orders': 3, 'vip_member': False},
    {'name': 'Emma Brown', 'total_spent': 980, 'orders': 7, 'vip_member': False},
    {'name': 'Frank Miller', 'total_spent': 1800, 'orders': 20, 'vip_member': True}
]

# Your Task
# Premium Customer Identification
# TODO: Use filter() to find customers who qualify for premium promotion
# Criteria: (total_spent >= 1000 AND orders >= 5) OR vip_member == True
premium_customers = list(filter(lambda customer: (customer['total_spent'] >= 1000 and customer['orders'] >= 5) or customer['vip_member'] == True, customers))

# Test your result
print(f"\n{Fore.MAGENTA}👑 Premium Customers for Special Promotion:{Style.RESET_ALL}")
for customer in premium_customers:
    # Highlight VIP members differently
    if customer['vip_member']:
        print(f"  {Back.YELLOW}{Fore.BLACK}VIP{Style.RESET_ALL} {Fore.CYAN}{customer['name']}{Style.RESET_ALL} - Spent: {Fore.GREEN}${customer['total_spent']}{Style.RESET_ALL}, Orders: {Fore.YELLOW}{customer['orders']}{Style.RESET_ALL}")
    else:
        print(f"  {Fore.CYAN}{customer['name']}{Style.RESET_ALL} - Spent: {Fore.GREEN}${customer['total_spent']}{Style.RESET_ALL}, Orders: {Fore.YELLOW}{customer['orders']}{Style.RESET_ALL}")

# Expected Output:
# Premium Customers for Special Promotion:
#   Alice Johnson - Spent: $1250, Orders: 8
#   Carol Davis - Spent: $2100, Orders: 15
#   Frank Miller - Spent: $1800, Orders: 20

# Task 4: List Comprehensions with Sales Data
# Scenario
# A retail analytics team needs to process quarterly sales data to generate insights and reports.
# The Dataset
sales_data = [
    {'product': 'Laptop', 'q1': 150, 'q2': 180, 'q3': 160, 'q4': 200},
    {'product': 'Mouse', 'q1': 300, 'q2': 280, 'q3': 320, 'q4': 350},
    {'product': 'Keyboard', 'q1': 200, 'q2': 190, 'q3': 210, 'q4': 230},
    {'product': 'Monitor', 'q1': 80, 'q2': 95, 'q3': 85, 'q4': 110},
    {'product': 'Headphones', 'q1': 120, 'q2': 140, 'q3': 130, 'q4': 160}
]

# Your Tasks
# Task 4a: Calculate Annual Totals
# TODO: Use list comprehension to create a new list with annual totals
# Include product name and total_sales
# [{'product': <product name>, 'total_sales': q1 + q2 + q3 + q4}]
annual_sales = [{'product': product['product'], 'total_sales': product['q1'] + product['q2'] + product['q3'] + product['q4']} for product in sales_data]

# Test your result
print(f"\n{Fore.GREEN}📊 Annual Sales Totals:{Style.RESET_ALL}")
for item in annual_sales:
    # Color based on sales volume
    if item['total_sales'] > 1000:
        color = Fore.RED  # High sales
    elif item['total_sales'] > 600:
        color = Fore.YELLOW  # Medium sales
    else:
        color = Fore.WHITE  # Low sales
    
    print(f"  {Fore.CYAN}{item['product']}: {color}{item['total_sales']} units{Style.RESET_ALL}")

# Expected Output:
# Annual Sales Totals:
#   Laptop: 690 units
#   Mouse: 1250 units
#   Keyboard: 830 units
#   Monitor: 370 units
#   Headphones: 550 units

# Task 4b: Find High-Performing Products
# TODO: Use list comprehension to find products with total sales > 600
# Return just the product names
high_performers = [product['product'] for product in annual_sales if product['total_sales'] > 600]

# Test your result
print(f"\n{Fore.YELLOW}🚀 High-Performing Products (>600 units):{Style.RESET_ALL}")
for product in high_performers:
    print(f"  {Fore.GREEN}✓ {product}{Style.RESET_ALL}")

# Expected Output:
# High-Performing Products (>600 units):
#   Laptop
#   Mouse
#   Keyboard

# Task 4c: Growth Analysis
# TODO: Use list comprehension to calculate Q4 vs Q1 growth percentage
# Formula: ((Q4 - Q1) / Q1) * 100
# Include products that had positive growth
growth_analysis = [{'product': product['product'], 'growth_percentage': ((product['q4'] - product['q1']) / product['q1']) * 100} for product in sales_data if product['q4'] > product['q1']]

# Test your result
print(f"\n{Fore.MAGENTA}📈 Products with Positive Growth (Q4 vs Q1):{Style.RESET_ALL}")
for item in growth_analysis:
    # Color based on growth percentage
    if item['growth_percentage'] > 30:
        growth_color = Fore.RED  # High growth
    elif item['growth_percentage'] > 20:
        growth_color = Fore.YELLOW  # Medium growth
    else:
        growth_color = Fore.GREEN  # Low growth
    
    print(f"  {Fore.CYAN}{item['product']}: {growth_color}{item['growth_percentage']:.1f}% growth{Style.RESET_ALL}")

# Expected Output:
# Products with Positive Growth (Q4 vs Q1):
#   Laptop: 33.3% growth
#   Mouse: 16.7% growth
#   Keyboard: 15.0% growth
#   Monitor: 37.5% growth
#   Headphones: 33.3% growth

# Submission Requirements
# What to Submit
# 1. Complete Python file with all your solutions
# 2. Test output showing all functions work correctly