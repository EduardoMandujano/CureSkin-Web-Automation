# Created by Eduardo Mandujano at 6/12/2023
Feature: Shop by Face - Hydration Gel
  Verify the navigation to Hydration Gel from Shop by Face

  Scenario: Shop by Face -  Hydration Gel
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on Shop By Face Link
    And Click on Hydration Gel
    Then Verify that the user is navigated to the Hydration Gel Page
