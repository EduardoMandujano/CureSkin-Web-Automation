# Created by Eduardo Mandujano at 7/17/2023
Feature: Shop by Face (Page 2) - TXA Clear Cream
  Verify the navigation to TXA Clear Cream from Shop by Face

  Scenario: Shop by Face (Page 2) - TXA Clear Cream
    Given Open CureSkin Home Page
    # When Click on the X to close the Popup Window
    When Click on Shop By Face Link
    And Click on the Next Page Link
    And Click on TXA Clear Cream
    Then Verify that the user is navigated to the TXA Clear Cream Page from Shop by Face