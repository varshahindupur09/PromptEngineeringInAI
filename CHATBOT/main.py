import streamlit as st
import requests
import json

# Function to get response from Ollama Gemma:2B
def get_llm_response(query):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "foodking-assistant",
        "prompt": query
    }

    try:
        response = requests.post(url, json=payload, stream=True)
        response.raise_for_status()  # Ensure we raise an error for bad status codes
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
        return None

    full_response = ""

    try:
        for line in response.iter_lines():
            if line:
                json_line = json.loads(line.decode('utf-8'))
                full_response += json_line.get("response", "")
                if json_line.get("done"):
                    break
    except json.JSONDecodeError as e:
        st.error(f"JSON decode failed: {e}")
        return None

    return full_response

# Initializing the cart
if 'cart' not in st.session_state:
    st.session_state['cart'] = []

# Function to reset session state
def reset_session():
    st.session_state['cart'] = []

# Streamlit app
st.set_page_config(layout="wide")

st.title("FoodKing Restaurant")
st.write("Ask about Food King restaurant menu on our latest new chatbot and place pickup orders.")

# Using columns for layout
menu_col, cart_col, bot_col = st.columns([4, 2, 2])

with menu_col:
    # Defining menu categories and items with sizes
    menu = {
        "Pizzas": {
            "Cheese Pizza": {"SM": 9.49, "LG": 14.49},
            "House Special Pizza": {"SM": 11.49, "LG": 18.49},
            "Veggie Deluxe Pizza": {"SM": 11.49, "LG": 18.99},
        },
        "Calzones": {
            "Cheese Calzone": {"JR": 9.49, "SM": 17.49, "LG": 27.49},
            "Steak Bomb Calzone": {"JR": 14.99, "SM": 19.99, "LG": 30.99},
        },
        "Appetizers": {
            "French Fries": {"SM": 3.99, "LG": 5.49},
            "Mozzarella Sticks with Marinara": {"SM": 6.49, "LG": 11.49},
        },
        "Wings Express": {
            "Boneless Wings": {"SM": 12.99, "MD": 18.90, "LG": 26.49, "Tray": 52.49},
            "Traditional Wings": {"SM": 9.49, "MD": 17.99, "LG": 24.49, "Tray": 47.49},
        },
        "Super Subs": {
            "Italian Cold Cut": {"One Size": 28.49},
            "Ham & Cheese": {"One Size": 27.49},
            "American Cold Cut": {"One Size": 28.49},
            "Turkey": {"One Size": 30.49},
            "Roast Beef": {"One Size": 31.49},
            "Tuna Salad": {"One Size": 28.49},
            "Chicken Salad": {"One Size": 28.49},
        },
        "Hot Subs": {
            "Steak": {"SM": 7.49, "MD": 9.99, "LG": 14.99},
            "Steak Combo": {"SM": 8.99, "MD": 11.49, "LG": 15.99},
            "Philly Steak": {"SM": 8.49, "MD": 10.49, "LG": 14.99},
            "Texas Steak & Cheese": {"SM": 8.49, "MD": 10.49, "LG": 14.99},
            "Steak & Cheese": {"SM": 8.49, "MD": 10.99, "LG": 15.99},
            "Hamburger": {"SM": 7.49, "MD": 8.99, "LG": 13.99},
            "Cheeseburger": {"SM": 7.99, "MD": 10.49, "LG": 14.99},
            "Baconburger": {"SM": 7.99, "MD": 9.99, "LG": 13.99},
            "Bacon Cheeseburger": {"SM": 8.99, "MD": 10.99, "LG": 15.99},
            "Hot Pastrami": {"SM": 7.99, "MD": 10.99, "LG": 15.99},
            "Meatball": {"SM": 6.99, "MD": 9.49, "LG": 14.99},
            "Meatball Parm": {"SM": 7.49, "MD": 10.49, "LG": 15.99},
            "Sausage, Peppers & Onions": {"SM": 8.49, "MD": 10.49, "LG": 15.99},
            "Eggplant Parm": {"SM": 7.49, "MD": 9.49, "LG": 14.99},
            "Veal Cutlet Parm": {"SM": 7.99, "MD": 10.49, "LG": 15.99},
            "Haddock": {"SM": 9.49, "MD": 13.99, "LG": 17.99},
            "Grilled Chicken": {"SM": 7.99, "MD": 9.99, "LG": 15.99},
            "Teriyaki Steak Tip": {"SM": 9.49, "MD": 11.49, "LG": 16.99},
            "Steakhouse Steak Tip": {"SM": 9.49, "MD": 11.49, "LG": 16.49},
        },
        "Roast Beefs Subs": {
            "Super Beef": {"One Size": 10.49},
            "Regular": {"One Size": 8.49},
            "Junior": {"One Size": 6.99},
            "Plate": {"One Size": 11.49},
            "Combo Plate": {"One Size": 13.99},
        },
        "Specialty Subs": {
            "Andrew's Spicy Italian": {"SM": 8.49, "MD": 10.49, "LG": 15.99},
            "The Stuffa": {"SM": 8.49, "MD": 10.49, "LG": 15.99},
            "Chicken Kabob": {"SM": 8.99, "MD": 11.49, "LG": 15.99},
            "Steak Tip Kabob": {"SM": 10.49, "MD": 13.99, "LG": 16.99},
            "Buffalo Finger": {"SM": 9.49, "MD": 12.99, "LG": 15.99},
            "Russian Turkey Melt": {"SM": 9.49, "MD": 12.99, "LG": 15.99},
            "Imperial Combo": {"SM": 9.49, "MD": 11.49, "LG": 15.99},
            "Steak Bomb": {"SM": 9.49, "MD": 12.99, "LG": 15.99},
            "Nicholas Combo": {"SM": 8.99, "MD": 11.49, "LG": 15.99},
            "Vegetarian": {"SM": 8.49, "MD": 10.49, "LG": 13.99},
            "Krissy Vegi": {"SM": 8.49, "MD": 10.49, "LG": 14.99},
            "Chicken Vegi": {"SM": 8.99, "MD": 11.49, "LG": 15.99},
            "Chicken Broccoli Negi": {"SM": 9.49, "MD": 12.99, "LG": 19.99},
            "Hamas Subs": {"SM": 8.49, "MD": 10.49, "LG": 14.99},
        },
        "Specialty Wraps": {
            "Vermont Street": {"One Size": 10.99},
            "Center Street": {"One Size": 10.99},
            "Steak Tip Special": {"One Size": 13.49},
            "Chicken Special": {"One Size": 11.49},
            "Steak Tips Golds": {"One Size": 12.99},
            "Chicken Golds": {"One Size": 11.49},
            "Chicken Kabob": {"One Size": 12.99},
            "Amanda": {"One Size": 11.49},
            "Park Street": {"One Size": 11.49},
            "Hamas Wrap": {"One Size": 12.99},
        },
        "Paninis": {
            "Bobby": {"One Size": 13.99},
            "Lorena": {"One Size": 13.99},
            "Godson": {"One Size": 13.99},
            "Godfather": {"One Size": 13.99},
            "Giovanni": {"One Size": 13.99},
            "Tony": {"One Size": 13.99},
            "Frankie": {"One Size": 13.99},
        },
        "Fresh Burgers": {
            "Hamburger": {"SM": 8.49, "LG": 11.49},
            "Cheeseburger": {"SM": 9.49, "LG": 12.99},
            "Bacon Cheeseburger": {"SM": 9.99, "LG": 13.99},
            "Bleu Cheeseburger": {"SM": 9.99, "LG": 13.99},
            "Mushroom Swiss": {"SM": 9.99, "LG": 13.99},
            "BBQ Bacon Cheeseburger": {"SM": 9.99, "LG": 13.99},
        },
        "Salads": {
            "Garden": {"One Size": 8.99},
            "Grilled Chicken Garden": {"One Size": 12.99},
            "Tuna Garden": {"One Size": 11.49},
            "Turkey Garden": {"One Size": 12.49},
            "Garden Chicken Salad": {"One Size": 11.49},
            "Buffalo Chicken Salad": {"One Size": 12.99},
            "Steakhouse Tips Garden": {"One Size": 14.99},
            "Teriyaki Tips Garden": {"One Size": 14.99},
            "Chefs": {"One Size": 12.99},
            "Antipasto": {"One Size": 12.99},
            "Greek": {"One Size": 9.99},
            "Grilled Chicken Greek": {"One Size": 13.99},
            "Teriyaki Tips Greek": {"One Size": 15.99},
            "Steakhouse Tips Greek": {"One Size": 15.99},
            "Caesar": {"One Size": 9.49},
            "Grilled Chicken Caesar": {"One Size": 11.49},
            "Steakhouse Tips Caesar": {"One Size": 15.99},
            "Teriyaki Tips Caesar": {"One Size": 15.99},
            "Buffalo Chicken Caesar": {"One Size": 13.99},
        },
        "Salad Wraps": {
            "Garden": {"One Size": 8.99},
            "Grilled Chicken Garden": {"One Size": 12.99},
            "Tuna Garden": {"One Size": 12.49},
            "Turkey Garden": {"One Size": 12.49},
            "Garden Chicken Salad": {"One Size": 11.49},
            "Buffalo Chicken Garden": {"One Size": 12.99},
            "Steakhouse Tips Garden": {"One Size": 14.99},
            "Teriyaki Tips Garden": {"One Size": 14.99},
            "Chefs": {"One Size": 12.99},
            "Caesar": {"One Size": 9.49},
            "Antipasto": {"One Size": 12.99},
            "Greek": {"One Size": 9.99},
            "Grilled Chicken Greek": {"One Size": 13.99},
            "Steakhouse Tips Greek": {"One Size": 15.99},
            "Teriyaki Tips Greek": {"One Size": 15.99},
        },
        "Dinner": {
            "Steak Tip": {"One Size": 17.99},
            "Wing Ding": {"One Size": 15.99},
            "Chicken Plate": {"One Size": 12.99},
            "Chicken Tender": {"One Size": 12.49},
            "Grilled Chicken Kebab": {"One Size": 15.99},
            "Lo-Crab Chicken Plate": {"One Size": 12.99},
            "Lo-Crab Steak Tip": {"One Size": 16.99},
            "Teriyaki Chicken": {"One Size": 15.99},
            "Chicken & Steak Combo": {"One Size": 20.99},
        },
        "Red Sauce Dinners & Saute Pasta Dishes": {
            "Pasta Marinara": {"One Size": 8.49},
            "Baked Ravioli": {"One Size": 8.49},
            "Stuffed Shells": {"One Size": 8.49},
            "Chicken Cutlet": {"One Size": 13.99},
            "Chicken Cacciatore": {"One Size": 13.99},
            "Chicken Broccoli Ziti": {"One Size": 11.49},
            "Chix Broc Ziti Alfredo": {"One Size": 14.99, "Family Size": 29.49},
            "Veal Cutlet": {"One Size": 13.99},
        },
        "Drinks": {
            "Diet Dr. Pepper": {"One Size": 2.49},
            "Coke Zero": {"Can": 1.99, "Bottle": 2.49, "2 Liter": 3.49},
            "Diet Ginger": {"One Size": 1.99},
            "Fanta Grape": {"One Size": 1.99},
            "Dr. Pepper": {"One Size": 2.49},
            "Ginger Ale": {"Can": 1.99, "Bottle": 2.49, "2 Liter": 3.49},
            "Sprite": {"Can": 1.99, "Bottle": 2.49, "2 Liter": 3.49},
            "Diet Coke": {"Can": 1.99, "Bottle": 2.49, "2 Liter": 3.49},
            "Fanta Orange": {"Can": 1.99, "Bottle": 2.49, "2 Liter": 3.49},
            "Coke": {"Can": 1.99, "Bottle": 2.49, "2 Liter": 3.49},
            "Pure Leaf Tea": {"One Size": 2.49},
            "Sobe": {"One Size": 4.49},
            "Gaterade": {"One Size": 2.49},
            "Ocean Spray": {"One Size": 2.49},
            "Aquafina": {"One Size": 1.99},
            "Sobe Life Water": {"One Size": 2.49},
            "Milk": {"One Size": 2.49},
            "Chocolate Milk": {"One Size": 2.99},
            "Coffee": {"One Size": 1.99},
            "Tea": {"One Size": 1.99},
            "Vitamin Water": {"One Size": 2.99},
        },
        "Desserts": {
            "Cheesecake": {"One Size": 4.99},
            "Carrot Cake": {"One Size": 4.99},
            "Chocolate Cake": {"One Size": 4.99},
            "Strawberry Topping": {"One Size": 1.99},
            "Choc Chips Cookie": {"One Size": 1.99},
            "Oatmeal Cookies": {"One Size": 1.99},
            "Brownie Cookie": {"One Size": 1.99},
        },
        "Seafood": {
            "Fish & Chips Dinner": {"One Size": 17.99},
            "Haddock Dinner": {"One Size": 20.99},
            "Scallops Dinner": {"One Size": 23.49},
            "Shrimp Dinner": {"One Size": 21.99},
            "Combo Dinner": {"One Size": 24.49},
            "Fishermen Plate Dinner": {"One Size": 31.49},
            "Salmon Dinner": {"One Size": 20.99},
            "Surf & Turf Dinner": {"One Size": 24.49},
            "Haddock Roll": {"One Size": 17.99},
            "Fried Scallop Box": {"SM": 15.99, "LG": 20.99},
            "Fried Calamari Box": {"SM": 12.99, "LG": 18.99},
            "Fried Shrimp Box": {"SM": 15.99, "LG": 20.99},
            "Fried Haddock Box": {"SM": 15.99, "LG": 20.99},
        },
        "Bowls & Veggie Menu": {
            "Grilled Chicken Bowl": {"One Size": 14.99},
            "Steak Tip Bowl": {"One Size": 15.99},
            "Grilled Shrimp Bowl": {"One Size": 15.99},
            "Baked Haddock Bowl": {"One Size": 17.99},
            "Baked Salmon Bowl": {"One Size": 17.99},
            "Grilled Veggie Bowl": {"One Size": 13.99},
            "Protien & Veggie Bowl": {"One Size": 16.99},
            "Grilled Chicken & Grains Bowl": {"One Size": 14.99},
            "Baked Salmon & Grains Bowl": {"One Size": 17.99},
            "Steak Tip & Grains Bowl": {"One Size": 15.99},
            "Shrimp & Broccoli Bowl": {"One Size": 17.99},
            "Veggie Burger Sandwich": {"One Size": 7.49},
            "Eggplant Sandwich": {"One Size": 8.49},
            "Veggie Meatball Sub": {"One Size": 10.49},
            "Veggie Meatball Pasta": {"One Size": 10.49},
            "Veggie Hot Sub": {"One Size": 10.49},
            "Grilled Veggie Hot Wrap": {"One Size": 10.49},
            "Hamad & Veggie Wrap": {"One Size": 10.49},
            "Grains Rice & Veggie Wrap": {"One Size": 10.49},
            "Veggie Meatball & Mixed Veggie": {"One Size": 10.49},
        },
        "Kids Menu": {
            "Kids Chicken Fingers": {"One Size": 7.99},
            "Kids Chicken Wings": {"One Size": 7.99},
            "Kids Chicken Nuggets": {"One Size": 7.99},
            "Kids Hot Dog": {"One Size": 6.99},
            "Kids Cheeseburger": {"One Size": 8.99},
            "Kids Hamburger": {"One Size": 8.99},
            "Kids Roastbeef": {"One Size": 8.99},
            "Kids Grilled Cheese": {"One Size": 7.99},
            "Kids Ziti Marinara": {"One Size": 5.99},
            "Kids Ziti Butter": {"One Size": 5.99},
            "Kids Linguine Marinara": {"One Size": 5.99},
            "Kids Linguine Butter": {"One Size": 5.99},
            "Kids Fish & Chips": {"One Size": 10.99},
        },
        "Sandwiches": {
            "Hamburger Sandwich": {"One Size": 7.99},
            "Cheeseburger Sandwich": {"One Size": 8.49},
            "Haddock Sandwich": {"One Size": 12.99},
            "Eggplant Sandwich": {"One Size": 7.99},
            "Veggie Burger Sandwich": {"One Size": 6.99},
            "Hamas Sandwich": {"One Size": 6.99},
            "Seafood Salad Sandwich": {"One Size": 7.99},
        },
        "Pan Pizza": {
            "Cheese Pizza": {"SM": 9.49, "LG": 14.49},
            "House Special": {"SM": 11.49, "LG": 18.49},
            "Veggie Deluxe": {"SM": 11.49, "LG": 18.99},
            "Eggplant Parmesan": {"SM": 11.49, "LG": 18.99},
            "Hawaiian Pizza": {"SM": 11.49, "LG": 18.99},
            "3 Cheese": {"SM": 11.49, "LG": 18.99},
            "Grilled Chicken": {"SM": 11.49, "LG": 19.99},
            "Chicken Kabob": {"SM": 11.49, "LG": 19.99},
            "Chicken Parmesan": {"SM": 11.49, "LG": 19.99},
            "Margarita": {"SM": 11.49, "LG": 18.99},
            "Chix Brocc Alfredo": {"SM": 12.99, "LG": 20.49},
            "Meat Lover": {"SM": 12.99, "LG": 19.99},
            "Buff Chicken Bomb": {"SM": 11.49, "LG": 19.99},
            "Shrimp Scampi": {"SM": 13.99, "LG": 22.99},
        },
    }

    # Displaying categories
    st.header("Menu Categories")
    selected_category = st.selectbox("Select a category", list(menu.keys()))

    # Display items for the selected category
    st.header(f"{selected_category} Menu")
    for item, sizes in menu[selected_category].items():
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
        col1.write(item)
        size = col2.selectbox("Size", list(sizes.keys()), key=item)
        price = sizes[size]
        col3.write(f"${price}")
        quantity = col4.number_input(f"Qty for {item} ({size})", min_value=0, key=f"{item}_{size}", label_visibility="collapsed")
        if col4.button(f"Add To Cart", key=f"button_{item}_{size}"):
            if quantity > 0:
                st.session_state['cart'].append((f"{item} ({size})", price, quantity))
                st.success(f"Added {quantity} x {item} ({size}) to cart")

