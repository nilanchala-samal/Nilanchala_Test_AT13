""" Python Section """
"""
1. What is decorator , write a decorator?
a: A decorator in Python is a special type of function that can modify or extend the behavior of another function without changing the original function itself.
e.g.
def decor1(func):
    def inner(name):
        print("decor1 execution...")
        func(name)

    return inner


@decor1
def wish(name):
    print("Hello", name, "good afternoon...")


wish("Nilanchala")

2. What is lambda expression, write a lambda expression?
a. A lambda expression is an anonymous function, which means it doesn't have a name. It's a shortcut way to create compact and one-time-use functions. The syntax for a lambda expression is:
  lambda arguments: expression
  
  e.g.
Below is the code to find the square of a given number using lambda function:
sq = lambda n: n * n
print(sq(4))

3. WAF, S = ‘Hello everyone’, count the occurrence of each char, return those repetitive character , without using any inbuilt function.
a. 
my_str = input("Enter the string: ")
di = {}
for x in my_str:
    if x not in di.keys():
        di[x] = 1
    else:
        di[x] = di.get(x) + 1
for k, v in di.items():
    print(k, '->', v)
    
4. WAF , Reverse a string words. > Input = ‘hello world’ > output:- ‘world hello’, without using inbuilt function
a. 
str = "hello world"
l = len(str)
i = j = l - 1

res = ""

while i >= 0:
    while i >= 0 and str[i] != ' ':
        i = i - 1

    k = i + 1
    temp = ''
    while k <= j:
        temp += str[k]
        k = k+1
    res += temp
    if i >= 0:
        res += ' '
        i = i - 1
        j = i
print(res)

5. WAF, input= ‘aaabbaacd’ output= ‘3a2b2a1c1d’
a. 
s = "aaabbaacd"

i = 0
l = len(s)
res = ""
while i < l:
    c = s[i]
    count = 1
    # checking if the next character is matching with the previous character
    while i < l-1 and c == s[i+1]:
        count += 1
        i += 1
    res += str(count) + c
    i += 1
print(res)

6. Sort a list integer element without using inbuilt function?
a. 
nums = [76, 23, 45, 12, 54, 9]
print("Original List:", nums)

for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i] > nums[j]:
            # exchanging the position of the elements
            nums[i], nums[j] = nums[j], nums[i]

print("Sorted List:", nums)

7. Li = [1,2,3,4], Li2 = [10,20,30]
Result = {1:10,2:20,3:30}
Take a two list a parameter, return dictionary, look like above result.

a. 
li1 = [1, 2, 3]
li2 = [10, 20, 30]

my_dict = {}
for x in li1:
    for y in li2:
        my_dict[x] = y

print(my_dict)

9. What is exception handling , how handel the exception in python , explain with each
block.
a. Exception handling provides a way to prevent the unexpected or unwanted termination or program so that our normal flow of the program continues.
-> In python, using try except block we can handle the exception
-> If any exception occurs, python interpreter checks if the except block for the occurred exception is present or not, if present then the except block executes and the program terminated normally. If not present, then the control goes to the default exception handler and our program terminates abnormally.
-> try:
    Inside try block, the risky codes were written. If the exception occurs, then the control shifts to the except block.
-> except:
    Inside the except block, exception handling code is present. 
-> finally:
    Inside finally block, we generally close all the resources. 
    It always executes except incase of python interpreter shut down.
-> else:
    It executes when no exception occurred in the try block.
    
10. . Difference between Module and Packages (3 diff)
a. 
->  module is a single Python file (.py extension) containing collections of class, functions and  variables whereas a package is a directory containing multiple modules.
-> Modules don't have an initialization file (init.py). But, Packages generally contain an init.py file, which tells Python that the directory should be considered as a package.
-> Modules define a single namespace but Packages have a hierarchical namespace structure, which allows for nested imports.

11. Difference between List vs tuple vs set vs dictionary?
a.
List:
------
-> Insertion order is preserved
2. Duplicates are allowed
-> Heterogeneous objects are allowed
-> Growable in nature
-> Represented using [] brackets
-> We can access the elements using index

Tuple:
-------
-> It is almost similar to the list
There are only two differences.
-> Tuple is immutable whereas list is mutable
-> It is enclosed by parenthesis.

Set:
----
-> Enclosed within curly braces
-> It doesn't allow duplicates
-> Insertion order is not preserved
-> Set object doesn't support indexing

Dictionary:
---------------
-> It is a collection of key-value pairs.
-> It is mutable in nature.
-> The dictionary keys must be immutable in nature.
-> It is represented using {}.
-> Nesting of dictionaries can be possible.


12. What is garbage collection?
-> Garbage collection in Python is the automatic memory management system used by the Python interpreter to reclaim the memory occupied by objects that are no longer referenced.
-> Programmers don't need to manually manage the memory.
-> It prevents memory leaks and optimizes memory usage.
-> It ensures efficient memory allocation for the program.

13. What is list comprehension, write code in list comprehension.
a. List comprehension in Python is a concise way to create a new list from an existing list or other iterable. It is generally a single line of code enclosed in square brackets.
eg. 
nums = [2, 4, 5, 6]
doubles_nums = [i * 2 for i in nums]
print("Using List Comprehension: ", doubles_nums)

14. Difference between Shallow copy vs Deep Copy?
The main differences are:
-> Shallow copy copies only the top level of the object, and not the nested objects. But deep copy copies everything including the nested objects.
-> In shallow copy, original and copied object are connected, changing to the one affects another. But in deep copy, Changes to one doesn't affect the other.
-> Shallow copy is faster, whereas deep copy is complex and slower.

15. Explain break, continue, pass with code?
a.
Break:
-------
-> break statement is used to terminate from the loop based on some conditions.
-> Execution continues with the next line after the loop

for i in range(5):
    if i == 3:
        break
    print(i)


Continue:
-------------
-> continue is used to skip one or more iterations based on some condition
-> Execution continues with the next iteration

for i in range(5):
    if i == 3:
        continue
    print(i)

Pass:
------
-> It does perform any action
-> It is commonly used in empty blocks.

for i in range(5):
    if i == 3:
        pass
    print(i)

"""

