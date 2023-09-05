# Created by Eduardo Mandujano at 8/24/2023
Feature: Shopping Cart Icon - Empty
  Verify the sidebar text when the Shopping Cart is empty

  Scenario: Shopping Cart Icon - Empty
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on the Header Shopping Cart Icon
    Then Verify the correct sidebar text when the Shopping Cart is empty