import numpy as np

class RetailAnalytics:
    """
    A simple NumPy-based retail data cleaning tool.
    Covers Day-12 & Day-13 concepts:
    - NumPy file reading
    - Masking & indexing
    - NaN handling
    - Broadcasting
    - Stacking arrays
    """

    def __init__(self, inputfile):
        self.inputfile = inputfile

    def load_data(self):
        """
        Loads the dataset using NumPy's genfromtxt.
        Returns date column and numeric data columns.
        """
        self.dates = np.genfromtxt(
            self.inputfile, delimiter=",", skip_header=1, dtype="U10", usecols=0
        )
        self.data = np.genfromtxt(
            self.inputfile, delimiter=",", skip_header=1, dtype=float, usecols=(1, 2, 3)
        )
        return self.dates, self.data

    def clean(self):
        """
        Cleans the dataset:
        1. Negative values → 0
        2. NaN values → column mean
        3. Isolated zero spikes → average of previous & next values
        """
        arr = self.data.copy()

        # Step 1: Replace negative values
        arr[arr < 0] = 0

        # Step 2: Replace NaN with column means
        col_means = np.nanmean(arr, axis=0)
        mask = np.isnan(arr)
        arr[mask] = col_means[np.where(mask)[1]]

        # Step 3: Fix isolated zero spikes
        prev = np.vstack([np.nan * np.ones((1, arr.shape[1])), arr[:-1]])
        nxt = np.vstack([arr[1:], np.nan * np.ones((1, arr.shape[1]))])

        zero_mask = arr == 0
        spike_mask = zero_mask & (prev != 0) & (nxt != 0)

        arr[spike_mask] = (prev[spike_mask] + nxt[spike_mask]) / 2

        self.cleaned = arr
        return arr

    def save(self, outputfile="cleaned_output.csv"):
        """
        Saves the cleaned dataset to a CSV file.
        """
        header = "Date,Customers,Revenue,ItemsSold"
        final = np.column_stack([self.dates, self.cleaned])
        np.savetxt(outputfile, final, delimiter=",", header=header, fmt="%s")
        return outputfile


if __name__ == "__main__":
    obj = RetailAnalytics("retail_sales.csv")
    obj.load_data()
    obj.clean()
    obj.save("result.csv")
    print("\nCleaning completed. File saved as result.csv\n")
