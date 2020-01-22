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
    #select_country_option_xpath = "//span[contains(text(),'United Kingdom')]"

    # same locator //*[@id="accountToDebit"] (mikey to change this)
    enter_statement_acct_textbox_xpath = "//input[@id='statementAccount']"

    #open_dom_acct_xpath = "//p[contains(text(),'Open Domiciliary Account')]"
    #open_additional_act_xpath = "//p[contains(text(),'Open Additional Account')]"
    select_start_date_icon_xpath = "//div[@class='form-group col-6 px-1']//*[@class='feather feather-calendar']"
    select_start_date_xpath = "//div[contains(text(),'1')]"
    select_end_date_icon_xpath = "//div[@class='form-group col-6 px-1 mb-0']//*[@class='feather feather-calendar']"
    select_end_date_xpath = "//div[contains(text(),'31')]"

    # same locator //*[@id="accountToDebit"] (mikey to change this)
    enter_account_to_debit_xpath = "//*[@id='accountToDebit']"

    enter_role_xpath = "//input[@id='role']"
    enter_applicant_xpath = "//input[@id='applicant']"
    click_send_statement_btn_xpath = "//button[@id='validate']"
    click_ok_bt_xpath = "//button[@class='btn btn-round btn-light btn-sm px-3 mx-auto']"
    enter_token_xpath = "//input[@id='token']"
    submit_btn_xpath = "//button[@class='btn btn-sm btn-primary mr-2 btn-round pull-right ng-tns-c21-58 ng-star-inserted']"