""" Selenium Section """
"""
1. What is webdriver?
a. 
-> It is one of the components of the selenium used to automate the web applications.
-> It is simply a module in python.
-> Each browser has its own webdriver.
-> It is also an API(Application programming Interface).

2. How to handel selective dropdown, write a snippet for it?
a. To handle selective dropdowns, Select class is used which is present in "selenium.webdriver.support.select" package.
-> First we need to launch the browser using the URL
-> then, we need to find the dropdown web-element
-> Inside Select class constructor pass that web-element as an argument. It will return a Select class object, which provides certain methods to work with the dropdowns.
-
snippet:
-------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get(url)

dropdown = driver.find_element(By.XPATH, XPATH_OF_ELEMENT)
dropdown_obj = Select(dropdown)

# selecting the option from dropdown
# 3 in-built methods are there to do so

# dropdown_obj.select_by_visible_text(TEXT)
# dropdown_obj.select_by_value(VALUE)
# dropdown_obj.select_by_index(INDEX)

driver.close()

3. How to handle auto suggestive dropdown, write a snippet for it?
-> First open the url in the desired browser.
-> Find the input box and send some suggested values using send_keys() method.
-> after sending the value, locate the suggested elements that using any of the locators.
-> Then using for loop, we can extract the text from each suggested element and compare that with our desired element.

eg.
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(URL)

driver.find_element(By.ID, ID_OF_INPUT_ELEMENT).send_keys(VALUE)

values = driver.find_elements(By.ID, "SUGGESTED_ELEMENTS")

for value in values:
    if value.text == DESIRED_VALUE:
        value.click()
        break

4. How to handle multiple windows and back to current window?
a. If multiple windows were opened in the browser, we can handle them using 'window_handles' variable. 
-> driver.window_handles will return a list in which each value represent the window_id of that particular window.
-> we can switch to another window by using window_id of a particular window 'driver.switch_to.window(window_id)' and perform the required actions on that window.
-> To get back to the current window we can use 'driver.switch_to.window(driver.window_handles[0])'

5. What StaleElementException?
a. A StaleElementReferenceException in Selenium occurs when a WebElement reference becomes invalid due to changes in the DOM. It happens when an element is found initially but later removed or modified from the DOM. To prevent this type of exception, we need to provide more dynamic locators to interact with the elements.

6. Explain the wait mechanism, write syntax and snippet for it.
a. The wait mechanism in Selenium is used to pause the execution of a test until a certain condition is met. This is useful for handling dynamic content and ensuring that elements are present before interacting with them.
It is of two types:
-> Implicit wait:
--------------------
-> If the element is loaded within the specified time, it will execute the further statements.
-> Single line statement is needed for the whole script
-> Performance will not be reduced.
syntax:
driver.implicitly_wait(timeout_in_seconds)

-> Explicit wait:
--------------------
->Explicit wait is more precise and allows us to specify the exact condition that we're looking for.
-> It is a bit complicated but more efficient.

syntax:
-------
my_wait = WebDriverWait(driver, 10, ignored_exceptions=[Exception])

# Here we're waiting for the element to be located on the web page (We can provide different conditions other than presence_of_element_located too)
element = my_wait.until(EC.presence_of_element_located((By.XPATH, XPATH_OF_ELEMENT)))
element.click()

7. How to handle dynamic web element, (write at least 3 point)
a. 
-> By Combining the multiple attributes in locators to increase specificity and reduce the chances of ambiguity
-> Using XPath or CSS selectors for finding the accurate match 
-> Locating the elements relative to stable elements on the page. Then using the XPATH Axes(Parent, sibling, following-sibling, preceding-sibling etc..) we can find the actual element.

8. How many locators in selenium?
-> Locators are used to locate the elements on the webpage. There are 8 types of selectors in selenium.
   i. ID
   ii. NAME
   iii. CLASS_NAME
   iv. TAG_NAME
   v. LINK_TEXT
   vi. PARTIAL_LINK_TEXT
   vii. CSS_SELECTOR
   viii. XPATH


9. In web table want to fetch 3rd Column , 3rd row data, write a xpath for it.
a. The XPATH should be, "//table[@id='id_of_table']/tbody/tr[3]/td[3]"


10. 
a.
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.nseindia.com/")

driver.maximize_window()

actions = ActionChains(driver)
market_data = driver.find_element(By.XPATH, "(//a[@id='link_2'])[1]")
pre_open_market = driver.find_element(By.LINK_TEXT, "Pre-Open Market")

actions.move_to_element(market_data).move_to_element(pre_open_market).click().perform()
time.sleep(5)
driver.quit()


xpath of Hindalco : //table[@id='livePreTable']//tbody/tr[2]/td[2]
xpath of prev.close: //table[@id='livePreTable']//tbody/tr[2]/td[3]
"""

