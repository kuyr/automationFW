/// <reference types="Cypress" />

context('Dashboard', () => {
    before(() => {
        cy.visit('/')
        cy.get('#Username').type('205132266')
       // cy.get('.keypad-font').contains('0').click()
        cy.get('.keypad-font').contains('1').click()
        cy.get('.keypad-font').contains('2').click()
        cy.get('.keypad-font').contains('3').click()
        cy.get('.keypad-font').contains('4').click()
        cy.get('.keypad-font').contains('5').click()
        cy.get('.keypad-font').contains('6').click()
        //cy.get('.keypad-btn').contains('SIGN IN').click()
        //cy.get('#clearLoader').click()
        
    })
     it('Account Balance is visible and clickable', () => {
        cy.contains('Account Balance').should('be.visible')
        cy.get(':nth-child(1) > .tile > .card > .card-block > .row > .col-12 > .f-w-400').click()
        cy.url().should('include', '/portal/accounts/statement')
        cy.get('[ng-reflect-group="dashboard"][item-border="true"] > li.ng-tns-c9-2 > .ng-star-inserted > .pcoded-mtext').click()
     })
    it('GT TrackIt (cheque book request)', () => {
        cy.contains('GT TrackIt').should('be.visible')
        cy.contains('Cheque Book').should('be.visible')
        cy.contains('Track ID').should('be.visible')
        
    })
})