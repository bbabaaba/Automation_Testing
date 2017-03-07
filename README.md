# Automation_Testing

Part1: UI Automation Test based on Selenium

Part2: API Test based on requests module ( Python )


### UI_test.py:

Safari Setting:

1. open Develop option of Safari;
2. Safari -> Preference -> Tab -> choose 'always open on tab'.

Preparation:

Python with module unittest2 and selenium installed.

Automate the test case "Purchase book at Amazon website" based on Selenium Webdriver
"Purchase book at Amazon website" 

And test case steps: 

1. Visit https://www.amazon.cn/
2. Input "软件测试" in search box and click search icon
3. Click "软件测试（原书第2版）"
4. Click "加入购物车" at “软件测试（原书第2版）” page
5. Assert that text "商品已加入购物车" appears 
6. Assert that book price is "20.40" (2017.03.06 the price of book is 24.50)


### API_test.py:

Preparation:

Python with module unittest2 and requests installed.

TestCases:

1. Test Matt Damon is not in actors list of the movie, which subject id is 1304102.

2. Test whether movie, which subject id is 1292052, is the first one in the Top 250 movies.

