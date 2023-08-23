# Created Eduardo Mandujano at 8/8/2023
Feature: Shop All Main Page
  Verify the navigation to the Shop All Main Page

  Scenario: Shop All Main Page
    Given Open CureSkin Home Page
    # When Click on the X to close the Popup Window
    When Click on the Shop All Header Link
    Then Verify that the user is navigated to the Shop All Main Page