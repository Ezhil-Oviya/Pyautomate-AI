import streamlit as st
import math
import numpy as np

# Initialize session state variables if they don't exist
if 'display' not in st.session_state:
    st.session_state.display = ""

def calculate_result(current_input):
    try:
        # This is where you could handle more complex calculations if needed
        result = eval(current_input)
        return result
    except:
        return "Error"

def update_display(value):
    # Update the session state with the new value
    st.session_state.display = value

def main():
    st.title("Scientific Calculator")
    
    # Light / Dark Mode toggle
    dark_mode = st.checkbox('Dark Mode', value=False)
    
    # Change theme based on the toggle
    if dark_mode:
        st.markdown('<style>body { background-color: #2e2e2e; color: white; }</style>', unsafe_allow_html=True)
    else:
        st.markdown('<style>body { background-color: white; color: black; }</style>', unsafe_allow_html=True)

    # Create buttons for numbers and operations
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button('1', on_click=update_display, args=("1",))
        st.button('2', on_click=update_display, args=("2",))
        st.button('3', on_click=update_display, args=("3",))
        st.button('4', on_click=update_display, args=("4",))
        st.button('5', on_click=update_display, args=("5",))
        st.button('6', on_click=update_display, args=("6",))
    
    with col2:
        st.button('7', on_click=update_display, args=("7",))
        st.button('8', on_click=update_display, args=("8",))
        st.button('9', on_click=update_display, args=("9",))
        st.button('0', on_click=update_display, args=("0",))
        st.button('+', on_click=update_display, args=("+",))
        st.button('-', on_click=update_display, args=("-",))

    with col3:
        st.button('C', on_click=update_display, args=("",))  # Clear screen
        st.button('=', on_click=update_display, args=(calculate_result(st.session_state.display),))

    st.text("Current Input:")
    st.text(st.session_state.display)

if __name__ == "__main__":
    main()
