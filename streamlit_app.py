import streamlit as st

# The Full Master List Categorized
MASTER_DATA = {
    "Protein": [
        "Chicken (thighs/breasts/Kevins)", "Salmon", "Shrimp", "Eggs", "Ham", 
        "Yogurt", "Whey", "Mozz", "Tofu", "Chicken patty", "Tofurkey sausage", 
        "Breakfast sausage", "Black bean burgers", "Beyond burgers", "Peanut butter", "Broth"
    ],
    "Veggies": [
        "Sweet potato", "Broccoli", "Brussels sprouts", "Carrots", "Red onion", 
        "White onion", "Garlic", "Red bell pepper", "Green bell pepper", "Jalapeño", 
        "Spinach", "Frozen spinach", "Celery", "Arugula", "Avocados", "Cucumber", 
        "Tomato", "Cilantro", "Parsley", "Romaine", "Cabbage", "Salad mix", 
        "Stir fry mix", "Slaw", "Mushrooms", "Chia/Walnuts/Peanuts", 
        "Pepitas/Sunflower seeds", "Pickles", "Basil/Pesto"
    ],
    "Fruits": [
        "Lemon", "Lime", "Kiwi", "Bananas", "Strawberry/Blueberry", 
        "Apple (Granny Smith)", "Nectarine", "Pear", "Clementines"
    ],
    "Cans": [
        "Black beans", "Kidney beans", "Garbanzo", "Chili beans", 
        "Chipotle in adobo", "Corn", "Tomatoes for sauce", "Pizza sauce"
    ],
    "Carbs": [
        "Rice (Basmati/Jasmine)", "Couscous/Faro", "Popcorn kernels", "Potato", 
        "Bread", "Burger buns", "Waffles", "Pancake mix (protein)", "Granola", 
        "Oats", "Cereal (Life/Cheerios)", "Pasta", "Low-carb wraps", 
        "Tofu noodles", "Pizza dough"
    ],
    "Beverages": [
        "Oat milk", "Almond milk", "Orange juice", "Whole milk", 
        "Coconut milk/cream", "Seltzer", "Seltzer tank", "Coffee creamer"
    ],
    "Complete Meals": [
        "Pizza", "Noodle bowls", "Sushi", "Salads", "Hoagies", "Frozen lunch/dinners"
    ],
    "Condiments": [
        "Horseradish", "Spicy mustard", "BBQ", "Ketchup", "Olive oil", 
        "Tahini", "Peppercorns", "Jelly/jam", "Everything spice", 
        "Taco seasoning", "Curry paste", "Pesto/basil"
    ],
    "Bathroom": [
        "Paper Towel", "Toilet Paper", "Hand soap", "Conditioner/Shampoo", 
        "Cleaning Supplies (Lysol)", "Toothpaste", "Floss", "Gum", "Lotion", "Dry shampoo"
    ]
}

st.set_page_config(page_title="Household Grocery Hub", page_icon="🛒")

# Title and Mode Selection
st.title("🛒 Grocery Mission Control")
mode = st.radio("Switch View:", ["Planning (Build List)", "Shopping (Store Mode)"], horizontal=True)

st.divider()

# Initialize session state for the shopping list if it doesn't exist
if 'shopping_list' not in st.session_state:
    st.session_state.shopping_list = []

# --- PLANNING MODE ---
if mode == "Planning (Build List)":
    st.subheader("Tap items we are low on:")
    
    for category, items in MASTER_DATA.items():
        with st.expander(f"{category}"):
            for item in items:
                # Check if item is already in the list
                is_checked = item in st.session_state.shopping_list
                
                if st.checkbox(item, value=is_checked, key=f"plan_{category}_{item}"):
                    if item not in st.session_state.shopping_list:
                        st.session_state.shopping_list.append(item)
                else:
                    if item in st.session_state.shopping_list:
                        st.session_state.shopping_list.remove(item)

# --- SHOPPING MODE ---
else:
    st.subheader("📍 Clean Shopping List")
    
    if not st.session_state.shopping_list:
        st.info("Nothing selected! Go to Planning mode to add items.")
    else:
        # We iterate through MASTER_DATA to maintain the correct store order
        for category, items in MASTER_DATA.items():
            # Find which items from this category are in the shopping list
            needed_here = [i for i in items if i in st.session_state.shopping_list]
            
            if needed_here:
                st.markdown(f"### {category}")
                for item in needed_here:
                    st.checkbox(f"**{item}**", key=f"shop_{item}")
        
        st.divider()
        if st.button("Clear Finished Trip"):
            st.session_state.shopping_list = []
            st.rerun()