""" SQL Section """

"""
1.  Explain about the DML,DDL,TCL,DQL commands?
a.
-> DDL: To define and modify database structure DDL is used
      Create, drop, alter, truncate are the common commands used in DDL.
-> DQL stands for Data Query Language. It is used to query and retrieve data from a database.
      select, where are used to retrieve and filter the data respectively.
-> DML: To manipulate data within existing database.
      insert, update, delete commands are used in DML
-> TCL: To manage transactions in the database TCL is used.
      commit and rollback are the commands used in TCL
      
2. What is join, explain about the all joins?
a. A join in SQL is a way to combine rows from two or more tables based on a related column between them.
Several types of joins are there in SQL:
-> INNER JOIN:
Returns only the rows that have matches in both tables.
Example: SELECT * FROM table1 INNER JOIN table2 ON table1.id = table2.id;
-> LEFT JOIN (or LEFT OUTER JOIN):
Returns all rows from the left table and the matched rows from the right table.
If there's no match, the result will contain NULL on the right side.
Example: SELECT * FROM table1 LEFT JOIN table2 ON table1.id = table2.id;
-> RIGHT JOIN (or RIGHT OUTER JOIN):
Similar to LEFT JOIN but returns all rows from the right table.
Example: SELECT * FROM table1 RIGHT JOIN table2 ON table1.id = table2.id;
-> FULL JOIN (or FULL OUTER JOIN):
Returns all rows from both tables, with NULL values in the columns.
Example: SELECT * FROM table1 FULL OUTER JOIN table2 ON table1.id = table2.id;
-> CROSS JOIN:
Returns the Cartesian product of both tables.
Every row of one table is combined with every row of the other table.
Example: SELECT * FROM table1 CROSS JOIN table2;
-> SELF JOIN:
Joins a table to itself.
Used to compare rows within the same table.

3. Difference between Joins vs Subquery?
-> Joins combine rows from multiple tables based on matching columns, while subqueries nest queries to filter or transform data.
-> Joins are generally faster for large datasets, while subqueries offer more flexibility in filtering data.

4. Find 3rd Highest Salary Of employee table ?
a.
SELECT DISTINCT salary
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET 2;

6. Difference between Rank vs Dense_rank? 
-> Rank Leaves gaps when there are ties (e.g., 1, 2, 2, 4, 5) but Dense_rank assigns consecutive ranks without gaps (e.g., 1, 2, 2, 3, 4)
-> Rank Uses non-consecutive integers but Dense_rank uses consecutive integers
"""


""" Unix section """

"""
1. Copy a file one directory to another directory?
a. 
Basic copy command: cp source_file destination/
Recursive copy of directory: cp -R source_dir/ destination/
Copy with verbose output: cp -v source_file destination/

2. How do you find the process IF(PID) of a running process?
a. Using ps command: ps aux | grep <process_name>
   Using pgrep command: pgrep <process_name>
3. difference between chown vs chmod?
a. chown: Used to change the ownership of a file or directory. It specifies which user and/or group owns the file.
  chmod: Used to adjust the access permissions for files or directories. It defines what actions (read, write, execute) are allowed for the owner, and group.
"""