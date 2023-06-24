# Created by Eduardo Mandujano at 6/20/2023
Feature: Shop by Hair - Hair Conditioner
  Verify the navigation to Hair Conditioner from Shop by Hair

  Scenario: Shop by Hair - Hair Conditioner
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on Shop By Hair
    And Click on Hair Conditioner
    Then Verify that the user is navigated to the Hair Conditioner Page