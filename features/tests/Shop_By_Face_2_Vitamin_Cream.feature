# Created by Eduardo Mandujano at 7/13/2023
Feature: Shop by Face (Page 2) - Vitamin ABC Cream
  Verify the navigation to Lightening Day Cream from Shop by Face

  Scenario: Shop by Face (Page 2) - Vitamin ABC Cream
     Given Open CureSkin Home Page
    # When Click on the X to close the Popup Window
    When Click on Shop By Face Link
    And Click on the Next Page Link
    And Click on Vitamin ABC Cream Cream
    Then Verify that the user is navigated to the Vitamin ABC Cream Page from Shop by Face