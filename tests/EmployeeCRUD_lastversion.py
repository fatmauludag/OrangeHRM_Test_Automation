import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()  # Pencereyi tam ekran yapar
    yield driver


# driver.quit()
def wait_until_page_load(driver, timeout=10):
    """Sayfa tamamen yüklenene kadar bekle."""
    WebDriverWait(driver, timeout).until(lambda d: d.execute_script("return document.readyState") == "complete")

def test_login(setup):
    driver = setup
    Admin = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
    # Wait for the element to be visible
    Admin.click()
    Admin.send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()


# assert "dashboard" in driver.current_url.lower()


def test_navigate_to_employee_list(setup):
    driver = setup
    Pim = WebDriverWait(driver, 100).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.oxd-main-menu>li:nth-child(2)>a")))
    Pim.click()
    # WebDriverWait(100)
    # assert "Employee List" in driver.title
    employee_list_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Employee List')]")
    assert employee_list_button.is_displayed(), "Employee List is not displayed"


def test_add_new_employee(setup):
    driver = setup
    add_btn = WebDriverWait(driver, 100).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".orangehrm-header-container>button")))
    add_btn.click()
    add_name = driver.find_element(By.XPATH, " //input[@name='firstName']").send_keys("Fatma")
    add_last = driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys("Uluda")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    # assert add_name in driver.page_source


def test_search_employee(setup):
    driver = setup
    # Sayfa yüklenmesini bekle
    wait_until_page_load(driver)
    pim_menu = WebDriverWait(driver, 100).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.oxd-main-menu>li:nth-child(2)>a")))
    pim_menu.click()
    src_emp_id = WebDriverWait(driver, 100).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, " div.oxd-form-row > div > div:nth-child(2) > div > div:nth-child(2) > input")))
    src_emp_id.click()
    src_emp_id.send_keys("01715")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    # assert emp_id == results

def test_delete(setup):
    driver = setup

    # Sayfa yüklenmesini bekle
    wait_until_page_load(driver)
    pim_menu = WebDriverWait(driver, 100).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.oxd-main-menu>li:nth-child(2)>a")))
    pim_menu.click()

    # Silme butonunu bul ve tıkla
    emp_delete = WebDriverWait(driver, 100).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".oxd-table-card > div > div:nth-child(9) > div > button:nth-child(2)")
        )
                                                 )
    emp_delete.click()

    # 'Evet, sil' butonunu bul ve tıkla
    emp_yesDelete = WebDriverWait(driver, 100).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".oxd-button.oxd-button--medium.oxd-button--label-danger.orangehrm-button-margin")
        )
    )
    emp_yesDelete.click()

    # Silme işleminin tamamlanmasını bekle (isteğe bağlı olarak doğrulama eklenebilir)
    #WebDriverWait(driver, 10).until(
     #   EC.invisibility_of_element((By.CSS_SELECTOR, ".oxd-table-card > div")))
