/// <reference types="Cypress" />

context('Accounts', () => {
    before(() => {
        cy.server()
        cy.visit('/')
        cy.get('#Username').type('205154202')
        //cy.get('.keypad-font').contains('0').click()
        cy.get('.keypad-font').contains('1').click()
        cy.get('.keypad-font').contains('2').click()
        cy.get('.keypad-font').contains('3').click()
        cy.get('.keypad-font').contains('4').click()
        cy.get('.keypad-font').contains('5').click()
        cy.get('.keypad-font').contains('6').click()
        cy.get('.keypad-btn').contains('SIGN IN').click()
        cy.get('#clearLoader').click()
    })

    it('View Account Statement', () => {
        cy.get('[ng-reflect-group="accounts"][item-border="true"] > li.ng-tns-c9-2 > .ng-star-inserted > .pcoded-mtext')
            .click()
        cy.wait(500)
        cy.contains('Account Statement')
        cy.contains('Available Balance:')
        cy.contains('₦')        
    })

    it('Sends Statement To Third Party', () => {
        cy.get('.submenu > :nth-child(2) > .card > .card-block > .img-fluid').click()
        cy.get('#destination').type('United Kingdom {enter}')
        //cy.get('#a20f03cbb34b-0 > .ng-tns-c31-14').click()
        cy.get('#statementAccount > .accountToDebit > .ng-select-container > .ng-value-container > .ng-input > #accountToDebit')
            .click()
        cy.get('#a182fb51f306-0 > .f-w-500').click()
        cy.get(':nth-child(3) > .input-group > .input-group-append > .btn > .ng-tns-c31-14 > .feather').click()
        
        // cy.get('[aria-label="Sunday, September 1, 2019"] > .btn-light').click()
        cy.get('[aria-label="Select month"]').contains('Jan').click()
        cy.get('.form-group.mb-0 > .input-group > .input-group-append > .btn > .ng-tns-c31-14 > .feather').click()
        cy.get('[aria-label="Thursday, October 31, 2019"] > .btn-light').click()
        cy.get(':nth-child(5) > .ng-tns-c31-14 > .accountToDebit > .ng-select-container > .ng-value-container > .ng-input > #accountToDebit')
            .click()
        cy.get(':nth-child(5) > .ng-tns-c31-14 > .accountToDebit > .ng-select-container > .ng-value-container > .ng-input > #accountToDebit')
            .click()
        cy.get('#aca40f6c9bb3-0 > .f-w-100').click()
        cy.get('#role').click()
        cy.get('#a8b20f22fdc5-0 > .ng-option-label').click()
        cy.get('#applicant').type('Automated Tester')
        cy.get('.form-row > :nth-child(9)').click()
        cy.get('.ng-tns-c30-15 > .btn').click()
        cy.get('#token').type('123456')
        cy.get('.card-footer > .btn-primary').click()
        cy.contains('Operation Successful')
    })

    it('Opens dom account', () => {
        cy.get('.submenu > :nth-child(3) > .card > .card-block > .m-b-0').click()

    })
})