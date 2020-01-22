class LocatorsE():
    cardtype_btn_xpath = "//select[@id='dpCardType']"
    regular_btn_xpath = "//option[contains(text(),'Regular')]"
    action_btn_xpath = "//select[@id='dpAction']"
    collection_btn_xpath = "//option[contains(text(),'COLLECTION')]"
    AcctNum_textbox_xpath = "//input[@id='nubanAcct']"
    #Go_click_xpath = "//button[@id='button-addon2']"
    Go_click_css_selector = "#button-addon2"
    #view_click_xpath = "//tr[1]//td[1]//a[1]//i[1]"
    view_click_css_selector = "div.main-dashboard div.function-section div.container-fluid.horizontal-container div.ps div.ps-content div.card.shadow-sm.mt-4 div.card-body div.pt-3:nth-child(4) table.table.table-bordered tbody:nth-child(2) tr:nth-child(1) td:nth-child(1) a:nth-child(1) > i.fa.fa-eye"
    self_click_xpath = "//div[1]//input[1]"
    submit_btn_xpath = "//button[@id='btnCollect']"

