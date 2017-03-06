# Automation_Testing

Part1: UI Automation Test based on Selenium

Part2: API Test based on requests module ( Python )


### UI_test.py:

Preparation:

1. open Develop option of Safari;
2. Safari -> Preference -> Tab -> choose 'always open on tab'.

Automate the test case "Purchase book at Amazon website" based on Selenium Webdriver
"Purchase book at Amazon website" 

And test case steps: 

1. Visit https://www.amazon.cn/
2. Input "软件测试" in search box and click search icon
3. Click "软件测试（原书第2版）"
4. Click "加入购物车" at “软件测试（原书第2版）” page
5. Assert that text "商品已加入购物车" appears 
6. Assert that book price is "20.40" (2017.03.06 the price of book is 24.50)
