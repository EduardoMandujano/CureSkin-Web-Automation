# Created by Eduardo Mandujano at 4/20/2023
Feature: Task 2
  Navigation - Top Logo takes user to the CureSkin Main Page

  Scenario: Clicking on the Top Logo navigates the user to the CureSkin Main Page
    Given Open CureSkin Search Results Page
    When Click on CureSkin logo in the Header
    Then Verify that user is taken to the main page
