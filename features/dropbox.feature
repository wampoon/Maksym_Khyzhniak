Feature: Dropbox API

    Scenario: Upload file
        Given file named "file.txt"
        When we upload file "file.txt" to Dropbox
        Then we see file "file.txt" uploaded
        
    Scenario: Get file metadata by id
        Given file named "file.txt" is uploaded
        When we request metadata of file "file.txt" by id
        Then we receive metadata for file "file.txt"
        
    Scenario: Delete file by path
        Given we have absolute file path after file "file.txt" was downloaded
        When we request to delete file "file.txt"
        Then we see file "file.txt" deleted
        