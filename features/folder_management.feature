Feature: Folder Management
  Scenario: Create New Folder
    Given Folder table is created and folders endpoint is available
    When a folder record is posted to api endpoint
    Then folder record is stored in database

  Scenario: Attempt To Create Invalid Folder
    Given Folder table is created and folders endpoint is available
    When a folder record with missing required data is posted to api endpoint
    Then api endpoint returns HTTP Status Bad Request

  Scenario: Get List of Folders
    Given Folder table is populated with data and folders endpoint is available
    When /folders endoint is requested
    Then list of folders are returned as json

  Scenario: Get List of Folders
    Given Folder table is empty and folders endpoint is available
    When /folders endoint is requested
    Then empty list is returned as json

  