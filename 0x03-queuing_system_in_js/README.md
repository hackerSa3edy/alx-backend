# Queueing System In JavaScript

This project contains tasks for learning to create a queueing system in JavaScript.

## Tasks To Complete

+ [x] 0. **Install a redis instance**
  + Download, extract, and compile Redis (version > 5.0.7)
  + Start Redis server, test connectivity with ping
  + Set value "School" for key "Holberton"
  + Requirements: Running `get Holberton` should return `School`

+ [x] 1. **Node Redis Client**
  + Install node_redis using npm
  + Write script to connect to Redis server
  + Implement connection success/error logging

+ [x] 2. **Node Redis client and basic operations**
  + Create functions:
    + setNewSchool(schoolName, value)
    + displaySchoolValue(schoolName)
  + Use callbacks for Redis operations

+ [x] 3. **Node Redis client and async operations**
  + Modify previous functions to use async/await with promisify

+ [x] 4. **Node Redis client and advanced operations**
  + Store hash values for HolbertonSchools
  + Add locations with hset: Portland=50, Seattle=80, etc.
  + Display stored hash using hgetall

+ [x] 5. **Node Redis client publisher and subscriber**
  + Create subscriber and publisher scripts
  + Implement channel subscription and message publishing
  + Handle special KILL_SERVER message

+ [x] 6. **Create the Job creator**
  + Create Kue queue
  + Create notification job with phoneNumber and message
  + Track job creation, completion and failure

+ [x] 7. **Create the Job processor**
  + Process jobs from queue
  + Implement sendNotification function
  + Handle job processing with Kue

+ [x] 8. **Track progress and errors with Kue: Create the Job creator**
  + Create multiple notification jobs from jobs array
  + Track job progress, completion and failures

+ [x] 9. **Track progress and errors with Kue: Create the Job processor**
  + Implement blacklist functionality
  + Process jobs with progress tracking
  + Handle concurrent job processing

+ [x] 10. **Writing the job creation function**
  + Implement createPushNotificationsJobs function
  + Validate jobs array
  + Create and track notification jobs

+ [x] 11. **Writing the test for job creation**
  + Write test suite for createPushNotificationsJobs
  + Test queue operations in test mode

+ [x] 12. **In stock?**
  + Create product inventory system
  + Implement Redis stock management
  + Create API endpoints:
    + GET /list_products
    + GET /list_products/:itemId
    + GET /reserve_product/:itemId

+ [x] 13. **Can I have a seat?**
  + Create seat reservation system with Redis
  + Implement reservation queue with Kue
  + Create endpoints:
    + GET /available_seats
    + GET /reserve_seat
    + GET /process
  + Handle concurrent reservations
