import time

from pages.registration_form_page import Calendar, TextForm, CheckBoxAndRadioBtn, DropDown, ResultTable


class TestCalendar:
    def test_select_deta(self, driver):
        registration_page = Calendar(driver, "https://demoqa.com/automation-practice-form")
        registration_page.open()
        month, month_num = registration_page.select_random_month()
        year = registration_page.select_random_year()
        day = registration_page.select_random_day(int(year), month_num)
        selected_date = f"{day} {month[:3]} {year}"
        result_deta = registration_page.get_result()
        # assert selected_date == result_deta, "Полученная дата не соответствует выбранной"


class TestTextForm:
    def test_fild_form(self, driver):
        registration_page = TextForm(driver, "https://demoqa.com/automation-practice-form")
        # registration_page.open()
        first_name, last_name, email, mobile, subjects, current_address = registration_page.fill_all_text_fields()
        return first_name, last_name, email, mobile, subjects, current_address


class TestCheckBoxAndRadioBtn:
    def test_radio_btn(self, driver):
        registration_page = CheckBoxAndRadioBtn(driver, "https://demoqa.com/automation-practice-form")
        # registration_page.open()
        gender = registration_page.select_random_radio()
        hobbies = registration_page.select_random_checkbox()
        return gender, hobbies


class TestDropDown:
    def test_drop_down(self, driver):
        registration_page = DropDown(driver, "https://demoqa.com/automation-practice-form")
        # registration_page.open()
        registration_page.select_state_and_city()
        state, citi = registration_page.get_result()
        return state, citi

    def test_result_table(self, driver):
        registration_page = ResultTable(driver, "https://demoqa.com/automation-practice-form")
        # registration_page.open()
        registration_page.click_submit()
        print(registration_page.get_result())


class TestPage:
    def test_all_page(self, driver):
        calendar = TestCalendar()
        text_form = TestTextForm()
        check_box = TestCheckBoxAndRadioBtn()
        drop_down = TestDropDown()
        calendar.test_select_deta(driver)
        text_form.test_fild_form(driver)
        check_box.test_radio_btn(driver)
        drop_down.test_drop_down(driver)
        time.sleep(5)
        drop_down.test_result_table(driver)