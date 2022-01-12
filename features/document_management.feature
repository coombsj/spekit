Feature: Document Management
  Background:
    Given Document table is created and documents endpoint is available

  Scenario: Create New Document
    When a document record is posted to api endpoint
    Then document record is stored in database

  Scenario: Attempt To Create Invalid Document
    When a document record with missing required data is posted to api endpoint
    Then api endpoint returns HTTP Status Bad Request

  Scenario: Get List of Documents
    Given Document table is populated with data
    When /documents endoint is requested
    Then list of documents are returned as json

  Scenario: Get List of Documents
    Given Document table is empty
    When /documents endoint is requested
    Then empty list is returned as json

  Scenario: Get List of Documents in Folder
    Given Document table is populated with data that is associated with folder 1
    When /documents endoint is requested with query param of folder_id=1
    Then list of documents that are associated with the folder with id=1 are returned as json

  Scenario: Get List of Documents for Empty Folder  
    Given Document table is populated with data where no documents are associated with folder 1
    When /documents endoint is requested with query param of folder_id=1
    Then empty list is returned as json

  Scenario: Get List of Documents By Topic
    Given Document table is populated with data that is associated with topic 1
    When /documents endoint is requested with query param of topic_id=1
    Then list of documents that are associated with the topic with id=1 are returned as json

  Scenario: Get List of Documents By Topic
    Given Document table is populated with data where no documents are associated with topic 1
    When /documents endoint is requested with query param of topic_id=1
    Then empty list is returned as json

  Scenario: Get List of Documents By Folder and Topic
    Given Document table is populated with data that is associated with folder 1 AND topic 1
    When /documents endoint is requested with query param of folder_id=1&topic_id=1
    Then list of documents that are associated with the folder with id=1 AND topic with id=1 are returned as json

  Scenario: Get List of Documents By Folder and Topic
    Given Document table is populated with data where no documents are associated with folder 1 AND topic 1
    When /documents endoint is requested with query param of folder_id=1&topic_id=1
    Then empty list is returned as json