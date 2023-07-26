# Created by Eduardo Mandujano at 7/9/2023
Feature: Shop by Body - Hydration Gel
  Verify the navigation to Hydration Gel from Shop by Body

  Scenario: Shop by Body - Hydration Gel
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on Shop by Body
    And Click on Hydration Gel from Shop by Body
    Then Verify that the user is navigated to the Hydration Gel Page from Shop by Body