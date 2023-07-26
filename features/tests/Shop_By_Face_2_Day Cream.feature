# Created by Eduardo Mandujano at 7/12/2023
Feature: Shop by Face (Page 2) - Lightening Day Cream
  Verify the navigation to Lightening Day Cream from Shop by Face

  Scenario: Shop by Face (Page 2) - Lightening Day Cream
    Given Open CureSkin Home Page
    # When Click on the X to close the Popup Window
    When Click on Shop By Face Link
    And Click on the Next Page Link
    And Click on Lightening Day Cream
    Then Verify that the user is navigated to the Lightening Day Cream Page from Shop by Face