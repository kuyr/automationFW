it('test', () => {
    cy.visit('https://www.facebook.com')
    cy.get('#u_0_m').type('babydaddy')
    cy.get('#u_0_o').type('Gb')
    cy.get('#u_0_r').type('09096030154')
    cy.get('#u_0_y').type('Alexandra')
    cy.get('#day').select('17')
    cy.get('#month').select('Apr')
    cy.get('#year').select('1995')
    cy.contains('Female').click()
    cy.get('#u_0_15').click()
    
    





  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    // cy.visit("https://facebook.com")
    // cy.get('#u_0_m').type("Lanre")
    // cy.get('#u_0_o').type("Jones")
    // cy.get('#u_0_r').type("08027804779")
    // cy.get('#u_0_y').type("menababy")
    // cy.get("#day").select("10")
    // cy.get("#month").select("Jun")
    // cy.get("#year").select("1992")
    // cy.get('#u_0_6').click()
    //cy.get('#Passwd').type('PythonJava')
    //cy.get('#signIn').click()

    

    

  
}
)