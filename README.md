# Sitejabber-Web-Scraping-with-BS4

### What this is
- Using Python's Beautiful Soup Library, this program allows for the gathering and storing of reviews from https://www.sitejabber.com/ to  .csv format. 

### How to use
1. Preparation
- Go to https://www.sitejabber.com/
- Find a company such as Uber: https://www.sitejabber.com/reviews/uber.com
- Find how many pages of reviews there are: As of 11/9/2019, last page is https://www.sitejabber.com/reviews/uber.com?page=32#reviews
2. Reorganizing sitejapper_bs.py code
- replace "FILE DESTINATION" with destination for .csv
- replace range(1, 33) with desired range
- replace 'https://www.sitejabber.com/reviews/uber.com?page=' with desired company
3. Execution
- Run sitejapper_bs.py!

### Example .csv
[![Image from Gyazo](https://i.gyazo.com/1325830faed24ce9f3eae04bd6b3c260.png)](https://gyazo.com/1325830faed24ce9f3eae04bd6b3c260)
