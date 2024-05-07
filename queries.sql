-- DDL Statements
-- Create Users table
CREATE TABLE Users (
  UserID INT PRIMARY KEY,
  Name VARCHAR(255),
  Email VARCHAR(255) UNIQUE,
  AccountCreationDate DATE
);

-- Create Components table
CREATE TABLE Components (
  HWID INT PRIMARY KEY,
  Name VARCHAR(255),
  Brand VARCHAR(255),
  Model VARCHAR(255),
  Year INT,
  Price INT
);

-- Create Builds table
CREATE TABLE Builds (
  BuildID INT PRIMARY KEY,
  UserID INT,
  TotalPrice INT,
  FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Create Guides table
CREATE TABLE Guides (
  GuideID INT PRIMARY KEY,
  UserID INT,
  Title VARCHAR(255),
  FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Create GuideReviews table
CREATE TABLE GuideReviews (
  ReviewID INT PRIMARY KEY,
  GuideID INT,
  Stars INT,
  FOREIGN KEY (GuideID) REFERENCES Guides(GuideID)
);

-- Create ForumPosts table
CREATE TABLE ForumPosts (
  PostID INT PRIMARY KEY,
  UserID INT,
  Topic VARCHAR(255),
  DiscussionContent TEXT,
  FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Create CPU table
CREATE TABLE CPU (
  HWID INT PRIMARY KEY,
  Cores INT,
  ClockSpeed INT,
  Chipset VARCHAR(255),
  TDP INT,
  FOREIGN KEY (HWID) REFERENCES Components(HWID)
);

-- Create Motherboard table
CREATE TABLE Motherboard (
  HWID INT PRIMARY KEY,
  Chipset VARCHAR(255),
  PcieSlots INT,
  Size VARCHAR(255),
  FOREIGN KEY (HWID) REFERENCES Components(HWID)
);

-- Create Memory table
CREATE TABLE Memory (
  HWID INT PRIMARY KEY,
  DDR VARCHAR(255),
  Speed INT,
  Latency VARCHAR(255),
  FOREIGN KEY (HWID) REFERENCES Components(HWID)
);

-- Create GPU table
CREATE TABLE GPU (
  HWID INT PRIMARY KEY,
  PcieSlots INT,
  Power INT,
  FOREIGN KEY (HWID) REFERENCES Components(HWID)
);

-- Create Storage table
CREATE TABLE Storage (
  HWID INT PRIMARY KEY,
  Capacity INT,
  Type VARCHAR(255),
  Interface VARCHAR(255),
  Size VARCHAR(255),
  FOREIGN KEY (HWID) REFERENCES Components(HWID)
);

-- Create BuildComponents table
CREATE TABLE BuildComponents (
  BuildID INT,
  HardwareID INT,
  FOREIGN KEY (BuildID) REFERENCES Builds(BuildID),
  FOREIGN KEY (HardwareID) REFERENCES Components(HWID),
  PRIMARY KEY (BuildID, HardwareID)
);

-- Create PostedBuilds table
CREATE TABLE PostedBuilds (
  BuildID INT PRIMARY KEY,
  PostDate DATE,
  Likes INT,
  Dislikes INT,
  FOREIGN KEY (BuildID) REFERENCES Builds(BuildID)
);

-- Create Feedback table
CREATE TABLE Feedback (
  CommentID INT PRIMARY KEY,
  ReviewID INT,
  Comment TEXT,
  FOREIGN KEY (ReviewID) REFERENCES GuideReviews(ReviewID)
);

-- Create Comments table
CREATE TABLE Comments (
  CommentID INT PRIMARY KEY,
  PostID INT,
  UserID INT,
  Text TEXT,
  Likes INT,
  Dislikes INT,
  FOREIGN KEY (PostID) REFERENCES ForumPosts(PostID)
);

-- Create Sponsor table
CREATE TABLE Sponsor (
  SponsorID INT PRIMARY KEY,
  GuideID INT,
  UserID INT,
  OrganizationName VARCHAR(255),
  FinancialContribution DECIMAL(10, 2),
  ContactInfo VARCHAR(255),
  FOREIGN KEY (GuideID) REFERENCES Guides(GuideID),
  FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Controllers/builds.py Line 6
-- INSERT INTO Builds (BuildID, UserID, TotalPrice) VALUES (%s, %s, %s)

-- Controllers/builds.py Line 12
-- SELECT * FROM Builds WHERE BuildID = %s

-- Controllers/builds.py Line 18
-- SELECT * FROM Builds WHERE BuildID = %s where total_price + filter + %s

-- Controllers/builds.py Lines 24-30

-- SELECT B.BuildID, C.Name, C.Brand, C.Model, C.Year, C.Price
-- FROM Builds B
-- JOIN BuildComponents BC ON B.BuildID = BC.BuildID
-- JOIN Components C ON BC.HardwareID = C.HWID
-- WHERE B.BuildID = %s


-- Controllers/builds.py Lines 36-44

-- SELECT UserID, COUNT(BuildID) AS TotalBuilds
-- FROM Builds
-- GROUP BY UserID
-- HAVING AVG(TotalPrice) >= (
--     SELECT AVG(TotalPrice)
--     FROM Builds
-- )


-- Controllers/builds.py Line 50
-- UPDATE Builds SET UserID = %s, TotalPrice = %s WHERE BuildID = %s

-- Controllers/builds.py Line 56
-- DELETE FROM Builds WHERE BuildID = %s

-- Controllers/builds.py Line 66
-- INSERT INTO BuildComponents (BuildID, HardwareID) VALUES (%s, %s)

-- Controllers/builds.py Line 72
-- SELECT * FROM BuildComponents WHERE BuildID = %s AND HardwareID = %s

-- Controllers/builds.py Line 78
-- DELETE FROM BuildComponents WHERE BuildID = %s AND HardwareID = %s

-- Controllers/builds.py Line 88
-- INSERT INTO PostedBuilds (BuildID, PostDate, Likes, Dislikes) VALUES (%s, %s, %s, %s)

-- Controllers/builds.py Line 94
-- SELECT * FROM PostedBuilds WHERE BuildID = %s

-- Controllers/builds.py Line 100
-- UPDATE PostedBuilds SET PostDate = %s, Likes = %s, Dislikes = %s WHERE BuildID = %s

-- Controllers/builds.py Line 106
-- DELETE FROM PostedBuilds WHERE BuildID = %s


-- Controllers/components.py Line 7
-- INSERT INTO Components (HWID, Name, Brand, Model, Year, Price) VALUES (%s, %s, %s, %s, %s, %s)

-- Controllers/components.py Line 13
-- SELECT * FROM Components WHERE HWID = %s

-- Controllers/components.py Line 20
-- SELECT {cols} FROM Components

-- Controllers/components.py Line 26
-- SELECT * FROM Components

-- Controllers/components.py Line 32
-- SELECT * FROM Components where (Price >= %s/Price <= %s/Year >= %s/Year <= %s)
-- conditions in the brackets joined with and if chosen by the user.

-- Controllers/components.py Line 54
-- UPDATE Components SET Name = %s, Brand = %s, Model = %s, Year = %s, Price = %s WHERE HWID = %s

-- Controllers/components.py Line 60
-- DELETE FROM Components WHERE HWID = %s

-- Controllers/components.py Line 72
-- INSERT INTO CPU (HWID, Cores, ClockSpeed, Chipset, TDP) VALUES (%s, %s, %s, %s, %s)

-- Controllers/components.py Line 78
-- SELECT * FROM CPU WHERE HWID = %s

-- Controllers/components.py Line 84
-- SELECT * FROM CPU

-- Controllers/components.py Line 91
-- UPDATE CPU SET Cores = %s, ClockSpeed = %s, Chipset = %s, TDP = %s WHERE HWID = %s

--  Controllers/components.py Line 97
-- DELETE FROM CPU WHERE HWID = %s

--  Controllers/components.py Line 110
-- INSERT INTO Motherboard (HWID, Chipset, PcieSlots, Size) VALUES (%s, %s, %s, %s)

--  Controllers/components.py Line 116
-- SELECT * FROM Motherboard WHERE HWID = %s

--  Controllers/components.py Line 122
-- SELECT * FROM Motherboard

--  Controllers/components.py Line 129
-- UPDATE Motherboard SET Chipset = %s, PcieSlots = %s, Size = %s WHERE HWID = %s

--  Controllers/components.py Line 135
-- DELETE FROM Motherboard WHERE HWID = %s

--  Controllers/components.py Line 148
-- INSERT INTO GPU (HWID, PcieSlots, Power) VALUES (%s, %s, %s)

--  Controllers/components.py Line 154
-- SELECT * FROM GPU WHERE HWID = %s

--  Controllers/components.py Line 160
-- SELECT * FROM GPU

--  Controllers/components.py Line 167
-- UPDATE GPU SET PcieSlots = %s, Power = %s WHERE HWID = %s

--  Controllers/components.py Line 173
-- DELETE FROM GPU WHERE HWID = %s

--  Controllers/components.py Line 186
-- INSERT INTO Storage (HWID, Capacity, Type, Interface, Size) VALUES (%s, %s, %s, %s, %s)

--  Controllers/components.py Line 192
-- SELECT * FROM Storage WHERE HWID = %s

--  Controllers/components.py Line 198
-- SELECT * FROM Storage

--  Controllers/components.py Line 205
-- UPDATE Storage SET Capacity = %s, Type = %s, Interface = %s, Size = %s WHERE HWID = %s

--  Controllers/components.py Line 211
-- DELETE FROM Storage WHERE HWID = %s

--  Controllers/users.py Line 6
-- INSERT INTO Users (UserID, Name, Email, AccountCreationDate) VALUES (%s, %s, %s, %s)

--  Controllers/users.py Line 12
-- SELECT * FROM Users WHERE UserID = %s

--  Controllers/users.py Line 19
-- SELECT U.UserID, U.Name, SUM(B.Price) AS TotalPrice
-- FROM Users U
-- JOIN Builds B ON U.UserID = B.UserID
-- GROUP BY U.UserID, U.Name

--  Controllers/users.py Line 30
-- SELECT UserID, COUNT(*) AS NumberOfBuilds
-- FROM Builds
-- GROUP BY UserID
-- HAVING COUNT(*) > %s

--  Controllers/users.py Line 41
-- SELECT DISTINCT U.UserID, U.Name
-- FROM Users U
-- WHERE NOT EXISTS (
--     SELECT C.HWID
--     FROM Components C
--     WHERE NOT EXISTS (
--         SELECT BC.HardwareID
--         FROM Builds B
--         JOIN BuildComponents BC ON B.BuildID = BC.BuildID
--         WHERE B.UserID = U.UserID AND BC.HardwareID = C.HWID
--     )
-- )

--  Controllers/users.py Line 59
-- UPDATE Users SET Name = %s, Email = %s WHERE UserID = %s

--  Controllers/users.py Line 65
-- DELETE FROM Users WHERE UserID = %s

--  Controllers/users.py Line 75
-- INSERT INTO Guides (GuideID, UserID, Title) VALUES (%s, %s, %s)

--  Controllers/users.py Line 81
-- SELECT * FROM Guides WHERE GuideID = %s

--  Controllers/users.py Line 87
-- UPDATE Guides SET UserID = %s, Title = %s WHERE GuideID = %s

--  Controllers/users.py Line 93
-- DELETE FROM Guides WHERE GuideID = %s

--  Controllers/users.py Line 103
-- INSERT INTO GuideReviews (ReviewID, GuideID, Stars) VALUES (%s, %s, %s)

--  Controllers/users.py Line 109
-- SELECT * FROM GuideReviews WHERE ReviewID = %s

--  Controllers/users.py Line 115
-- UPDATE GuideReviews SET GuideID = %s, Stars = %s WHERE ReviewID = %s

--  Controllers/users.py Line 121
-- DELETE FROM GuideReviews WHERE ReviewID = %s

--  Controllers/users.py Line 131
-- INSERT INTO Feedbacks (CommentID, ReviewID, Comment) VALUES (%s, %s, %s)

--  Controllers/users.py Line 137
-- SELECT * FROM Feedbacks WHERE CommentID = %s

--  Controllers/users.py Line 143
-- UPDATE Feedbacks SET ReviewID = %s, Comment = %s WHERE CommentID = %s

--  Controllers/users.py Line 149
-- DELETE FROM Feedbacks WHERE CommentID = %s

--  Controllers/users.py Line 159
-- INSERT INTO ForumPosts (PostID, UserID, Topic, DiscussionContent) VALUES (%s, %s, %s, %s)

--  Controllers/users.py Line 165
-- SELECT * FROM ForumPosts WHERE PostID = %s

--  Controllers/users.py Line 171
-- UPDATE ForumPosts SET UserID = %s, Topic = %s, DiscussionContent = %s WHERE PostID = %s

--  Controllers/users.py Line 177
-- DELETE FROM ForumPosts WHERE PostID = %s

--  Controllers/users.py Line 188
-- INSERT INTO Comments (CommentID, PostID, UserID, Text, Likes, Dislikes) VALUES (%s, %s, %s, %s, %s, %s)

--  Controllers/users.py Line 194
-- SELECT * FROM Comments WHERE CommentID = %s

--  Controllers/users.py Line 200
-- UPDATE Comments SET PostID = %s, UserID = %s, Text = %s, Likes = %s, Dislikes = %s WHERE CommentID = %s

--  Controllers/users.py Line 206
-- DELETE FROM Comments WHERE CommentID = %s

--  Controllers/users.py Line 217
-- INSERT INTO Sponsors (SponsorID, GuideID, UserID, OrganizationName, FinancialContribution, ContactInfo) VALUES (%s, %s, %s, %s, %s, %s)

--  Controllers/users.py Line 223
-- SELECT * FROM Sponsors WHERE SponsorID = %s

--  Controllers/users.py Line 229
-- UPDATE Sponsors SET GuideID = %s, UserID = %s, OrganizationName = %s, FinancialContribution = %s, ContactInfo = %s WHERE SponsorID = %s

--  Controllers/users.py Line 235
-- DELETE FROM Sponsors WHERE SponsorID = %