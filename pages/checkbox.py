from pages.base import BasePage


class CheckboxPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkbox = self.page.get_by_role("checkbox")
        self.url = "https://the-internet.herokuapp.com/checkboxes"

    def navigate(self):
        self.page.goto(self.url)

    def select_checkbox(self, index):
        checkbox_length = self.get_number_of_checkboxes()

        if (index > checkbox_length) or (index < 1):
            raise ValueError(f"Index is out of range. Max index is {checkbox_length} and starts at 1.")
        else:
            self.unselect_all()

        if index == 1:
            self.checkbox.first.check()
        else:
            self.checkbox.nth(index-1).check()
    
    def select_all(self):
        self.checkbox.first.check()
        for checkbox in range(self.get_number_of_checkboxes()):
            self.checkbox.nth(checkbox-1).check()

    def unselect_all(self):
        self.checkbox.first.uncheck()
        for checkbox in range(self.get_number_of_checkboxes()):
            self.checkbox.nth(checkbox-1).uncheck()
    
    def get_number_of_checkboxes(self):
        return self.checkbox.evaluate_all("nodes => nodes.length")