Feature: Topic Management
  Scenario: Create New Topic
    Given Topic table is created and topic endpoint is available
    When a topic record is posted to api endpoint
    Then topic record is stored in database

  Scenario: Attempt To Create Invalid Topic
    Given Topic table is created and topic endpoint is available
    When a topic record with missing required data is posted to api endpoint
    Then api endpoint returns HTTP Status Bad Request

  Scenario: Get List of Topics
    Given Topic table is populated with data and topic endpoint is available
    When /topics endoint is requested
    Then list of topics are returned as json

  Scenario: Get List of Topics
    Given Topic table is empty and topic endpoint is available
    When /topics endoint is requested
    Then empty list is returned as json
