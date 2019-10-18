/// <reference types ="Cypress"/>

context('Transfer2Gtb', () => {
    before('login',() => {
        cy.visit('/')
        cy.get('#Username').type('205132266')
        cy.get('.keypad-font').contains('1').click()
        cy.get('.keypad-font').contains('2').click()
        cy.get('.keypad-font').contains('3').click()
        cy.get('.keypad-font').contains('4').click()
        cy.get('.keypad-font').contains('5').click()
        cy.get('.keypad-font').contains('6').click()
        cy.get('.keypad-btn').contains('SIGN IN').click()
        cy.get('#clearLoader').click()
    })
    it('test', () => {
        cy.get('[ng-reflect-group="transfers"][item-border="true"] > li.ng-tns-c9-2 > .ng-star-inserted > .pcoded-micon').click()
        cy.get('#accountToDebit').type('{enter}')

    })
})