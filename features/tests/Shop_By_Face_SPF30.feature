# Created by Eduardo Mandujano at 6/13/2023
Feature: Shop by Face - SPF30
  Verify the navigation to the Gentle Cleanse Face Foam from Shop by Face

  Scenario: Shop by Face - SPF 30
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on Shop By Face Link
    And Click on SPF30
    Then Verify that the user is navigated to the SPF30 Page
