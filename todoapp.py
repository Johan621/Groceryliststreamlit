import streamlit as st

# Function to add item
def add_item(Notes, item):
    if not item:
        st.warning("⚠️ Invalid input.")
        return Notes
    if item in Notes:
        st.warning(f"⚠️ Item '{item}' already exists in grocery list.")
    else:
        Notes.append(item)
        st.success(f"✅ Item '{item}' added to the list.")
    return Notes

# Function to view items
def view_items(Notes):
    if len(Notes) == 0:
        st.info("📝 No items added to view.")
    else:
        st.subheader("📌 Grocery List")
        for i, item in enumerate(Notes, 1):
            st.write(f"{i}. {item}")

# Function to remove item
def remove_item(Notes, item):
    if not item:
        st.warning("⚠️ Invalid input.")
        return Notes
    if item in Notes:
        Notes.remove(item)
        st.success(f"🗑️ Item '{item}' deleted successfully.")
    else:
        st.warning("⚠️ Item does not exist in the list.")
    return Notes

# Main app
def main():
    st.title("🛒 Grocery To-Do List")

    # Store items in session state (persists while app is running)
    if "Notes" not in st.session_state:
        st.session_state.Notes = []

    # Input field
    new_item = st.text_input("Enter grocery item:")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("➕ Add Item"):
            st.session_state.Notes = add_item(st.session_state.Notes, new_item)

    with col2:
        if st.button("👀 View List"):
            view_items(st.session_state.Notes)

    with col3:
        if st.button("🗑️ Remove Item"):
            st.session_state.Notes = remove_item(st.session_state.Notes, new_item)

    # Always show current list
    st.markdown("---")
    view_items(st.session_state.Notes)

if __name__ == "__main__":
    main()
