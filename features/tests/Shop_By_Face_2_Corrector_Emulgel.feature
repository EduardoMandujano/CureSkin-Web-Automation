# Created by Eduardo Mandujano at 7/11/2023
Feature: Shop by Face (Page 2) - Corrector Emulgel
  Verify the navigation to Corrector Emulgel from Shop by Face

  Scenario: Shop by Face (Page 2) - Corrector Emulgel
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on Shop By Face Link
    And Click on the Next Page Link
    And Click on Corrector Emulgel
    Then Verify that the user is navigated to the Corrector Emulgel Page from Shop by Face