with cart_col:
    st.header("Cart")
    if st.session_state['cart']:
        total = 0
        for item, price, quantity in st.session_state['cart']:
            st.write(f"{item} (x{quantity}): ${price * quantity:.2f}")
            total += price * quantity
        st.write(f"**Total: ${total:.2f}**")
    else:
        st.write("Your cart is empty.")

    # Submiting button for placing orders
    if st.button("Submit Order"):
        if st.session_state['cart']:
            order_details = "\n".join([f"{quantity} x {item} (${price * quantity:.2f})" for item, price, quantity in st.session_state['cart']])
            st.write("Thank you for placing your order with Food King! Hope you have a good food experience.")
            st.write(f"Order details:\n{order_details}")
            # Clearing the cart after placing the order
            st.session_state['cart'] = []
        else:
            st.write("Your cart is empty. Add items to the cart before placing an order.")

    # Refreshing button to clear session state
    if st.button("Refresh"):
        reset_session()
        st.experimental_rerun()

with bot_col:
    st.image("chatbot_icon.png", width=50)  # Replacing with the path to your chatbot icon image
    st.header("Interact with the Bot")
    bot_query = st.text_input("Ask the Bot")
    if st.button("Ask"):
        bot_response = get_llm_response(bot_query)
        if bot_response:
            st.write("Bot Response:")
            st.write(bot_response)
        else:
            st.write("No response from the server.")
