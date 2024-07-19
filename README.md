# Dollar Price Web Scraping and Statistical Analysis

This repository contains a Python script that scrapes historical dollar prices from the TGJU website and performs statistical analysis on the collected data.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Script Overview](#script-overview)
- [Notes](#notes)
- [License](#license)

## Installation

To run this script, you need the following libraries installed:

- `selenium`
- `pandas`
- `numpy`
- `statistics`
- `scipy`

You can install these libraries using `pip`:

```sh
pip install selenium pandas numpy scipy
```

You also need to have the Chrome WebDriver installed and accessible in your system's PATH. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/).

## Usage

1. **Clone the repository or download the script.**

2. **Install the required libraries:**

    ```sh
    pip install selenium pandas numpy scipy
    ```

3. **Run the script:**

    ```sh
    python script_name.py
    ```

## Script Overview

The script performs the following steps:

1. **Set Up and Load the Web Page:**

    The script initializes the Chrome WebDriver and navigates to the specified URL.

    ```python
    url = "https://www.tgju.org/profile/price_dollar_rl/history"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(4)
    ```

2. **Scrape the Data:**

    The script scrapes the historical dollar prices from the table on the webpage. It iterates through multiple pages to collect data.

    ```python
    data = []
    p = 5
    for i in range(p):
        table = driver.find_element(By.XPATH, value="//table[@class='table widgets-dataTable table-hover text-center history-table dataTable no-footer']")
        rows = table.find_elements(By.XPATH, value=".//tr")[1:]
        for row in rows:
            cols = row.find_elements(By.XPATH, value=".//td[4]")
            for col in cols:
                data.append(col.text)
        driver.refresh()
        search_button = driver.find_element(By.ID, value="DataTables_Table_0_next")
        search_button.click()
        time.sleep(4)
    ```

3. **Process the Data:**

    The scraped data is cleaned (removing commas) and saved into a CSV file.

    ```python
    price = [int(s.replace(',', '')) for s in data]
    np.savetxt("samplingfinaldata.csv", price, delimiter=",")
    ```

4. **Statistical Analysis:**

    The script calculates the mean, variance, and performs sampling for statistical analysis.

    ```python
    mean = st.mean(price)
    var = st.variance(price)
    N = len(price)
    presample = random.sample(price, 10)
    xbar = st.mean(presample)
    s2 = st.variance(presample)
    r = 0.01
    alpha = 0.05
    z = norm.ppf(1-alpha/2, loc=0, scale=1)
    n = (((r*xbar)**2)/((z**2)*s2))**(-1)
    sample1 = random.sample(price, 35)
    sample = presample + sample1
    xbarfinal = st.mean(sample)
    s2final = st.variance(sample)
    ```

5. **Output Results:**

    The script prints the collected data, initial sample, and the results of the statistical analysis.

    ```python
    print("mean =", mean, "var =", var)
    print("nemoone moghadamti:", presample)
    print("n =", n)
    print("xbarfinal =", xbarfinal, "s2final =", s2final)
    ```

## Notes

- Ensure the webpage structure hasn't changed, as it might affect the XPATH used in the script.
- Adjust the `time.sleep()` durations if needed, depending on your internet speed and webpage loading times.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
