# Created by Eduardo Mandujano at 6/22/2023
Feature: Shop by Body - Restructure Cream
  Verify the navigation to Restructure Cream from Shop by Hair

  Scenario: Shop by Body - Restructure Cream
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on Shop By Body
    And Click on Restructure Cream
    Then Verify that the user is navigated to the Restructure Cream Page