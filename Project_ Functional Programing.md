# **Lesson 4: Functional Programming** 

## **Task 1: Lambda Functions with Movie Data**

### **Scenario**

You're building a movie recommendation system and need to process movie data using lambda functions.

### **The Dataset**

```py
movies = [
    {'title': 'The Matrix', 'year': 1999, 'rating': 8.7, 'genre': 'Sci-Fi'},
    {'title': 'Inception', 'year': 2010, 'rating': 8.8, 'genre': 'Thriller'},
    {'title': 'Pulp Fiction', 'year': 1994, 'rating': 8.9, 'genre': 'Crime'},
    {'title': 'The Godfather', 'year': 1972, 'rating': 9.2, 'genre': 'Crime'},
    {'title': 'Avatar', 'year': 2009, 'rating': 7.8, 'genre': 'Sci-Fi'},
    {'title': 'Titanic', 'year': 1997, 'rating': 7.8, 'genre': 'Romance'}
]
```

### **Your Tasks**

**Task 1a: Movie Sorting**

```py
# TODO: Sort movies by rating (highest first)
by_rating = sorted(movies, key=# YOUR CODE HERE)

# TODO: Sort movies by year (newest first) 
by_year = sorted(movies, key=# YOUR CODE HERE)

# Test your sorting
print("Highest rated:", by_rating[0]['title'])
print("Newest movie:", by_year[0]['title'])
```

**Expected Output:**

```py
Highest rated: The Godfather
Newest movie: Inception
```

**Task 1b: Movie Classification**

```py
# TODO: Create a lambda to classify movies by era
# - Year >= 2000: 'Modern'
# - Year >= 1990: 'Recent'  
# - Otherwise: 'Classic'
classify_era = lambda year: # YOUR CODE HERE

# TODO: Create a lambda to determine rating category
# - Rating >= 9.0: 'Masterpiece'
# - Rating >= 8.0: 'Excellent'
# - Otherwise: 'Good'
rating_category = lambda rating: # YOUR CODE HERE

# Test your lambdas
print("Movie Classifications:")
for movie in movies:
    era = classify_era(movie['year'])
    category = rating_category(movie['rating'])
    print(f"{movie['title']}: {era}, {category}")
```

**Expected Output:**

```py
Movie Classifications:
The Matrix: Recent, Excellent
Inception: Modern, Excellent
Pulp Fiction: Recent, Excellent
The Godfather: Classic, Masterpiece
Avatar: Modern, Good
Titanic: Recent, Good
```

## **Task 2: Map Function with Temperature Data**

### **Scenario**

A weather station has recorded temperatures in Celsius and needs them converted to Fahrenheit and Kelvin for international reports.

### **The Dataset**

```py
weather_data = [
    {'city': 'New York', 'temp_celsius': 22, 'humidity': 65},
    {'city': 'London', 'temp_celsius': 15, 'humidity': 80},
    {'city': 'Tokyo', 'temp_celsius': 28, 'humidity': 70},
    {'city': 'Sydney', 'temp_celsius': 18, 'humidity': 60},
    {'city': 'Dubai', 'temp_celsius': 35, 'humidity': 45}
]
```

### **Your Task**

**Temperature Conversion**

```py
# TODO: Use map() with lambda or user defined function to add Fahrenheit and Kelvin temperatures
# Formula: Fahrenheit = (Celsius × 9/5) + 32
# Formula: Kelvin = Celsius + 273.15
weather_converted = list(map(lambda data: # YOUR CODE HERE, weather_data))

# Test your result
print("Temperature Conversions:")
for data in weather_converted:
    print(f"{data['city']}:")
    print(f"  Celsius: {data['temp_celsius']}°C")
    print(f"  Fahrenheit: {data['temp_fahrenheit']:.1f}°F")
    print(f"  Kelvin: {data['temp_kelvin']:.1f}K")
```

**Expected Output:**

```py
Temperature Conversions:
New York:
  Celsius: 22°C
  Fahrenheit: 71.6°F
  Kelvin: 295.2K
London:
  Celsius: 15°C
  Fahrenheit: 59.0°F
  Kelvin: 288.2K
Tokyo:
  Celsius: 28°C
  Fahrenheit: 82.4°F
  Kelvin: 301.2K
Sydney:
  Celsius: 18°C
  Fahrenheit: 64.4°F
  Kelvin: 291.2K
Dubai:
  Celsius: 35°C
  Fahrenheit: 95.0°F
  Kelvin: 308.2K
```

