Feature: Example

  @google
  Scenario: Search Selenium on Google
  Given open Google page
  When type Selenium on search input
  Then verify the results are being shown