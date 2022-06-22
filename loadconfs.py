import configparser
import os

# get the initial variables from the environment
# these have been set outside the class so that it is earier to refer to them throughtout the application
userConfFile = 'config\\user.conf'
appConfFile = 'config\\app.conf'

userLoggingConfigurationSection = 'LoggingConfigurationSection'
appMongoDBConfigurationSection = 'MongoDBConfigurationSection'
appMqConfigurationSection = 'IBMMQConfigurationSection'

class initConf:
    def __init__(self):
        UserConfiguration = configparser.ConfigParser()
        UserConfiguration.read(userConfFile)
        self.LogPath = UserConfiguration[userLoggingConfigurationSection]['logPathKey']
        self.LogFile = UserConfiguration[userLoggingConfigurationSection]['logFileKey']
        self.LogDateFormat = UserConfiguration[userLoggingConfigurationSection]['logDateFormatKey']
        self.LogDataFormat = UserConfiguration[userLoggingConfigurationSection]['logDataFormatKey']
        self.LogWriteMode = UserConfiguration[userLoggingConfigurationSection]['logWriteModeKey']
        
        AppConfiguration = configparser.ConfigParser()
        AppConfiguration.read(appConfFile)
        self.MongoHostName = AppConfiguration[appMongoDBConfigurationSection]['mongoHostName']
        self.MongoPort = AppConfiguration[appMongoDBConfigurationSection]['mongoPort']
        self.MongoUser = AppConfiguration[appMongoDBConfigurationSection]['mongoUser']
        self.MongoPassword = AppConfiguration[appMongoDBConfigurationSection]['mongoPassword']
        self.MongoDb = AppConfiguration[appMongoDBConfigurationSection]['mongoDb']
        self.MongoTestCollection = AppConfiguration[appMongoDBConfigurationSection]['mongoTestCollection']
        self.MongoTransactionIdCollection = AppConfiguration[appMongoDBConfigurationSection]['mongoTransactionIdCollection']
        self.MongoRequestIdCollection = AppConfiguration[appMongoDBConfigurationSection]['mongoRequestIdCollection']
        
        self.MqHostName = AppConfiguration[appMqConfigurationSection]['mqHostname']
        self.MqUser = AppConfiguration[appMqConfigurationSection]['mqUser']
        self.MqPassword = AppConfiguration[appMqConfigurationSection]['mqPassword']

    def getLogPath(self):
        return self.LogPath

    def getLogFile(self):
        return self.LogFile

    def getLogDateFormat(self):
        return self.LogDateFormat

    def getLogDataFormat(self):
        return self.LogDataFormat

    def getLogWriteMode(self):
        return self.LogWriteMode

    def getMongoHostName(self):
        return self.MongoHostName

    def getMongoPort(self):
        return self.MongoPort

    def getMongoUser(self):
        return self.MongoUser

    def getMongoPassword(self):
        return self.MongoPassword
    
    def getMongoDb(self):
        return self.MongoDb
        
    def getMongoTestCollection(self):
        return self.MongoTestCollection

    def getMongoRequestIdCollection(self):
        return self.MongoRequestIdCollection

    def getMongoTransactionIdCollection(self):
        return self.MongoTransactionIdCollection


    def getMqHostName(self):
        return self.MqHostName

    def getMqUser(self):
        return self.MqUser

    def getMqPassword(self):
        return self.MqPassword