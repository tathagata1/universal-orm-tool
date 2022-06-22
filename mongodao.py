import pymongo
from datetime import datetime
import os

class initMongoDAO:
    def __init__(self, log, config):
        hostname = config.getMongoHostName()
        port = config.getMongoPort()
        #username = config.getMongoUser()
        #password = config.getMongoPassword()
        normdb = config.getMongoDb()
        testCollectionName = config.getMongoTestCollection()
        requestIdCollectionName = config.getMongoRequestIdCollection()
        transactionIdCollectionName = config.getMongoTransactionIdCollection()
        log.writeInfo(os.path.basename(__file__)+": initializing mongo")
        log.writeInfo(os.path.basename(__file__)+": mongodb://"+hostname+':'+port)
        log.writeDebug(os.path.basename(__file__)+": database used: "+normdb)
        log.writeDebug(os.path.basename(__file__)+": test collection used: "+testCollectionName)
        
        try:
            #create the database connection
            log.writeDebug(os.path.basename(__file__)+": checking mongodb and connection")
            connection = pymongo.MongoClient('mongodb://'+hostname+':'+port)
            self.normDatabase = connection[normdb]
            log.writeDebug(os.path.basename(__file__)+": done..")
            #connection complete..
            
            #as the first test, we shall create a test collection and then write
            #some data to that connection. If it fails then mongo is not setup correctly
            #and the application will stop
            data = { "lastInitialization": datetime.now().strftime("%d/%m/%Y %H:%M:%S") }
            log.writeDebug(os.path.basename(__file__)+": checking "+testCollectionName+" connection with data: "+str(data))
            col = self.normDatabase[testCollectionName]
            col.drop()
            col.insert_one(data)
            log.writeDebug(os.path.basename(__file__)+": done..")
            #test complete..

            # now that the mongo connection has been successfully completed and verified we shall
            # test whether our required system collections are present, if not we shall create them
            # and populate them with initial data where ever needed 

            # checking requestIdCol
            log.writeInfo(os.path.basename(__file__)+": checking "+requestIdCollectionName)
            col = self.normDatabase[requestIdCollectionName]
            if (requestIdCollectionName in self.normDatabase.list_collection_names()):
                result = col.find()
                obj = next(result, None)
                if obj:
                    log.writeInfo(os.path.basename(__file__)+": "+requestIdCollectionName+' has RequestId: '+str(obj['RequestId']))
            else:
                data = { "RequestId": 0 }
                ObjectID = col.insert_one(data).inserted_id
                log.writeInfo(os.path.basename(__file__)+": "+requestIdCollectionName+' initialized to '+str(data))
            log.writeInfo(os.path.basename(__file__)+": checked "+requestIdCollectionName+'..')
            #checked..

            # checking transactionIdCol
            log.writeInfo(os.path.basename(__file__)+": checking "+transactionIdCollectionName)
            col = self.normDatabase[transactionIdCollectionName]
            if (transactionIdCollectionName in self.normDatabase.list_collection_names()):
                result = col.find()
                obj = next(result, None)
                if obj:
                    log.writeInfo(os.path.basename(__file__)+": "+transactionIdCollectionName+' has RequestId: '+str(obj['RequestId']))
            else:
                data = { "TransactionId": 0 }
                ObjectID = col.insert_one(data).inserted_id
                log.writeInfo(os.path.basename(__file__)+": "+transactionIdCollectionName+' initialized to '+str(data))
            log.writeInfo(os.path.basename(__file__)+": checked "+transactionIdCollectionName+'..')
            #checked..

            log.writeInfo(os.path.basename(__file__)+": mongo initialized..")
        except Exception as error:
            template = "Unable to initialize mongoDb due to {0}. Arguments:{1!r}. Exiting.."
            message = template.format(type(error).__name__, error.args)
            log.writeCritical(os.path.basename(__file__)+' '+message)
            connection.close()
            exit()

        
#transactionid
    def getTransactionId(self):
        return 'asd'
#requestid

#function registerUser()
#function updateUser()
#function getUserData()
#function getUserDataAll()
#function deregisterUser()

#function registerTable()
#function updateTable()
#function getTableData()
#function getTableDataAll()
#function deregisterTable()

#function selectData()
#function selectInnerJoinData()
#function selectLeftJoinData()
#function selectRightJoinData()
#function selectFullJoinData()
#function insertData()
#function updateData()
#function upsertData()
#function deleteData()
#function truncateTable()
