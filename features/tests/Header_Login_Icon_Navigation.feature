# Created by Eduardo Mandujano at 5/7/2023
Feature: Header Login Icon Navigation
  Verification that clicking on the Header Login Icon takes the user to the Login Page

  Scenario: On click, the Header Login Icon takes the user to the Login Page
    Given Open CureSkin Home Page
    When Click on Login Icon in the Header
    Then Verify that the user is taken to the Login Page