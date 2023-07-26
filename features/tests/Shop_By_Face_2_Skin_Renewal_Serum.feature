# Created by Eduardo Mandujano at 7/25/2023
Feature: Shop by Face (Page 2) - Skin Renewal Serum
  Verify the navigation to Skin Renewal Serum from Shop by Face

  Scenario: Shop by Face (Page 2) - Skin Renewal Serum
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on Shop By Face Link
    And Click on the Next Page Link
    And Click on Skin Renewal Serum
    Then Verify that the user is navigated to the Skin Renewal Serum Page from Shop by Face