## **Task 3: Filter Function with Customer Data**

### **Scenario**

An e-commerce company wants to identify premium customers for a special promotion based on their purchase history and account status.

### **The Dataset**

```py
customers = [
    {'name': 'Alice Johnson', 'total_spent': 1250, 'orders': 8, 'vip_member': True},
    {'name': 'Bob Smith', 'total_spent': 750, 'orders': 12, 'vip_member': False},
    {'name': 'Carol Davis', 'total_spent': 2100, 'orders': 15, 'vip_member': True},
    {'name': 'David Wilson', 'total_spent': 450, 'orders': 3, 'vip_member': False},
    {'name': 'Emma Brown', 'total_spent': 980, 'orders': 7, 'vip_member': False},
    {'name': 'Frank Miller', 'total_spent': 1800, 'orders': 20, 'vip_member': True}
]
```

### **Your Task**

**Premium Customer Identification**

```py
# TODO: Use filter() to find customers who qualify for premium promotion
# Criteria: (total_spent >= 1000 AND orders >= 5) OR vip_member == True
premium_customers = list(filter(# YOUR CODE HERE, customers))

# Test your result
print("Premium Customers for Special Promotion:")
for customer in premium_customers:
    print(f"  {customer['name']} - Spent: ${customer['total_spent']}, Orders: {customer['orders']}")
```

**Expected Output:**

```py
Premium Customers for Special Promotion:
  Alice Johnson - Spent: $1250, Orders: 8
  Carol Davis - Spent: $2100, Orders: 15
  Frank Miller - Spent: $1800, Orders: 20
```

## **Task 4: List Comprehensions with Sales Data**

### **Scenario**

A retail analytics team needs to process quarterly sales data to generate insights and reports.

### **The Dataset**

```py
sales_data = [
    {'product': 'Laptop', 'q1': 150, 'q2': 180, 'q3': 160, 'q4': 200},
    {'product': 'Mouse', 'q1': 300, 'q2': 280, 'q3': 320, 'q4': 350},
    {'product': 'Keyboard', 'q1': 200, 'q2': 190, 'q3': 210, 'q4': 230},
    {'product': 'Monitor', 'q1': 80, 'q2': 95, 'q3': 85, 'q4': 110},
    {'product': 'Headphones', 'q1': 120, 'q2': 140, 'q3': 130, 'q4': 160}
]
```

### **Your Tasks**

**Task 4a: Calculate Annual Totals**

```py
# TODO: Use list comprehension to create a new list with annual totals
# Include product name and total_sales
# [{'product': <product name>, 'total_sales': q1 + q2 + q3 + q4}]

annual_sales = [# YOUR CODE HERE for product in sales_data]

# Test your result
print("Annual Sales Totals:")
for item in annual_sales:
    print(f"  {item['product']}: {item['total_sales']} units")
```

**Expected Output:**

```py
Annual Sales Totals:
  Laptop: 690 units
  Mouse: 1250 units
  Keyboard: 830 units
  Monitor: 370 units
  Headphones: 550 units
```

**Task 4b: Find High-Performing Products**

```py
# TODO: Use list comprehension to find products with total sales > 600
# Return just the product names
high_performers = [# YOUR CODE HERE for product in sales_data # YOUR CONDITION HERE]

# Test your result
print("High-Performing Products (>600 units):")
for product in high_performers:
    print(f"  {product}")
```

**Expected Output:**

```py
High-Performing Products (>600 units):
  Laptop
  Mouse
  Keyboard
```

**Task 4c: Growth Analysis**

```py
# TODO: Use list comprehension to calculate Q4 vs Q1 growth percentage
# Formula: ((Q4 - Q1) / Q1) * 100
# Include products that had positive growth
growth_analysis = [# YOUR CODE HERE for product in sales_data # YOUR CONDITION HERE]

# Test your result
print("Products with Positive Growth (Q4 vs Q1):")
for item in growth_analysis:
    print(f"  {item['product']}: {item['growth_percentage']:.1f}% growth")
```

**Expected Output:**

```py
Products with Positive Growth (Q4 vs Q1):
  Laptop: 33.3% growth
  Mouse: 16.7% growth
  Keyboard: 15.0% growth
  Monitor: 37.5% growth
  Headphones: 33.3% growth
```

## **Submission Requirements**

### **What to Submit**

1. **Complete Python file** with all your solutions  
2. **Test output** showing all functions work correctly

