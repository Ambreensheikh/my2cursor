import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Include Tailwind CSS
st.markdown('<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">', unsafe_allow_html=True)

# Sample data for marksheet
data = {
    'Subject': ['Math', 'Science', 'English', 'History', 'Art'],
    'Marks': [85, 90, 78, 88, 95]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate percentage
df['Percentage'] = (df['Marks'] / 100) * 100

# Set the title of the app
st.title("Student Marksheet")

# Display the marksheet
st.subheader("Marksheet")
st.dataframe(df)

# Plotting the growth mindset graph
st.subheader("Growth Mindset Graph")
plt.figure(figsize=(10, 5))
plt.bar(df['Subject'], df['Percentage'], color=['#6C63FF', '#8A2BE2', '#32CD32', '#7FFF00', '#ADFF2F'])
plt.ylim(0, 100)
plt.xlabel('Subjects')
plt.ylabel('Percentage')
plt.title('Growth Mindset in Learning')
plt.axhline(y=80, color='r', linestyle='--', label='Passing Marks (80%)')
plt.legend()
st.pyplot(plt)

# Add a footer
st.markdown("""
<style>
footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)