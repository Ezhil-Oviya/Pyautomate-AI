import streamlit as st
import math

# Function to apply themes
def set_theme(mode):
    if mode == "Dark":
        st.markdown(
            """
            <style>
            body {
                background-color: #1E1E1E;
                color: white;
            }
            .stButton {
                background-color: #F39C12;
                color: white;
            }
            </style>
            """, 
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <style>
            body {
                background-color: white;
                color: black;
            }
            .stButton {
                background-color: #F39C12;
                color: black;
            }
            </style>
            """, 
            unsafe_allow_html=True
        )

# Main function for the app
def main():
    st.title("Scientific Calculator")
    
    # Mode selection for light or dark theme
    mode = st.radio("Select Theme", ("Light", "Dark"))
    set_theme(mode)

    # Initialize session state if not already done
    if 'display' not in st.session_state:
        st.session_state.display = "0"
    
    display = st.text_input("Display", st.session_state.display, key="display", disabled=True, label_visibility="collapsed")

    # Button Layout
    cols = st.columns(4)
    button_labels = [
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "0", ".", "C", "+",
        "sin", "cos", "tan", "sqrt",
        "^", "ln", "log", "exp"
    ]
    
    # Handle button presses
    for i, label in enumerate(button_labels):
        with cols[i % 4]:
            if st.button(label):
                if label == "C":
                    st.session_state.display = "0"
                elif label == "=":
                    try:
                        # Handle exponentiation and other operations
                        if "^" in st.session_state.display:
                            st.session_state.display = str(eval(st.session_state.display.replace("^", "**")))
                        else:
                            st.session_state.display = str(eval(st.session_state.display))
                    except Exception as e:
                        st.session_state.display = "Error"
                else:
                    if st.session_state.display == "0":
                        st.session_state.display = label
                    else:
                        st.session_state.display += label

    # If there is a button press for the operator or number, the display will update

if __name__ == "__main__":
    main()
