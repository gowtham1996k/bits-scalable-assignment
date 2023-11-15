IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'jwt_auth')
CREATE DATABASE jwt_auth;
GO
