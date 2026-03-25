import streamlit as st
import pandas as pd

# 1. Your Master List (categorized)
MASTER_DATA = {
    "Protein": ["Salmon", "Ham", "Yogurt", "Whey", "Mozz", "Tofu", "Chicken Patty", "Tofurkey", "Black Bean Burgers"],
    "Veggies": ["Sweet Potato", "Broccoli", "Carrots", "Red Onion", "Garlic", "Spinach", "Cilantro", "Mushrooms"],
    "Carbs": ["Rice", "Couscous", "Popcorn", "Bread", "Waffles", "Pancake Mix", "Pasta", "Pizza Dough"],
    "Beverages": ["Oat Milk", "Almond Milk", "Orange Juice", "Seltzer", "Coffee Creamer"],
    "Bathroom/Home": ["Paper Towel", "Toilet Paper", "Hand Soap", "Toothpaste", "Lysol"]
}

st.set_page_config(page_title="Our Shared List", layout="centered")

# 2. Shared Sync Logic
# (For a simple setup, we'll use Streamlit's cache or a persistent file)
if 'needs' not in st.session_state:
    st.session_state.needs = []

st.title("🛒 The Household Hub")

tab1, tab2 = st.tabs(["📝 Add to List", "🏃 Store Mode"])

with tab1:
    st.subheader("What do we need?")
    for category, items in MASTER_DATA.items():
        with st.expander(f"{category}"):
            for item in items:
                # If she checks it, it gets added to the shared 'needs' list
                is_needed = st.checkbox(item, key=f"check_{item}")
                if is_needed and item not in st.session_state.needs:
                    st.session_state.needs.append(item)
                elif not is_needed and item in st.session_state.needs:
                    st.session_state.needs.remove(item)

with tab2:
    st.subheader("Ready to Shop")
    if not st.session_state.needs:
        st.write("List is empty. Add things in the first tab!")
    else:
        # Show ONLY the items selected, grouped by their original category
        for category, items in MASTER_DATA.items():
            matching_items = [i for i in items if i in st.session_state.needs]
            if matching_items:
                st.info(f"**{category}**")
                for match in matching_items:
                    st.write(f"☐ {match}")
        
        if st.button("Clear Everything (Trip Done)"):
            st.session_state.needs = []
            st.rerun()
