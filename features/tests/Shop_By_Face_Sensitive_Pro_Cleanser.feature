# Created by Eduardo Mandujano at 6/14/2023
Feature: Shop by Face - Sensitive Pro Cleanser
  Verify the navigation to Sensitive Pro Cleanser from Shop by Face

  Scenario: Shop by Face - Sensitive Pro Cleanser
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on Shop By Face Link
    And Click on Sensitive Pro Cleanser
    Then Verify that the user is navigated to the Sensitive Pro Cleanser Page