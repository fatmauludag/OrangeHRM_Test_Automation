import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    yield driver
    driver.quit()

def test_login(setup):
    driver = setup
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit'").click()
    assert "dashboard" in driver.current_url.lower()

def test_navigate_to_employee_list(setup):
    driver = setup
    driver.find_element(By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']").click()
    assert "Employee List" in driver.title

def test_verify_existing_employee(setup):
    driver = setup
    name = driver.find_element(By.XPATH, "//tr[1]/td[3]").text
    emp_id = driver.find_element(By.XPATH, "//tr[1]/td[2]").text
    assert name and emp_id, "Name or ID is empty"

def test_add_new_employee(setup):
    driver = setup
    driver.find_element(By.CssSelector, "div.orangehrm-header-container > button
").click()
    driver.find_element(By.XPATH, " //input[@name="firstName"]").send_keys("Fatma")
    driver.find_element(By.XPATH, "//input[@name='lastName'").send_keys("Uluda")
    emp_id = driver.find_element(By.CssSelector, "div.oxd-form-row > div > div:nth-child(2) > div > div:nth-child(2) > input").get_attribute("value")
    driver.find_element(By.XPATH,  //button[@type='submit']").click()
    driver.find_element(By.ID, "menu_pim_viewEmployeeList").click()
    assert emp_id in driver.page_source

def test_search_employee(setup):
    driver = setup
    emp_id = "some_employee_id"
    driver.find_element(By.CssSelector, "div.oxd-form-row > div > div:nth-child(2) > div > div:nth-child(2) > input").send_keys(emp_id)
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    results = driver.find_element(By.CssSelector, ".oxd-table-card").text
    assert emp_id == results

def test_delete_employee(setup):
    driver = setup
    emp_id = "some_employee_id_to_delete"
    driver.find_element(By.XPATH, "//div[@class="oxd-table-body"]/div[1]/div[1]/div[9]/div/button[2]").click()
    driver.find_element(By.XPATH, "div.orangehrm-modal-footer > button.oxd-button.oxd-button--medium.oxd-button--label-danger.orangehrm-button-margin
").click()
    assert emp_id not in driver.page_source
