def calculate_and_plot_percent_changes(wildtype, perturbed, cb_labels):
    # This function serves to calculate percent changes between the wildtype and perturbed results and then produces a simple 2D visualiztion
    
    with np.errstate(divide='ignore', invalid='ignore'):  # Ignore divide-by-zero and invalid warnings
        percent_changes = (perturbed - wildtype) / perturbed * 100
        percent_changes[np.isinf(percent_changes)] = np.nan  # Replace infinite values with NaN

    # Visualizing 
    rows_CBs = percent_changes.shape[0]
    plt.figure(figsize=(9, 7))

    for i in range(rows_CBs):
        plt.plot(
            percent_changes[i],
            label=cb_labels[i]
        )

    plt.title("% Change of wildtype vs Perturbed CB Species")
    plt.xlabel("# of Data Points")
    plt.ylabel("Percent Change (%)")
    plt.legend(title="CB Species")
    plt.axhline(0, color='black', linewidth=1, linestyle='--')  # Reference line at 0
    plt.grid(True)
    plt.show()

    return percent_changes
