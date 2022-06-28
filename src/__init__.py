import ETL as etl

if __name__ == '__main__':
    logfile    = "logfile"            # all event logs will be stored in this file
    targetfile = "transformed_data"   # file where transformed data is stored
    currency = 'EUR'

    # Logs that the ETL Job Started
    etl.log("ETL Job Started", logfile)

    #############################################################
    ########################## EXTRACT ##########################
    #############################################################

    # Logs that the Extract phase started
    etl.log("Extract phase started", logfile)
    # Gets the exchange rate
    exchange_rate = etl.get_exchange_rate(currency)
    # Calls the function to Extract the data
    extracted_data = etl.extract()
    # Logs that the Extract phase ended
    etl.log("Extract phase ended", logfile)

    #############################################################
    ########################## TRANSFORM ########################
    #############################################################

    # Logs that the Transform phase started
    etl.log("Transform phase started", logfile)
    # Calls the function to Transform the data
    transformed_data = etl.transform(extracted_data, exchange_rate, currency)
    # Logs that the Transform phase ended
    etl.log("Transform phase ended", logfile)

    #############################################################
    ########################## LOAD #############################
    #############################################################

    # Logs that the Load phase started
    etl.log("Load phase started", logfile)
    # Calls the function to Load the data
    etl.load(transformed_data, targetfile)
    # Logs that the Load phase ended
    etl.log("Load phase ended", logfile)

    # Logs that the ETL Job ended
    etl.log("ETL processes ended", logfile)