class LocatorsC():
    # loginPage Object Locators
    username_textbox_xpath = "//input[@id='Username']"
    pass_btn_1_xpath = "//h6[contains(text(),'1')]"
    pass_btn_2_xpath = "//h6[contains(text(),'2')]"
    pass_btn_3_xpath = "//h6[contains(text(),'3')]"
    pass_btn_4_xpath = "//h6[contains(text(),'4')]"
    pass_btn_5_xpath = "//h6[contains(text(),'5')]"
    pass_btn_6_xpath = "//h6[contains(text(),'6')]"
    pass_btn_7_xpath = "//h6[contains(text(),'7')]"
    pass_btn_8_xpath = "//h6[contains(text(),'8')]"
    pass_btn_9_xpath = "//h6[contains(text(),'9')]"
    pass_btn_0_xpath = "//h6[contains(text(),'0')]"
    sign_in_btn_xpath = "//div[@class='col-12 text-center my-auto h-100']"
    proceed_btn_xpath = "//button[@id='clearLoader']"

    # DashboardPage Object Locators
    frequent_transaction_xpath = "//h4[contains(text(),'Frequent Transactions')]"
    frequent_transfers_xpath = "//h5[contains(text(),'Frequent Transfers')]"
    frequent_topup_xpath = "//h5[contains(text(),'Frequent Topup')]"
    frequent_bills_xpath = "//h5[contains(text(),'Frequent Bills')]"
    gt_track_it_xpath = "//h5[contains(text(),'GT TrackIt')]"
    view_statement_btn_xpath = "//ngu-tile[1]//div[1]//div[1]//div[1]//div[1]//div[1]"
    account_statement_xpath = "//h5[@class='text-primary f-w-100 f-18 mb-0']"

    # AccountPage Object Locators
    send_to_3rd_party_btn_xpath = "//div[@class='row submenu text-center mx-1 mt-3']//div[2]//div[1]//div[1]"
    enter_country_textbox_xpath = "//input[@id='destination']"
    # select_country_option_xpath = "//span[contains(text(),'United Kingdom')]"

    # same locator //*[@id="accountToDebit"] (mikey to change this)
    enter_statement_acct_textbox_xpath = "/html/body/app-root/app-customer/div[1]/div[2]/div[3]/div/div/div/div/div/app-accounts/div[2]/div[1]/div/gtibank-generate-statement/div/div/div/div/form/div[2]/div[2]/gtibank-accounts-typeahead/ng-select/div/div/div[2]/input"

    # open_dom_acct_xpath = "//p[contains(text(),'Open Domiciliary Account')]"
    # open_additional_act_xpath = "//p[contains(text(),'Open Additional Account')]"
    select_start_date_icon_xpath = "//div[@class='form-group col-6 px-1']//*[@class='feather feather-calendar']"
    select_start_date_xpath = "//div[contains(text(),'1')]"
    select_end_date_icon_xpath = "//div[@class='form-group col-6 px-1 mb-0']//*[@class='feather feather-calendar']"
    select_end_date_xpath = "//div[contains(text(),'31')]"

    # same locator //*[@id="accountToDebit"] (mikey to change this)
    enter_account_to_debit_xpath = "/html[1]/body[1]/app-root[1]/app-customer[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/app-accounts[1]/div[2]/div[1]/div[1]/gtibank-generate-statement[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[5]/gtibank-accounts-typeahead[1]/ng-select[1]/div[1]/div[1]/div[2]/input[1]"

    enter_role_xpath = "//input[@id='role']"
    enter_applicant_xpath = "//input[@id='applicant']"
    click_send_statement_btn_xpath = "//button[@id='validate']"
    click_ok_bt_xpath = "//button[@class='btn btn-round btn-light btn-sm px-3 mx-auto']"
    enter_token_xpath = "//input[@id='token']"
    submit_btn_xpath = "//button[contains(text(),'Submit')]"
    open_dom_account_btn_xpath = "//p[contains(text(),'Open Domiciliary Account')]"
    enter_currency_type_xpath = "//input[@id='currency']"
    enter_secret_question_xpath = "//input[@placeholder='Answer to secret Question']"
    accept_checkbox_xpath = "//i[@class='cr-icon icofont icofont-ui-check txt-primary']"
    submit_btn_validate_xpath = "//button[@id='validate']"
    # submit_btn_xpath

    open_additional_account_btn_xpath = "//p[contains(text(),'Open Additional Account')]"
    enter_account_type_xpath = "//input[@id='accountType']"
    success_text_xpath = "//p[contains(@class,'my-auto')]"  # Success - Additional Account has been Opened
