# Created by Eduardo Mandujano at 7/5/2023
Feature: Shop by Body - Restructure Cream
  Verify the navigation to Restructure Cream from Shop by Hair

  Scenario: Shop by Body - Restructure Cream
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on Shop by Body
    And Click on SPF30 from Shop by Body
    Then Verify that the user is navigated to the SPF30 Page from Shop by Body