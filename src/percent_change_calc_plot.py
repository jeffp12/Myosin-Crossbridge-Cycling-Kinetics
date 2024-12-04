# This function calculates perfect change for my produced arrays and returns them in their individual arrays
def calculate_percent_change(control, perturbed):
    with np.errstate(divide='ignore', invalid='ignore'):  # Ignore divide-by-zero and invalid warnings
        percent_change = (perturbed - control) / perturbed * 100
        percent_change[np.isinf(percent_change)] = np.nan  # Replace infinite values with NaN
    return percent_change

control = np.array([CB0, CB1, CB2, CB3, CB4, CB5, CB6])
perturbed = np.array([NewCB0, NewCB1, NewCB2, NewCB3, NewCB4, NewCB5, NewCB6])

percent_changes = []
for cb_control, cb_perturbed in zip(control, perturbed):
    percent_changes.append(calculate_percent_change(cb_control, cb_perturbed))

percent_changes = np.array(percent_changes)
print("Percent Changes for all CBs:", percent_changes)


# Producing a visualization showing the percent change of each species 
cb_labels = ['CB0', 'CB1', 'CB2', 'CB3', 'CB4', 'CB5', 'CB6']

def plot_percent_changes(percent_changes, cb_labels):
    rows_CBs = percent_changes.shape[0]
    plt.figure(figsize=(7, 4))

    for i in range(rows_CBs):
        plt.plot(
            percent_changes[i], 
            label=cb_labels[i]
            )
    
    plt.title("% change of Control vs Pertrubed CB species")
    plt.xlabel(" # of Data Points")
    plt.ylabel("Percent Change (%)")
    plt.legend(title="CB Species")
    plt.axhline(0, color='black', linewidth=1, linestyle='--')  # Reference line at 0
    plt.grid(True)

plot_percent_changes(percent_changes, cb_labels)
