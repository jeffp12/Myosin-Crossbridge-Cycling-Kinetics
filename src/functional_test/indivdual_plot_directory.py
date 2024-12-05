# This part of the code is to make a directory to store the output images so that they can be used as foundation curve when we compare how therapies effect the CB cycling
import os
import matplotlib.image as mpimg
output_dir = "Control_plots"
os.makedirs(output_dir, exist_ok=True)

species = [CB0, CB1, CB2, CB3, CB4, CB5, CB6]
labels = [
    '[MYOSIN + ATP / MYOSIN w ADP + Pi]',
    '[COCKED MYOSIN w ADP + Pi]',
    '[ACTOMYOSIN COMPLEX w ADP + Pi]',
    '[PRE ACTOMYOSIN COMPLEX w ADP]',
    '[POST ACTOMYOSIN COMPLEX w ADP]',
    '[ISO ACTOMYOSIN COMPLEX w ADP]',
    '[ACTOMYOSIN COMPLEX]'
]

# Loop through each species and plot separately
for i, (data, label) in enumerate(zip(species, labels)):
    plt.figure(figsize=(9, 7))
    plt.plot(time, data, label=label, linestyle='-')
    plt.xlabel('Time')
    plt.ylabel('% Concentration')
    plt.title(f'Dynamics of {label}')
    plt.legend()
    plt.grid(True)
    plt.xlim(0, 0.3)  # Set the x-axis range to remove extra space

    # Save the plot as an image file
    file_name = f"{output_dir}/control curve_{i + 1}.png"
    plt.savefig(file_name)
    plt.close()  # Close the figure to avoid overlapping plots

    print(f"Saved plot: {file_name}")

# This is a test function to print out all the individual graphs. Can also be used to extropolate these graphs from the overall reactions.
output_dir = "Control_plots"
plot_files = [
    f"{output_dir}/control curve_1.png",
    f"{output_dir}/control curve_2.png",
    f"{output_dir}/control curve_3.png",
    f"{output_dir}/control curve_4.png",
    f"{output_dir}/control curve_5.png",
    f"{output_dir}/control curve_6.png",
    f"{output_dir}/control curve_7.png"
]
for file in plot_files:
    img = mpimg.imread(file)
    plt.figure(figsize=(8, 6))
    plt.imshow(img)
    plt.axis('off')
    plt.show()
