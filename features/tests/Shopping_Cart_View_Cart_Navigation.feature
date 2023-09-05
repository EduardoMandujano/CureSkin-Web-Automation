# Created by Eduardo Mandujano at 8/29/2023
Feature: Shopping Cart - View Cart Page Navigation
  Verify that after adding an item, the user is navigated to the Your Cart Page

  Scenario: Shopping Cart - View Cart Page Navigation
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on What's New Item Add to Cart Button
    And Click on the Sidebar View Cart Button
    Then Verify that the user was navigated to the Your Cart Page
    Then Verify that the cart contains the Item Added

