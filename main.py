import matplotlib.pyplot as plt

# Define the text and colors
text = "Goolag"
colors = ["#4285F4", "#EA4335", "#FBBC05", "#34A853", "#EA4335", "#4285F4"]

# Create a new figure
plt.figure(figsize=(10, 2))

# Multiplier for spacing
multiplier = 0.9

# Monospace font for consistent letter widths
font_name = "DejaVu Sans Mono"

# Plot each letter with the corresponding color
for i, (letter, color) in enumerate(zip(text, colors)):
    plt.text(i * multiplier, 0, letter, fontsize=100, fontweight='regular', color=color, fontname=font_name)

# Remove axes and save the image
plt.axis('off')
plt.xlim(-1, len(text) * multiplier)
plt.ylim(-1, 1)
plt.savefig('goolag_logo.png', format='png', bbox_inches='tight', pad_inches=0.1)
plt.savefig('goolag_logo.jpg', format='jpg', bbox_inches='tight', pad_inches=0.1)