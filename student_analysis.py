
import pandas as pd
import matplotlib.pyplot as plt

# Student performance dataset
data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Maths": [85, 90, 75, 60, 95],
    "Science": [80, 88, 70, 65, 92],
    "English": [78, 85, 80, 70, 90]
}

df = pd.DataFrame(data)

# Calculate average marks
df["Average"] = df[
    ["Maths", "Science", "English"]
].mean(axis=1)

# Display student details
print("STUDENT PERFORMANCE ANALYSIS")
print(df)

# Find topper
topper = df.loc[df["Average"].idxmax()]

print("\nTop Performing Student:")
print(topper["Student"])
print("Average:", topper["Average"])

# Subject-wise average
print("\nSubject-wise Average:")
print(df[["Maths", "Science", "English"]].mean())

# Create visualization
df.plot(
    x="Student",
    y=["Maths", "Science", "English"],
    kind="bar"
)

plt.title("Student Academic Performance")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()
