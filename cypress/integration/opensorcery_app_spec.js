describe('Opensorcery App', function () {
  it('should() - assert that <title> is correct', function () {
    cy.visit('localhost:8000')
    cy.title().should('include', 'Opensorcery')
  })
})
